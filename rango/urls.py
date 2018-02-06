from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    
    # \w denotes a sequence of alphanumeric characters
    # \- denotes any hyphens
    # [\w\-]+ denotes as many of these combined as we like
    # The sequence will be stored in the parameter <category_name_slug>
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    
    
]
