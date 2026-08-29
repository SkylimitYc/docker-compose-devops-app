CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO users (name, email)
VALUES
    ('Yashank', 'yashank@example.com'),
    ('DevOps User', 'devops@example.com')
ON CONFLICT (email) DO NOTHING;