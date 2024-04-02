import pika
import os

from consumer.consumer_interface import mqConsumerInterface


class mqConsumer(mqConsumerInterface):

    def __init__(self, binding_key : str , exchange_name : str, queue_name : str):
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name

        self.setupRMQConnection()


    def setupRMQConnection(self) -> None:
        
        # Establish Connection to Rabbit
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.channel = self.connection.channel()


        # Declaring Queue
        self.channel.queue_declare(queue= "Queue Name")
        
        # Declaring Exchange
        self.exchange = self.channel.exchange_declare(exchange="Exchange Name")

        self.channel.queue_bind(
            queue= "Queue Name",
            routing_key=  self.binding_key,
            exchange="Exchange Name",
        )

        # Set-up Callback function for receiving messages
        self.channel.basic_consume ("Queue Name", self.channel.queue_bind, auto_ack=False)


        

        '''channel.basic_publish(
            exchange="Exchange Name",
            routing_key="Routing Key",
            body="Message",
        )'''



        #Callback receive msgs
        channel.basic_consume(
    "Queue Name", Function Name, auto_ack=False
        )



        #return super().setupRMQConnection()









