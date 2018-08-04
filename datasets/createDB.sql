CREATE DATABASE ouvido_musical;
CREATE USER ouvidoMusicalAPI WITH PASSWORD 'lovelovelove';
ALTER ROLE ouvidoMusicalAPI SET client_encoding TO 'utf8';
ALTER ROLE ouvidoMusicalAPI SET default_transaction_isolation TO 'read committed';
ALTER ROLE ouvidoMusicalAPI SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ouvido_musical TO ouvidoMusicalAPI;
