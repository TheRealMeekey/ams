from django.contrib import admin
from django.contrib.auth.models import User
from .models import Application, Executor
from django.contrib.admin import AdminSite

class ExecutorInline(admin.TabularInline):
	model = Executor
	insert_after = 'status'
	extra = 1

class ApplicationAdmin(admin.ModelAdmin):
    
	list_display = ('id', 'title', 'cabinet', 'published_date', 'status', 'author')
	list_filter = ('status', 'published_date')
	search_fields = ('title',)
	date_hierarchy = 'published_date'
	ordering = ['status', 'published_date']
	inlines = [ExecutorInline]

	class Media:
		css = {
			'all': (
				'css/admin.css',
			)
		}
        
admin.site.site_header = 'Сайт Администратора'
admin.site.site_title = 'Сайт Администратора'
admin.site.index_title = 'Администратор Helpdesk'
admin.site.site_url = '/helpdesk/application_list'

admin.site.register(Application, ApplicationAdmin)