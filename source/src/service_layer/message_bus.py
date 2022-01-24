import logging
from typing import Callable, Dict, Type, TYPE_CHECKING

from src.domain import commands

logger = logging.getLogger(__name__)


class MessageBus:

    def __init__(self, command_handlers: Dict[Type[commands.Command], Callable]):
        self.command_handlers = command_handlers
        self.queue = []

    def handle(self, message):
        """General message handler"""

        if isinstance(message, commands.Command):
            result = self.handle_command(message)
        else:
            raise Exception(f'`{message}` is not Command.')

        return result

    def handle_command(self, command: commands.Command):
        """Command handler"""
        logger.debug(f'Trying to handle command `{command}`.')

        try:
            handler = self.command_handlers[type(command)]
            result = handler(command)
        except Exception:
            logger.exception(f'Exception handling command {command}.')
            raise

        logger.debug(f'Command `{command}` handled successfully with result equal {result}.')
        return result
