from django.conf.urls import url
from .views.AttachmentType import RestrictedView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^login_check/', obtain_jwt_token),
    url(r'^attachmenttypes$', RestrictedView.as_view()),
]
