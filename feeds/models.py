from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Feed(models.Model):
    """
    A model to enter baby's feeds
    """

    FEED_TYPE = (
        ("formula", "Formula"),
        ("breast", "Breast"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="feeds_list")
    date_and_time = models.DateTimeField()
    feed_type = models.CharField(
        max_length=10, choices=FEED_TYPE, null=False, blank=False
    )
    formula_amount_ml = models.IntegerField(default=0)
    breast_feed_time_minutes = models.IntegerField(default=0)
    notes = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["-date_and_time"]

    def __str__(self):
        return (
            f"{self.feed_type} feed from \
            {self.date_and_time} | entered by {self.user}"
        )
