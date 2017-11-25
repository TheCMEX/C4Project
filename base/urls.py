from base import views
from base.views import homepage, discuss, teams_c4, teams_face2face, teams_isopromat, achievements, product, news, \
    newspost
from django.conf.urls import url


urlpatterns = [
    url(r'^$', homepage),
    url(r'^discuss/$', discuss),
    url(r'^discuss/base/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^discuss/base/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^teams/c4$', teams_c4),
    url(r'^teams/face2face$', teams_face2face),
    url(r'^teams/isopromat$', teams_isopromat),
    url(r'^achievements/$', achievements),
    url(r'^product/$', product),
    url(r'^news/$', news),
    url(r'^news/post/(?P<id>[0-9]+)/$', newspost),
    url(r'^error/$', newspost),
]
