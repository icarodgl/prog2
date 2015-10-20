#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silabator.py
#  
#  Autor: Icaro Duarte Gavazza Lima ifes <ifes@ifes-vbox>
#  Criado em: 22/09/15 13:21:10
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: gera uma lista de silabas retiradas de uma string
#  Versão inicial: 1.0
#  ----------------------------------------------------------------

def separasilaba(parstr):
	result=[] #resultado
	straux="" #usado para acumular
	vog={"a","e","i","o","u"} #dicionario de vogais
	con={"b", "c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "q", "r", "s","t", "v", "w", "x", "z"} #dicionario de consoantes
	espec={"r","s","n","m","nh","gu","lh", "ch"}
##----------------------------------------------------------------------------------
	for ind in range(len(parstr)):
		straux+=parstr[ind]
		if ind == 0 and parstr[ind] in vog: #confere a primeira letra se é vogal.
			result.append(straux)
			straux=""
##-----------------------------------------------------------------------------------
		if len(straux) >= 0 and ind+1 < len(parstr): #confere se já acabou a palavra
			if parstr[ind+1] in espec or parstr[ind+1] in vog:
				straux
			
			if len(straux) >1 and straux[0] in con and (straux[1] in vog or straux[1] in con) and parstr[ind+1] not in vog: ##testa se é vogal seguida por consoante
				#if len(straux) >1 and straux[-1] in vog and parstr[ind+1] in con:
					result.append(straux)
					straux=""
				
				
			if len(straux)>= 1 and straux[-1] in "rs"and parstr[ind+1] in "rs":## testa se possue RR ou SS separando corretmente ex: TER-RA
				result.append(straux)
				straux=""
			if len(straux) >2 and straux[0] + straux[1] in espec and straux[-1] in vog:
				if  parstr[ind+1] in "rs":
					straux
				else:
					result.append(straux)
					straux=""
##-----------------------------------------------------------------------------------
	if len(straux)> 0:## garante que não sobrou letra na auxiliar
		result.append(straux)
##-----------------------------------------------------------------------------------
	return result
		
def main():
	textstr="piscina"
	print(separasilaba(textstr))
	return 0

if __name__ == '__main__':
	main()

