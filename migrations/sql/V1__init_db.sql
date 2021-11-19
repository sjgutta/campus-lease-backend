CREATE TABLE listing (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(255),
    image_url VARCHAR(255),
    email VARCHAR(255),
    description TEXT,
    amenities TEXT
);
