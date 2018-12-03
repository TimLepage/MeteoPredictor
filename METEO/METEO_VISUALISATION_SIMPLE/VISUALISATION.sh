#!/bin/bash
if [ "$#" -eq 0 ]; then
        echo "vous devez donnez le nombre d'heure a partir du moment actuel pour lequel vous voulez la prevision"
	echo
	exit
else
        echo "== TELECHARGEMENT ET VISUALISATION DES DONNEES DE SIMULATION METEOFRANCE POUR DANS $1 HEURE(S)"
fi

# ==================================================================================================
echo "=== TELECHARGEMENT DES DONNEES DE SIMULATION A METEOFRANCE"
echo

NomDuFichierMeteoFrance=`python PYTHON/RequeteAromeHD.py $1 SP1`
rc=$?
if ! [ $rc == 0 ]; then
	echo "LE CHARGEMENT DU FICHIER NE S EST PAS CORRECTEMENT EFFECTUE"
	exit 1
fi

DateDeLaPrevision=`python PYTHON/DateDeLaPrevisionAromeHD.py $1`
DateDuRun=`python PYTHON/DateDuRunAromeHD.py $1`
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
echo "=== CREATION DE L IMAGE PNG PAR PARAVIEW Ligne Vent"
echo

if [ -e KML/IMAGES/$NomDuFichierMeteoFrance.nc.lignevent.png ]; then
	echo "L IMAGE EXISTE DEJA"
else
#  /home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/ScriptTest.py DATA/$NomDuFichierMeteoFrance.nc
/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython --force-offscreen-rendering PYTHON/VisualisationLigneVent.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/Visualisationhumidite.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationVentTemperature.py DATA/$NomDuFichierMeteoFrance.nc

#	pvpython --force-offscreen-rendering PYTHON/VisuAvecTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentEtTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentSeulement.py DATA/$NomDuFichierMeteoFrance.nc
	rc=$?

	if ! [ $rc == 0 ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi

	if ! [ -e DATA/$NomDuFichierMeteoFrance.nc.lignevent.png ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi
	mv DATA/$NomDuFichierMeteoFrance.nc.lignevent.png KML/IMAGES
	convert -trim -define png:color-type=6 KML/IMAGES/$NomDuFichierMeteoFrance.nc.lignevent.png KML/IMAGES/$NomDuFichierMeteoFrance.nc.lignevent.png
	if ! [ $rc == 0 ]; then
		echo "L IMAGE N A PAS PU ETRE TRAITEE PAR IMAGEMAGICK"
		exit 1
	fi
fi

echo "L IMAGE EST SAUVEE DANS LE FICHIER KML/IMAGES/$NomDuFichierMeteoFrance.nc.lignevent.png"
echo

# ==================================================================================================
echo "=== CREATION DU FICHIER KML POUR GOOGLE EARTH"
echo
cat KML/templateKMZ.kml | sed "s/ICILEFICHIER/$NomDuFichierMeteoFrance.nc.lignevent.png/g" > tmp.kml
cat tmp.kml | sed "s/ICILENOM/Ligne de vent/g" > tmp1.kml
cat tmp1.kml | sed "s/ICILADATEDELAPREVISION/$DateDeLaPrevision/g" > KML/$NomDuFichierMeteoFrance.nc.lignevent.png.kml
rm tmp.kml tmp1.kml

echo "LE FICHIER KML KML/$NomDuFichierMeteoFrance.nc.lignevent.png.kml PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo





# ==================================================================================================
echo "=== CREATION DE L IMAGE PNG PAR PARAVIEW Ligne Vent Temperature"
echo

if [ -e KML/IMAGES/$NomDuFichierMeteoFrance.nc.humidite.png ]; then
	echo "L IMAGE EXISTE DEJA"
else
#  /home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/ScriptTest.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationLigneVent.py DATA/$NomDuFichierMeteoFrance.nc
/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython --force-offscreen-rendering PYTHON/VisualisationHumidite.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationVentTemperature.py DATA/$NomDuFichierMeteoFrance.nc

#	pvpython --force-offscreen-rendering PYTHON/VisuAvecTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentEtTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentSeulement.py DATA/$NomDuFichierMeteoFrance.nc
	rc=$?

	if ! [ $rc == 0 ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi

	if ! [ -e DATA/$NomDuFichierMeteoFrance.nc.humidite.png ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi
	mv DATA/$NomDuFichierMeteoFrance.nc.humidite.png KML/IMAGES
	convert -trim -define png:color-type=6 KML/IMAGES/$NomDuFichierMeteoFrance.nc.humidite.png KML/IMAGES/$NomDuFichierMeteoFrance.nc.humidite.png
	if ! [ $rc == 0 ]; then
		echo "L IMAGE N A PAS PU ETRE TRAITEE PAR IMAGEMAGICK"
		exit 1
	fi
fi

echo "L IMAGE EST SAUVEE DANS LE FICHIER KML/IMAGES/$NomDuFichierMeteoFrance.nc.humidite.png"
echo

# ==================================================================================================
echo "=== CREATION DU FICHIER KML POUR GOOGLE EARTH"
echo
cat KML/templateKMZ.kml | sed "s/ICILEFICHIER/$NomDuFichierMeteoFrance.nc.humidite.png/g" > tmp.kml
cat tmp.kml | sed "s/ICILENOM/Humidite/g" > tmp1.kml
cat tmp1.kml | sed "s/ICILADATEDELAPREVISION/$DateDeLaPrevision/g" > KML/$NomDuFichierMeteoFrance.nc.humidite.png.kml
rm tmp.kml tmp1.kml

echo "LE FICHIER KML KML/$NomDuFichierMeteoFrance.nc.humidite.png.kml PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo





# ==================================================================================================
echo "=== CREATION DE L IMAGE PNG PAR PARAVIEW Temperature"
echo

if [ -e KML/IMAGES/$NomDuFichierMeteoFrance.nc.temperature.png ]; then
	echo "L IMAGE EXISTE DEJA"
else
#  /home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/ScriptTest.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationLigneVent.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/Visualisationhumidite.py DATA/$NomDuFichierMeteoFrance.nc
/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython --force-offscreen-rendering PYTHON/VisualisationTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationVentTemperature.py DATA/$NomDuFichierMeteoFrance.nc

#	pvpython --force-offscreen-rendering PYTHON/VisuAvecTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentEtTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentSeulement.py DATA/$NomDuFichierMeteoFrance.nc
	rc=$?

	if ! [ $rc == 0 ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi

	if ! [ -e DATA/$NomDuFichierMeteoFrance.nc.temperature.png ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi
	mv DATA/$NomDuFichierMeteoFrance.nc.temperature.png KML/IMAGES
	convert -trim -define png:color-type=6 KML/IMAGES/$NomDuFichierMeteoFrance.nc.temperature.png KML/IMAGES/$NomDuFichierMeteoFrance.nc.temperature.png
	if ! [ $rc == 0 ]; then
		echo "L IMAGE N A PAS PU ETRE TRAITEE PAR IMAGEMAGICK"
		exit 1
	fi
fi

echo "L IMAGE EST SAUVEE DANS LE FICHIER KML/IMAGES/$NomDuFichierMeteoFrance.nc.temperature.png"
echo

# ==================================================================================================
echo "=== CREATION DU FICHIER KML POUR GOOGLE EARTH"
echo
cat KML/templateKMZ.kml | sed "s/ICILEFICHIER/$NomDuFichierMeteoFrance.nc.temperature.png/g" > tmp.kml
cat tmp.kml | sed "s/ICILENOM/Temperature/g" > tmp1.kml
cat tmp1.kml | sed "s/ICILADATEDELAPREVISION/$DateDeLaPrevision/g" > KML/$NomDuFichierMeteoFrance.nc.temperature.png.kml
rm tmp.kml tmp1.kml

echo "LE FICHIER KML KML/$NomDuFichierMeteoFrance.nc.temperature.png.kml PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo



# ==================================================================================================
echo "=== CREATION DE L IMAGE PNG PAR PARAVIEW Vent Temperature"
echo

if [ -e KML/IMAGES/$NomDuFichierMeteoFrance.nc.vent.png ]; then
	echo "L IMAGE EXISTE DEJA"
else
#  /home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/ScriptTest.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationLigneVent.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/Visualisationhumidite.py DATA/$NomDuFichierMeteoFrance.nc
#/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython PYTHON/VisualisationTemperature.py DATA/$NomDuFichierMeteoFrance.nc
/home/terrier/srilm/ParaView-5.6.0-MPI-Linux-64bit/bin/pvpython --force-offscreen-rendering PYTHON/VisualisationVent.py DATA/$NomDuFichierMeteoFrance.nc

#	pvpython --force-offscreen-rendering PYTHON/VisuAvecTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentEtTemperature.py DATA/$NomDuFichierMeteoFrance.nc
#	pvpython --force-offscreen-rendering PYTHON/VisuAvecVentSeulement.py DATA/$NomDuFichierMeteoFrance.nc
	rc=$?

	if ! [ $rc == 0 ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi

	if ! [ -e DATA/$NomDuFichierMeteoFrance.nc.vent.png ]; then
		echo "PARAVIEW N A PAS PU CALCULER L IMAGE"
		exit 1
	fi
	mv DATA/$NomDuFichierMeteoFrance.nc.vent.png KML/IMAGES
	convert -trim -define png:color-type=6 KML/IMAGES/$NomDuFichierMeteoFrance.nc.vent.png KML/IMAGES/$NomDuFichierMeteoFrance.nc.vent.png
	if ! [ $rc == 0 ]; then
		echo "L IMAGE N A PAS PU ETRE TRAITEE PAR IMAGEMAGICK"
		exit 1
	fi
fi

echo "L IMAGE EST SAUVEE DANS LE FICHIER KML/IMAGES/$NomDuFichierMeteoFrance.nc.vent.png"
echo

# ==================================================================================================
echo "=== CREATION DU FICHIER KML POUR GOOGLE EARTH"
echo
cat KML/templateKMZ.kml | sed "s/ICILEFICHIER/$NomDuFichierMeteoFrance.nc.vent.png/g" > tmp.kml
cat tmp.kml | sed "s/ICILENOM/Sens du vent/g" > tmp1.kml
cat tmp1.kml | sed "s/ICILADATEDELAPREVISION/$DateDeLaPrevision/g" > KML/$NomDuFichierMeteoFrance.nc.vent.png.kml
rm tmp.kml tmp1.kml

echo "LE FICHIER KML KML/$NomDuFichierMeteoFrance.nc.vent.png.kml PEUT ETRE OUVERT AVEC GOOGLE EARTH"
echo








# ==================================================================================================
echo "=== CREATION DE L ARCHIVE KMZ POUR GOOGLE EARTH"
echo

cd KML; zip $NomDuFichierMeteoFrance.nc.humidite.png.kmz $NomDuFichierMeteoFrance.nc.humidite.png.kml IMAGES/$NomDuFichierMeteoFrance.nc.humidite.png
zip $NomDuFichierMeteoFrance.nc.temperature.png.kmz $NomDuFichierMeteoFrance.nc.temperature.png.kml  IMAGES/$NomDuFichierMeteoFrance.nc.temperature.png
zip $NomDuFichierMeteoFrance.nc.vent.png.kmz $NomDuFichierMeteoFrance.nc.vent.png.kml  IMAGES/$NomDuFichierMeteoFrance.nc.vent.png
zip $NomDuFichierMeteoFrance.nc.lignevent.png.kmz $NomDuFichierMeteoFrance.nc.lignevent.png.kml  IMAGES/$NomDuFichierMeteoFrance.nc.lignevent.png

echo "LES FICHIERS KMZ PEUVENT ETRE OUVERT AVEC GOOGLE EARTH"
echo

exit 0
# ==================================================================================================
