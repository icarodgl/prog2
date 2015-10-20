#retira acentos, separa palavras em uma lista e conta palavras.
#icaro Duarte Gavazza Lima
#  
#este programa retira acentos de uma sting
#
def remove_acento(par_strA):
	dic_compara={"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", "â":"a", "ê":"e", "î":"i", "ô":"o", "û":"u", "ç":"c", "ã":"a", "õ":"õ" }
	straux=""
	for i in range (len(par_strA)):
		if par_strA[i] in dic_compara:
			straux=straux+dic_compara[par_strA[i]]
		else:
			straux=straux+par_strA[i]
		#if
	#for
	return straux
#fim
def listador(par_strB):
	lista_aux = []
	pegastr=""
	for i in range (len(par_strB)):
		
		if not par_strB[i].isalnum():
			if pegastr != "":
				lista_aux.append(pegastr)
				pegastr=""
			else:
				pegastr=""
			#if
		#if
		else:
			pegastr=pegastr+par_strB[i]
		#if
	#for
	return lista_aux
#fim
def main():
	strA="O avô é índio! também bebe cachaça? b01."
	strB=remove_acento(strA)
	lisA=[]
	print(strB)
	lisA=listador(strB)
	print(lisA)
	intA=len(lisA)
	print("A string possue: ", intA, "palavras alfanumericas.")
	return 0
##fim main
if __name__ == '__main__':
	main()

