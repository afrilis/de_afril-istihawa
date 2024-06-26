CREATE TABLE users (
  id INT PRIMARY KEY,
  username VARCHAR (20),
  name VARCHAR(255),
  password VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

CREATE TABLE posts (
  id INT PRIMARY KEY,
  user_id INT,
  category_id INT,
  title VARCHAR,
  content TEXT,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

CREATE TABLE comments (
  id INT PRIMARY KEY,
  post_id INT,
  user_id INT,
  content VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

CREATE TABLE categories (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);
