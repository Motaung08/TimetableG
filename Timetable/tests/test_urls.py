from django.test import SimpleTestCase ,TestCase
from django.urls import reverse, resolve
from django.test import TestCase, Client

class TestUrls(TestCase):
    
    def test_login_url_resolved(self):
        url = reverse('login')

        self.assertEquals(resolve(url).func, 'login')


    def test_register_url_resolved(self):
        url = reverse('register')

        self.assertEquals(resolve(url).func, 'register')

    def test_Confirm_log(self):
        url = reverse('courses')
        self.assertEquals(resolve(url).func, 'courses')

    def test_forgot(self):
        url = reverse('forgot')
        self.assertEquals(resolve(url).func, 'forgot')

    def test_reset(self):
        url = reverse('reset')
        self.assertEquals(resolve(url).func, 'resetp')






