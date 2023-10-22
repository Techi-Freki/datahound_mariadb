# Datahound Mariadb

A MariaDB connector for [datahound](https://github.com/Techi-Freki/datahound).

## Usage

### Extending provider base

    from datahound import DataProviderBase, ConnectionString


    # add your connection string data to the ConnectionString object
    mariadb_connection = ConnectionString('datahound_mariadb', # required to use mariadb, otherwise datahound defaults to sqlite
                                          user='test_user',
                                          password='test_pass',
                                          host='127.0.0.1',
                                          port=3306,
                                          database_name='test_db'
                                          )


    sqlite_connection = ConnectionString(database_path='/path/to/db.sqlite') # datahound defaults to sqlite3 when a connector_name is not passed in


    # extend the DataProviderBase class
    class MariaDbProvider(DataProviderBase):
        def __init__(self, connection_string):
            super().__init__(connection_string)


    class SqLite3Provider(DataProviderBase):
        def __init__(self, connection_string):
            super().__init__(connection_string)


    class DataProvider(object):
        mariadb = MariaDbProvider(mariadb_connection)
        sqlite = SqLite3Provider(sqlite_connection)


    # you are now ready to use the DataProvider class to access your database
    # See the datahound README for additional information

## Changelog

1.0.0
* Initial Release.
