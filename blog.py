from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f'Blog: {self.title}, Author: {self.author}, Posts: {len(self.posts)}'

    def create_post(self, title, content):
        p = Post(title, content)
        self.posts.append(p)

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }
