import pymongo

def conectar_mongo():
    try:
        # Conectar ao banco de dados
        cliente = pymongo.MongoClient('mongodb://localhost:27017/')
        db = cliente['estoque_db']
        return db
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
