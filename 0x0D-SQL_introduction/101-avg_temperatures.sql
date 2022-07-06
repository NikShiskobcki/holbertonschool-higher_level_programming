-- average temperatures
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY avg_temp DESC
