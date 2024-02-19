from souhaiel import GestionListe


def main():
    ma_liste = ["a", "b", "c", "d", "e"]
    gestion_liste = GestionListe(ma_liste)

    print("Affichage initial de la liste :")
    gestion_liste.afficher_liste()

 
    gestion_liste.modifier_liste(2, "z")

    print("\nAffichage de la liste après modification :")
    gestion_liste.afficher_liste()

if __name__ == "__main__":
    main()
