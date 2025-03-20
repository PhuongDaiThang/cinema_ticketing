from fastapi import FastAPI
import mysql.connector
import time

app = FastAPI()

@app.get("/")
def read_root():
    # Retry khi MySQL chưa sẵn sàng
    for i in range(10):
        try:
            connection = mysql.connector.connect(
                host="db",
                port=3306,
                user="root",
                password="1234",
                database="testdb"
            )
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            connection.close()
            return {"message": "Connected to MySQL!", "databases": databases}
        except mysql.connector.Error as e:
            print(f"MySQL not ready yet, retrying... {i+1}/10")
            time.sleep(3)
    return {"error": "MySQL not available"}
