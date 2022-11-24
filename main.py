#Importar arquivo pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
filipe = Pessoa(1, "Filipe Mello")
print(filipe)

#Quero mostrar só nome
print(filipe.nome)

print("Daqui pra frente é o acesso ao banco")
#Chama o objeto de banco de dados
db = Database()

#instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)