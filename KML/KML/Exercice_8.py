fichier = open("Exercice_8.kml","w")
fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>Polygone</name>\n")
with open('cities.txt', "r") as inf:
    for line in inf:
        line = line.strip()
        if not line:
            continue
        mots = line.split(' ')
        if not mots:
            continue
        fichier.write("<Placemark>\n<name>"+mots[0]+"</name>\n<Polygon>\n<extrude>1</extrude>\n<altitudeMode>relativeToGround</altitudeMode>\n<outerBoundaryIs><LinearRing><coordinates>")
        fichier.write(str(float(mots[1])-0.1) +","+str(float(mots[2])+0.1)+",55555\n")
        fichier.write(str(float(mots[1])-0.1) +","+str(float(mots[2])-0.1)+",55555\n")
        fichier.write(str(float(mots[1])+0.1) +","+str(float(mots[2])-0.1)+",55555\n")
        fichier.write(str(float(mots[1])+0.1)+","+str(float(mots[2])+0.1)+",55555\n")
        fichier.write(str(float(mots[1])-0.1) +","+str(float(mots[2])+0.1)+",55555\n")
        fichier.write("</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>\n")
    fichier.write("</Document></kml>")
    fichier.close()
