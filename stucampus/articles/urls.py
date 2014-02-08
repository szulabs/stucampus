from django.conf.urls import url, patterns

from stucampus.articles.views import AddView, ModifyView
from stucampus.articles.views import manage
from stucampus.articles.views import del_article, set_important
from stucampus.articles.views import CategoryView

from stucampus.articles.views import article_list, article_display


urlpatterns = patterns(
    '',
    url(r'^manage/$', manage, name='manage'),
    url(r'^add/$', AddView.as_view(), name='add'),
    url(r'^modify/$', ModifyView.as_view(), name='modify'),
    url(r'^del_article/$', del_article, name='del_article'),
    url(r'^set_important/$', set_important, name='set_important'),
    url(r'^category/$', CategoryView.as_view(), name='category'),

    url(r'^list/$', article_list, name='list'),
    url(r'^display/$', article_display, name='display'),
)
