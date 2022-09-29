n_chats1 = int(input())

for i in range(n_chats1):
    msg = input()
    
    # opcion uno
    persona, texto = msg.split(": ")
    if texto.lower().find("yo no fui") != -1:
        impostor = persona
        
    # opcion dos
    '''
    lista_mensaje = msg.split(": ")
    if "yo no fui" in lista_mensaje[1].lower():
        impostor = lista_mensaje[0]
    '''

n_chats2 = int(input())

for i in range(n_chats2):
    msg = input()
    
    persona, texto = msg.split(": ")
    
    if impostor in texto:
        palabras_mensaje = texto.split(" ")
        
        for palabra in palabras_mensaje:
            if palabra.isdigit():
                dia = palabra
            
print(f"El impostor es {impostor} y fue visto por última vez en el día {dia}")
