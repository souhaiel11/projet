class GestionListe:
    def init(animal, ma_liste):
        animal.ma_liste = ma_liste

    def afficher_liste(animal):
        print("Contenu de la liste :")
        for element in animal.ma_liste:
            print(element)

    def modifier_liste(animal, index, nouvel_element):
        if 0 <= index < len(animal.ma_liste):
            animal.ma_liste[index] = nouvel_element
            print("Élément à l'index {} modifié avec succès.".format(index))
        else:
            print("Index invalide. Impossible de modifier l'élément.")
