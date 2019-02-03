from django.db import models

# Create your models here.
class Dpt_user(models.Model):
    dptname = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    userdesc = models.CharField(max_length=64)
    stat = models.BooleanField(default=True)
    class Meta():
        db_table = "dpt_user"
    @classmethod
    def creator(cls,username,userdesc,dpt_name):
        b = Dpt_user()
        b.dptname = dpt_name
        b.userdesc = userdesc
        b.username = username
        return b
    def show(self):
        b = Dpt_user.objects.values()
        return b

