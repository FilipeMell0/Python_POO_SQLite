#Importar arquivo pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
filipe = Pessoa(1, "Filipe Mello")
print(filipe)

#Quero mostrar só nome
print(filipe.nome)