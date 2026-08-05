
create table products(name text DEFAULT 'Unknown' NOT NULL,price integer NOT NULL,quantity integer Default 0);





-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
