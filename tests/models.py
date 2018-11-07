from django.db import models


class BaseManagerModel(models.Model):
    @classmethod
    def create(cls):
        return cls.objects.create()


class TestManager(models.Manager):
    def get_queryset(self):
        return super(TestManager, self).get_queryset().none()


class RenameManagerModel(models.Model):
    instances = models.Manager()

    @classmethod
    def create(cls):
        return cls.instances.create()


class ReplaceManagerModel(models.Model):
    objects = TestManager()

    @classmethod
    def create(cls):
        return cls.objects.create()


class MultipleManagerModel(models.Model):
    objects = models.Manager()
    instances = TestManager()

    @classmethod
    def create(cls):
        return cls.objects.create()
