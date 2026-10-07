# Les imports + alphabet
alphabet = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
# Liste donnée

contacts_tries = [ ("Bernard", "0656789012"), ("Chevalier", "0645678901"), ("Diallo", "0623456789"), ("Girard", "0690123456"), ("Lefevre", "0689012345"), ("Martin", "0612345678"), ("Nguyen", "0667890123"), ("Petit", "0601234567"), ("Roux", "0634567890"), ("Simon", "0678901234"), ]

# PARTIE 1
# Carnet vide
def creer_carnet():
    carnet = []
    return carnet

# PARTIE 2
# Ajouter contact
def ajouter_contact(carnet, nom, telephone):
    if carnet == [] :
        base_tpl = (nom.title(), telephone) # Définition du tuple
        place=0
        return [(nom,telephone)]
    else:
        base_tpl = (nom.title(), telephone) # Définition du tuple
        # Variables nulles pour caller après
        place = 0
        for contacts in carnet: # Check tout l'annuaire
            if int(alphabet[nom.upper()[0]]) > int(alphabet[contacts[0][0]]): # Si la lettre est plus grande
                while int(alphabet[nom.upper()[0]]) > int(alphabet[contacts[0][0]]):
                    place += 1 # On change de place
                    break # On sort de la boucle
            if int(alphabet[nom.upper()[0]]) == int(alphabet[contacts[0][0]]): # Si la lettre est la même
                for i in range(len(nom.upper())):
                    if int(alphabet[nom.upper()[i]]) == int(alphabet[contacts[0][0]]):
                        while int(alphabet[nom.upper()[i]]) == int(alphabet[contacts[0][0]]):
                            if int(alphabet[nom.upper()[i]]) > int(alphabet[contacts[0][0]]): # Si la lettre est plus grande
                                place += 1 # On change de place
                                break # On sort de la boucle
                            if int(alphabet[nom.upper()[i]]) < int(alphabet[contacts[0][0]]): # Si la lettre est plus petite
                                place -= 1 # On change de place
                                break # On sort de la boucle
                            break
        carnet.insert(place, base_tpl) # Add
        return carnet

# PARTIE 3
# Supprimer contact
def supprimer_contact(carnet, nom):
    if nom in carnet:
        carnet.remove(nom) # Remove