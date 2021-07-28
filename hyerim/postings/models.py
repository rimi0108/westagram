from django.db import models

from users.models import User

# Create your models here.

class Post(models.Model):
  creation_time   = models.DateTimeField()
  image_url       = models.CharField(max_length=200)
  posting_content = models.CharField(max_length=1000)
  user_id         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

  class Meta:
    db_table = 'posts'