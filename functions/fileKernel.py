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
        text = input('Insira o texto\n')
        file_created = open('documents/'+strFile+".txt", "w")
        file_created.write(text)
        file_created.close()
    else:
        print('Esse arquivo não existe')

def selection_sort(strFile):
    if verifyFile(strFile):
        fl = open('documents/'+strFile+".txt", "r")
        listtxt = fl.read().split(' ')

        for i in range(0, len(listtxt)-1):
            imin = i
            for j in range(i+1, len(listtxt)):
                if(listtxt[j] < listtxt[imin]):
                    imin = j
            aux = listtxt[imin]
            listtxt[imin] = listtxt[i]
            listtxt[i] = aux
        print(listtxt)

def verifyFile(strFile):
    if os.path.isfile('documents/'+strFile+".txt"):
        return True
    else:
        return False