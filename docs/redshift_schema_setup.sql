-- One-time Redshift schema & table setup
-- Run once only

CREATE TABLE IF NOT EXISTS public.users_test (
    user_id INT,
    user_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS public.users_from_spark (
    user_id INT,
    user_name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS public.users_stage (
    user_id INT,
    user_name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS public.users_final (
    user_id INT,
    user_name VARCHAR(100),
    city VARCHAR(100)
);
