fichier = open("Exercice_5.kml","w")
fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>Chemin</name>\n")
with open('cities.txt', "r") as inf:
    fichier.write("<Placemark>\n<name>Chemin</name>\n<description>Chemin entre les villes.</description>\n<styleUrl>#yellowLineGreenPoly</styleUrl>\n<LineString>\n<extrude>1</extrude>\n<tessellate>1</tessellate>\n<altitudeMode>absolute</altitudeMode>\n<coordinates>")
    for line in inf:
        line = line.strip()
        if not line:
            continue
        mots = line.split(' ')
        if not mots:
            continue
        fichier.write(mots[1] +","+mots[2]+",55555\n")
    fichier.write("</coordinates></LineString></Placemark>\n")
    fichier.write("</Document></kml>")
    fichier.close()
