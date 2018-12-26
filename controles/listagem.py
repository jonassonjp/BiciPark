#!/usr/bin/env python3
# listagem.py

from clientes.cliente import Cliente
from controles import controle
from datetime import datetime

class ListaRegistros():

    def __init__(self):
        self.registros = []
        self.inicializa_registros()


    def atualiza_registros(self, novos_registros=None):
        if novos_registros is None:
            self.atualiza_registros()
        else:
            self.registros.extend(novos_registros)

    def inicializa_registros(self):
        # self.clientes = listagem.ListaClientes.clientes
        clientes = [
            Cliente('Armindo', 'Rua do Rio, 343', '(11) 2323-2323'),
            Cliente('Arnaldo', 'Rua do Mercado, 232', '(21) 3434-3434'),
            Cliente('Orlando', 'Rua do Porto, 454', '(31) 2525-2525'),
            Cliente('Rosangela', 'Rua da Boa Viagem, 656', '(51) 3232-3232')
        ]
        entradas = (
            datetime(2015, 3, 12, 10),
            datetime(2015, 3, 15, 11),
            datetime(2015, 3, 16, 9),
            datetime(2015, 3, 16, 14),
        )
        saidas = (
            datetime(2015, 3, 12, 10, 15),
            datetime(2015, 3, 15, 11, 30),
            datetime(2015, 3, 16, 10),
            datetime(2015, 3, 16, 14, 45),
        )
        for indice, cliente in enumerate(clientes):
            registro = controle.Registro(cliente, entradas[indice], saidas[indice])
            self.registros.append(registro)


    def relacao_ent_saida(self):
        if self.registros is None:
            self.inicializa_registros()

        return self.registros


    def relatorio_ent_sai(self):
        if self.registros is None:
            print ('Sem dados')
        else:
            print('\n')
            print('=' * 90)
            print('{:^90}'.format('*** RELATÓRIO DE ENTRADA/SAÍDA  ***'))
            print('=' * 90)
            print('{:^30}\t{:<20}\t{:<20}'.format('Nome', 'Entrada', 'Saída'))
            print('=' * 90)
            for reg in self.registros:
                print('{:^30}\t{:<20}\t{:<20}'.format(reg.cliente.nome, str(reg.entrada), str(reg.saida)))

