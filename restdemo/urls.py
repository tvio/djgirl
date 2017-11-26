from django.conf.urls import url,include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from . import views
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'detail', views.snippet_detail,  base_name='detail')
router.register(r'list', views.snippet_list,  base_name='detail')


urlpatterns = [


   url(r'^/xxx', views.schema_view),
   url(r'^/xxx', include(router.urls)),
   url(r'^/xxx', include('rest_framework.urls', namespace='rest_framework')),
   # url(r'^restdemo/v1/(?P<pk>[0-9]+)/$', views.snippet_detail),
]