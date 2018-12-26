#!/usr/bin/env python3
# bicipark.py
import sys
from clientes.listagem import ListaClientes


def lista_clientes():
    lista_clientes = ListaClientes()
    lista_clientes.relatorioClientes()
    # print(lista_clientes.lista())

def main(argv):
    if argv is None:
        argv = sys.argv
    lista_clientes()

if __name__ == "__main__":
    main(sys.argv)

