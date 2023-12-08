def fonctionnom() :					#function returning the list of every president's name from the file 'speeches'
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

def fonctionPrenom (i):						#function returning the fullname of a precised president
	prenom_dictionnaire = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron" : "Emmanuel", "Mitterrand" : "François", "Sarkozy" : "Nicolas"}
	return prenom_dictionnaire[i] + " " + i

def fonctionCleaned(nom_fichier) :					#function cleaning copying and cleaning from caps and non-alphanumeric character every file from 'speeches' to an other file 'cleaned'
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

def fonctionTF(filename) :					#function returning the frequency of appearence of a word in a text
	dicoIF = {}
	with open('cleaned/'+filename, "r") as f :
		lmots = f.read().split(" ")
	for i in range(len(lmots)):
		if '\n' in lmots[i]:
			lmots[i] = lmots[i].replace('\n', '')
		if 'Ã' in lmots [i] : 									#non alphanumeric character correction
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
	return dicoIF

def fonctionIDF () :					#function returning the importance of a word in a document corpus
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
			if 'Ã' in lmots[i]:  					#non alphanumeric charcater correction
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

	for i in dicoIDF :
		dicoIDF[i] = math.log((8 / dicoIDF[i] + 1), 10)
	return dicoIDF

def fonctionmatriceTFIDF (doc) :					#function returning a matrice containing TF and IDF
	import os
	matriceTFIDF = []
	tableauIDF = fonctionIDF()
	ligne = len(tableauIDF)
	col = 8
	for i in range(ligne+2) :
		matriceTFIDF.append([0]*(col+2))
	pos = int(2)
	for i in tableauIDF :
		matriceTFIDF[pos][0] = i
		matriceTFIDF[pos][1] = '|'
		pos += 1
	for i in range (2, len(matriceTFIDF)):
		for j in range (col) :
			matriceTFIDF[i][j+2] = tableauIDF[matriceTFIDF[i][0]]

	pos = 2

	for filename in os.listdir(doc):
		tableauTF = fonctionTF(filename)
		for i in range (2, len(matriceTFIDF)) :
			val = matriceTFIDF[i][0]
			if val not in tableauTF :
				tableauTF[val] = 0


		filename = filename[11:]
		filename = filename.replace('.txt', '')
		matriceTFIDF[0][pos] = filename
		matriceTFIDF[1][pos] = '_'

		for i in tableauTF :
			for j in range (2, len(matriceTFIDF)) :
				if i == matriceTFIDF[j][0] :
					matriceTFIDF[j][pos] = matriceTFIDF[j][pos] * tableauTF[i]

		pos += 1
	matriceTFIDF[0][0] = ' '
	matriceTFIDF[1][0] = ' '
	matriceTFIDF[0][1] = ' '
	matriceTFIDF[1][1] = ' '

	return matriceTFIDF

def fonctionprintTFIDF ():
	matriceTFIDF = fonctionmatriceTFIDF('cleaned')
	for i in range(len(matriceTFIDF)):
		for j in range(10):
			decalage = 20
			decalage -= len(str(matriceTFIDF[i][j]))
			print(matriceTFIDF[i][j], ' ' * decalage, end='')
		print('\n')

def fonctionMotNonImportants():					#function returning words that have a TFIDF score <1
	import os
	tableauIDF = fonctionIDF()
	util = {}
	for filename in os.listdir('cleaned'):
		tableauTF = fonctionTF(filename)
		for i in tableauTF:

			if i not in util:
				util[i] = 8

			if (tableauTF[i] * tableauIDF[i]) > 1:
				util[i] -= 1
	for i in util:
		if util[i] == 8 :
			print(i, end=' - ')
def fonctionImportants () :					#function returning the words that have a the biggest TFIDF score
	import os
	tableauIDF = fonctionIDF()
	util = {}
	for filename in os.listdir('cleaned'):
		tableauTF = fonctionTF(filename)
		for i in tableauTF:
			if i not in util :
				util[i] = tableauIDF[i]*tableauTF[i]
			else :
				if tableauIDF[i]*tableauTF[i] > util[i] :
					util[i] = tableauIDF[i] * tableauTF[i]
	max = 0
	mot = str()
	for i in util :
		if util[i] > max :
			mot = i
			max = util[i]
	print(mot)

def fonctionChirac () :					#fucntion returning the word that chirac mostly said
	dicofinal = {}
	for j in range(1, 3) :
		val = 'Nomination_Chirac'+ str(j) + ".txt"
		tableautf = fonctionTF(val)
		for i in tableautf :
			if i not in dicofinal :
				dicofinal[i] = tableautf[i]
			else :
				dicofinal[i] += tableautf[i]
	max = 0
	mot = str()
	for i in dicofinal :
		if dicofinal[i] > max :
			mot = i
			max = dicofinal[i]
	print("'",mot,"' dit ", dicofinal[mot], " fois")

def fonctionNation () :					#function returning the name of every president who said nation in his speeche and the one who said it the most
	import os
	tous =[]
	liste=fonctionnom()
	plus =[]
	plusn = 0
	i=-1
	for filename in os.listdir('cleaned'):
		tableauTF = fonctionTF(filename)
		filename = filename[11:]
		filename = filename.replace('.txt', '')
		if 'nation' in tableauTF :
			if filename not in liste:
				tous.append(filename[:-1])
			else:
				tous.append(filename)
			if tableauTF['nation'] > plusn :
				plusn = tableauTF['nation']
				if filename not in liste :
					tous.append(filename[:-1])
					plus.append(filename[:-1])
				elif filename in liste :
					tous.append(filename)
					plus.append(filename)
	tous=set(tous)
	tous1=''
	plus1=''
	for i in tous:
		tous1+= i
		tous1+= ', '
	for j in plus:
		plus1+=j
	print("Tout les présidents ayant dit le mot 'Nation' : ", tous1, "\nEt celui l'ayant le plus dit : ", plus1, plusn, "fois")

def fonctionEcologie () :					#function returning the name of the first president who talked about environement
	import os
	dates = {"Chirac1": 1995,"Chirac2": 2002, "Giscard dEstaing": 1974, "Hollande": 2012, "Macron" : 2017, "Mitterrand1" : 1988, "Mitterrand2" : 1995, "Sarkozy" : 2007}
	date = int(2050)
	president = str()
	for filename in os.listdir('cleaned'):
		tableauTF = fonctionTF(filename)
		if 'climat' in tableauTF or 'écologie' in tableauTF or 'climatique' in tableauTF or 'écologique' in tableauTF:
			filename = filename[11:]
			filename = filename.replace('.txt', '')
			if dates[filename] < date :
				date = dates[filename]
				president = filename
	print("Le premier président à parler du climat et/ou de l'écologie est :", president)

def fonctionMotCommun () :					#function returning the common words between two texts
	matricetfidf = fonctionmatriceTFIDF('cleaned')
	listemotcommun = str()

	for i in range (2, len(matricetfidf)) :
		compte = 0
		for j in range (2, len(matricetfidf[0])) :
			if matricetfidf[i][j] != 0 :
				compte += 1
				if compte == 8 :
					if matricetfidf[i][0] != '' :
						listemotcommun += matricetfidf[i][0]
						listemotcommun += ', '
	print('La liste des mots communs à tous les discours est : ', listemotcommun[:-2])
