from django.conf.urls import url
from basic_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^contacts/$',views.UserContactListView.as_view(),name='contacts_list'),
    url(r'^contacts_details/(?P<pk>\d+)$',views.USerContactDetailView.as_view(),name='contacts_detail'),

]
