import random

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APILiveServerTestCase, APITestCase

from snippets.models import Snippet

data_me = {"title": "Test Snippet",
           "code": "class MyUser(AbstractUser):\n\timg_profile = models.ImageField(upload_to='user', blank=True)"}
data2_me = {"title": "Test Snippet2",
            "code": "class MyUser(AbstractUser):\n\timg_profile = models.ImageField(upload_to='user', blank=True)"}

User = get_user_model()


class SnipeetTest_lecture(APILiveServerTestCase):
    test_title = 'Test Snippet[{}] Title'
    test_code = 'print("Hello, world{}")'
    default_linenos = False
    default_language = 'python'
    default_style = 'friendly'

    test_username = 'test_username'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(username=self.test_username, password=self.test_password)
        return user

    def create_snippet(self, num=1):

        for i in range(num):
            test_title = self.test_title.format(i + 1)
            test_code = self.test_code.format('!' * (i + 1))
            url = reverse('snippet-list')
            data = {'title': test_title, 'code': test_code}
            response = self.client.post(url, data, format='json')
            if num == 1:
                return response

    def test_snippet_list(self):
        self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)
        num = random.randrange(1, 10)
        self.create_snippet(num)
        self.assertEqual(Snippet.objects.count(), num)
        # use values_list to get specific part in query
        for index, snippet_value_tuple in enumerate(Snippet.objects.values_list('title', 'code')):
            self.assertEqual(snippet_value_tuple[0], self.test_title.format(index + 1))
            self.assertEqual(snippet_value_tuple[1], self.test_code.format('!' * (index + 1)))
        # use only part of query when query is too big
        for index, snippet in enumerate(Snippet.objects.all().iterator()):
            self.assertEqual(snippet.title, self.test_title.format(index + 1))
            self.assertEqual(snippet.code, self.test_code.format('!' * (index + 1)))
            # for i in range(num):
            #     cur_snippet = Snippet.objects.all()[i]
            #     self.assertEqual(cur_snippet.title, self.test_title.format(i + 1))
            #     self.assertEqual(cur_snippet.code, self.test_code.format('!' * (i + 1)))

    def test_snippet_create(self):
        self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)
        response = self.create_snippet()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('title'), self.test_title.format(1))
        self.assertEqual(response.data.get('code'), self.test_code.format('!'))
        self.assertEqual(response.data.get('linenos'), self.default_linenos)
        self.assertEqual(response.data.get('language'), self.default_language)
        self.assertEqual(response.data.get('style'), self.default_style)

        pass

    def test_snippet_retrieve(self):
        pass

    def test_snippet_update_partial(self):
        pass

    def test_snippet_updata(self):
        pass

    def test_snippet_delete(self):
        pass

    # def test_snippet_highlight2(self):
    #     self.create_user()
    #     self.client.login(username=self.test_username, password=self.test_password)
    #     self.client.post('/snippets/',
    #                      data_me,
    #                      format='json')
    #     self.client.post('/snippets/',
    #                      data_me,
    #                      format='json')
    #     print(Snippet.objects.first())
    #     url = reverse('snippet-highlight', kwargs={'pk': 1})
    #     response = self.client.get(reverse('snippet-detail',kwargs={'pk': 1}))
    #     print(response)

    def test_snippet_highlight(self):
        self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)
        num = random.randrange(1, 10)
        self.create_snippet(num)
        pk = Snippet.objects.first().pk
        url = reverse('snippet-highlight', kwargs={'pk': pk})
        response = self.client.get(url)
        # print(response.data)
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('<div class="highlight">', response.data)

    #     """
    #     snippet의 save() method 참조해서 만들어진 snippet instance의 hightlighted 된 필드의 값이
    #     pygments를 사용해서 만들어낸 syntax highlighted HTLM과 같은지 assertEqual확인
    #     :return:


class SnippetTests(APITestCase):
    test_title = 'Test Snippet[{}] Title'
    test_code = 'print("Hello, world{}")'
    default_linenos = False
    default_language = 'python'
    default_style = 'friendly'

    test_username = 'test_username'
    test_password = 'test_password'

    def create_user(self):
        user = User.objects.create_user(username=self.test_username, password=self.test_password)
        return user

    def create_snippet(self, num=1):

        for i in range(num):
            test_title = self.test_title.format(i + 1)
            test_code = self.test_code.format('!' * (i + 1))
            url = reverse('snippet-list')
            data = {'title': test_title, 'code': test_code}
            response = self.client.post(url, data, format='json')
            if num == 1:
                return response
    def test_snippet_highlight2(self):
        self.create_user()
        self.client.login(username=self.test_username, password=self.test_password)
        self.client.post('/snippets/',
                         data_me,
                         format='json')
        self.client.post('/snippets/',
                         data_me,
                         format='json')
        print(Snippet.objects.first())
        url = reverse('snippet-highlight', kwargs={'pk': 1})
        response = self.client.get(url)
        print(response)

# # def test_post(self):
#     #     factory = APIRequestFactory()
#     #     print(factory)
#     #     factory.post('/snippets/', data, format='json')
#     #     self.assertEqual(Snippet.objects.count(), 1)
#
#     test_username = 'test_username'
#     test_password = 'test_password'
#
#     def create_user(self):
#         user = User.objects.create_user(username=self.test_username, password=self.test_password)
#         return user
#
#     def test_post_correct(self):
#         response = self.client.post('/snippets/',
#                                     data_me,
#                                     format='json')
#         response2 = self.client.get('/snippets/')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response2.data[0]['title'], "Test Snippet")
#         self.assertEqual(response2.data[0]['code'],
#                          "class MyUser(AbstractUser):\n\timg_profile = models.ImageField(upload_to='user', blank=True)")
#         self.assertEqual(Snippet.objects.count(), 1)
#
#     def test_get_correct(self):
#
#         self.client.post('/snippets/', data_me, format='json')
#         self.client.post('/snippets/', data2_me, format='json')
#
#         response = self.client.get('/snippets/2/')
#         self.assertEqual(response.data['title'], "Test Snippet2")
#
#     def test_patch_correct(self):
#         self.client.post('/snippets/', data_me, format='json')
#         self.client.post('/snippets/', data2_me, format='json')
#         response = self.client.patch('/snippets/1/', {"title": "new title"}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], "new title")
#
#     def test_put_correct(self):
#         self.client.post('/snippets/', data_me, format='json')
#         self.client.put('/snippets/1/', data2_me, format='json')
#         response = self.client.get('/snippets/1/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], "Test Snippet2")
#
#     def test_delete_correct(self):
#         self.client.post('/snippets/', data_me, format='json')
#         self.client.post('/snippets/', data2_me, format='json')
#         self.assertEqual(Snippet.objects.count(), 2)
#         self.client.delete('/snippets/1/')
#         self.assertEqual(Snippet.objects.count(), 1)
#         self.client.delete('/snippets/2/')
#         self.assertEqual(Snippet.objects.count(), 0)
