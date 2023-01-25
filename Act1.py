from fastapi import FastAPI

#importamos pydantic para obtener una entiad qu pueda definir el usiario
from pydantic import BaseModel

#creamos un objeto a partir de la clase FastAPI
app= FastAPI()


class User(BaseModel):
    id:int
    Survived:int
    Pclass:int
    Name:str
    Sex:str
    Age:int

#Creamos un objeto en forma de lista 

users_list=[
    User(id=1,Name="Braund, Mr. Owen Harris", Survived="0", Pclass="3", Sex="male",Age="22"),
    User(id=2,Name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)", Survived="1", Pclass="1", Sex="famale",Age="38"),
    User(id=3,Name="Heikkinen, Miss. Laina", Survived="1", Pclass="3", Sex="famale",Age="26"),
    User(id=4,Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)", Survived="1", Pclass="1", Sex="famale",Age="35"),
    User(id=5,Name="Allen, Mr. William Henry", Survived="0", Pclass="3", Sex="male",Age="35"),
    User(id=6,Name="Moran, Mr. James", Survived="0", Pclass="3", Sex="male",Age="0"),
    User(id=7,Name="McCarthy, Mr. Timothy J", Survived="0", Pclass="1", Sex="male",Age="54"),
    User(id=8,Name="Palsson, Master. Gosta Leonard", Survived="0", Pclass="3", Sex="male",Age="2"),
    User(id=9,Name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)", Survived="1", Pclass="3", Sex="famale",Age="27"),
    User(id=10,Name="Nasser, Mrs. Nicholas (Adele Achem)", Survived="1", Pclass="2", Sex="famale",Age="14"),
    User(id=11,Name="Sandstrom, Miss. Marguerite Rut", Survived="1", Pclass="3", Sex="famale",Age="4"),
    User(id=12,Name="Bonnell, Miss. Elizabeth", Survived="1", Pclass="1", Sex="famale",Age="58"),
    User(id=13,Name="Saundercock, Mr. William Henry", Survived="0", Pclass="3", Sex="male",Age="20"),
    User(id=14,Name="Andersson, Mr. Anders Johan", Survived="0", Pclass="3", Sex="male",Age="39"),
    User(id=15,Name="Vestrom, Miss. Hulda Amanda Adolfina", Survived="0", Pclass="3", Sex="famale",Age="14"),
    User(id=16,Name="Hewlett, Mrs. (Mary D Kingcome)", Survived="1", Pclass="2", Sex="famale",Age="55"),
    User(id=17,Name="Rice, Master. Eugene", Survived="0", Pclass="3", Sex="male",Age="2"),
    User(id=18,Name="Williams, Mr. Charles Eugene", Survived="1", Pclass="2", Sex="male",Age="0"),
    User(id=19,Name="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Survived="0", Pclass="3", Sex="famale",Age="31"),
    User(id=20,Name="Masselmani, Mrs. Fatima", Survived="1", Pclass="3", Sex="famale",Age="0"),
    User(id=21,Name="Fynney, Mr. Joseph J", Survived="0", Pclass="2", Sex="male",Age="35"),
    User(id=22,Name="Beesley, Mr. Lawrence", Survived="1", Pclass="2", Sex="male",Age="34"),
    User(id=23,Name="McGowan, Miss. Anna (Annie)", Survived="1", Pclass="3", Sex="famale",Age="15"),
    User(id=24,Name="Sloper, Mr. William Thompson", Survived="1", Pclass="1", Sex="male",Age="28"),
    User(id=25,Name="Palsson, Miss. Torborg Danira", Survived="0", Pclass="3", Sex="famale",Age="8"),

]

@app.get("/usersclass")
async def usersclass():
    return (users_list)


################################ POST ##################################

@app.post("/usersclass")
async def usersclass(user:User):

    for index, saved_user in enumerate(users_list):
         if saved_user.id == user.id:
            return {"error":"El usuario ya existe"}
    else:
       users_list.append(user)
       return user

# uvicorn Act1:app --reload