Set Up the Database (MySQL Workbench):
 CREATE DATABASE food_db;

 CREATE TABLE stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    date_inserted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY (name, category)
 );

Within VScode
 Configure Your Credentials:
  class DatabaseConfig:
    HOST = "your_hostname"
    USER = "your_root"                
    PASSWORD = "your_password"   
    DATABASE = "your_db"

  # Make sure you have the Python Dependencies installed
   pip install mysql-connector-python
   pip install requests
