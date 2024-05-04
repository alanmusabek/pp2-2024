import psycopg2
from config import load_config

def update_phone(id, phone_name, phone_number):
    """ Update phone number and name based on the phone id """
    
    updated_row_count = 0

    sql = """ UPDATE phone_book
              SET phone_name = %s, phone_number = %s
              WHERE id = %s"""
    
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (phone_name, phone_number, id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

if __name__ == '__main__':
    update_phone(2, "Alexey", "+301766351")
