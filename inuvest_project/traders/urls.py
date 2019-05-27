from django.conf.urls import url

from traders import views

urlpatterns = [
    #for my benefit
    url(r'upload_file/', views.upload_file),

]
