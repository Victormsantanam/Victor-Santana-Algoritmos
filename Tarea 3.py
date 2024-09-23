""" El programa debe pedir: Sexo, Región, Pokémon preferido (de entre 3 opciones)
y adaptarse en consecuencia (por ejemplo, una vez pedido el sexo, si el usuario declara ser chica,
 debe referirse al usuario siempre con adjetivos femeninos)"""

print("Bienvenido al programa pokemon.")
nombre = input("Cual es tu nombre? ")
sexo = input (""" 
                    F: femenino.
                    M: masculino.
                    Na: prefiero no especificar.
                    Seleccione segun el sexo que le corresponda: """)
region = input(" A que region perteneces? ")
pokemon = input (""" 
                    1: pikachu.
                    2: charmander.
                    3: Bulbasaur.
                    Seleccione el numero de su pokemon favorito segun corresponda: """)

if sexo.lower() == "m":
    print("Listo para tu aventura")
elif sexo.lower() == "f":
    print("Lista para tu aventura")
elif sexo.lower() == "na":
    print("Liste para tu aventura")


    