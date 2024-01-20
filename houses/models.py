from django.db import models

# Create your models here.
class House(models.Model):

    """definition model for house"""

    name = models.CharField(max_length=140)  # CharField는 글자수 제한이 있는 문자열을 저장할 때 사용
    price_per_night = models.PositiveIntegerField() # PositiveIntegerField는 양수를 저장할 때 사용
    description = models.TextField()  # TextField는 글자수 제한이 없는 문자열을 저장할 때 사용
    address = models.CharField(max_length=140) # CharField는 글자수 제한이 있는 문자열을 저장할 때 사용
    pet_allowed = models.BooleanField(default=True) # BooleanField는 True/False를 저장할 때 사용
    
    def __str__(self):
        return self.name
    

