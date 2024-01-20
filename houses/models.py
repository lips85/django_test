from django.db import models

# Create your models here.
class House(models.Model):

    """definition model for house"""

    name = models.CharField(max_length=140)  # CharField는 글자수 제한이 있는 문자열을 저장할 때 사용
    price = models.PositiveIntegerField() # PositiveIntegerField는 양수를 저장할 때 사용
    description = models.TextField()  # TextField는 글자수 제한이 없는 문자열을 저장할 때 사용
    address = models.CharField(max_length=140) # CharField는 글자수 제한이 있는 문자열을 저장할 때 사용