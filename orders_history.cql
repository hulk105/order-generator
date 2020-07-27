CREATE KEYSPACE orders 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'} 
AND durable_writes = true;

DESCRIBE keyspace orders;

USE orders;

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
    PRIMARY KEY((provider_id, direction, currency), order_id, status)
);

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
    PRIMARY KEY((creation_date), order_id, status)
);

SELECT * FROM orders_history WHERE order_id='0xdeadbeef00' ALLOW FILTERING;
SELECT * FROM orders_history where creation_date > '2020-06-05 16:20:00' and creation_date < '2020-06-05 16:30:00' ALLOW FILTERING ;