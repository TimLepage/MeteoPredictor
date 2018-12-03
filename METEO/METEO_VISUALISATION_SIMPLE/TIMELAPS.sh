# !/bin/bash
if [ "$#" -eq 0 ]; then
        echo "Vous devez donner le nombre d'heure a partir du moment actuel pour lequel vous voulez la prevision"
	echo
	exit
else
        echo "== TELECHARGEMENT ET VISUALISATION DES DONNEES DE SIMULATION METEOFRANCE POUR DANS $1 HEURE(S)"
fi

# ==================================================================================================
echo "=== TELECHARGEMENT DES DONNEES DE SIMULATION A METEOFRANCE"
echo

i=0

cd KML
rm timelaps.kml
touch timelaps.kml
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<kml xmlns=\"http://www.opengis.net/kml/2.2\">
  <Folder>
    <name>Prévision météo</name>
    <description>Prévision température</description>" >> timelaps.kml
cd ..

while [ $i -lt $1 ]
do

NomDuFichierMeteoFrance=`python PYTHON/RequeteAromeHD.py $i SP1`
rc=$?
if ! [ $rc == 0 ]; then
	echo "LE CHARGEMENT DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUE"
	exit 1
fi

DateDeLaPrevision=`python PYTHON/DateDeLaPrevisionAromeHD.py $i`
DateDuRun=`python PYTHON/DateDuRunAromeHD.py $i`
if [ -e  $NomDuFichierMeteoFrance ]; then
	mv $NomDuFichierMeteoFrance DATA
fi

if ! [ -e DATA/$NomDuFichierMeteoFrance ]; then
	echo "LE CHARGEMENT DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUE"
	exit 1
fi

echo "LES DONNEES DE SIMULATION SONT SAUVEES DANS LE FICHIER DATA/$NomDuFichierMeteoFrance"
echo


# ==================================================================================================
echo "=== CONVERSION EN NC DES DONNEES METEOFRANCE"
echo

if [ -e DATA/$NomDuFichierMeteoFrance.nc ]; then
	echo "LE FICHIER NC EXISTE DEJA"
else
	/home/terrier/Téléchargements/wgrib2/grib2/wgrib2/wgrib2 DATA/$NomDuFichierMeteoFrance -netcdf DATA/$NomDuFichierMeteoFrance.nc

	rc=$?
fi

if ! [ $rc == 0 ]; then
	echo "LA CONVERSION DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUEE"
	exit 1
fi

if ! [ -e DATA/$NomDuFichierMeteoFrance.nc ]; then
	echo "LA CONVERSION DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUEE"
	exit 1
fi


echo "LES DONNEES PARAVIEW SONT SAUVEES DANS LE FICHIER DATA/$NomDuFichierMeteoFrance.nc"
echo

# ==================================================================================================
echo "=== CREATION DE L IMAGE PNG PAR PARAVIEW"
echo

if [ -e KML/IMAGES/$NomDuFichierMeteoFrance.nc.png ]; then
	echo "L IMAGE EXISTE DEJA"
else

/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationTemperatureTemporel.py DATA/$NomDuFichierMeteoFrance.nc $i

	rc=$?

	if ! [ $rc == 0 ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi

	if ! [ -e DATA/$NomDuFichierMeteoFrance.nc.temperature.$i.png ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE ZZZ DATA/$NomDuFichierMeteoFrance.nc.$i.png"
		exit 1
	fi
	mv DATA/$NomDuFichierMeteoFrance.nc.temperature.$i.png KML/IMAGES
	convert -trim -define png:color-type=6 KML/IMAGES/$NomDuFichierMeteoFrance.nc.temperature.$i.png KML/IMAGES/$NomDuFichierMeteoFrance.nc.temperature.$i.png
	if ! [ $rc == 0 ]; then
		echo "L IMAGE N A PAS PU ETRE TRAITEE PAR IMAGEMAGICK"
		exit 1
	fi
fi

echo "L IMAGE EST SAUVEE DANS LE FICHIER KML/IMAGES/$NomDuFichierMeteoFrance.nc.$i.png"
echo

cd KML
echo "<GroundOverlay>
	<TimeStamp>
	<when> $DateDeLaPrevision </when>
	</TimeStamp>
      <name>RUN_DU_$DateDuRun</name>
      <!-- <color>96ffffff</color> -->
      <!-- <color>ffffffff</color> -->
<Icon><href>
<![CDATA[./IMAGES/$NomDuFichierMeteoFrance.nc.temperature.$i.png]]></href>
      </Icon>
      <LatLonBox>
        <north>55.4</north>
        <south>37.5</south>
        <west>-12</west>
        <east>16</east>
        <rotation>0</rotation>
      </LatLonBox>
    </GroundOverlay>" >> timelaps.kml
cd ..


i=$((i+1))

done

# ==================================================================================================
echo "=== CREATION DU FICHIER KML POUR GOOGLE EARTH"
echo

cd KML
  echo "  </Folder>
</kml>" >> timelaps.kml
cd ..

echo "LE FICHIER KML KML/timelaps.kml PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo

# ==================================================================================================
echo "=== CREATION DE L ARCHIVE KMZ POUR GOOGLE EARTH"
echo

cd KML; zip timelaps.kmz IMAGES/ timelaps.kml

echo "LE FICHIER KMZ KML/timelaps.kmz PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo

exit 0
# ==================================================================================================
