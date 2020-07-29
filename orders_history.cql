CREATE KEYSPACE orders WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'} AND durable_writes = true;

CREATE TABLE orders_history (
    order_id text,
    provider_id text,
    direction text,
    tags list<text>,
    description text,
    extra_data text,
    creation_date text,
    change_date text,
    status text,
    currency text,
    px float,
    vol float,
    PRIMARY KEY((creation_date), status)
);