from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += [
    path('signup/', views.signup,name='signup'),
]
urlpatterns += [
    path('user/', views.user_home.as_view(), name='user-home'),
    path('user/task/<uuid:pk>', views.taskDetailView.as_view(), name='task-detail'),
]
urlpatterns += [
    path('user/profile', views.profile, name='profile'),
]

urlpatterns += [  
    path('user/task/create/', views.taskCreate.as_view(), name='task_create'),
    path('user/task/<uuid:pk>/update/', views.taskUpdate.as_view(), name='task_update'),
    path('user/task/<uuid:pk>/delete/', views.taskDelete.as_view(), name='task_delete'),
]
'''
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns +=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
'''