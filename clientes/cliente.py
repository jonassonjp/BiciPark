#!/usr/bin/env python3
# cliente.py

"""
Classe Cliente, com os atributos nome, endereço e telefone.
A classe Cliente deve implementar o método __str__, quando um
objeto cliente for convertido em string deve mostrar o nome - endereço

"""

class Cliente():

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone


    def __str__():
        return self.nome + ' - ' + self.endereco


