"""
    Responsible for reading input from the producer. 
"""

from confluent_kafka import Producer, KafkaError
import socket

running = True

def consumer_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.value().decode('utf-8'))
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


from confluent_kafka import Consumer

conf = {
    'bootstrap.servers': "kafka1:19092",
    'group.id': "foo",
    'auto.offset.reset': 'smallest'
}


def main():
    consumer = Consumer(conf)

    consumer_loop(consumer, ['simple-message-topic'])


if __name__ == '__main__':
    main()

