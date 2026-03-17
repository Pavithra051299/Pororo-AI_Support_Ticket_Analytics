CREATE TABLE tickets (
ticket_id SERIAL PRIMARY KEY,
subject TEXT,
priority VARCHAR(20),
created_at TIMESTAMP
);