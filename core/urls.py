from django.urls import path
from .views import feed_page, login_page, register_page

urlpatterns = [
    path('', feed_page, name="feed_page"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page")
]
