from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

''' HomePageTests class check that the HTTP status code for the homepage equals
200 which means that it exists.'''
class HomePageTests(SimpleTestCase):
    '''we’re creating a variable
       called response that accesses the homepage (/) and then uses Python’s assertEqual
       to check that the status code matches 200 '''
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        response = self.client.get(reverse('home')) #we are calling the URL name of home via the reverse method
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):   #SimpleTestCase comes with a method assertTemplateUsed for testing templates
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        '''We’ve created a response variable  and then checked that the template home.html
        is used.'''

    def test_homepage_html(self):  # new
        response = self.client.get('/')
        self.assertContains(response, 'Ethio Book Store')




