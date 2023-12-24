from django.db.models.signals import pre_delete, post_delete
import argon2
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
                field_name = f"{field=}".split("=")[0]
                raise ValidationError(f"{field_name} cannot be null")
        return True

    def create_user(self, id=None, library_card=None, name=None, surname=None, mail=None, role=None, password=None, salt=None, last_name=None):

        # how tf do you make proper error-handling without breaking the server?
        self.__field_check(id, library_card, name, surname,
                           mail, role, password, salt, last_name)

        id = self.normalize_email(id)
        user = self.model(
            id=id,
            library_card=library_card,
            name=name,
            surname=surname,
            mail=mail,
            role=role,
            salt=salt,
            last_name=last_name
        )
        user.password = argon2.hash(password + salt)
        user.save(using=self._db)
        return user

    def create_superuser(self, id=None, library_card=None, name=None, surname=None, mail=None, role=None, password=None, salt=None, last_name=None):

        self.__field_check(id, library_card, name, surname,
                           mail, role, password, salt, last_name)

        id = self.normalize_email(id)
        user = self.model(
            id=id,
            library_card=library_card,
            name=name,
            surname=surname,
            mail=mail,
            role=role,
            salt=salt,
            last_name=last_name
        )
        user.password = argon2.hash_password(password + salt)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    password = models.BinaryField()
    salt = models.BinaryField()
    library_card = models.TextField()
    name = models.TextField()
    surname = models.TextField()
    last_name = models.TextField(null=True, blank=True)
    role = models.TextField()
    mail = models.TextField()
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'id'


class Author(models.Model):
    author_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    name = models.TextField()

# questionable code


@receiver(pre_delete, sender=Author)
def remove_author_from_books(sender, instance, **kwargs):
    for book in instance.books.all():
        if book.authors.count() > 1:
            book.authors.remove(instance)
        else:
            instance.books.filter(author__id=instance.author_id)


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
        Author, related_name="books", null=True, through="BookAuthor")
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


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)


class Reservation(models.Model):
    reservation_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.TextField()
