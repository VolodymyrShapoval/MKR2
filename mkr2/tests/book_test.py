from audioop import reverse
from unittest import TestCase

from mkr2.books.models import Book


class BookViewTests(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title="Book One", author="Author One", published_date="2023-01-01")
        self.book2 = Book.objects.create(title="Book Two", author="Author Two", published_date="2023-01-02")

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')
        self.assertContains(response, self.book1.title)
        self.assertNotContains(response, self.book2.title)