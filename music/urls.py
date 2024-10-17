from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('song/<str:song_id>/', views.song_detail, name='song_detail'),
    path('singers/', views.singer_list, name='singer_list'),
    path('singer/<str:singer_id>/', views.singer_detail, name='singer_detail'),
    path('search/', views.search, name='search'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)