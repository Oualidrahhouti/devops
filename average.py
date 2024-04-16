def moyenne_liste(liste):
    # Vérifier si la liste est vide
    if len(liste) == 0:
        return 0  # Retourner 0 si la liste est vide pour éviter une division par zéro
    else:
        # Calculer la somme des valeurs dans la liste
        somme = sum(liste)
        # Calculer la moyenne en divisant la somme par le nombre d'éléments dans la liste
        moyenne = somme / len(liste)
        return moyenne

