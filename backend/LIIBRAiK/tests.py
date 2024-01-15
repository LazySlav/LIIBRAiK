from rest_framework.test import APITestCase
from rest_framework import status
from LIIBRAiK.models import Book

TEST_BOOK = {
    "book_id": "f7fc0020-aae2-4033-b539-452ec37a2b10",
    "name": "test_book",
    "year": None,
    "ISBN": "",
    "authors": [
        "dff9f769-87ea-49da-9e32-3f4e806fba9f",
        "0895af3e-5751-4b90-b3fc-27cfccf096ee",
        "bd16d9d7-a417-477d-8cab-1556a28ab766",
        "3bac043b-a2a6-419b-9636-a5afa2cd16ee",
        "1b3e2af6-1b83-4f3c-8852-13ba415e3865",
        "07242733-8511-4bdb-aab7-761ef8f2c789",
        "63ca7278-3e11-48e2-938b-39700ea99ae9",
        "f16312d5-22fc-47bf-8824-ad4954f42ec9",
        "b75660c3-240c-4498-a9f0-07a6b892d960",
        "aeb767d6-78aa-4760-a02d-cf2d793b296c",
        "9463f5e7-7615-45f8-aa05-f4061d0334c7"
    ],
    "publisher": None,
    "description": "",
    "amounts": [
        1,
        2,
        3
    ],
    "cover": None,
    "pdf": None
}


class BookTests(APITestCase):
    def test_create_book(self):
        url = '/books/'
        data = TEST_BOOK
        book_amount = Book.objects.all().count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count()-1, book_amount)
        self.assertEqual(Book.objects.get(book_id=TEST_BOOK.get(
            "book_id")).name, TEST_BOOK.get("name"))

    def test_get_books(self):
        url = '/books/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_pk(self):
        pk = "f7fc0020-aae2-4033-b539-452ec37a2b10"
        url = f'/books/{pk}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], Book.objects.get(book_id=pk))

    def test_patch_book(self):
        pk = "f7fc0020-aae2-4033-b539-452ec37a2b10"
        url = f'/books/{pk}/'
        TEST_BOOK["authors"].pop()
        data = TEST_BOOK
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()["authors"], Book.objects.get(book_id=pk).authors)

    def test_delete_book(self):
        pk = "f7fc0020-aae2-4033-b539-452ec37a2b10"
        url = f'/books/{pk}/'
        book_amount = Book.objects.all().count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.all().count()+1, book_amount)
        self.assertRaises(Book.DoesNotExist, Book.objects.get(book_id=pk))
