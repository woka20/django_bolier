from . import views
from an_rajaongkir import thirdapi
from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router= routers.DefaultRouter()
# router.register(r'heroes_man', views.HeroView)
# router.register(r'api/books', views.BookViewSet)



urlpatterns=[
    path('', include (router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('third-api/',thirdapi.ThirdAPIView.as_view(),name="thirdAPI"),
    path('generic/', views.AuthorView.as_view(), name='generic-sample' ),
    path('generic/book', views.BookViewSet.as_view(), name='book' ),
    path('generic/<int:pk>', views.AuthorProfileView.as_view(), name='sample' ),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth')
]