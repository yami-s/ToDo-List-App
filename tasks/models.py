from django.db import models


class ToDo(models.Model):
    content = models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    creation_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.content