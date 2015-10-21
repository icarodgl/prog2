def extraidata(parstr):
	lispals=separaPals(parstr)
	buff= ""
	dicresp={"dia":"","mes":"","ano":""}
	dicmeses={"janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro","jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"}
	for ind in range (len(lispals)):
	
		if lispals[ind].lower() in dicmeses :
			
			dicresp["mes"]=lispals[ind].lower()
			if buff.isdecimal():
				 dicresp["dia"]=buff
			#
			if buff in ["de","do"]:
				dicresp["dia"] = lispals[ind-2]
			if len(lispals)>= 2 and (lispals[ind-2]).isdecimal():
				dicresp["dia"]=lispals[ind-2]
			#
		#
		if lispals[ind].isdecimal():
			if int(lispals[ind]) <= 12 and buff in ["do","de"]:
				if buff.isdecimal():
					 dicresp["dia"]=int(buff)
				dicresp["mes"]=int(lispals[ind])
		#
		if lispals[ind].isdecimal():
			if int(lispals[ind]) >= 1800:
				dicresp["ano"]=int(lispals[ind])
			#if
		#if
		buff= lispals[ind]
	#for
	return dicresp
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
def n_grama(par_str,par_n): 
	listares=[]
	straux=""
	intaux=0
	for ind in range (len(par_str)):
		intaux=ind+par_n
		if intaux <= len(par_str):
			for indn in range(ind,intaux):
				straux+=par_str[indn]
			listares.append(straux)
			straux=""
			#for
		else:
			return listares
		#if
	#for
#def
def corrente(parstr,parint):
	strpal=""
	ind= parint
	if not parstr[parint].isalnum() or parint > len(parstr):
		 return None
	#if
	while parstr[ind].isalnum() and len(parstr) > 0: #rebobina
		ind-=1
	#while
	ind+=1
	while parstr[ind].isalnum() and len(parstr) > ind+1 : # pega a palavra
		strpal+=parstr[ind]
		ind+=1
	#while
	return strpal
#fim
#~ def corrente(parstr,parint):
	#~ strpal=""
	#~ ind= parint
	#~ if not parstr[parint].isalnum() or parint > len(parstr):
		 #~ return None
	#~ #if
	#~ 
	#~ while parstr[ind].isalnum() and len(parstr) > 0: #rebobina
		#~ ind-=1
	#~ #while
	#~ while parstr[ind+1].isalnum():
		#~ ind+=1
		#~ strpal+=parstr[ind]
	#~ #while
	#~ return strpal
#fim
def justificador(parstr,parint):
	indic=0
	intcont=0
	lisresp=[]
	checa=True
	while checa == True:
		checa=False
		if len(parstr)> intcont:
			
#			if parstr[intcont].isalnum:
#				indic = intcont+parint
#				while indic > 0 and parstr[indic].isalnum() : #rebobina
#					indic-=1
#				intcont=indic
			lisresp.append(parstr[intcont:indic])
			intcont+=parint
			checa=True
		#if
	#while
	return lisresp
			
def imprime(parlista):
	
	for elem in parlista:
		print(elem)

def separaPals(paramtxt):
	strbuffer = ""
	lst = []
	
	for elem in paramtxt:
		if (elem == "-" or elem == "'") or elem.isalnum():
			strbuffer += elem
		else:
			if strbuffer != "":
				lst.append(strbuffer)
				strbuffer = ""			
			#if
		#else
	#for
	if len(strbuffer) > 0:
		lst.append(strbuffer)
		
	return lst
#fim separaPalavras		

def extrairPlural(lstparam):
	dicsufixo = {"as":"as","es":"es","os":"os","is":"is","ns":"ns"}
	lstaux = []
	
	for pal in lstparam:
		aux = (pal[len(pal)-2])+(pal[len(pal)-1])
		
		if aux in dicsufixo:
			lstaux.append(pal)
			aux = ""
		#if
	#for
		
	return lstaux
#fim extrairPlural

def extrairdimi(lstparam):
	dicsufixo = {"nha": 1,"nho": 1}
	lstaux = []
	for pal in lstparam:
		if len(pal) > 3:
			aux = (pal[len(pal)-3])+(pal[len(pal)-2])+(pal[len(pal)-1])
		#if
		
		if aux in dicsufixo:
			lstaux.append(pal)
			aux = ""
		#if
	#for 
	return lstaux
#fim extrairdimi	

def extraiaument(lstparam):
	dicsufixo = {"ão": 1,"rra": 1,"zão":"zão"}
	lstaux = []
	
	for pal in lstparam:
		if len(pal) > 3:
			aux = (pal[len(pal)-3])+(pal[len(pal)-2])+(pal[len(pal)-1])
		#if
		if aux in dicsufixo:
			lstaux.append(pal)
			aux = ""
		#if
	#for	
	return lstaux

#~ def frequenciador(parls,pardic):
	#~ dicesp={jesus,cristo,deus}
	#~ for elem in parls:
		#~ if elem in dicesp:
			#~ 
			#~ 
		#~ elif elem.lower() not in pardic :
			#~ pardic[elem.lower()]=1
			#~ else:
				#~ pardic[elem.lower()]+=1
	#~ return pardic

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



def anterior(parstr,parint):
	strpal=""
	ind= parint
	
	if not parstr[parint].isalnum() or parint < 0:
		 return None
	#if
	while parstr[ind].isalnum() and len(parstr) > 0 and ind >= 0: #rebobina até o primeiro espaço
		ind-=1
		if ind <=0 :
			return None
		#if
	#while
	while not parstr[ind].isalnum() and len(parstr) > 0 and ind >= 0: #rebobina até a primeira letra
		ind-=1
		if ind <=0 :
			return None
		#if
	#while
	while parstr[ind].isalnum() and len(parstr) > 0 and ind >= 0: #rebobina a palavra
		ind-=1
	#while
	ind+=1
	while parstr[ind].isalnum():# escreve a palavra
		strpal+=parstr[ind]
		ind+=1
	#while
	return strpal
#fim



def posterior(parstr,parint):
	strpal=""
	ind= parint
	
	if not parstr[parint].isalnum() or parint > len(parstr):
		 return None
	#if
	
	while parstr[ind].isalnum() and len(parstr) > 0: #avança até o primeiro espaço
		if ind+1 >= len(parstr):
			return None
		#if
		ind+=1
	#while
	while not parstr[ind].isalnum() and len(parstr) > 0: #avança enquanto for separador
		if ind+1 >= len(parstr):
			return None
		#if
		ind+=1
	#while
	while parstr[ind].isalnum():# escreve a palavra
		if ind+1 >= len(parstr):
			return None
		#if
		strpal+=parstr[ind]
		ind+=1
	#while
	return strpal
def main():
	
	return 0

if __name__ == '__main__':
	main()

