from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query/<str:city>/<str:state>/<str:type>/<int:price_limit>/<int:thc_limit>', views.query_without_keywords, name='query_without_keywords'),
    path('query/<str:city>/<str:state>/<str:type>/<str:price_limit>/<int:thc_limit>/<str:keywords>/', views.query_with_keywords, name='connections'),
    # path('connections/', views.connections, name='connections'),
    # path('connections/<int:connection_id>/test_connection', views.test_connection, name='test_connection'),
    # path('connections/<int:connection_id>/close_connection', views.close_connection, name='close_connection'),
    # path('connections/<int:connection_id>/open_connection', views.open_connection, name='open_connection'),
    # path('<int:report_id>/get', views.get_report, name='get_report'),
    # path('<int:report_id>/getjson', views.get_report_json, name='get_report_json'),
    # path('<int:report_id>/run', views.run_report, name='run_report'),
]