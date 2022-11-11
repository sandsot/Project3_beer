from django.db import models

from django.core.validators import MaxValueValidator

class Community(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Post Model
class Event(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # TODO : 장고의 URL Reverse 기능을 사용하기
        return f"/column/{self.pk}/"

    def __str__(self):
        return f"[{self.pk}] {self.title}"

