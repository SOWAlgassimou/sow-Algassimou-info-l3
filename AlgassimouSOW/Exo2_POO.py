class Personne:
    def __init__(self,nom,sante,proba_infection):
        self.nom=nom
        self.sante=sante
        self.proba_infection=proba_infection

    def __init__(self,nom,proba_infection):
        return self.nom and self.proba_infection

    def infecter(self):
        print("l'etat de santé est infecté")

    def immuniser(self):
        print("l'etat de santé est immunisé")

    def __str__(self):
        return self.nom and self.sante

class Population:
    def __init__(self,nom,sante,proba_infection):
        self.nom=nom
        self.sante=sante
        self.proba_infection=proba_infection

    def __init__(self, taille_population, proba_infection):
        self.taille_population=taille_population
        return self.taille_population and self.proba_infection

    def introduire_infection(self, nombre_infectes):
        self.nombre_infectes=nombre_infectes
        return self.nombre_infectes

    def simuler_jour(self, proba_guerison):
        self.proba_guerison=proba_guerison
        return self.proba_guerison

    def __str__(self):
        return self.nombre_infectes

personne1=Personne("SOW", "Saine", "25.45%")
print(personne1.nom)
print(personne1.sante)
print(personne1.proba_infection)

personne1.__init__()
personne1.infecter()
personne1.immuniser()
personne1.__init__("Barry", "Saine")

Population1=Population("SOW", "Saine", "25.45%")
Population1.__init__()
Population1.introduire_infection()
Population1.simuler_jour()


## 1) Creation d'une population de 1000 personnes avec une probabilité d'infection de 0.1
i = 0
for populat in Population:
    if i <= 1000 and i >=0:
        print(personne1.nom)
        print(personne1.proba_infection(0.1))
    else:
        print("veillez entrer un nombre compris entre 1 et 1000 ")
print("Fin du programme")

## 2) Introduisons 10 personnes:
i = 0
for populat in Population:
    if i <= 10 and i>=0:
        print(personne1.nom)
    else:
        print("veillez entrer un nombre compris entre 1 et 10 ")
print("Fin du programme")

