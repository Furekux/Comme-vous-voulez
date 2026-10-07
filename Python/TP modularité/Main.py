import Recherche
import bdd
import Contacts

connexion = bdd.connecter("carnet.db")
liste = bdd.charger(connexion)
liste = Contacts.ajouter_contact(liste,"Hazard","0622188456")
liste = Contacts.ajouter_contact(liste,"Loree","0789038516")
liste = Contacts.ajouter_contact(liste,"Loqmani","0676767676")
liste = Contacts.ajouter_contact(liste,"Zannier","0689541754")
bdd.inserer(connexion, "Hazard","0622188456")
bdd.inserer(connexion, "Loree","0789038516")
bdd.inserer(connexion, "Loqmani","0676767676")
bdd.inserer(connexion, "Zannier","0689541754")
print(Recherche.recherche_dichotomique(liste, "Hazard"))
print(Recherche.recherche_dichotomique(liste, "Cacaproutjesuistrèsmature"))
if __name__ == "__main__":
    connexion.close()