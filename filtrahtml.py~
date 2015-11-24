import sys
def salvatxt(parlis):
	#~ nomearq = input("nome do arquivo: ")
	nomearq= sys.argv[2]
	if nomearq [-4:len(nomearq)] != ".txt":
		nomearq+=".txt"
	arq = open(nomearq,"w")
	for elem in parlis:
		arq.write(elem)
	arq.close()
def filtrahtml(parstr,parlis):
	strresp = ""
	confere= True
	for ind in range (len(parstr)):
		if parstr[ind] == "<":
			#print(parstr[ind:ind+5])
			#if ind+5 < len(parstr) and parstr[ind:ind+5] == "<style": #style
			confere = False
		if confere == True:
			strresp+=parstr[ind]
		if parstr[ind] == ">":
			confere = True
	parlis.append(strresp)
	#
def abrehtml ():
	
	#~ nomehtml= input("nome do arquivo a ser filtrado: ")
	nomehtml = sys.argv[1]
	try:
		if nomehtml [-5:len(nomehtml)] != ".html":
			nomehtml +=".html"
		arq = open(nomehtml,"r")
		lisconteudo=[]
		linha = arq.readline()
		while linha != "":
			filtrahtml(linha,lisconteudo)
			linha = arq.readline()
		#~ tudo= arq.read()
		#~ filtrahtml(tudo,lisconteudo)
		arq.close()
		salvatxt(lisconteudo)
		#while
	#fim
		print("TADAAAAA!")
	except :
		print("Arquivo não encontrado")
def main():
	abrehtml()
	return 0

if __name__ == '__main__':
	main()

