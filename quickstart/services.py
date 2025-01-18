# quickstart/services.py
from django_socio_grpc import generics

from quickstart.models import User, Post
from quickstart.serializers import UserProtoSerializer, PostProtoSerializer


# This service will have only the List and Retrieve actions
class UserActionService(generics.AsyncModelService):
    queryset = User.objects.all()
    serializer_class = UserProtoSerializer


# This service will have only the List and Retrieve actions
class UserService(generics.AsyncReadOnlyModelService):
    queryset = User.objects.all()
    serializer_class = UserProtoSerializer


# This service will have all the CRUD actions
class PostService(generics.AsyncModelService):
    queryset = Post.objects.all()
    serializer_class = PostProtoSerializer
