from confluent_kafka import Producer
from random import choice


if __name__ == "__main__":
    config = {'bootstrap.servers': 'localhost:9092'}

    producer = Producer(config)

    topic = "user_actions"
    user_ids = ['Ivan', 'Andrey', 'Igor', 'Sergey', 'Mukhammad', 'Ramil']
    actions = ['register', 'authentication', 'logout', 'subcribe', 'like']

    count = 0
    for _ in range(10):

        user_id = choice(user_ids)
        product = choice(actions)
        producer.produce(topic, product, user_id)
        count += 1

    producer.poll(10000)
    producer.flush()