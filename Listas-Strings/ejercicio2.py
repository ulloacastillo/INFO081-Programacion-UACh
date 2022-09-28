from curses.ascii import isdigit


n_lineas_primer_chat = int(input("Ingrese numero de lineas: "))
msg_primer_chat = []
for i in range(n_lineas_primer_chat):
    msg = input("Ingrese mensaje: ")
    msg_primer_chat.append(msg)
n_lineas_segundo_chat = int(input("Ingrese numero de lineas: "))
msg_segundo_chat = []
for i in range(n_lineas_segundo_chat):
    msg = input("Ingrese mensaje: ")
    msg_segundo_chat.append(msg)
culpable = ""
for mensaje in msg_primer_chat:
    usuario,msg = mensaje.split(": ")
    if "yo no fui" in msg:
        culpable = usuario
dia = ""
for mensaje in msg_segundo_chat:
    usuario,msg = mensaje.split(": ")
    if culpable in msg:
        lista_msg = msg.split(" ")
        for msg_sep in lista_msg:
            if msg_sep.isdigit():
                dia = msg_sep

print(f"El impostor es {culpable} y fue visto por última vez en el día {dia}")