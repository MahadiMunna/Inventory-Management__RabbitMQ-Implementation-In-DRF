import pika
import json
from app.models import Inventory


def inventory_actions():
    
    def callback(channel, method, properties, body):
        data = body.decode()
        data = json.loads(data)
        action = data["action"]
        item_name = data["item_name"]
        quantity = data["quantity"]
        print(f"Received {action} event for item {item_name} with quantity {quantity}")

        if action == "product_added":
            inventory, created = Inventory.objects.get_or_create(name=item_name)
            inventory.quantity += quantity
            inventory.save()
        elif action == "product_checked_out":
            inventory = Inventory.objects.get(name=item_name)
            inventory.quantity -= quantity
            inventory.save()

    params = pika.URLParameters("http://localhost:5672/")
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="inventory_queue")
    channel.basic_consume(
        queue="inventory_queue", on_message_callback=callback, auto_ack=True
    )
    print("Consumer is ready")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nConsumer stopped by user.")
    finally:
        if channel.is_open:
            channel.close()
        if connection.is_open:
            connection.close()
        print("Connection closed.")
