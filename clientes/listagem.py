#!/usr/bin/env python3
# listagem.py

from clientes.cliente import Cliente


class ListaClientes():

    def __init__(self):
        self.clientes = self.atualiza_clientes()

    def atualiza_clientes(self, clientes=None):
        if clientes is None:
            return self.inicializa_clientes()

        # self.clientes.extend(clientes)

    def inicializa_clientes(self):
        novos_clientes = [
            Cliente('Armindo', 'Rua do Rio, 343', '(11) 2323-2323'),
            Cliente('Arnaldo', 'Rua do Mercado, 232', '(21) 3434-3434'),
            Cliente('Orlando', 'Rua do Porto, 454', '(31) 2525-2525'),
            Cliente('Rosangela', 'Rua da Boa Viagem, 656', '(51) 3232-3232'),
        ]
        return novos_clientes
        # self.clientes.extend(clientes)

    def lista(self, cliente=None):
        if cliente is None:
            return self.clientes
        else:
            return self.clientes[cliente]

    def relatorioClientes(self):
        pass