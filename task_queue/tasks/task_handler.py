import time
import os


class TaskHandler():

    @staticmethod
    def print_something():
        print("something")

    @staticmethod
    def save_foo_object():
        from tasks.models import Foo
        Foo.objects.create(bar=20)

    @staticmethod
    def sleep():
        time.sleep(2.7)

    @staticmethod
    def raise_exception():
        assert False

    @staticmethod
    def long_task():
        for i in range(10):
            print(f"{i} / worker pid: {os.getpid()}")
            time.sleep(2)
        print('complete')
