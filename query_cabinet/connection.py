import configparser

import psycopg2
import psycopg2.extras

global_config = configparser.ConfigParser()
global_config.read('db.config')

def get_connection(password, config='DEFAULT'):
    db_config = {
        'USER': global_config[config]['DATABASE_USER'],
        'HOST': global_config[config]['DATABASE_HOST'],
        'NAME': global_config[config]['DATABASE_NAME'],
        'PORT': global_config[config]['DATABASE_PORT'],
    }
    try:
        print('Trying to connect to {HOST}:{PORT}/{NAME} as {USER}'.format(**db_config))
        db_config['PASSWORD'] = password
        return psycopg2.connect("dbname='{NAME}' user='{USER}' host='{HOST}' port='{PORT}' password='{PASSWORD}'".format(**db_config))
    except KeyboardInterrupt:
        pass

dict_cursor = psycopg2.extras.DictCursor
