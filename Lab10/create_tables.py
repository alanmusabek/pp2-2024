import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE phone_book (
            id SERIAL PRIMARY KEY,
            phone_number VARCHAR(255),
            phone_name VARCHAR(255) NOT NULL
        )
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
