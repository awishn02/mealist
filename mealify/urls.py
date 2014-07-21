from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('mealifyapp.views',
    url(r'^$', 'index'),
    url(r'^recipes/$', 'recipes'),
    url(r'^recipes/(?P<recipe_id>\d+)/$', 'recipe')
)
