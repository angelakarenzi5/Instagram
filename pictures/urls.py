from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.pictures_of_day,name='picturesToday'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^view/profile$', views.profile, name='view-profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)