from django.contrib.auth.models import User
from .models import Topics
from rest_framework import status
from rest_framework.test import APITestCase


class TopicPostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_topic_posts(self):
        adam = User.objects.get(username='adam')
        Topics.objects.create(owner=adam, question='a question')
        response = self.client.get('/topics/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_topic_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/topics/', {'question': 'a question'})
        count = Topics.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_topic_post(self):
        response = self.client.post('/topics/', {'question': 'a question'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
