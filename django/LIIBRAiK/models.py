import inspect
from django.db.models.signals import pre_delete, post_save
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, PermissionsMixin
from django.dispatch import receiver
from django.forms import ValidationError
from django.contrib.postgres import fields as postgres_models

"""
Bullet-points:
1. No CharFields, only TextField, since there's no difference in speed and flexibility is always good
2. Might wanna check sometime later if uuid4 is safe for UID generation
3. While in ERD we reference isolated columns, here we use reference by object
4. django-db-constraints? WTH it this lol
"""


class UserManager(BaseUserManager):

    def __field_check(*fields):
        if None in fields:
            raise ValidationError(
                f"Something went wrong when checking fields")

    def create_user(self, id=None, library_card=None, name=None, surname=None, mail=None, password=None, last_name=None, role=None):

        # how tf do you make proper error-handling without breaking the server?
        self.__field_check(id, library_card, name, surname,
                           mail, password)

        mail = self.normalize_email(mail)
        user: User = self.model(
            id=id,
            library_card=library_card,
            name=name,
            surname=surname,
            mail=mail,
            last_name=last_name,
        )
        # questionable, since default role is student and we can theoretically catch a forged request with role="librarian"
        user.role = role if (role is not None) and (
            role != "admin") else "student"
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id=None, library_card=None, name=None, surname=None, mail=None, password=None, last_name=None):

        self.__field_check(id, library_card, name, surname,
                           mail, password)

        id = self.normalize_email(id)
        user: User = self.model(
            id=id,
            library_card=library_card,
            name=name,
            surname=surname,
            mail=mail,
            last_name=last_name,
        )
        user.role = "admin"
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.TextField(primary_key=True, default=uuid.uuid4)
    library_card = models.TextField(default="default")
    name = models.TextField()
    surname = models.TextField()
    last_name = models.TextField(null=True, blank=True)
    mail = models.TextField()
    last_login = models.DateTimeField(blank=True, null=True)
    objects = UserManager()
    role = models.TextField(default="student")
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'id'
    EMAIL_FIELD = 'mail'
    REQUIRED_FIELDS = ["library_card", "name", "surname", "mail"]

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return True if self.role == "admin" else False

# configuring default groups is probably not supposed to be this hard, eh?
# @receiver(post_save, sender=User)
# def add_to_group(sender, instance: User, created, **kwargs):
#     if created:
#         default_group_name = 'student' if not (instance.is_staff) else 'admin'
#         default_group = Group.objects.get_or_create(name=default_group_name)
#         instance.groups.add(default_group)


class Author(models.Model):
    author_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    name = models.TextField()

# questionable code made for proper book authors deletions
@receiver(pre_delete, sender=Author)
def remove_author_from_books(sender, instance, **kwargs):
    books_to_delete = []
    for book in instance.books.all():
        if book.authors.count() > 1:
            book.authors.remove(instance)
        else:
            books_to_delete.append(book)
    Book.objects.filter(id__in=[book.id for book in books_to_delete]).delete()


class Publisher(models.Model):
    publisher_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    name = models.TextField()


class Book(models.Model):
    book_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    name = models.TextField()
    year = models.SmallIntegerField(null=True, blank=True)
    ISBN = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(
        Author, related_name="books", through="BookToAuthor")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amounts = postgres_models.ArrayField(
        models.IntegerField(null=True, blank=True), size=3)
    cover = models.FileField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.authors = self.authors.all()[:10]
        super().save(*args, **kwargs)


# ethically questionable practices here, folks
class BookToAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)


class Reservation(models.Model):
    reservation_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.TextField()
