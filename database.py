from table import Table

class Database:
    def __init__(self, name):
        self.name = name
        self.tables = []

    def create_table(self, name):        
        self.tables.append(Table(name))