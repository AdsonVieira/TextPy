import os.path


def fileCreate(strFile): 
    if os.path.isfile('documents/'+strFile+".txt"):
        print('Esse arquivo já existe')
    else:
        file_created = open('documents/'+strFile+".txt", "w")
        file_created.close()
        print('Arquivo criado com sucesso')

def fileDelete(strFile): 
    if os.path.isfile('documents/'+strFile+".txt"):
        os.remove('documents/'+strFile+".txt")
        print('Arquivo deletado')
    else:
        print('Esse arquivo não existe')
        
def textpy(strFile):
    if os.path.isfile('documents/'+strFile+".txt"):
        pass
    else:
        print('Esse arquivo não existe')
    