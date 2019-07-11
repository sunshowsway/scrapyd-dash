from django.urls import path

from . import views

urlpatterns = [
	path('', views.ServersListView.as_view(), name="servers"),
	path('tasks/', views.TasksListView.as_view(), name="tasks"),
	path('tasks/add/', views.TasksAddView.as_view(), name="add_task"),
	path('tasks/<slug:pk>', views.TaskDetailsView.as_view(), name="task_details"),
	
	path('api/v3/get_projects/', views.get_projects, name="get_projects"),
	path('api/v3/get_versions/', views.get_versions, name="get_versions"),
	path('api/v3/get_spiders/', views.get_spiders, name="get_spiders"),
]