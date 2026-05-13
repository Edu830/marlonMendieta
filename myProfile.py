#Uso de los tipos de datos básicos en Python
#Datos básicos ( str, int, bool, float)
name = "Marlon Alfredo Mendieta Restrepo"
years = 16
tall = 1,65
is_student = True
#Tupla
red_social = ("@mendi", "@mend7")
#Lista en diccionarios
playlist =[
  {
    "Nombre" : "Ozil",
    "Artista" : "Pirlo420",
    "Duracion" : "02:47 mts"
  },
  {
    "Nombre"  : "Power",
     "Artista" : "Pirlo420",
     "Duracion" : "02:51 mts"
  },
  {
    "Nombre" : "Como Jerry",
     "Artista" : "Pirlo420",
     "Duracion" : "04:16 mts"
  }
]
#Mostrar datos
print(f"""
*** PRESENTACION PERSONAL ***\n Mi nombre es {name}, tengo {years} y mido {tall}mts\nEstatus en el colegio: {is_student}.\nMi playlist fav:\n {playlist[0]}\n{playlist[1]}\n{playlist[2]}
""")