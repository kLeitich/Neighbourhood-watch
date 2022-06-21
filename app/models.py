from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    ppic=models.ImageField(upload_to ='ppic') 
    bio=models.TextField(max_length=600, default="Bio")
    phone=models.CharField(max_length=20, default="Phone")
    fname=models.CharField(max_length=30, default="First name")
    lname=models.CharField(max_length=30, default="last name")
    neighborhood=models.OneToOneField('Neighborhood', on_delete=models.CASCADE, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='profile')

    def __str__(self):
        return f'{self.user.username} insta-profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Neighborhood(models.Model):
    image=models.ImageField(upload_to ='hood_pics') 
    name=models.CharField(max_length=30, default="Neighbourhood")
    location=models.CharField(max_length=30, default="Location")
    occupants_count=models.IntegerField(default=0)
    admin=models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.name}'

    @classmethod
    def delete_neighborhood(self):
        self.delete()
    
    @classmethod
    def find_neighborhood(cls, id):
        hood = Neighborhood.objects.filter(id = id).first()
        return hood

    @classmethod
    def search_hood(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    @classmethod
    def get_neighbourhoods(cls):
        return cls.objects.all()

class Business(models.Model):
    business_name=models.CharField(max_length=30, default="Business name")
    business_email=models.EmailField(max_length=30, default="Business email")
    business_phone=models.CharField(max_length=30, default="Business phone")
    business_location=models.CharField(max_length=30, default="Business location")
    business_description=models.TextField(max_length=600, default="Business description")
    business_image=models.ImageField(upload_to ='business_pics')
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.business_name}'

    @classmethod
    def save_business(self):
        self.save()

    @classmethod
    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, id):
        business = Business.objects.filter(id = id).first()
        return business

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(business_name__icontains=name).all()

    @classmethod
    def get_businesses(cls):
        return cls.objects.all()

class Post(models.Model):
    title=models.CharField(max_length=30, default="Title")
    post=models.TextField(max_length=600, default="Post")
    image=models.ImageField(upload_to ='post_pics')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.title}'

    @classmethod
    def delete_post(self):
        self.delete()

    @classmethod
    def find_post(cls, id):
        post = Post.objects.filter(id = id).first()
        return post

    @classmethod
    def search_post(cls, name):
        return cls.objects.filter(title__icontains=name).all()

    @classmethod
    def get_posts(cls):
        return cls.objects.all()

    