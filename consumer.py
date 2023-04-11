from confluent_kafka import Consumer, OFFSET_BEGINNING


if __name__ == "__main__":
    config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'python_example_group_1',

    }
    consumer = Consumer(config)

    def reset_offset(consumer, partitions):
        for p in partitions:
            p.offset = OFFSET_BEGINNING
            consumer.assign(partitions)

    topic = "user_actions"
    consumer.subscribe([topic], on_assign=reset_offset)

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                print("Ждем...")
            elif msg.error():
                print(f"Ошибка: {msg.error()}")
            else:
                print(f"Получено событие из топика {msg.topic()}:"
                      f" key = {msg.key().decode('utf-8'):12} value = {msg.value().decode('utf-8'):12}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
