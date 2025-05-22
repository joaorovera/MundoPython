from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: return True

def criarArquivo(nome,path):
    try:
        a = open(path, 'wt+')
        a.close()
    except:
        print("Houve um erro na execução")
    else:
        print(f"\33[32mArquivo {nome} criado com sucesso!\33[m")

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo")
    else:
        cabecalho("Pessoas Cadastradas")
        for i in a:
            dado = i.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome="desconhecido", idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print("ERRO NO CADASTRO")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("ERRO AO ESCREVER")
        else:
            print(f"\33[32mNovo registro de {nome} adicionado\33[m")
            a.close()