from database import Database

bancoTeste = Database("banco_teste")

bancoTeste.create_table("users")
print(f"Tabelas criadas: {bancoTeste.tables}")
bancoTeste.create_table("products")
print(f"Tabelas criadas: {bancoTeste.tables}")

bancoTeste.create_table("users")
print(f"Tabelas criadas: {bancoTeste.tables}")