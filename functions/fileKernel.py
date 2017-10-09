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

        ## ordernando em ordem decrescente com selection sort  
        for i in range(0, len(listtxt)-1):
            imin = i
            for j in range(i+1, len(listtxt)):
                if(listtxt[j] > listtxt[imin]):
                    imin = j
            aux = listtxt[imin]
            listtxt[imin] = listtxt[i]
            listtxt[i] = aux

        # calculando ocorrências
        dic_palavras = {}
        for i in range(0, len(listtxt)-1):
            chave = listtxt[i]
            if chave in dic_palavras:
                dic_palavras[listtxt[i]] += 1
            else:
                dic_palavras[listtxt[i]] =1



        segundo_dic = list(dic_palavras.items())
        
        #ordernando orcorrências em ordem decrescente
        for i in range(0,len(segundo_dic)-1):
            for j in range(i+1,len(segundo_dic)):
                if segundo_dic[i][1]<segundo_dic[j][1]:
                    segundo_dic[i],segundo_dic[j]=segundo_dic[j],segundo_dic[i]
        

        listtxt = "\n".join(str(x) for x in listtxt)
        segundo_dic = "\n".join(str(x) for x in segundo_dic)
        #salvando palavras na ordem
        salvaArquivo('palavras', listtxt)

        #salvando palavras na ordem de ocorrência
        salvaArquivo('ocorrencia',segundo_dic)


def verifyFile(strFile):
    if os.path.isfile('documents/'+strFile+".txt"):
        return True
    else:
        return False

def salvaArquivo(nomeArquivo, data):
    arquivo= open('documents/'+nomeArquivo+'.txt', "w")
    arquivo.write(data)
    arquivo.close()