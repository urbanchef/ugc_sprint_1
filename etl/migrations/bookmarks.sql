CREATE TABLE bookmarks (
    user_uuid UUID,
    movie_uuid UUID,
    datetime DateTime,
    bookmarked UInt8
) Engine = MergeTree
PARTITION BY toYYYYMM(datetime)
ORDER BY (movie_uuid, user_uuid, datetime);


CREATE TABLE bookmarks_queue (
    user_uuid UUID,
    movie_uuid UUID,
    datetime DateTime,
    progress UInt8
)
ENGINE = Kafka
SETTINGS    kafka_broker_list = 'rc1b-5902ancqg160diig.mdb.yandexcloud.net:9091',
            kafka_topic_list = 'bookmarks',
            kafka_group_name = 'clickhouse-bookmarks-group',
            kafka_format = 'JSONEachRow';


CREATE MATERIALIZED VIEW bookmarks_queue_mv TO bookmarks AS
    SELECT user_uuid, movie_uuid, datetime, progress
    FROM bookmarks_queue;