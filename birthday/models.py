from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from .validators import real_age

User = get_user_model()

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20, blank=True, help_text='Необязательное поле')
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    
    author = models.ForeignKey(
        User, 
        verbose_name='Автор записи', 
        on_delete=models.CASCADE, 
        null=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})