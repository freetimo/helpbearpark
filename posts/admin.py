from django.contrib import admin
from .models import Directory, Post, Task, Contact

class DirectoryAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'title',]
	list_display = ('id', 'title',)

class PostAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'title', 'created_at']
	list_display = ('id', 'title', 'created_at',)

class TaskAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'title',]
	list_display = ('id', 'title',)

class ContactAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'title', 'description']
	list_display = ('id', 'title', 'description', 'created_at')

admin.site.register(Directory, DirectoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Task, TaskAdmin)
