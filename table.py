from column import Column
class Table:
    def __init__(self,name):
        self.name = name
        self.columns = []

    def add_column(self, name, type_data):
        column_exists = False
        for column in self.columns:
            if column.name == name:
                column_exists = True
                break
        if column_exists == False:
            self.columns.append(Column(name, type_data))