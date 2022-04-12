CREATE TABLE views (
    user_uuid UUID,
    movie_uuid UUID,
    datetime DateTime,
    progress UInt32
) Engine = MergeTree
PARTITION BY toYYYYMM(datetime)
ORDER BY (movie_uuid, user_uuid, datetime);


CREATE TABLE views_queue (
    user_uuid UUID,
    movie_uuid UUID,
    datetime DateTime,
    progress UInt32
)
ENGINE = Kafka
SETTINGS    kafka_broker_list = 'rc1b-5902ancqg160diig.mdb.yandexcloud.net:9091',
            kafka_topic_list = 'views',
            kafka_group_name = 'clickhouse-views-group',
            kafka_format = 'JSONEachRow';


CREATE MATERIALIZED VIEW views_queue_mv TO views AS
    SELECT user_uuid, movie_uuid, datetime, progress
    FROM views_queue;