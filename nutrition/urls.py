from django.conf.urls import url
from . import views

app_name = 'nutrition'

urlpatterns = [
    # /nutrition/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /nutrition/<daily_diet_totals_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/nutrition/daily_diet_totals/add
    url(r'daily_diet_totals/add/$', views.DailyDietTotalsCreate.as_view(), name='daily_diet_totals-add'),
    #/nutrition/daily_diet_totals/<daily_diet_totals_id>
    url(r'daily_diet_totals/(?P<pk>[0-9]+)/$', views.DailyDietTotalsUpdate.as_view(), name='daily_diet_totals-update'),
    #/nutrition/daily_diet_totals/<daily_diet_totals_id>/delete
    url(r'daily_diet_totals/(?P<pk>[0-9]+)/delete/$', views.DailyDietTotalsDelete.as_view(), name='daily_diet_totals-delete'),
]
