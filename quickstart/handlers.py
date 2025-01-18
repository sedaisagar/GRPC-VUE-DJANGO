# quickstart/handlers.py
from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from quickstart.services import UserService, PostService, UserActionService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("quickstart", server)
    app_registry.register(UserService)
    app_registry.register(UserActionService)
    app_registry.register(PostService)
