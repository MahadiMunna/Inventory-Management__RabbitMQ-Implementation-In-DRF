import pika
import json

def publish_task(data):
    params = pika.URLParameters("http://localhost:5672/")
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="inventory_queue")
    data = json.dumps(data)
    channel.basic_publish(exchange="", routing_key="inventory_queue", body=data)
    channel.close()