import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="automation_db",
    user="your_user",
    password="your_password",
    host="localhost"
)

# Create a cursor object
cur = conn.cursor()

# Create table for storing customer requests
cur.execute('''CREATE TABLE requests (
                id SERIAL PRIMARY KEY,
                customer_id INT,
                request_type VARCHAR(100),
                request_data TEXT
            )''')

# Insert new request into the table
cur.execute("INSERT INTO requests (customer_id, request_type, request_data) VALUES (%s, %s, %s)",
            (123, 'Refund', 'Request for refund on order #456'))

# Commit and close connection
conn.commit()
cur.close()
conn.close()
