def equilibrada(palabra):
    s = 0
    for letra in palabra.lower():
        if letra in "aeiou":
            s += 1
    if len(palabra) - s == 0:
        return "Equilibrada"
    elif abs(len(palabra) - s) == 1:
        return "Semi-Equilibrada"
    else:
        return "No Equilibrada"

def k_equilibrada(palabra, k):
    equilibradas = 0;no_equilibradas = 0; semi_equilibradas = 0;
    for i in range(0, len(palabra), k):
        vocales = 0
        consonantes = 0
        for j in range(len(palabra[i:i+k])):
            if palabra[i:i+k][j].lower() in "aeiou":
                vocales += 1
            else:
                consonantes += 1
        if abs(vocales - consonantes) == 0:
            equilibradas += 1
        elif abs(vocales - consonantes) == 1:
            semi_equilibradas += 1
        else:
            no_equilibradas += 1
    if no_equilibradas == 0 and semi_equilibradas == 1 and equilibradas >= 1:
        return "K-Equilibrada"
    elif semi_equilibradas >= 1 and no_equilibradas == 0 and equilibradas >= 0:
        return "semi-k-equilibrada"
    else:
        return "no-k-equilibrada"
