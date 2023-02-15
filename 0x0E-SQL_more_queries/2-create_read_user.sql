-- creates a user_0d_2 and grants
-- SELECT priviledges on hbtn_0d_2 to the user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
