class GestionListe:
    def __init__(self, ma_liste):
        self.ma_liste = ma_liste

    def afficher_liste(self):
        print("Contenu de la liste :")
        for element in self.ma_liste:
            print(element)

    def modifier_liste(self, index, nouvel_element):
        if 0 <= index < len(self.ma_liste):
            self.ma_liste[index] = nouvel_element
            print("Élément à l'index {} modifié avec succès.".format(index))
        else:
            print("Index invalide. Impossible de modifier l'élément.")
