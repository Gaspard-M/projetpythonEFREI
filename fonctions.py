def fonctionnom() :
	files_names = []
	names = []
	import os
	for filename in os.listdir('speeches'):
		if filename.endswith(".txt"):
			files_names.append(filename)
	for name in files_names:
		name = name[11:]
		name = name.split('.')
		name = name[0]
		if '1' in name or '2' in name:
			name = name[:-1]
		names.append(name)
	return sorted(set(names))

def fonctionPrenom (i):
	prenom_dictionnaire = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron" : "Emmanuel", "Mitterrand" : "François", "Sarkozy" : "Nicolas"}
	return prenom_dictionnaire[i] + " " + i

def fonctionCleaned(nom_fichier) :
	import os
	l1 = [',',';',':','/','.','(',')','"',"_","!","?"]
	l2 = ["-","'", " "]
	if not os.path.exists('cleaned') :
		os.mkdir('cleaned')
	with open ('cleaned/'+nom_fichier,"w" ) as f :
		with open ('speeches/'+nom_fichier,"r" ) as d :
			txt = d.read()
			for i in txt :
				for j in i :
					if j not in l1 :
						if ord(j) < 91 and ord(j) > 64 :
							f.write(chr(ord(j)+32))
						elif j in l2 :
							f.write(" ")
						elif ord(j) == 10 :
							f.write(" ")
							f.write(j)
						else :
							f.write(j)

def fonctionIF(filename, mot) :
	dicoIF = {}
	with open('cleaned/'+filename, "r") as f :
		lmots = f.read().split(" ")
	for i in range(len(lmots)):
		if '\n' in lmots[i]:
			lmots[i] = lmots[i].replace('\n', '')
		if 'Ã' in lmots [i] : 									#Correction des caractères spéciaux
			lmots[i] = lmots[i].replace('Ã©', 'é')
			lmots[i] = lmots[i].replace('Ã¹', 'ù')
			lmots[i] = lmots[i].replace('Ã\xa0', 'à')
			lmots[i] = lmots[i].replace('Ã§', 'ç')
			lmots[i] = lmots[i].replace('Ã¢', 'â')
			lmots[i] = lmots[i].replace('Ãª', 'ê')
			lmots[i] = lmots[i].replace('Ã¨', 'è')
			lmots[i] = lmots[i].replace('Ãª', 'ê')
			lmots[i] = lmots[i].replace('Ã´', 'ô')
		if lmots[i] == ' ':
			del(lmots[i])
	#print(
	for i in lmots :
		if i not in dicoIF :
			dicoIF[i] = 1
		else :
			dicoIF[i] = dicoIF[i]+1
	return dicoIF[mot]
def fonctionIDF (mot) :
	dicoIDF={}
	import os
	import math
	for filename in os.listdir('cleaned'):
		util=[]
		with open('cleaned/' + filename, "r") as f:
			lmots = f.read().split(" ")
		for i in range(len(lmots)):
			if '\n' in lmots[i]:
				lmots[i] = lmots[i].replace('\n', '')
			if 'Ã' in lmots[i]:  # Correction des caractères spéciaux
				lmots[i] = lmots[i].replace('Ã©', 'é')
				lmots[i] = lmots[i].replace('Ã¹', 'ù')
				lmots[i] = lmots[i].replace('Ã\xa0', 'à')
				lmots[i] = lmots[i].replace('Ã§', 'ç')
				lmots[i] = lmots[i].replace('Ã¢', 'â')
				lmots[i] = lmots[i].replace('Ãª', 'ê')
				lmots[i] = lmots[i].replace('Ã¨', 'è')
				lmots[i] = lmots[i].replace('Ãª', 'ê')
				lmots[i] = lmots[i].replace('Ã´', 'ô')
			if lmots[i] == ' ':
				del (lmots[i])

		for i in lmots:
			if i not in dicoIDF:
				if i not in util :
					util.append(i)
					dicoIDF[i] = 1
			else:
				if i not in util:
					util.append(i)
					dicoIDF[i] = dicoIDF[i] + 1
			#print(util)
	return math.log((8/dicoIDF[mot]+1))

def fonctionIFIDF (a, b) : #('nom de fichier', 'mot pour lequel il faut calculer le tfidf')
	return fonctionIF(a,b) * fonctionIDF(b)

