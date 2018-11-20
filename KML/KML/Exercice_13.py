fichier = open("Exercice_13.kml","w")
fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>Polygones prop base couleurs</name>\n")
colors = ['fff1ff2d','ff8dfc32','ff3d7ca0','ff2d0f56','ffcc1294','ff099638','ffe02c14']
i = 0
with open('cities.txt', "r") as inf:
    for line in inf:
        line = line.strip()
        if not line:
            continue
        mots = line.split(' ')
        if not mots:
            continue
        fichier.write("<Placemark>\n<Style>\n<PolyStyle><color>"+colors[i]+"</color>\n</PolyStyle></Style>\n<name>"+mots[0]+"</name>\n<Polygon>\n<extrude>1</extrude>\n<altitudeMode>relativeToGround</altitudeMode>\n<outerBoundaryIs><LinearRing><coordinates>")
        alpha = (float(mots[3])*2)/8.674
        fichier.write(str(float(mots[1])-alpha) +","+str(float(mots[2])+alpha)+",55555\n")
        fichier.write(str(float(mots[1])-alpha) +","+str(float(mots[2])-alpha)+",55555\n")
        fichier.write(str(float(mots[1])+alpha) +","+str(float(mots[2])-alpha)+",55555\n")
        fichier.write(str(float(mots[1])+alpha) +","+str(float(mots[2])+alpha)+",55555\n")
        fichier.write(str(float(mots[1])-alpha) +","+str(float(mots[2])+alpha)+",55555\n")
        fichier.write("</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark>\n")
        i = i+1
    fichier.write("</Document></kml>")
    fichier.close()
