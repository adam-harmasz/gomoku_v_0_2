from django.urls import path

from . import views

app_name = 'gomoku_app'


urlpatterns = [
    path('upload_file/',
         views.ExtractDataRedirectView.as_view(),
         name='upload-file'
    ),
    path('download_file/',
         views.DownloadExtractDataRedirectView.as_view(),
         name='download-file'),
    path('game_list', views.GameRecordListView.as_view(), name='game-list'),
    path('game/<int:pk>',
         views.GameRecordDetailView.as_view(),
         name='game-detail'),
]
