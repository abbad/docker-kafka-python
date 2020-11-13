### Docker Kafka with Python Consumer Producer

Sample demonstrating creating dockerized zookeeper and kafka. 
The app also demos how to use Python kafka client, please look inside 
producer and consumer main.py files. 

The producer takes the user input and puts sends to kafka and then the consumer reads what the user has put there. 

### To Start Demo

1. Make sure that you have docker installed. 
2. `docker-compose -f kafka-single-zk-single-kafka.yml up --build` 
This will start kafka and zookeeper. 
3. `docker-compose -f docker-python-producer.yml run producer bash -c 'python main.py'` 
This will start the message interface.
4. `docker-compose -f docker-python-consumer.yml up --build`  
This will start the consumer. 
