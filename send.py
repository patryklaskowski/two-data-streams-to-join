import pika

HOST = 'localhost'

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST, credentials=credentials))
channel = connection.channel()

print(connection.is_open)

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()

print(connection.is_open)
