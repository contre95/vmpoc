# This is also part of our interface adapter layer, and container all the storage implementations.
from vuln_mgmt import Storage, Vulnerability
import sqlite3


class SQLite(Storage):
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.name = "SQLite"
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vulnerabilities (
                id TEXT PRIMARY KEY,
                severity TEXT,
                service TEXT
            )
        ''')
        self.conn.commit()

    def store(self, vuln: Vulnerability):
        print(f'Storing vuln for  {vuln.service.name} with {self.name}')
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO vulnerabilities (id, severity, service) VALUES (?, ?, ?)',
                       (str(vuln.id), vuln.severity, vuln.service.name))
        self.conn.commit()

    def storeMultiple(self, vuln_list: list[Vulnerability]):
        cursor = self.conn.cursor()
        for vuln in vuln_list:
            cursor.execute('INSERT INTO vulnerabilities (id, severity, service) VALUES (?, ?, ?)',
                           (str(vuln.id), vuln.severity, vuln.service.name))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


class FakeStorgae(Storage):
    def __init__(self, name):
        self.name = name

    def store(self, vuln: Vulnerability):
        print(f'Storing vuln for  {vuln.service.name} with {self.name}')

    def storeMultiple(self, vuln_list: list[Vulnerability]):
        for vuln in vuln_list:
            print(f'Storing vuln for  {vuln.service.name} with {self.name}')
