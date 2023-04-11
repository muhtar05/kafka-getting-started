from confluent_kafka import Producer
from random import choice


if __name__ == "__main__":
    print("Запускаем наш producer")
    config = {'bootstrap.servers': 'localhost:9092'}

    producer = Producer(config)

    topic = "user-actions"
    user_ids = ['Иван', 'Андрей', 'Игорь', 'Сергей', 'Мухаммад', 'Рамиль']
    actions = ['регистрация', 'аутентификаця', 'выход', 'подписка', 'лайк']

    def delivery_callback(err, msg):
        if err:
            print(f'Ошибка: Сообщение не доставлено : {err}')
        else:
            print(f"Публикуем сообщение в топик: {msg.topic()}:"
                  f"с ключом = {msg.key().decode('utf-8'):12} и значением = {msg.value().decode('utf-8'):12}")

    count = 0
    for _ in range(10):
        user_id = choice(user_ids)
        product = choice(actions)
        producer.produce(topic, product, user_id, callback=delivery_callback)
        count += 1

    producer.poll(10000)
    producer.flush()
