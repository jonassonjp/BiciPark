from json import dump

NOME_ARQUIVO = 'clientes.txt'

class Manutencao():

    def salvar_relacao_clientes(self, dados, nome_arquivo=NOME_ARQUIVO):
        data= dict()
        data['clientes'] = []
        for registro in dados:
            data['clientes'].append({
                'nome': registro.nome,
                'endereço': registro.endereco,
                'telefone': registro.telefone
            })

        with open(nome_arquivo, 'w') as outfile:
            dump(data, outfile)
        print('Arquivo {} salvo com sucesso'.format(NOME_ARQUIVO.upper()))

    def ler_relacao_clientes(self, nome_arquivo=NOME_ARQUIVO):
        pass
