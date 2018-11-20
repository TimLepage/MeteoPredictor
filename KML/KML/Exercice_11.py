fichier = open("Exercice_11.kml","w")
fichier.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\"><Document><name>Chemin-points-intermediaires-couleur</name>\n")
with open('cities.txt', "r") as inf:
    fichier.write("<Style id='yellowLineGreenPoly'>\n<LineStyle><color>b000ffff</color>\n<width>4</width>\n</LineStyle>\n<PolyStyle><color>b000ffff</color>\n</PolyStyle></Style>");
    fichier.write("<Placemark>\n<name>Chemin</name>\n<description>Chemin entre les villes.</description>\n<styleUrl>#yellowLineGreenPoly</styleUrl>\n<LineString>\n<extrude>1</extrude>\n<tessellate>1</tessellate>\n<altitudeMode>absolute</altitudeMode>\n<coordinates>")
    lat=0.0
    long=0.0
    cpt=0
    for line in inf:
        line = line.strip()
        if not line:
            continue
        mots = line.split(' ')
        if not mots:
            continue
        if cpt < 1:
            fichier.write(mots[1] +","+mots[2]+",55555\n")
            lat=float(mots[1])
            long=float(mots[2])
        else:
            i=1
            while i < 10:
                fichier.write(str((float(mots[1])-lat)*(i/10)+lat)+","+str((float(mots[2])-long)*(i/10)+long)+",55555\n")
                i=i+1
            fichier.write(mots[1] +","+mots[2]+",55555\n")
            lat=float(mots[1])
            long=float(mots[2])
        cpt=cpt+1
    fichier.write("</coordinates></LineString></Placemark>\n")
    fichier.write("</Document></kml>")
    fichier.close()
