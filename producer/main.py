"""
    Responsible for taking user input and sending it to the kafka consumer. 
"""

from confluent_kafka import Producer
import socket

conf = {
    'bootstrap.servers': "kafka1:19092",
    'client.id': socket.gethostname()
}

def main():
    producer = Producer(conf)

    print('Write To Consumer')

    while True: 
        # read user input. 
        value = input("")

        producer.produce('simple-message-topic', key="key", value=value)
        print("Message added " + value)
    
        producer.flush()


if __name__ == '__main__':
    main()