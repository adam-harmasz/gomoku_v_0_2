from django.urls import path

from . import views

urlpatterns = [
    path(
        'upload_file',
        views.ExtractDataRedirectView.as_view(),
        name='upload-file'
    )
]