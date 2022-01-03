import time
import threading
import uuid

from django.core.management.base import BaseCommand
from django.utils import timezone

from tasks.models import Task
from tasks.task_handler import TaskHandler


lock = threading.Lock()


class Command(BaseCommand):
    help = ""
    worker_count = 3

    def handle(self, *args, **options):
        workers = list()

        for i in range(self.worker_count):
            worker_id = uuid.uuid1()
            thread = threading.Thread(target=self.work, args=[worker_id])
            workers.append({
                "thread": thread,
                "worker_id": worker_id
            })
            thread.start()

        worker_ids = [worker["worker_id"] for worker in workers]
        Task.objects.exclude(worker_id__in=worker_ids).filter(status=Task.STATUS_IN_PROGRESS).update(status=Task.STATUS_FAILED)

    def work(self, worker_id):
        while(True):
            with lock:
                task = Task.objects.order_by("date_created").filter(status__in=[Task.STATUS_IN_QUEUE, Task.STATUS_FAILED]).first()

                if task:
                    task.status = Task.STATUS_IN_PROGRESS
                    task.worker_id = worker_id
                    task.save()
                else:
                    continue

            try:
                print(f"Worker {worker_id} is executing the task: {task.name}")
                getattr(TaskHandler, task.name)()
            except Exception as e:
                task.status = Task.STATUS_FAILED
                task.exception = e.__str__()
                task.save()
                continue

            task.status = Task.STATUS_COMPLETED
            task.date_completed = timezone.now()
            task.save()

            time.sleep(1)
