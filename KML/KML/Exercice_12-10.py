fichier = open("Exercice_12-10.kml","w")
fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>Polygones prop base couleurs</name>\n")
with open('cities.txt', "r") as inf:
    fichier.write("<Style id='yellowLineGreenPoly'>\n<PolyStyle><color>fff1ff2d</color>\n</PolyStyle></Style>");
    for line in inf:
        line = line.strip()
        if not line:
            continue
        mots = line.split(' ')
        if not mots:
            continue
        fichier.write("<Placemark>\n<styleUrl>#yellowLineGreenPoly</styleUrl>\n<name>"+mots[0]+"</name>\n<Polygon>\n<extrude>1</extrude>\n<altitudeMode>relativeToGround</altitudeMode>\n<outerBoundaryIs><LinearRing><coordinates>")
        alpha = (float(mots[3])*2)/8.674
        fichier.write(str(float(mots[1])-alpha) +","+str(float(mots[2])+alpha)+",55555\n")
        fichier.write(str(float(mots[1])-alpha) +","+str(float(mots[2])-alpha)+",55555\n")
        fichier.write(str(float(mots[1])+alpha) +","+str(float(mots[2])-alpha)+",55555\n")
        fichier.write(str(float(mots[1])+alpha)+","+str(float(mots[2])+alpha)+",55555\n")
        fichier.write(str(float(mots[1])-alpha) +","+str(float(mots[2])+alpha)+",55555\n")
        fichier.write("</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>\n")
    fichier.write("</Document></kml>")
    fichier.close()
