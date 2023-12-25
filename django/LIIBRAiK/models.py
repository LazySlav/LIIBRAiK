import inspect
from django.db.models.signals import pre_delete
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
        for field in fields:
            if field is None:
                raise ValidationError(
                    f"Something went wrong when checking fields")
        return True

    def create_user(self, id=None, library_card=None, name=None, surname=None, mail=None, role=None, password=None, last_name=None):

        # how tf do you make proper error-handling without breaking the server?
        self.__field_check(id, library_card, name, surname,
                           mail, role, password)

        mail = self.normalize_email(mail)
        user: User = self.model(
            id=id,
            library_card=library_card,
            name=name,
            surname=surname,
            mail=mail,
            role=role,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id=None, library_card=None, name=None, surname=None, mail=None, role=None, password=None, last_name=None):

        self.__field_check(id, library_card, name, surname,
                           mail, role, password)

        id = self.normalize_email(id)
        user: User = self.model(
            id=id,
            library_card=library_card,
            name=name,
            surname=surname,
            mail=mail,
            role=role,
            last_name=last_name
        )
        user.role = "admin"
        print(password)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.TextField(primary_key=True, default=uuid.uuid4)
    library_card = models.TextField(default="default")
    name = models.TextField()
    surname = models.TextField()
    last_name = models.TextField(null=True, blank=True)
    role = models.TextField(default="student")
    mail = models.TextField()
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ["library_card", "name", "surname", "role", "mail"]


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
