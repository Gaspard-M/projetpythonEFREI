from fonctions2 import*

for i in fonctionnom() :
	print(fonctionPrenom(i))

listfonctionnalites = ["mots non important", "tfidf élevé", 'repetchirac', "nation", "eco", 'commun', 'afficher tout les TFIDF', 'fin']
fini = 0
while fini == 0 :
	val = str(input("Liste des fonctionnalités : 'mots non important', 'tfidf élevé', 'repetchirac', 'nation', 'eco', 'commun', 'afficher tout les TFIDF', 'fin' : "))
	while val not in listfonctionnalites :
		val = str(input("Liste des fonctionnalités : 'mots non important', 'tfidf élevé', 'repetchirac', 'nation', 'eco', 'commun', 'afficher tout les TFIDF', 'fin' : "))

	if val == "mots non important" :
		print("Listes des mots avec un TFIDF inférieur à 1 dans tout les document : ")
		fonctionMotNonImportants()
	if val == "tfidf élevé" :
		print("Listes des mots avec les TFIDF les élevé : ")
		fonctionImportants()
	if val == "repetchirac" :
		print("Le mot le plus répété par Chirac au cours de ces deux discours est : ")
		fonctionChirac()
	if val == 'afficher tout les TFIDF' :
		fonctionprintTFIDF()
	if val == 'nation' :
		fonctionNation()
	if val == 'eco' :
		fonctionEcologie()
	if val == 'commun' :
		fonctionMotCommun()
	if val == 'fin' :
		fini = 1