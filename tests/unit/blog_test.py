from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test Title', 'Test Author')

        self.assertEqual('Test Title', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test Title', 'Test Author')
        self.assertEqual(b.__repr__(), 'Blog: Test Title, Author: Test Author, Posts: 0')

    def test_repr_multiple_posts(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Post Title', 'Post Content')

        self.assertEqual(b.__repr__(), 'Blog: Test Title, Author: Test Author, Posts: 1')
