from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Post


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='shadow')
        cls.post1 = Post.objects.create(
            title='shadow_title_1',
            text='shadow_text_1',
            author=user,
            status=Post.STATUS_CHOICES[1][0],
        )
        cls.post2 = Post.objects.create(
            title='shadow_title_2',
            text='shadow_text_2',
            author=user,
            status=Post.STATUS_CHOICES[0][0],
        )

    def test_post_list_view_url(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)

    def test_post_list_view_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEquals(response.status_code, 200)

    def test_post_title_exist_on_post_list_view_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_view_url(self):
        response = self.client.get(f'/blog/{self.post1.pk}/')
        self.assertEquals(response.status_code, 200)

    def test_post_detail_view_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.pk]))
        self.assertEquals(response.status_code, 200)

    def test_post_details_exist_on_post_detail_view_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.pk]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_status_choices(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_404_if_post_id_does_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[8888]))
        self.assertEquals(response.status_code, 404)
