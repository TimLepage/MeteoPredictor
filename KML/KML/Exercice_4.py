fichier = open("Exercice_4.kml","w")
fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>Animation</name>\n")
with open('cities.txt', "r") as inf:
    date=2000
    for line in inf:
        line = line.strip()
        if not line:
            continue
        mots = line.split(' ')
        if not mots:
            continue
        fichier.write("<Placemark>\n<name>"+mots[0] +" : "+ mots[3]+" millions</name>\n<TimeSpan><begin>"+str(date)+"</begin></TimeSpan>\n")
        fichier.write("<Point>\n<coordinates>")
        fichier.write(mots[1] +","+mots[2] +"</coordinates>\n</Point>\n")
        fichier.write("</Placemark>\n")
        date=date+1
    fichier.write("</Document></kml>")
    fichier.close()
