from django.db import models

CHOICE_FIELD = (('complete', 'completed'), ('pending', 'pending'))


class Task(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=12, choices=CHOICE_FIELD)

    def __str__(self):
        return self.task
