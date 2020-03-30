from django.urls import path
from corona_tweet_analysis import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='CategoryView'),
    path('tweets/', views.TwitterDataView.as_view(), name='TwitterDataView'),
    path('add_spam_count/', views.SpamCountView.as_view(), name='SpamCountView'),
    path('get_statistics/', views.StatisticsView.as_view(), name='StatisticsView'),
    path('hashtags/', views.HashtagsView.as_view(), name='HashtagView'),
    path('categoriessql/', views.CategorySqlView.as_view(), name='CategorySqlView'),
    path('report/world/', views.CoronaWorldReportView.as_view(), name='CoronaReportView'),
    path('report/', views.CoronaReportView.as_view(), name='CoronaReportView')
]

