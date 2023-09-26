from datetime import datetime, timedelta

from django.db import models
from django.db.models import Count


class Robot(models.Model):
    # serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.model}-{self.version}"

    @classmethod
    def get_weekly_count(cls):
        week_ago = datetime.now() - timedelta(days=7)
        return cls.objects.filter(created__gte=week_ago).values('model', 'version').annotate(mcount=Count('version'))
