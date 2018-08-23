from django.db import models

# Create your models here.

class Sa_deploy(models.Model):
    section_name = models.CharField(max_length=32)
    key_name = models.CharField(max_length=32)
    value_name = models.CharField(max_length=32)
    is_delete = models.BooleanField(default=False)
    class Meta():
        db_table = 'sa_deploy'
    @classmethod
    def creator(cls,section_name,key_name,value_name):
        b = Sa_deploy()
        b.section_name = section_name
        b.key_name = key_name
        b.value_name = value_name
        return b
    def show(self):
        b = Sa_deploy.objects.values()
        return b
