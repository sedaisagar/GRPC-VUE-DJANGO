# quickstart/serializers.py
from django_socio_grpc import proto_serializers
from rest_framework import serializers
from quickstart.models import User, Post

from quickstart.grpc.quickstart_pb2 import (
    UserResponse,
    UserListResponse,
    PostResponse,
    PostListResponse,
)


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    # This line is written here as an example,
    # but can be removed as the serializer integrates all the fields in the model
    full_name = serializers.CharField(allow_blank=True)

    class Meta:
        model = User
        fields = "__all__"

        proto_class = UserResponse
        proto_class_list = UserListResponse


class PostProtoSerializer(proto_serializers.ModelProtoSerializer):
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

        proto_class = PostResponse
        proto_class_list = PostListResponse
