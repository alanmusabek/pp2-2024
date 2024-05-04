from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    # get section, default to postgresql
    config = {
        "host" : "localhost",
        "database" : "phonebook",
        "user" : "postgres",
        "password" : "6eQ_TGceTx5MNCh"
    }
    return config

if __name__ == '__main__':
    config = load_config()
    print(config)
