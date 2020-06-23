# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:09:41 2019

@author: tarique.ramos
"""

import pandas as pd



#base = pd.read_csv('LotOrgao_DistOcupVagas112019.csv', encoding = 'latin-1', sep = ';')
base = pd.read_excel('http://repositorio.dados.gov.br/segrt/LotOrgao_DistOcupVagas%20-%20202001.xlsx','por Orgao e Cargo')

#separa colunas

texto = base.iloc[:,[0,2,3,4,6,7,9,10]]



#retira os valores nulos
#df_sn = texto.loc[(texto['VAGO'] > 0) ]
#df_remove2 = texto.loc[(texto['VAGO'] < 1)]
#txtosn = texto.drop(df_remove2.index)
#txtosn = texto.loc[(texto['VAGO'] > 0) ]


# criar uma nova coluna

texto['PERTMINIST'] = ''



# inserir ministerios
def ministerio(minis,valorf):  
    #verifica quantos orgaos pertence aquele ministerios   
    n=len(minis)
    i=0
    while(i < n):
        #
        texto.loc[texto['SIGLA_ORGAO'] == minis[i], 'PERTMINIST'] = valorf
        i=i+1
     
         
##################  
        
        
  

                      
# entidades do MEC
valor = 'MEC'
conmec = ['MEC','INES','I.B.CONST','C.PEDROII','UNIVASF','UFAL','UFBA','UFCE','UFES','UFGO','UFF','UFMG','UFPA','UFPB','UFPE','UFRN','UFRGS/RS','UFRJ','UFSC','UFSM/RS','UFRPE','UFRRJ','UFRR','FUFT','UFCG','UFRA','UFTM','UFVJM','CEFET/RJ','CEFET/MG','UTFPR','UNIFAL-MG','UNIFEI','UFLA','UFERSA-RN','UNIPAMPA','UNILA','FUAM','UNB','FUMA','FURG','UFU','UFAC','UFMT','FUFOP','FUFPEL','UFPI','UFV','FUFS','FUFSCAR','UFMS','UFCSPA','FUNREI','UNIFAP','CAPES','UFGD','UFRB','UFABC','IFAC','IFBAIANO','IFCE','IFES','IFGOIANO','IFMA','IFMG','IFNORTEMG','IFSUDMG','IFSULMG','IFTRIANMG','IFMT','IFMS','IFPA','IFPB','IFPE','IFRS','IFFARROUP','IFRO','IFCATARINA','IFSE','IFTO','IFAP','IFBA','IFBRASILIA','IFGO','IFSERTPE','IFPI','IFPR','IFRJ','IFFLU','IFRN','IFSRIOGRAN','IFRR','IFSC','IFSP','UFFS','UFOPA','UNILAB','UFOB','UNIFESSPA','UFCA','UFMG','UFJF','UFESBA','UNIR','UNIRIO','INEP','FUNDO NACIONAL DE DESENVOLV. DA EDUCACAO','IFAL','IFAM','CAPES','UFPR','UNIFESP','FNDE','FJN']
ministerio(conmec,valor) 
# entidades do ministerio da economia
valor = 'ME'
conme = ['CVM','SUSEP','INSS','INMETRO','ME','SIPEC','INPI','PREVIC','SUFRAMA','ENAP','IBGE','IPEA','F.CENTRO','DECIP/SGP']
ministerio(conme,valor)
# entidades do Ministerio da defesa

valor = 'MD'
conmd = ['MD','CM','C.AER','C.EX','F OSORIO']
ministerio(conmd,valor)

# entidades do ministerio do meio ambiente
valor = 'MMA'
conmma = ['IBAMA','ICMBIO','JBRJ','MMA']
ministerio(conmma,valor)

#Entidades ministerio da jutiça
valor = 'MJ'
conmj = ['MJ','DPF','DPRF','FUNAI','CADE']
ministerio(conmj,valor)
# Entidades do ministerio da saúde
valor = 'MS'
conms = ['MS','FUNASA','FIOCRUZ','ANVS','ANS']
ministerio(conms,valor)
# ENTIDADES DO MAPA
valor = 'MAPA'
conmapa = ['INCRA','MAPA']
ministerio(conmapa,valor)
# MINISTERIO DA CIDADANIA
valor = 'MC'
conmc = ['MC','IPHAN','FCP','ANCINE','IBRAM','FCRB','FBN','FUNARTE']
ministerio(conmc,valor)
# MINISTERIO DA INFRAESTRUTURA
valor = 'MINFRA'
conminfra = ['MINFRA','DNIT','ANTAQ','ANAC','ANTT']
ministerio(conminfra,valor)


# MINISTERIO RELAÇÕES EXTERIORES
valor = 'MRE'
conmre = ['MRE','FAG']
ministerio(conmre,valor)

#minas e Energia
valor = 'MME'
conmme = ['MME','ANM','ANEEL','ANP']
ministerio(conmme,valor)

#AGU

valor = 'AGU'
conagu = ['AGU']
ministerio(conagu,valor)


#CGU
valor = 'CGU'
concgu = ['CGU']
ministerio(concgu,valor)
# ministerio ciencia e tecnologia
valor = 'MCTIC'
conmctic = ['MCTIC','ANATEL','CNPQ','AEB','CNEN']
ministerio(conmctic,valor)



#DENFENSORIA DA UNIÃO
valor = 'DPU'
condpu = ['DPU']
ministerio(condpu,valor)
# presidencia
valor = 'PR'
conpr = ['PR','ABIN']
ministerio(conpr,valor)


# Desenvolvimento regional
valor = 'MDR'
conmdr = ['MDR','SUDAM','SUDENE','SUDECO','DNOCS','ANA']
ministerio(conmdr,valor)

# MINISTERIO DO TURISMO
valor = 'MTUR'
conmtur = ['MTUR','EMBRATUR']
ministerio(conmtur,valor)

# Direitos humanos
valor = 'MMFDH'

condir = ['MMFDH']
ministerio(condir,valor)
#GOVERNO DO EX-TERRITORIO DO AMAPA

valor = 'EX-TER/AP'
conap = ['EX-TER/AP']
ministerio(conap,valor)
#GOVERNO DO EX-TERRITORIO DE RONDONIA

valor = 'EX-TER/RO'
conro = ['EX-TER/RO']
ministerio(conro,valor)
#GOVERNO DO EX-TERRITORIO DE RORAIMA

valor = 'EX-TER/RR'
conrr = ['EX-TER/RR']
ministerio(conrr,valor)


#Exportar aquivos 
texto.to_csv('ogao112019.csv', index=None,sep = ';')    
