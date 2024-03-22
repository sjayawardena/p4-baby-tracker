from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NappyChange(models.Model):
    """
    A model to enter and edit nappy changes
    """
    NAPPY_CONTENTS = (
        ('Wet', 'Wet'),
        ('Dirty', 'Dirty'),
        ('Nothing', 'Nothing')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baby_carer')
    date_and_time = models.DateTimeField()
    nappy_contents = models.CharField(max_length=10, choices=NAPPY_CONTENTS, null=False, blank=False)
    rash = models.BooleanField(default=False)
    notes = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-date_and_time']
    
    def __str__(self):
        return f"{self.nappy_contents} nappy from {self.date_and_time} | entered by {self.user}"

