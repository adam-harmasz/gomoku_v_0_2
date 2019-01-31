from rest_framework import routers

from accounts.api import views


router = routers.DefaultRouter()
router.register(r'profiles', views.UserViewset)
