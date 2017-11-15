from boards.views import homepage
from django.conf.urls import url

urlpatterns = [
    url(r'^$', homepage)
]
