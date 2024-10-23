from django.db import models


class ProjectQuerySet(models.QuerySet):
    """
    QuerySet for ProjectManager
    """

    def tasks(self):
        return self.prefetch_related("tasks")


class ProjectManager(models.Manager):
    """
    Project Manager
    """

    def get_queryset(self):
        return ProjectQuerySet(model=self.model, using=self._db)

    def tasks(self):
        return self.get_queryset().tasks()


class TaskQuerySet(models.QuerySet):
    """
    QuerySet for TaskManager
    """

    def project(self):
        return self.select_related("project")


class TaskManager(models.Manager):
    """
    Task Manager
    """

    def get_queryset(self):
        return TaskQuerySet(model=self.model, using=self._db)

    def project(self):
        return self.get_queryset().project()
