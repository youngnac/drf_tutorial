from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from snippets.models import Snippet

data = {"title": "Test Snippet",
        "code": "class MyUser(AbstractUser):\n\timg_profile = models.ImageField(upload_to='user', blank=True)"}
data2 = {"title": "Test Snippet2",
         "code": "class MyUser(AbstractUser):\n\timg_profile = models.ImageField(upload_to='user', blank=True)"}


class SnippetTests(APITestCase):
    # def test_post(self):
    #     factory = APIRequestFactory()
    #     print(factory)
    #     factory.post('/snippets/', data, format='json')
    #     self.assertEqual(Snippet.objects.count(), 1)


    def test_post_correct(self):
        response = self.client.post('/snippets/',
                                    data,
                                    format='json')
        response2 = self.client.get('/snippets/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.data[0]['title'], "Test Snippet")
        self.assertEqual(response2.data[0]['code'],
                         "class MyUser(AbstractUser):\n\timg_profile = models.ImageField(upload_to='user', blank=True)")
        self.assertEqual(Snippet.objects.count(), 1)

    def test_get_correct(self):
        self.client = APIClient()

        self.client.post('/snippets/', data, format='json')
        self.client.post('/snippets/', data2, format='json')

        response = self.client.get('/snippets/2/')
        self.assertEqual(response.data['title'], "Test Snippet2")

    def test_patch_correct(self):
        self.client = APIClient()
        self.client.post('/snippets/', data, format='json')
        self.client.post('/snippets/', data2, format='json')
        response = self.client.patch('/snippets/1/', {"title": "new title"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "new title")

    def test_put_correct(self):
        self.client.post('/snippets/', data, format='json')
        self.client.put('/snippets/1/', data2, format='json')
        response = self.client.get('/snippets/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Snippet2")

    def test_delete_correct(self):
        self.client.post('/snippets/', data, format='json')
        self.client.post('/snippets/', data2, format='json')
        self.assertEqual(Snippet.objects.count(), 2)
        self.client.delete('/snippets/1/')
        self.assertEqual(Snippet.objects.count(), 1)
        self.client.delete('/snippets/2/')
        self.assertEqual(Snippet.objects.count(), 0)

