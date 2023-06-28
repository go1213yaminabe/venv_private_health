from django.db import models
class Health(models.Model):
    morning_state = models.TextField(verbose_name='朝の症状', blank=True, null=True)
    morning_temperature = models.TextField(verbose_name='朝の体温', blank=True, null=True)
    night_state = models.TextField(verbose_name='夜の症状', blank=True, null=True)
    night_temperature = models.TextField(verbose_name='夜の体温', blank=True, null=True)
    note = models.TextField(verbose_name='備考', blank=True, null=True)
    niti = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)


    class Meta:
        verbose_name_plural = 'health'

    def __str__(self):
        return self.title
