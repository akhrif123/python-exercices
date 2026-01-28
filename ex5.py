
def TROUVER_MAXIMUM(liste):
    
    if not liste:
        return None
    
    maximum = liste[0]
    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
    return maximum


if __name__ == "__main__":
    nombres = [3, 7, 2, 9, 5]
    print("Le maximum est :", TROUVER_MAXIMUM(nombres))
