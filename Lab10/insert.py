import psycopg2
from config import load_config

def check_name_exists(name):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                sql = """SELECT COUNT(*) FROM phone_book WHERE phone_name = %s"""
                cur.execute(sql, (name,))
                count = cur.fetchone()[0]
                print(count)
                return count
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False

def check_number_exists(number):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                sql = """SELECT COUNT(*) FROM phone_book WHERE phone_number = %s"""
                cur.execute(sql, (number,))
                count = cur.fetchone()[0]
                return count > 0
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False


def insert_phone(phone_number, phone_name):
    """ Insert a new phone number into the phone book table """

    sql = """INSERT INTO phone_book(phone_number, phone_name)
             VALUES(%s, %s) RETURNING id;"""
    
    id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (phone_number, phone_name))

                # fetch the generated id back
                row = cur.fetchone()
                if row:
                    id = row[0]
                else:
                    print("No rows returned after INSERT.")
                    
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return id

def update_phone_by_name(phone_name, phone_number):
    """ Update phone number and name based on the phone name """
    
    updated_row_count = 0

    sql = """ UPDATE phone_book
              SET phone_name = %s, phone_number = %s
              WHERE phone_name = %s"""
    
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (phone_name, phone_number))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

def update_phone_by_number(phone_name, phone_number):
    """ Update phone number and name based on the phone number """
    
    updated_row_count = 0

    sql = """ UPDATE phone_book
              SET phone_name = %s, phone_number = %s
              WHERE phone_number = %s"""
    
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (phone_name, phone_number))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count



if __name__ == '__main__':
    number = input("Enter a phone number: ")
    name = input("Enter a name: ")
    if(check_name_exists(name)):
        update_phone_by_name(name, number)
    elif(check_number_exists(number)):
        update_phone_by_number(name, number)
    else:
        insert_phone(number, name)