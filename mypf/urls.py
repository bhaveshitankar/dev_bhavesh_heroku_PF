from django.urls import path, re_path
from django.conf import settings
from . import views #import views
# from django.urls import patterns, url
import django
# adding url
urlpatterns = [
    path('', views.index, name='home'), #home
    path('tryMore', views.tryMore, name='tryMore'),
    path('portfolio', views.portfolio, name='portfolio'), #portfolio
    path('contact', views.contact, name='contact'), #contact
    path('cdn/<int:id>/', views.getdataAPI, name='cdn'), #contact
    # re_path(r'media/mypf/files/(*.pdf)', django.views.static.serve, {'document_root': settings.MEDIA_ROOT,}),
    # re_path(r'media/mypf/portfolio_config/(config.json)', django.views.static.serve, {'document_root': settings.MEDIA_ROOT,})
]

# if settings.DEBUG:
#     #urlpatterns += staticfiles_urlpatterns() #this servers static files and media files.
#     #in case media is not served correctly
#     urlpatterns.append(re_path(r'^media/(?P<path>.*)$', django.views.static.serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }))
    