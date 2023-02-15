-- creates a new table unique_id
-- where id is 1 by default and is unique
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
