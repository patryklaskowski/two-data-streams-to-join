import pika
from abc import ABC, abstractmethod
from threading import Thread


class AbstractSender(ABC):

    def __init__(self):
        self.threads = []

    @abstractmethod
    def send(self, data):
        """Sends data"""

    def send_async(self, data):
        """Sends data asynchronously"""
        t = Thread(target=self.send, args=(data,))
        self.threads.append(t)
        t.start()

    def alive_threads_number(self):
        """Returns number of alive threads"""
        print(f'Number of threads in list: {len(self.threads)}')
        return len([t for t in self.threads if t.is_alive()])


# TODO: Check and activate RabbitMQSender
# class RabbitMQSender(AbstractSender):
#
#     def __init__(self, host='localhost', username='guest', password='guest'):
#         self.__init__()
#         self.host = host
#
#         credentials = pika.PlainCredentials(username, password)
#         params = pika.ConnectionParameters(host, credentials=credentials)
#         self.connection = pika.BlockingConnection(params)
#         self.channel = self.connection.channel()
#
#     def declare_channel(self, name):
#         self.channel.queue_declare(queue=name)
#
#     def send(self, data):
#         self.channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
#
#     def __del__(self):
#         self.connection.close()


class FakeSender(AbstractSender):

    def send(self, data):
        print(f'FakeSender sends `{data}`')
