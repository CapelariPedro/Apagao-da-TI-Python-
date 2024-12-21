from flask import Flask , request , jsonify
from pymongo import MongoClient

app = Flask(__name__)

# C o n e x ã o com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["estoque_db"]
collection = db["estoque"]

# Rota para adicionar um item
@app.route("/adicionar", methods=["POST"])
def adicionar_item():
    data = request.json
    nome = data["nome"]
    quantidade = data["quantidade"]

    item = collection.find_one({"nome": nome})
    if item:
        nova_quantidade = item["quantidade"] + quantidade
        collection.update_one({
            "nome": nome
            }, 
            {"$set": 
             {
                 "quantidade":nova_quantidade
                 }})
    else:
        collection.insert_one({
            "nome": nome, 
            "quantidade": quantidade
            })
    return jsonify({"message": f"Item '{nome}' adicionado com sucesso."})

# Rota para remover um item
@app.route("/remover", methods=["POST"])
def remover_item():
    data = request.json
    nome = data["nome"]
    quantidade = data["quantidade"]

    item = collection.find_one({"nome": nome})
    if item:
        nova_quantidade = item["quantidade"] - quantidade
        if nova_quantidade <= 0:
            collection.delete_one({"nome": nome})
        else:
            collection.update_one({
                "nome": nome
                }, 
                {"$set": 
                {
                    "quantidade": nova_quantidade
                    }})
        
        return jsonify({"message": f"Item '{nome}' removido com sucesso."})
    else:
        return jsonify({"error": f"Item '{nome}' não encontrado."}), 404

# Rota para listar todos os itens
@app.route("/listar", methods=["GET"])
def listar_itens():
    itens = list(collection.find({}, {"_id": 0}))
    return jsonify(itens)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)