from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('artists/', views.artist_list ),
    # path('songs/', views.song_list ),
    # path('lyrics/', views.lyric_list ),
    path('songs/', views.song_list),
    path('songs/<int:id>', views.song_detail),
    path('lyrics/', views.lyric_list ),
]