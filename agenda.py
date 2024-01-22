def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {'nome': nome_contato, 'telefone': telefone_contato, 'email': email_contato, 'favorito': False}
    contatos.append(contato)
    print(f'O contato\nNome: {nome_contato}\nTelefone: {telefone_contato}\nEmail: {email_contato}\nfoi adicionada com '
          'sucesso!')
    return


def ver_contatos(contatos):
    print('\nLista de Contatos:')
    for indice, contato in enumerate(contatos, start=1):
        status = '\u2713' if contato["favorito"] else ' '
        nome_contato_adicionado = contato['nome']
        telefone_contato_adicionado = contato['telefone']
        email_contato_adicionado = contato['email']
        print(
            f'{indice}. {nome_contato_adicionado} - {telefone_contato_adicionado} - {email_contato_adicionado} | Favorito: [{status}]')


def ver_contatos_favoritos(contatos):
    print('\nLista de Contatos Favoritos:')
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            status = '\u2713' if contato["favorito"] else ' '
            nome_contato_adicionado = contato['nome']
            telefone_contato_adicionado = contato['telefone']
            email_contato_adicionado = contato['email']
            print(
                f'{indice}. {nome_contato_adicionado} - {telefone_contato_adicionado} - {email_contato_adicionado} | '
                f'Favorito: [{status}]'
            )


def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    if verifica_digitos_opcoes(indice_contato):
        indice_contato_ajustado = int(indice_contato) - 1
        novos_dados_contato = [novo_nome_contato, novo_telefone_contato, novo_email_contato]
        if 0 <= indice_contato_ajustado < len(contatos):
            if novos_dados_contato[0] != '':
                contatos[indice_contato_ajustado]['nome'] = novo_nome_contato
                print(f'Nome do Contato {indice_contato} atualizado para {novo_nome_contato}')
            if novos_dados_contato[1] != '':
                contatos[indice_contato_ajustado]['telefone'] = novo_telefone_contato
                print(f'Telefone do Contato {indice_contato} atualizado para {novo_telefone_contato}')
            if novos_dados_contato[2] != '':
                contatos[indice_contato_ajustado]['email'] = novo_email_contato
                print(f'Email do Contato {indice_contato} atualizado para {novo_email_contato}')
            if novos_dados_contato[0] == '' and novos_dados_contato[1] == '' and novos_dados_contato[2] == '':
                print(f'Nada foi alterado no Contato de índice {indice_contato}')
        else:
            print('Índice de Tarefa inválido!')
    return


def favoritar_contato(contatos, indice_contato):
    if verifica_digitos_opcoes(indice_contato):
        indice_contato_ajustado = int(indice_contato) - 1
        if not contatos[indice_contato_ajustado]['favorito']:
            contatos[indice_contato_ajustado]['favorito'] = True
            print(f'Contato {indice_contato} marcado como favorito!')
        else:
            contatos[indice_contato_ajustado]['favorito'] = False
            print(f'Contato {indice_contato} não é mais favorito!')
    return


def deletar_contato(contatos, indice_contato):
    if verifica_digitos_opcoes(indice_contato):
        indice_contato_ajustado = int(indice_contato) - 1
        contatos.remove(contatos[indice_contato_ajustado])
        print(f'Contato {indice_contato} foi removido \u274c')
    return


def verifica_digitos_opcoes(case):
    case.replace(' ', '')
    if '-' in case:
        print('Valor não pode ser negativo.')
        return False
    if case.isdigit():
        if 0 >= int(case) or int(case) > len(contatos):
            print('Valor digitado não existe na lista de contatos...')
            return False
    else:
        print('Apenas valores numéricos são permitidos.  Digite apenas o valor entre as opções listadas')
    return case.isdigit()


contatos = []

while True:
    print('\nMenu da Agenda:')
    print('1 - Adicionar contato à Agenda')
    print('2 - Ver Contatos da Agenda')
    print('3 - Atualizar Contatos da Agenda')
    print('4 - Marcar/Desmarcar como Favorito')
    print('5 - Ver Contatos Favoritos')
    print('6 - Apagar Contato da Agenda')
    print('7 - Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == "1":
        nome_contato = input('Digite o nome do Contato que deseja Adicionar: ')
        telefone_contato = input('Digite o telefone do Contato que deseja Adicionar: ')
        email_contato = input('Digite o email do Contato que deseja Adicionar: ')
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input('Digite o número do Contato que deseja atualizar: ')
        if verifica_digitos_opcoes(indice_contato):
            novo_nome = input('Digite o novo nome do Contato: ')
            novo_telefone = input('Digite o novo telefone do Contato: ')
            novo_email = input('Digite o novo email do Contato: ')
            atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input('Digite o número do Contato que deseja favoritar: ')
        if verifica_digitos_opcoes(indice_contato):
            favoritar_contato(contatos, indice_contato)
    elif escolha == "5":
        ver_contatos_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input('Digite o número do Contato que deseja excluir: ')
        if verifica_digitos_opcoes(indice_contato):
            deletar_contato(contatos, indice_contato)
    elif escolha == "7":
        break

print('Programa Finalizado')
