from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): #커스텀 할수있게 설정
    class GenderChoices(models.TextChoices):
        MALE = ('male','Male')
        FEMALE = ('femail','Femail')

    class LanguageChoices(models.TextChoices):
        KR = ('kr','Korean')
        EN = ('en','English')
        ES = ('es','Español')

    class CurrencyChoices(models.TextChoices):
        WON = ('won','Korean Won')
        USD = ('usd','US Dollar')
        EUR = ('euro','EU Euro')
    first_name = models.CharField(
        max_length=150,
        editable=False, # 안씀
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.ImageField(
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default=""
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length= 2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices
    )