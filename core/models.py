from django.db import models

class League(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
     
class Team(models.Model):
    
    name = models.CharField(max_length=100)
    league = models.ForeignKey(
        League,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name