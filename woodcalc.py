import math
emvado_filou = dict()
emvado_filou['plati'] = 360
emvado_filou['kouti'] = 375
apantisi = input("einai gia plati i gia kouti?")
def prakseis (filo):
    mikos = input("Dwse mikos:\n")
    mikos = float(mikos)
    platos = input("Dwse platos:\n")
    platos = float(platos)
    emvado = mikos * platos
    print ("to emvado sou einai" + str(emvado))
    arithmos_filon = math.ceil(emvado/filo)
    return (arithmos_filon)

if (apantisi == "plati"):
    fila = prakseis(emvado_filou['plati'])
    print (fila)
elif (apantisi == "kouti"):
    fila = prakseis(emvado_filou['kouti'])
    print (fila)