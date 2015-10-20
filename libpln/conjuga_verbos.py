#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  conjuga_verbos.py
#  
#  Autor: Icaro Duarte Gavazza Lima
#  Criado em: 18/09/15 10:40:00
#  Usuário: IFES Serra Lógica Prog\Téc Prog\Prog I\Prog II
#  
#  Função do programa: conjuga verbos regulares da 1ª, 2ª e 3ª conjugação no presente.
#  Versão inicial: 1.0
#  ----------------------------------------------------------------
def conjugador(parstr):
	conjdic={"ir":["o","es","e","imos","is","em"],"ar":["o","as","a","amos","ais","am"],"er":["o","es","a","emos","eis","em"]}# 1ª,2ª ou 3ª conjugação.
	lisconj=[]
	straux=""
	strrad=""
	straux=(parstr[len(parstr)-2])+(parstr[len(parstr)-1]) #armazena o sulfixo
	if straux not in conjdic or len(parstr)-2 < 1:
		return None
	#if
	for ind in range (len(parstr)-2):
		strrad+=parstr[ind]
	#for
	for sulf in conjdic[straux]:
		lisconj.append(strrad+sulf)
	#for
	return lisconj
#fim
def main():
	strverbo= "estudar"
	print(conjugador(strverbo))
	return 0
#fim
if __name__ == '__main__':
	main()

