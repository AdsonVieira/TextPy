import os.path
import sys

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

    palavras_recorrentes = ['gastronomia', 'culinária', 'gastronômico',
                            'restaurante', 'cozinha', 'cardápios', 
                            'ingredientes', 'bebidas']

    if verifyFile(strFile):
        fl = open('documents/'+strFile+".txt", "r")
        listtxt = fl.read()
        #removendo caractesres 
        cesp = ",.-#@–():"
        for i in range(0,len(cesp)):
            listtxt=listtxt.replace(cesp[i],"")

        #deixando tudo minúsculo
        listtxt = listtxt.lower()

        #transformando em array
        listtxt = listtxt.split()

        
        for i in range(0, len(listtxt)-1):
            imin = i
            for j in range(i+1, len(listtxt)):
                if(listtxt[j] < listtxt[imin]):
                    imin = j
            aux = listtxt[imin]
            listtxt[imin] = listtxt[i]
            listtxt[i] = aux

        dic_palavras = {}
        for i in range(0, len(listtxt)-1):
            chave = listtxt[i]

            if chave in dic_palavras:
                dic_palavras[listtxt[i]] += 1
            else:
                dic_palavras[listtxt[i]] =1
             

        listtxt = "\n".join(str(x) for x in listtxt)
        list_ocor = "Número de ocorrencias\n" + "\n".join("{}: {}".format(k, v) for k, v in dic_palavras.items()) + ""

        #salvando no arquivo por ordem de ocorrencia
        palavras= open('documents/palavras.txt', "w")
        palavras.write(listtxt)
        palavras.close()

        ocorrencia= open('documents/ocorrencia.txt', "w")
        ocorrencia.write(list_ocor)
        ocorrencia.close()

def verifyFile(strFile):
    if os.path.isfile('documents/'+strFile+".txt"):
        return True
    else:
        return False
