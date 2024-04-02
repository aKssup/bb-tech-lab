import pika
import os
from ..producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name):
        # Save parameters to class variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        # Call setupRMQConnection
        self.setupRMQConnection()
        pass

    def setupRMQConnection(self):
        # Set-up Connection to RabbitMQ service
        self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange="Exchange Name")
        pass

    def publishOrder(self, message: str):
        # Basic Publish to Exchange
        self.channel.basic_publish(
        exchange="Exchange Name",
        routing_key="Routing Key",
        body=message,
        )

        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()
        pass
