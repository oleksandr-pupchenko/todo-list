from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.content
