from fonctions import*

for i in fonctionnom() :
	print(fonctionPrenom(i))

val = str(input("Chercher le TFIDF du mot : "))
dossier = str(input("Entrez le nom du fichier dans lequel vous voulez calculer le TFIDF : "))
print("Le TFIDF de ", val, " est de", fonctionIFIDF("Nomination_"+dossier+".txt",val))
