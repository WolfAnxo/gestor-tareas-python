import psycopg
import os 
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:
        conexion = psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conexion
    except psycopg.Error:
        print("No se ha podido conectar con la base de datos.")
