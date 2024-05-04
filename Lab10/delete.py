import psycopg2
from config import load_config


def delete_by_id(id):
    """ Delete phone data by id """

    rows_deleted  = 0
    sql = 'DELETE FROM phone_book WHERE id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

def delete_by_name(phone_name):
    """ Delete phone data by name"""

    rows_deleted  = 0
    sql = 'DELETE FROM phone_book WHERE phone_name = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (phone_name,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

def delete_by_number(phone_number):
    """ Delete phone data by number """

    rows_deleted  = 0
    sql = 'DELETE FROM phone_book WHERE phone_number = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (phone_number,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted

if __name__ == '__main__':
    deleted_by_id = delete_by_id(3)
    deleted_by_name = delete_by_name("Alex")
    deleted_by_name = delete_by_number("Albert")
    print('The number of deleted rows: ', deleted_by_id + deleted_by_name)