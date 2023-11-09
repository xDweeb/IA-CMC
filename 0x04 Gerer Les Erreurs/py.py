try:
    i = int(input('i ? ')) #code à risque
    j = int(input('j ? ')) #code à risque
    print(i, '/', j, '=', i / j) #code à risque
except Exception as e: # variable e de type Exception
    print(type(e)) #afficher le type de l'exception
print(e)