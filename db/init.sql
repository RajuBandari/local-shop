CREATE TABLE public.product (
    id int PRIMARY KEY,
    prod_name varchar(255),
    brand varchar(255),
    price decimal
);

INSERT INTO product (id, prod_name, brand, price)
VALUES
	(1, 'Galaxy S10', 'Samsung', 124.56)