from tasks.task_handler import TaskHandler

from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_text


class Task(models.Model):
    STATUS_IN_QUEUE = "in-queue"
    STATUS_IN_PROGRESS = "in-progress"
    STATUS_COMPLETED = "completed"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = (
        (STATUS_IN_QUEUE, STATUS_IN_QUEUE),
        (STATUS_IN_PROGRESS, STATUS_IN_PROGRESS),
        (STATUS_COMPLETED, STATUS_COMPLETED),
        (STATUS_FAILED, STATUS_FAILED)
    )

    NAME_CHOICES = (
        (task_name, task_name) for task_name in dir(TaskHandler) if "__" not in task_name
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=255, default=STATUS_IN_QUEUE)
    name = models.CharField(choices=NAME_CHOICES, max_length=255)
    exception = models.CharField(max_length=255, null=True, blank=True)
    worker_id = models.CharField(max_length=255, null=True, blank=True)

    date_created = models.DateTimeField(default=timezone.now)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return smart_text(f"Task '{self.name}' with status {self.status}")


class Foo(models.Model):
    bar = models.IntegerField()
