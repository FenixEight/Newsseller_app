CREATE SEQUENCE seq_users MINVALUE 1;
CREATE SEQUENCE seq_letters MINVALUE 1;


CREATE TABLE "users"(
user_id int not null default nextval('"seq_users"'::text) primary key,
full_name varchar,
email varchar
);

CREATE TABLE "letters"(
newsletter_id int not null default nextval('"seq_letters"'::text) primary key,
newsletter_name varchar,
from_name varchar,
from_email varchar,
subject varchar,
body_text varchar,
body_html varchar
);

