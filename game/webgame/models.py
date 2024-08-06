from django.db import models

# Create your models here.


class UserInfo(models.Model):
    PHONENUM_MAX_LENGTH = 15
    GENDER_CHOICES = [
        (1, '男'),
        (2, '女'),
        (3, '其他'),
    ]

    phonenum = models.CharField(max_length=PHONENUM_MAX_LENGTH, unique=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.phonenum} - {self.get_gender_display()}"
