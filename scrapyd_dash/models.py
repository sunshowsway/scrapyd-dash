from django.db import models
from django.core.validators import MaxValueValidator


class ScrapydServer(models.Model):
    ip = models.CharField(max_length=128, null=False, blank=False)
    port = models.CharField(max_length=32, null=False, blank=False)
    node_name = models.CharField(max_length=256)
    status = models.CharField(max_length=64)
    status_message = models.CharField(max_length=512, null=True)
    pending_tasks = models.PositiveIntegerField(default=0)
    finished_tasks = models.PositiveIntegerField(default=0)
    running_tasks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s%s" % (self.ip.replace('.', ''),
                         self.port.replace('.', ''))

    class Meta:
        unique_together = (("ip", "port"),)
        ordering = ['-status']
        db_table = 'scrapyd_dash_servers'

class ScrapydProject(models.Model):
    server = models.ForeignKey(ScrapydServer,
                        on_delete=models.CASCADE,
                        null=False,
                        blank=False)
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("server", "name"),)
        db_table = 'scrapyd_dash_projects'

class ScrapydProjectVersion(models.Model):
    version = models.CharField(primary_key=True, max_length=125)
    project = models.ForeignKey(ScrapydProject,
                                 on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.version


class Task(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    
    project = models.ForeignKey(ScrapydProject,
                         on_delete=models.CASCADE,
                         null=False,
                         blank=False)
    spider = models.CharField(max_length=256, null=False)
    status = models.CharField(max_length=64, null=False)

    server = models.ForeignKey(ScrapydServer,
                        on_delete=models.CASCADE,
                        null=False,
                        blank=False)

    pages = models.PositiveIntegerField(null=True)
    items = models.PositiveIntegerField(null=True)
    pid = models.PositiveIntegerField(null=True)
    runtime = models.CharField(max_length=64, null=True, blank=True)
    start_datetime = models.DateTimeField(null=True, blank=True)
    finished_datetime = models.DateTimeField(null=True, blank=True)

    log_href = models.CharField(max_length=1024, null=True)
    items_href = models.CharField(max_length=1024, null=True)

    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(null=False, default=False)

    """
    Prints out start datetime in a custom format
    """
    def print_start(self):
        return self.start_datetime.strftime('%Y-%m-%d %H:%M')

    """
    Prints out finished datetime in a custom format
    """
    def print_finish(self):
        return self.finished_datetime.strftime('%Y-%m-%d %H:%M')

    class Meta:
        ordering = ['-create_datetime', '-status']
        db_table = 'scrapyd_dash_tasks'

class ScheduledTasks(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=256, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    project = models.CharField(max_length=256, null=False)
    spider = models.CharField(max_length=256, null=False)

    year = models.PositiveIntegerField(null=False)
    month = models.PositiveIntegerField(null=False,
                                 validators=[MaxValueValidator(12)])
    day = models.PositiveIntegerField(null=False,
                               validators=[MaxValueValidator(32)])
    week = models.PositiveIntegerField(null=False)
    day_of_week = models.PositiveIntegerField(null=False,
                                       validators=[MaxValueValidator(7)])
    hour = models.PositiveIntegerField(null=False,
                                validators=[MaxValueValidator(24)])
    minute = models.PositiveIntegerField(null=False,
                                  validators=[MaxValueValidator(60)])
    second = models.PositiveIntegerField(null=False,
                                  validators=[MaxValueValidator(60)])

    deleted = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'scrapyd_dash_scheduled_tasks'