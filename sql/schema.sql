CREATE TABLE support_tickets (
    ticket_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    customer_age SMALLINT,
    customer_gender VARCHAR(20),
    date_of_purchase DATE,
    ticket_type VARCHAR(100) NOT NULL,
    ticket_status VARCHAR(50) NOT NULL,
    resolution TEXT,
    ticket_priority VARCHAR(20) NOT NULL,
    ticket_channel VARCHAR(50) NOT NULL,
    first_response_time VARCHAR(50),
    time_to_resolution VARCHAR(50),
    customer_satisfaction_rating SMALLINT
        CHECK (customer_satisfaction_rating BETWEEN 1 AND 5),
    ticket_subject VARCHAR(255) NOT NULL,
    ticket_description TEXT NOT NULL,
    product_name VARCHAR(150));
