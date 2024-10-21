from django.db import models
from .managers import TaskManager, ProjectManager


class Project(models.Model):
    """
    Project model
    """

    title: models.CharField = models.CharField(
        max_length=64,
        unique=False,
        null=False,
        blank=False,
        verbose_name="Название проекта",
    )
    description: models.TextField = models.TextField(
        null=False, blank=False, verbose_name="Описание проекта"
    )
    count_assigners: models.IntegerField = models.IntegerField(
        default=0,
        null=False,
        blank=False,
        verbose_name="Кол-во сотрудников на проекте",
    )

    objects: ProjectManager = ProjectManager()

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Task(models.Model):
    """
    Task model
    """

    title: models.CharField = models.CharField(
        max_length=64,
        unique=False,
        null=False,
        blank=False,
        verbose_name="Название задачи",
    )
    description: models.TextField = models.TextField(
        null=False, blank=False, verbose_name="Описание задачи"
    )
    status: models.CharField = models.CharField(
        null=False,
        blank=False,
        choices=[
            ("todo", "ToDo"),
            ("process", "In Process"),
            ("done", "Done"),
        ],
        verbose_name="Статус задачи",
    )
    start_date: models.DateField = models.DateField(
        null=False, blank=False, verbose_name="Дата начала выполнения задачи"
    )
    end_date: models.DateField = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата окончания выполнения задачи",
    )
    project: models.ForeignKey = models.ForeignKey(
        to="Project",
        on_delete=models.CASCADE,
        related_name="tasks",
        null=False,
        blank=False,
        verbose_name="Проект определённой задачи",
    )

    objects: TaskManager = TaskManager()

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
