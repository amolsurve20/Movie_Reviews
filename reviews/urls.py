from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /movie/
    url(r'^movie$', views.movie_list, name='movie_list'),
    # ex: /movie/5/
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),
    url(r'^movie/(?P<movie_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]