"""accounts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from register.views import RegView, PaidReg, OfflineReg, SchoolReg, Certi, SearchByView
from controlroom.views import PostCreate, Android, VenueDetail, Download, VenueUpdate, Winnerapi, EventNav, Intermediate, WinnerDownload, EventView, ControlRoomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('online/',RegView.as_view(),name='home'),
    path('paidreg/',PaidReg.as_view(),name='paidreg'),
    path('offlinereg/',OfflineReg.as_view(),name='offline'),
    path('studentreg/',SchoolReg.as_view(),name='stud'),
    path('controlroom/',ControlRoomView.as_view(),name='controlroom'),
    path('eventpage/(?P<event>[\w,()-]+)/$',EventView.as_view(),name='eventview'),
    path('eventpage/',Intermediate,name='eventview'),
    path('eventnav/',EventNav.as_view(),name='eventnav'),
    path('venuepage/(?P<venue>[\w,()-]+)/$',VenueDetail.as_view(),name='venueview'),
    path('certificate/',Certi,name='certificate'),
    path('searchby/$',SearchByView.as_view(),name='searchby'),
    path('eventpage/(?P<pk>[\w,()-]+)/create/$',PostCreate,name='controolroom'),
    path('venuepage/(?P<ven>[\w,()-]+)/create/$',VenueUpdate.as_view(),name='venupdate'),
    path('eventpage/(?P<eve>[\w,()-]+)/download/$',Download.as_view(),name='down'),
    path('eventpage/(?P<eve>[\w,()-]+)/winnerdownload/$',WinnerDownload.as_view(),name='windown'),
    path('api/(?P<pk>[\w,()-]+)',Android.as_view(),name='api'),
    path('winnerapi/(?P<pk>[\w,()-]+)',Winnerapi.as_view(),name='winnerapi')
]