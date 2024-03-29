from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

# Create your models here.

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
    formula_amount_ml = models.IntegerField(null=True, blank=True)
    breast_feed_time_minutes = models.IntegerField(null=True,blank=True)
    notes = models.CharField(max_length=200, blank=True)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="feeds/",
        force_format="WEBP",
        blank=False,
        null=False,
        default = "static/images/baby-tracker-default-image.jpg",
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False, default="Tracker.Baby default image")
    
    class Meta:
        ordering = ['-date_and_time']
    
    def __str__(self):
        return f"{self.feed_type} feed from {self.date_and_time} | entered by {self.user}"
