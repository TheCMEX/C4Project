from base import views
from base.views import homepage, discuss, teams_c4, achievements, news, \
    newspost, board_topics, new_topic
from django.conf.urls import url


urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^discuss/$', discuss, name='discuss'),
    url(r'^discuss/board/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^discuss/board/(?P<pk>\d+)/$', board_topics, name='board_topics'),
    url(r'^discuss/board/(?P<pk>\d+)/new/$', new_topic, name='new_topic'),
    url(r'^teams/c4$', teams_c4),
    url(r'^achievements/$', achievements),
    url(r'^news/$', news),
    url(r'^news/post/(?P<id>[0-9]+)/$', newspost),
    url(r'^error/$', newspost),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),

]

