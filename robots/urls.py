from django.urls import path

from .views import RobotView
from .report import DownoloadExcelFile



urlpatterns = [
    path('', RobotView.as_view()),
    path('report/', DownoloadExcelFile.as_view(), name='weekly_report')
]