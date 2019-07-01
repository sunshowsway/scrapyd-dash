from django.urls import path

from . import views

urlpatterns = [
	path('', views.index_view, name="index"),
	path('add-server/', views.add_server, name="add_server"),
	path('delete-server/', views.delete_server, name="delete_server"),
]

from .operations.check_servers import CheckServers

c = CheckServers()
c.check_servers()