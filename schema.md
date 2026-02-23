```sql
CREATE TABLE weather_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) NOT NULL,          
    log_date DATE NOT NULL,                  
    log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    temperature DECIMAL(5,2),                  
    feels_like DECIMAL(5,2),
    humidity INT,                              
    pressure INT,                              
    weather_main VARCHAR(50),                  
    weather_description VARCHAR(100),
    wind_speed DECIMAL(5,2),                   
    wind_deg INT,                              
    rain_1h DECIMAL(5,2) NULL,                 
    clouds_all INT,                            
    sunrise TIME NULL,                           
    sunset TIME NULL
);
```