from django.db import models


class User(models.Model):
    username = models.TextField(verbose_name='Юзернэйм')
    telegram_id = models.CharField(verbose_name='Телеграм айди', max_length=30)

    def __str__(self):
        return f"{self.username} | {self.telegram_id}"


class Valentine(models.Model):
    sender = models.TextField(verbose_name='Отправитель', blank=True)
    recipient = models.ForeignKey(User, verbose_name='Получатель', on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(verbose_name='Статус валентинки', default=False)
    is_publish = models.BooleanField(verbose_name='Публичность', default=False)
    text = models.TextField(verbose_name='Коментарий к валентинке', blank=True)
    file_id = models.TextField(verbose_name='Фото айди', blank=True)

    def __str__(self):
        return f"{self.sender} | {self.recipient} | {self.status}"

