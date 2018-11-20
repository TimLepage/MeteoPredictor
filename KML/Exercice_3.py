fichier = open("Exercice_3.kml","w")
fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>Citites</name>\n")
with open('cities.txt', "r") as inf:
    for line in inf:
        line = line.strip()
        if not line:
            continue
        mots = line.split(' ')
        if not mots:
            continue
        fichier.write("<Placemark>\n<name>"+mots[0] +" : "+ mots[3]+" millions</name>\n")
        fichier.write("<Point>\n<coordinates>")
        fichier.write(mots[1] +","+mots[2] +"</coordinates>\n</Point>\n")
        fichier.write("</Placemark>\n")
    fichier.write("</Document></kml>")
    fichier.close()
