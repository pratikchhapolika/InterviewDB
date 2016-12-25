from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'interview.views.home', name='home'),
    # url(r'^search/$', 'interview.views.search', name='search'),
    url(r'^company/(?P<username>[\w.@+-]+)/questions/(?P<slug>[\w-]+)/$', 'interview.views.questions', name='questions'),
    url(r'^contact/$', 'interview.views.contact', name='contact'),
    url(r'^company/(?P<username>[\w.@+-]+)/$', 'interview.views.company', name='company'),
    # url(r'^blog/', include('blog.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
