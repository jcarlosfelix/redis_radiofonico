import random


#Divide una cadena en una lista de caracters
def listar_cadena(cadena):
    return [caracter for caracter in cadena] 


#Verifica si un caracter es entero
def es_entero(caracter):
	try:
		int(caracter)
		return True
	except:
		return False


#Convierte un número entero a su nombre (en inglés)
def convertir_numero(entero):
    diccionario = { 
        0: 'Zero', 
        1: 'One', 
        2: 'Two', 
        3: 'Three', 
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        #Default: VACIO
    } 
  
    return diccionario.get(int(entero), '')


#Convierte un caracter a su alfabeto radiofónico (en inglés)
def convertir_caracter(letra):
    diccionario = { 
        'A': 'Alfa', 
        'B': 'Bravo', 
        'C': 'Charlie', 
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliett',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'Xray',
        'Y': 'Yankee',
		'Z': 'Zulu',
        #Default: VACIO
    } 
  
    return diccionario.get(str(letra), '')

