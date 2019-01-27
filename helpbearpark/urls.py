from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from posts import views
from .routers import router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('help_bear/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
	path('api/', include(router.urls)),
	path('ckeditor/', include('ckeditor_uploader.urls')),
	path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
	path('', views.home, name="home"),
	path('post/<str:choice>/', views.directory, name="directory"),
	path('post/<str:choice>/<str:slug>', views.post_list, name="post_list"),
	path('post/<str:choice>/<str:directory_slug>/<str:post_slug>', views.post_detail, name="post_detail"),
	path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'posts.views.handler404'
handler500 = 'posts.views.handler500'
