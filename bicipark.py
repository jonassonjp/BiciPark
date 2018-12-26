#!/usr/bin/env python3
# bicipark.py
import sys
from clientes.listagem import ListaClientes
from clientes.manutencao import Manutencao
from controles.listagem import ListaRegistros

def lista_clientes():
    lista_clientes = ListaClientes()
    lista_clientes.relatorioClientes()
    Manutencao.salvar_relacao_clientes(dados=lista_clientes.relacao_clientes())



def lista_ent_sai():
    lista_ent_sai = ListaRegistros()
    lista_ent_sai.relatorio_ent_sai()


def main(argv):
    if argv is None:
        argv = sys.argv
    lista_clientes()
    lista_ent_sai()


if __name__ == "__main__":
    main(sys.argv)

