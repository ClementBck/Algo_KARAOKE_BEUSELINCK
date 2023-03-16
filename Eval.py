#Création de la classe Player
class Player:
    def __init__(self,pseudo, score):
        self.pseudo = pseudo
        self.score = score
    #Création de la liste des score (les éléments sont à 0 car il n'y a pas encore de musique jouée)
        self.score = [0, 0, 0, 0, 0]

    #Création de la méthode afficherScore qui renvoie la liste de score
    def afficherScore(self):
        print(self.score)

    #Création de la méthode ajouterScore permettant d'ajouter un score au tableau en fonction de la musique choisie
    def ajouterScore(self, numMusique, nouveauScore):
        #Vérification des différentes condition afin de savoir si le score est bien supérieur au précédent, celui-ci sera alors écrasé
        if (nouveauScore > self.score[numMusique] and nouveauScore >= 50 and nouveauScore <= 100):
            self.score[numMusique] = nouveauScore
        #Le score minimum étant 50/100, on vérifie alors que le score minimal par musique sera de 50 et le max de 100 afin d'avoir un max de 100/100
        if (nouveauScore < 50 or nouveauScore > 100):
            print("Le score rentré n'est pas valide !")

    #Création de la méthode permettant de calculer le score total d'un joueur grâce à une boucle For
    def totalScore(self):
        total = 0
        for i in range (len(self.score)):
            total = total + self.score[i]
        print(total)
    #Création de la méthode permettant de calculer la moyenne de d'un joueur grâce à une boucle For et au score total
    def moyenneScore(self):
        total = 0
        for i in range (len(self.score)):
            total = total + self.score[i]
        moyenne = (total / 5)
        print(moyenne)

    #Création de la méthode meilleureMusique vérifiant dans la liste à quel emplacement se situe le meilleur score d'un joueur, puis renvoie la musique en question
    def meilleureMusique(self):
        meilleurScore = 0
        meilleureMusique = 0
        for i in range (len(self.score)):
            if (self.score[i] > meilleurScore):
                meilleurScore = self.score[i]
                meilleureMusique = i
        print("La meilleure musique pour " + self.pseudo + " est : ") 
        print(meilleureMusique)

    #Création de la méthode pireMusique vérifiant dans la liste à quel emplacement se situe le pire score du joueur avant de lui renvoyer la musique en question
    def pireMusique(self):
        pireScore = 9999
        pireMusique = 0
        for i in range (len(self.score)):
            if (self.score[i] < pireScore):
                pireScore = self.score[i]
                pireMusique = i
        print("La pire musique pour " + self.pseudo + " est : ") 
        print(pireMusique)

#Création du player test puis ajout du score et test des différentes méthodes
test = Player("test", 0)
test.afficherScore()
test.ajouterScore(1, 50)
test.afficherScore()
test.ajouterScore(1, 55)
test.afficherScore()
test.ajouterScore(1, 52)
test.ajouterScore(0, 58)
test.ajouterScore(2, 80)
test.ajouterScore(3, 54)
test.ajouterScore(4, 78)
test.afficherScore()
test.totalScore()
test.moyenneScore()
test.meilleureMusique()
test.pireMusique()
