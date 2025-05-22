from lib.interface import *
from lib.arquivo import *
from time import sleep
import os

arqName = "pessoas.txt"
arq = os.path.join(os.path.dirname(__file__), arqName)

if not arquivoExiste(arq):
    criarArquivo(arqName,arq)

while True:
    resposta = menu(["Listar pessoas", "Cadstrar nova Pessoa","Sair"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("Cadastrando")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("saindo")
        break
    else:
        print("\033[31mopção inválida\033[m")
    sleep(1.5)