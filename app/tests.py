from django.test import TestCase
from . models import *
# Create your tests here.
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.neighborhood = Neighborhood(name='Kasa',image='media/hood_pics/appstore.png')
        self.user = User(id=1,username='Kevin')
    def test_instances(self):
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))

    def test_save_neighbourhood(self):
        self.user.save()
        




class ProfileTestClass(TestCase):
    def setUp(self):
        self.neighborhood= Neighborhood(name='Kasa')
        self.neighborhood.save_neighborhood()
        self.profile = Profile(bio='this is a bio',
        email='testemail@gmail.com',neighborhood=self.neighborhood)
        self.user = User(id=1,username='Kevin')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.user.save()
       
    def test_delete_profile(self):
        self.user.delete()
       
    

class BusinessTestClass(TestCase):
    def setUp(self):
        self.neighborhood= Neighborhood(name='Kasa')
        self.business= Business(business_name='liqour')
        # self.business.save_business()
        self.profile = Profile(bio='this is a bio',
        email='testemail@gmail.com',neighborhood=self.neighborhood)
        self.user = User(id=1,username='Kevin')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
       
    def test_delete_business(self):
        self.user.delete()

    def test_save_business(self):
        self.user.save()

    def test_update_method(self):
        self.user.save()

    def test_search_business(self):
        self.user.save()

class PostTestClass(TestCase):
    def setUp(self):
        self.neighborhood= Neighborhood(name='Kasa')
        self.post= Post(title='crime')
        self.post.save_post()
        self.profile = Profile(bio='this is a bio',
        email='testemail@gmail.com',neighborhood=self.neighborhood)
        self.user = User(id=1,username='Kevin')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.user.save()
       
    def test_delete_post(self):
        self.user.delete()