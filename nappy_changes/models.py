from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NappyChange(models.Model):
    """
    A model to enter and edit nappy changes
    """
    NAPPY_CONTENTS = (
        ('wet', 'Wet'),
        ('dirty', 'Dirty'),
        ('nothing', 'Nothing')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nappy_changes_list')
    date_and_time = models.DateTimeField()
    nappy_contents = models.CharField(max_length=10, choices=NAPPY_CONTENTS, null=False, blank=False)
    rash = models.BooleanField(default=False)
    notes = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['-date_and_time']
    
    def __str__(self):
        return f"{self.nappy_contents} nappy from {self.date_and_time} | entered by {self.user}"
    

class Feed(models.Model):
    """
    A model to enter baby's feeds
    """
    
    FEED_TYPE = (
        ('formula', 'Formula'),
        ('breast', 'Breast'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feeds_list')
    date_and_time = models.DateTimeField()
    feed_type = models.CharField(max_length=10, choices=FEED_TYPE, null=False, blank=False)
    formula_amount_ml = models.IntegerField(blank=True)
    breast_feed_time_minutes = models.IntegerField(blank=True)
    notes = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['-date_and_time']
    
    def __str__(self):
        return f"{self.feed_type} feed from {self.date_and_time} | entered by {self.user}"