"""Music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from Music.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
# from django.contrib import admin
from rest_framework.authtoken import views
from songs.views import SongsListViewSet, CategoryViewset, HotSearchsViewset
from songs.views import IndexCategoryViewset
from singers.views import SingerViewset
from cds.views import CDsViewset
from users.views import SmsCodeViewset, UserViewset
from user_operations.views import UserFavViewset, LeavingMessageViewset

router = DefaultRouter()

#配置songs的url
router.register(r'songs', SongsListViewSet, base_name="songs")
#首页歌曲系列数据
router.register(r'indexsongs', IndexCategoryViewset, base_name="indexsongs")
#配置category的url
router.register(r'categorys', CategoryViewset, base_name="categorys")
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
router.register(r'singers', SingerViewset, base_name="singers")
router.register(r'cds', CDsViewset, base_name="cds")
router.register(r'codes', SmsCodeViewset, base_name="codes")
router.register(r'users', UserViewset, base_name="users")
#收藏
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
#留言
router.register(r'messages', LeavingMessageViewset, base_name="messages")
songs_list = SongsListViewSet.as_view({
    'get': 'list',
})
# from django.views.generic import TemplateView
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    # url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'docs/', include_docs_urls(title="Music")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),
]
