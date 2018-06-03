from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group, Permission, User


'''---------------------------Заявка---------------------------'''

class Application(models.Model):

	STATUS_CHOICES = (
		('In the work', 'В работе'),
		('New', 'Новая'),
		('Complited', 'Завершена')
	)

	author = models.ForeignKey(User, related_name = 'author', verbose_name = 'Автор', 
								null = True, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, verbose_name = 'Заголовок')
	text = models.TextField(verbose_name = 'Описание проблемы')
	cabinet = models.CharField(max_length = 5, verbose_name = 'Кабинет')
	published_date = models.DateField(blank=True, null=True, default = timezone.now, 
										verbose_name = 'Дата')
	status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='New', 
								verbose_name = 'Статус')
	phone = models.CharField(max_length = 15, verbose_name = 'Телефон', null = True)
   
	class Meta:
		permissions = (
			("can_add_change", "Пользователь"),
			("can_close", "Техническая поддержка")
		)
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'
    
	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Executor(models.Model):
	application = models.ForeignKey('Application', null = True, verbose_name='Заявка', 
										on_delete=models.CASCADE, related_name = 'application_executor')
	owner = models.ForeignKey(User, related_name = 'owner', null = True, blank = True, 
			on_delete=models.CASCADE, limit_choices_to={ 'groups__name': 'ЦИК'}, 
			verbose_name = 'Исполнитель')
    

	class Meta:
		verbose_name = 'Исполнитель'
		verbose_name_plural = 'Исполнители'
    

