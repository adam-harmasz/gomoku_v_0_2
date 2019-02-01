from rest_framework import routers

from accounts.api import views as accounts_views
from gomoku_file_app.api import views as file_views
from gomoku_app.api import views as game_record_views


router = routers.DefaultRouter()
router.register(r'profiles', accounts_views.UserViewset)
router.register(r'files', file_views.GomokuRecordImageViewset)
router.register(r'game_records', game_record_views.GomokuRecordViewset)