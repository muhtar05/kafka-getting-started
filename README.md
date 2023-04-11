# Apache Kafka для начинающих

Исходный код к статье https://gadjimuradov.ru/post/apache-kafka-vvedenie-dlya-nachinayushih/

Запустите брокер Apache Kafka локально на докере с помощью команды:

```
docker-compose up -d
```

Создайте топик следующим образом:

```
docker compose exec broker \
  kafka-topics --create \
    --topic user-actions \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1
```

Запуск продьюсера 
```shell
python producer.py 
```


Запуск косьюмера 
```shell
python consumer.py 
```