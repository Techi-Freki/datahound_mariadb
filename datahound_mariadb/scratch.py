from datahound import DataProviderBase, ConnectionString


mariadb_connection = ConnectionString('datahound_mariadb',
                                      user='cms_user',
                                      password='cms_pass',
                                      host='127.0.0.1',
                                      port=3307,
                                      database_name='cms_test'
                                      )


class MariaDbProvider(DataProviderBase):
    def __init__(self, mariadb_connection):
        super().__init__(mariadb_connection)


class DataProvider(object):
    mariadb = MariaDbProvider(mariadb_connection)


sql = 'select id, name, email from test_data'
records = DataProvider.mariadb.fetchall(sql)

for record in records:
    print(record)
