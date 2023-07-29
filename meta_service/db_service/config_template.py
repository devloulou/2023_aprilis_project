db_config = {
    "user": '',
    "password": '',
    "host": "",
    "port": "",
    "db": ""
}

url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db']}"