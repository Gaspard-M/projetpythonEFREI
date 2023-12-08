from fonctions3 import *
from time import sleep

print('Nom des différents présidents de la 5ème république étudiés :')
for i in fonctionnom():
	if i != fonctionnom()[-1]:
		print(fonctionPrenom(i), end=' - ')
	else:
		print(fonctionPrenom(i), '\n')

listfonctionnalites = ['1', '2', '3', '4', '5', '6', '7', '8']
fini = 0
while fini == 0:
	val = str(input(
		"Liste des fonctionnalités :\n1 - Mots non importants\n2 -  TFIDF le plus élevé\n3 -  Mot répété par Chirac\n4 -  Liste des présidents ayant dit 'Nation'\n5 -  Premier président à parler d'environement\n6 -  Liste des mots communs aux discours\n7 -  Afficher tout les TFIDF\n8 -  Arrêt du programme\nInsérer le numéro de la fonction :\n"))
	while val not in listfonctionnalites:
		val = str(input(
			"Liste des fonctionnalités :\n1 - Mots non importants\n2 -  TFIDF le plus élevé\n3 -  Mot répété par Chirac\n4 -  Liste des présidents ayant dit 'Nation'\n5 -  Premier président à parler d'environement\n6 -  Liste des mots communs aux discours\n7 -  Afficher tout les TFIDF\n8 -  Arrêt du programme\nInsérer le numéro de la fonction :\n"))

	if val == '1':
		print("Liste des mots avec un TFIDF inférieur à 1 dans tout les document : ")
		fonctionMotNonImportants()
		print('\n')
		sleep(5)
	if val == "2":
		print("Liste des mots avec les TFIDF les plus élevés : ")
		fonctionImportants()
		sleep(5)
	if val == "3":
		print("Le mot le plus répété par Chirac au cours de ces deux discours est : ")
		fonctionChirac()
		sleep(5)
	if val == '7':
		fonctionprintTFIDF()
		sleep(5)
	if val == '4':
		fonctionNation()
		sleep(5)
	if val == '5':
		fonctionEcologie()
		sleep(5)
	if val == '6':
		fonctionMotCommun()
		sleep(5)
	if val == '8':
		fini = 1