from django.conf.urls import url
from .views import AttachmentType, PublicationType
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^login_check/', obtain_jwt_token),

    url(r'^attachmenttypes$', AttachmentType.View.as_view()),
    url(r'^publicationtypes$', PublicationType.View.as_view()),
]
