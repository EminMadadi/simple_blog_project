from django.db import models


class Post(models.Model):

    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )

    title = models.CharField(max_length=40)
    text = models.TextField()
    author = models.ForeignKey('auth.USER', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.title} | {self.author}'
