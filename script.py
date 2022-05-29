# %% [markdown]
# # **Teoria dos Grafos e Computabilidade**
# ##**Trabalho Prático 1**
# 
# ###**Professor:**  *Felipe Augusto Lara Soares*
# **Grupo:** 
# *   *Gustavo de Castro Nogueira*
# *   *Horácio Salvador Ngunga*
# *   *Nelson de Campos Nolasco*
# *   *Rafaella Cristina de Sousa Sacramento*
# *   *Vitor de Souza Xavier*
# *   *Vitor José Lara Bastos*
# ---
# 
# ## **Etapa 1 - (3 pontos)**
# 
# 
# O trabalho consiste em ler o arquivo disponibilizado no Canvas que contém dados referentes às latitudes e longitudes de algumas cidades brasileiras (você pode escolher ler: CSV ou JSON).
# 
# Após a leitura desses dados, o programa deve ser capaz de gerar um grafo não direcionado e ponderado que represente esse contexto, considerando os vértices como as cidades brasileiras (presentes no arquivo) e as arestas como as rotas entre essas cidades, cujo peso é a distância da rota.
# 
# **Informação Importante:** para cada cidade criada (vértice), considere que ela possua ligações (arestas) somente com as três cidades mais próximas a ela. Essa característica irá deixar o nosso grafo um pouco fora do contexto real, porém será importante para testarmos diferentes alternativas nos algoritmos que serão criados nas próximas etapas.
# 
# Como o arquivo contém latitudes e longitudes, fica como responsabilidade do grupo procurar como encontrar distância entre diferentes latitudes e longitudes, bem como desenvolver o programa responsável por encontrar essa distância e definir quais arestas serão criadas.
# 
# *   Entregáveis etapa 1: código para leitura do arquivo e criação do grafo.
# 
# 
# ---
# 
# 

# %% [markdown]
# # **PRIMEIRA PARTE:**
# 
# 
# 
# ### > ***Baixar o arquivo 'br.csv', analisá-lo, e prepará-lo para gerar o grafo solicitado nesta Etapa 1 do trabalho.***
# 
# 

# %% [markdown]
# 
# 
# > Primeiramente, serão necessários instalar e importar as bibliotecas a serem utilizadas no tratamento dos dados do arquivo *'Br.csv'* disponibilizado.
# 
# 
# 

# %% [markdown]
# #### ! -> se estiver utilizando o google colab
# #### % -> se estiver utilizando o vscode

# %%
# !pip install haversine 
# %pip install haversine 

# %%
from operator import index
import pandas as pd #biblioteca Python que fornece ferramentas para análise e manipulação de dados - criar, ler, visualizar, printar infos de DataFrame (df)
import haversine

# %% [markdown]
# 
# 
# > Importar o arquivo br.csv disponibilizado com os dados de latitude e longitude a ser trabalhado.
# Neste caso, o arquivo "br.csv" deverá ser localizado no diretório onde se encontra no computador local.
# 
# 

# %%
#### se estiver no colab, rodar a célula abaixo e anexar o arquivo br.csv 

# %%
# from google.colab import files
# data_to_load = files.upload()

# %% [markdown]
# 
# 
# > Ler e visualizar o DataFrame baixado 'br.csv'

# %%
df = pd.read_csv('br.csv') #Função usada para ler e transformar os dados do arquivo 'csv' em um DataFrame (aqui abreviada para 'df')

# %% [markdown]
# > Explorando as informações do DataFrame "br.csv" disponibilizado para ser usado no trabalho

# %%
df.head(110) #Função usada para retornar as primeiras n (5 por padrão) linhas do DataFrame. Aqui foi utilizada 10 entre parênteses para visualizar as 10 primeiras linhas.

# %%
len(df) #Função que retorna a contagem do número de linhas do DataFrame, que no caso coincide com o número de cidades a terem os dados de latitude e longitude a serem manipuladas no trabalho.

# %%
df.info() #dataframe.info() é usada para obter um resumo conciso do dataframe. É muito útil ao fazer análises exploratórias dos dados. Para obter uma visão geral rápida do conjunto de dados.

# %% [markdown]
# > Próximo passo, limpeza do DataFrame, removendo colunas e dados não necessários para o trabalho, retornando apenas as colunas City, lat, lng (que informam o nome da cidade, sua latitude e longitude).
# 
# >Por padrão, as operações efetuadas no DataFrame não o afetam. Assim, ao remover uma coluna, linha etc., o que o Pandas faz é devolver um novo DataFrame sem aquele dado. Ou seja, o DataFrame original se mantém intacto.
# 
# > O que se pode fazer para resolver isso é atribuir esse DataFrame que é devolvido pelo método na mesma variável:

# %%
df = df.drop(columns=["country", "iso2", "admin_name", "capital", "population", "population_proper"])
df.head()

# %% [markdown]
# > Agora, passa-se ao cálculo das distâncias das cidades a partir dos dados de latitude e longitude.
# 
# > Aqui foi usada a biblioteca **Haversine** do Python para calcular a distância (em várias unidades) entre dois pontos na terra usando sua latitude e longitude. A unidade padrão é o Km.
# 
# > No final se terá um array 'finalMat' com as cidades e respectivas distâncias em Km.

# %%
from haversine import haversine, haversine_vector, Unit

# %%
# Pegando os valores da tabela
lats = pd.Series(df.lat.values.flatten())
lngs = pd.Series(df.lng.values.flatten())
cities = pd.Series(df.city.values.flatten())

#sp = (lats[0], lngs[0])
#rj = (lats[1], lngs[1])
#bh = (lats[2], lngs[2])
#br = (lats[3], lngs[3])
#sv = (lats[4], lngs[4])

# Criando o vetor que terá a coordenada de cada cidade
combVet = []
for x in range(len(lats)):
  aux = (lats[x], lngs[x])
  combVet.append(aux)

# Calculando a distância das cidades (*ATENÇÃO* em cada vetor há o valor 0)
allVet = haversine_vector(combVet, combVet, comb=True) 


# Criando uma matriz que terá TODAS as distâncias e suas respectivas cidades
arrayAux = []
finalMat = []
for i in range(len(lats)):
  arrayAux = [] # Limpando o array
  for j in range(len(lats)):
    aux = (allVet[i][j], cities[j]) # Pegando a matriz das distâncias e adicionando o nome da cidade que foi calculado a distância
    arrayAux.append(aux) # Inserindo em um array auxiliar (ex: [(...) ...., (13.2313, 'São Paulo'), .... (...)])
    
  arrayAux.sort() # Ordenando-o para inserir corretamente no finalVet
  finalMat.append(arrayAux)

print(finalMat[23]) 



# %%
df.head() #Como informado a cima, se lermos o DataFrame original ele continua intacto


# %%
#transformando o Array 'finalMat' novamente em um DataFrame
ciddist_df = pd.DataFrame(finalMat)

# %%
ciddist_df.head() #Visualizando as 5 primeiras linhas do DataFrame contendo a cidade referência e distâncias em km das demais

# %% [markdown]
# > Em sequência serão deletadas as colunas com as cidades à cima da terceira menor distância em relação à cidade referenciada na primeira coluna, conforme solicitado na **Etapa 1** do trabalho para a geração do grafo.
# 
# > Usou-se o comando *Drop* do Pandas para remover as colunas 4 à 109.

# %%
cid_menores_dist_df = ciddist_df.drop(columns=[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
cid_menores_dist_df.head()

# %%
cid_menores_dist_df.head () #Visualizando as 5 primeiras linhas do DataFrame contendo a cidade referência e distâncias em km das três outras mais próximas.

# %%
#será realizada a alteração do label (de 0,1,2,3 para: origem, distância_1, distancia_2,distancia_3) para maior clareza
cid_menores_dist_df.rename({0: "origem"}, axis=1, inplace=True)
cid_menores_dist_df.rename({1: "distancia_1"}, axis=1, inplace=True)
cid_menores_dist_df.rename({2: "distancia_2"}, axis=1, inplace=True)
cid_menores_dist_df.rename({3: "distancia_3"}, axis=1, inplace=True)
cid_menores_dist_df


# %% [markdown]
# 
# 
# ---
# 
# 

# %% [markdown]
# # **SEGUNDA PARTE:**
# 
# 
# 
# ### > ***Geração do grafo solicitado nesta Etapa 1 do trabalho.***

# %% [markdown]
# > A partir do Dataframe 'cid_menores_dist' (as três cidades com menores distâncias entre si, de cada uma das 110), será gerado o grafo cujos **Vértices** serão os nomes das cidades e as **Arestas** a distância em Km entre cada uma das três mais próximas.

# %% [markdown]
# ## Criando as classes necessárias:

# %%
class Aresta():
    def __init__(self, vertice1, vertice2, peso):
        self.vertices = tuple((vertice1, vertice2))
        self.peso = peso


# %%
class Vertice():
    def __init__(self, rotulo):
        self.arestasIncidentes = []
        self.rotulo = rotulo #Nome da cidade

    def addAresta(self, aresta):
        self.arestasIncidentes.append(aresta)

    def getRotulo(self):
        return self.rotulo


# %%
class Grafo():
    def __init__(self):
        self.vertices = []
    
    def dataframeToGrafo(self, dataframe):
        # Cria os vertices apartir do dataframe coluna 'origem':
        for i in range(len(dataframe)): # iterar linhas do dataframe
            tuplaOrigem = tuple(dataframe['origem'][i])
            verticeOrigem = Vertice(str(tuplaOrigem[1]))
            self.addVertice(verticeOrigem)

        # Cria arestas associando os vertices criados acima, apartir das colunas distancia_1, distancia_2, distancia_3:
        for linha in range(len(dataframe)):  # iterar linhas do dataframe
            for i in range(1,4): #iterar colunas
                nomeColuna = f'distancia_{i}'
                tuplaCidadeDistancia = tuple(dataframe[nomeColuna][linha])
                distancia = tuplaCidadeDistancia[0]
                nomeCidadeDestino = tuplaCidadeDistancia[1]
                nomeCidadeOrigem = dataframe['origem'][linha][1]

                indexCidadeOrigem = self.getIndexCidadeByName(nomeCidade=nomeCidadeOrigem)
                indexCidadeDestino = self.getIndexCidadeByName(nomeCidade=nomeCidadeDestino)

                aresta = Aresta(vertice1=self.vertices[indexCidadeOrigem], vertice2=self.vertices[indexCidadeDestino], peso=distancia)
                self.vertices[indexCidadeOrigem].addAresta(aresta)
                self.vertices[indexCidadeDestino].addAresta(aresta)



        
    def getIndexCidadeByName(self, nomeCidade: str):
        for v in range(len(self.vertices)):
            if self.vertices[v].getRotulo() == nomeCidade:
                return v
        return None



    def addVertice(self, vertice):
        self.vertices.append(vertice)

  
    def _gerarDFMatrizZerada(self):
        cidades = [vertice.getRotulo() for vertice in self.vertices]
        matriz = {}
        
        for cidade in cidades:
            linhaDF = []
            for i in range(len(cidades)):
                linhaDF.append(0)
            matriz[cidade] = linhaDF

        dfMatriz = pd.DataFrame(data=matriz, columns=cidades, index=cidades )
        return dfMatriz

    def gerarMatrizAdjacencia(self):
        if len(self.vertices) == 0:
            return None

        dfMatriz = self._gerarDFMatrizZerada()
        
        for vertice in self.vertices:
            for aresta in vertice.arestasIncidentes:
                dfMatriz.loc[aresta.vertices[0].getRotulo(), aresta.vertices[1].getRotulo()] = aresta.peso
                dfMatriz.loc[aresta.vertices[1].getRotulo(), aresta.vertices[0].getRotulo()] = aresta.peso

        return dfMatriz
    
    def getVertices(self):
        return self.vertices

# %%
grafoCidades = Grafo()
grafoCidades.dataframeToGrafo(cid_menores_dist_df)
matriz = grafoCidades.gerarMatrizAdjacencia()
matriz

# %%
matriz.to_csv("MatrizAdjacencia.csv")

# %%
def buscaLargura(grafoBusca: Grafo, origem: Vertice):

    # Montando tabela
  header = [v.getRotulo() for v in grafoBusca.getVertices()]
  indices = ['TD','TT', 'Pai']

  matriz = []
  # Lista de vertices não explorados
  nao_explorados = list(grafoBusca.getVertices())
  
  # Matriz zerada
  for linhas in range(len(indices)):
    m = []
    for cols in range(len(header)):
        m.append(0)

    matriz.append(m)

  matrizDF = pd.DataFrame(matriz, index=indices ,columns=header) 

  marcados = []
  explorados = []
  ultimo_analisado = None

  tempo = 0
  # Parada: todos os vértices explorados
  while(len(nao_explorados) > 0):
    if tempo == 0:
        em_analise = origem
    else:
        # em_analise =
        pass
     
    # Marca vértice em análise
    marcados.append(nao_explorados.pop(nao_explorados.index(em_analise)))
    matrizDF.at['TD' , em_analise.getRotulo()] = tempo
    tempo += 1
    matrizDF.loc[matrizDF['Pai'], em_analise.getRotulo() ] = ultimo_analisado

    # Explorar vertices:
    for ars in em_analise.arestasIncidentes:
        destino = filter(lambda a: a != origem, ars)
        if not (destino in marcados):
            marcados.append(nao_explorados.pop(index(destino)))
            matrizDF.at['TD' , destino.getRotulo()] = tempo
            tempo +=1

    # Recebe vértice com menor TD


    # em_analise
    explorados.append(marcados.pop(marcados.index(em_analise)))
    matrizDF.at['TT' , explorados.getRotulo()] = tempo
    tempo+=1


buscaLargura(grafoCidades, grafoCidades.getVertices()[0])



