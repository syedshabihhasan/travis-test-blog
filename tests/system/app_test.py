from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        b = Blog('Blog Title', 'Blog aUthor')
        app.blogs = {'Blog Title': b}

    def test_input_prompt(self):
        # b = Blog('Blog Title', 'Blog aUthor')
        # app.blogs = {'Test': b}
        with patch('builtins.input', return_value='q') as mocked_patch:
            app.menu()
            mocked_patch.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        # b = Blog('Blog Title', 'Blog aUthor')
        # app.blogs = {'Test': b}
        with patch('app.print_blogs') as mocked_patch:
            with patch('builtins.input', return_value='q') as mocked_input:
                app.menu()
                mocked_patch.assert_called()

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        # b = Blog('Blog Title', 'Blog aUthor')
        # app.blogs = {'Blog Title': b}
        with patch('builtins.input', return_value='Blog Title') as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Blog Title'])

    def test_print_posts(self):
        # b = Blog('Blog Title', 'Blog aUthor')
        app.blogs['Blog Title'].create_post('Test Post Title', 'Test Post Content')
        #app.blogs = {'Blog Title': app.blogs['Blog Title']}
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(app.blogs['Blog Title'])
            mocked_print_post.assert_called_with(app.blogs['Blog Title'].posts[0])

    def test_print_post(self):
        # b = Blog('Blog Title', 'Blog aUthor')
        app.blogs['Blog Title'].create_post('Test Post Title', 'Test Post Content')
        #app.blogs = {'Blog Title': app.blogs['Blog Title']}
        with patch('builtins.print') as mocked_print:
            app.print_posts(app.blogs['Blog Title'])
            mocked_print.assert_called_with(app.POST_TEMPLATE.format('Test Post Title', 'Test Post Content'))

    def test_ask_create_post(self):
        # b = Blog('Blog Title', 'Blog aUthor')
        # app.blogs = {'Blog Title': b}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Blog Title', 'Test Post Title', 'Test Post Content')
            app.ask_create_post()
            self.assertEqual(app.blogs['Blog Title'].posts[0].title, 'Test Post Title')
            self.assertEqual(app.blogs['Blog Title'].posts[0].content, 'Test Post Content')

    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'q')
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_print_blogs(self):
        # b = Blog('Blog Title', 'Blog aUthor')
        # app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Blog: Blog Title, Author: Blog aUthor, Posts: 0')
