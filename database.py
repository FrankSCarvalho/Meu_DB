from table import Table

class Database:
    def __init__(self, name):
        self.name = name
        self.tables = []

    def create_table(self, name):
        table_exists = False
        for table in self.tables:
            if table.name == name:
                table_exists = True                
                return
        if table_exists == False:    
            self.tables.append(Table(name))
           
                