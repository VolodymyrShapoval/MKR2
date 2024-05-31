from audioop import reverse
from unittest import TestCase

from mkr2.books.models import Author


class AuthorViewTests(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertContains(response, self.author1.name)
        self.assertContains(response, self.author2.name)

    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', args=[self.author1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_detail.html')
        self.assertContains(response, self.author1.name)
        self.assertNotContains(response, self.author2.name)
