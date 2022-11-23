from fastapi import FastAPI
app = FastAPI()


#GET
@app.get("/getdata/{nome_do_usuario}")
def get_data(nome_do_usuario: str):
    return {
        "nome": nome_do_usuario
    }

#POST
@app.post("/postdata")
def get_data(nome_do_usuario: str):
    return {
        "nome": nome_do_usuario
    }

#PUT
lista_de_nomes = []
@app.put("/putdata/{nome_do_usuario}")
def put_data(nome_do_usuario: str):
    lista_de_nomes.append(nome_do_usuario)
    return {
        "nome_do_usuario":lista_de_nomes
    }
    
#DELETE
@app.delete("/deletedata/{nome_do_usuario}")
def delete_data(nome_do_usuario: str):
    lista_de_nomes.remove(nome_do_usuario)
    return {
        "nome_do_usuario":lista_de_nomes
    }


