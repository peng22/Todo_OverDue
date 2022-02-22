from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    status_choices= (
              ("finished","finished"),
              ("pending","pending"),
              ("assigned","assigned")
                  )
    name=models.CharField(max_length=50)
    status = models.CharField(max_length=20,
                            choices=status_choices,
                             default='assigned')
    due_date=models.DateField()
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                               related_name="tasks"
                                )
    def __str__(self):
        return self.name
