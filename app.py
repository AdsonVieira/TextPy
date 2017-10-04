'''
    Comandos para acessar as funções do editor

    create-file (nome do arquivo)

    delete-file (nome do arquivo)

    textpy (nome do arquivo)

    src-textpy (nome do arquivo)

'''

from functions import fileKernel

print('===================Editor de texto txtpy===================')

loop = 's'

while loop =='s': 
    action = input('')

    action = action.split()

    if action[0]=='create-file':
        fileKernel.fileCreate(action[1])
    elif action[0]=='delete-file':
        fileKernel.fileDelete(action[1])
    elif action[0]=='textpy':
        fileKernel.textpy(action[1])
    elif action[0]=='src-textpy':
        fileKernel.selection_sort(action[1])
    else:
        print('Esse comando não existe ')

    loop = input('Deseja continuar?  S ou N\n')





