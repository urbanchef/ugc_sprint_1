CREATE TABLE likes (
    user_uuid UUID,
    movie_uuid UUID,
    datetime DateTime,
    liked UInt8
) Engine = MergeTree
PARTITION BY toYYYYMM(datetime)
ORDER BY (movie_uuid, user_uuid, datetime);


CREATE TABLE likes_queue (
    user_uuid UUID,
    movie_uuid UUID,
    datetime DateTime,
    liked UInt8
)
ENGINE = Kafka
SETTINGS    kafka_broker_list = 'rc1b-5902ancqg160diig.mdb.yandexcloud.net:9091',
            kafka_topic_list = 'likes',
            kafka_group_name = 'clickhouse-likes-group',
            kafka_format = 'JSONEachRow';


CREATE MATERIALIZED VIEW likes_queue_mv TO likes AS
    SELECT user_uuid, movie_uuid, datetime, liked
    FROM likes_queue;
