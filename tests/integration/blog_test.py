from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Post Title', 'Post Content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual(b.posts[0].title, 'Post Title')
        self.assertEqual(b.posts[0].content, 'Post Content')

    def test_json(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Post Title', 'Post Content')

        self.assertDictEqual(b.json(), {'title': 'Test Title',
                                        'author': 'Test Author',
                                        'posts': [
                                            {
                                                'title': 'Post Title',
                                                'content': 'Post Content'
                                            }
                                        ]})

    def test_json_no_posts(self):
        b = Blog('Test Title', 'Test Author')
        self.assertDictEqual(b.json(), {'title': 'Test Title',
                                        'author': 'Test Author',
                                        'posts': []}
                             )