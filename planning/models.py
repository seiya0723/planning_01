from django.db import models


STATUS  = [
            ("未選択","未選択"),
            ("承認"  ,"承認"),
            ("未承認","未承認"),
        ]


class Plan(models.Model):

    name        = models.CharField(verbose_name="企画名",max_length=50)

    staff       = models.CharField(verbose_name="担当の許可",choices=STATUS,max_length=3,default="未選択")
    manager     = models.CharField(verbose_name="課長の許可",choices=STATUS,max_length=3,default="未選択")
    director    = models.CharField(verbose_name="部長の許可",choices=STATUS,max_length=3,default="未選択")
    company     = models.CharField(verbose_name="部長の許可",choices=STATUS,max_length=3,default="未選択")

