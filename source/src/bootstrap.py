import inspect
from typing import Callable, Dict

from src.adapters import sender
from src.service_layer import handlers, message_bus


def bootstrap(
        sender: sender.AbstractSender = sender.FakeSender(),
):
    """
    Sets up required dependencies for command handlers
    """
    dependencies = {
        'sender': sender
    }
    dependency_injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return message_bus.MessageBus(
        command_handlers=dependency_injected_command_handlers
    )


def inject_dependencies(handler: Callable, dependencies: Dict) -> Callable:
    """
    Dependency injection for handlers.
    Returns automatically filled partial function (final handlers will require only a message to run).
    """
    params = inspect.signature(handler).parameters
    injected_dependencies = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **injected_dependencies)
