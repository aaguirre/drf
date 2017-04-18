from django.conf.urls import url, include


from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^sources/', views.sources, name='sources'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
