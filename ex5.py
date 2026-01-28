# ex5.py

def TROUVER_MAXIMUM(liste):
    """
    Retourne le plus grand élément d'une liste de nombres.
    """
    if not liste:
        return None
    
    maximum = liste[0]
    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
    return maximum

# Exemple d'utilisation
if __name__ == "__main__":
    nombres = [3, 7, 2, 9, 5]
    print("Le maximum est :", TROUVER_MAXIMUM(nombres))