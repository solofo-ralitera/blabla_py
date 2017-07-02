from django.conf.urls import url
from .views import AttachmentType, PublicationType, Comment, Attachment, Publication, AttachmentComments
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^login_check/', obtain_jwt_token),

    url(r'^attachmenttypes/(\d*)$', AttachmentType.View.as_view()),

    url(r'^publicationtypes/(\d*)$', PublicationType.View.as_view()),

    url(r'^comments/(\d*)$', Comment.View.as_view()),

    url(r'^attachments/(\d*)$', Attachment.View.as_view()),
    url(r'^attachments/(?P<attachment_id>\d+)/comments$', AttachmentComments.View.as_view()),

    url(r'^publications/(\d*)$', Publication.View.as_view()),

]
