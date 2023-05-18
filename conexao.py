import mysql.connector

config = {
        'user':'admin',
        'password':'admin123',
        'host':'aula1005.cy2egmarhyai.us-east-1.rds.amazonaws.com',
        'database':'africa_brasil'
    }
# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Fechar a conexão
conn.close()