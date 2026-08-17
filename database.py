from table import Table

class Database:
    def __init__(self, name):
        self.name = name
        self.tables = []

    def create_table(self, name):
        for table in self.tables:
            if table.name == name:
                print("Esta tabela já existe no banco")    
                return
            else:    
                self.tables.append(Table(name))
                print(f"Tabela {name} criada com sucesso!")
                return