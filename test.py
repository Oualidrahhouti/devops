import pytest

# Importer la fonction moyenne_liste du fichier où elle est définie
from average import moyenne_liste


# Définir la fonction de test
def test_moyenne_liste():

    data = [5 ,2 ,5]
    # Appeler la fonction moyenne_liste avec la liste de test
    result = moyenne_liste(data)
    # Vérifier si le résultat est égal à la moyenne attendue
    assert result == 4
