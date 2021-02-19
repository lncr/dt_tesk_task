import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from ...models import Comment, Post


User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        usernames = [
            "John",
            "Edward",
            "Alice",
            "Brad",
        ]
        titles = ["Super post", "Greetings", "Level up", "Simple", "Chocolate"]
        for i in range(3):
            user = User.objects.create_user(
                username=usernames[i], password="SuperSecretPassword123"
            )
            Post.objects.create(
                author=user, title=titles[random.randint(0, len(titles) - 1)]
            )
            Post.objects.create(
                author=user, title=titles[random.randint(0, len(titles) - 1)]
            )
        users = User.objects.all()
        posts = Post.objects.all()

        for post in posts:
            Comment.objects.create(
                author=users[random.randint(0, len(users) - 1)],
                post=post,
                content="Good comment",
            )
            Comment.objects.create(
                author=users[random.randint(0, len(users) - 1)],
                post=post,
                content="Bad comment",
            )
