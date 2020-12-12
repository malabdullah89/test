from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.name
