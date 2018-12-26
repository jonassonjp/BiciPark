#!/usr/bin/env python3
# controle.py

"""
classe Controle, com os atributos cliente, entrada e saída.
A classe Controle  deve implementar o método __str__ e deve retornar o cliente - entrada - saída.

"""

class Registro():

    def __init__(self, cliente, entrada, saida):
        self.cliente = cliente
        self.entrada = entrada
        self.saida = saida

    def __str__():
        return 'Cliente: ' + self.cliente + ' - Entrada: ' + self.entrada + ' - Saída: ' + self.saida



