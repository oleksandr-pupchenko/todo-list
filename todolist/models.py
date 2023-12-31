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
    is_done = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created_date"]

    def __str__(self):
        return f"Task {self.id}"
