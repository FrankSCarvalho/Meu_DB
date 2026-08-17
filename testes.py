from database import Database

bancoTeste = Database("banco_teste")

bancoTeste.create_table("users")
print(f"Tabelas criadas: {bancoTeste.tables}")
bancoTeste.create_table("products")
print(f"Tabelas criadas: {bancoTeste.tables}")

bancoTeste.create_table("users")
print(f"Tabelas criadas: {bancoTeste.tables}")

print("========TESTES DE CRIAÇÃO DE COLUNAS========")
bancoTeste.tables[0].add_column("ID","INTEGER")
print(f"Colunas criadas: {bancoTeste.tables[0].columns}")
bancoTeste.tables[0].add_column("User","TEXT")
print(f"Colunas criadas: {bancoTeste.tables[0].columns}")
bancoTeste.tables[0].add_column("ID","INTEGER")
print(f"Colunas criadas: {bancoTeste.tables[0].columns}")