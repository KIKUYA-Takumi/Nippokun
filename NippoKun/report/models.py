from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Report(models.Model):
    report_author = models.ForeignKey(User, related_name='report_author')
    report_title = models.CharField(max_length=50)
    report_content = models.TextField(max_length=999)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Score(models.Model):
    report = models.ForeignKey(Report, related_name='score')
    score_author = models.ForeignKey(User, related_name='score_author')
    score = models.IntegerField(
        default=3,
        choices=(
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
        )
    )
    evaluate_point = models.TextField(max_length=30)
    comment = models.TextField(max_length=999, blank=True)
    scored_at = models.DateTimeField(auto_now=True)
