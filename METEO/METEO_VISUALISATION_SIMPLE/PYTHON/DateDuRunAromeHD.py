import sys
import RequeteAromeHD

#=================================================================================
if __name__ == "__main__":

# AUCUN ARGUMENT NECESSAIRE
# ON SE CONTENTE DE CHERCHER LA DATE DU PLUS RECENT RUN
# ON DONNE DEUX ARGUMENTS PAR DEFAUT BIDON POUR APPELER LA FONCTION DU PROGRAMME RequeteAromeHD
	[DateDuRun, IntervalleEnHeure, DateDeLaPrevision, Requete] = RequeteAromeHD.RequetePrevisionPourUnDeltaEnHeure("SP1",  int(sys.argv[1]))

	print(DateDuRun.isoformat())
