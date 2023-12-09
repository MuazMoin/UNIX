# OEFENING 1:
# Als input krijg je een .tgz archief (assignment-archief) waarin meerdere archieven zitten, die telkens een inzending van een student bevatten (student-archieven). Het assignment-archief heeft een filename volgens het volgende patroon: assignment_UA_{VAK}_{TITEL VAN TAAK}_{DEADLINE (yyyy-mm-dd)}.
#
# Je script wordt als volgt opgeroepen:
#
# extract_tasks.sh archive-with-student-submissions.tgz
# In Inginious moet je je script geen aparte naam geven, Inginious doet dit reeds voor jou.
#
# Pak dit archief uit en bewaar de inhoud in de volgende directory: {VAK}/{TITEL VAN TAAK}, zodat deze directory al de originele student-archieven bevat. Merk op dat het lastig is om te werken met whitespaces in filenames. Zet alle whitespaces in de directory naam om naar _.
tar -xvzf "$1"  #archief uitpakken
FILENAME=$1
METADATA="${FILENAME##assignment_UA_}"
VAK=$(cut -d'_' -f1 <<<$METADATA)
TITEL_VAN_TAAK=$(cut -d'_' -f2 <<<$METADATA)
DEADLINE=$(cut -d'_' -f3 <<<$METADATA)
DEADLINE=$(cut -d'.' -f1 <<<$DEADLINE)

mkdir "$VAK"
mkdir "$VAK/$TITEL_VAN_TAAK"


DIRECTORY_NAME=$(cut -d'.' -f1 <<<$FILENAME)

mv $DIRECTORY_NAME/* $VAK/$TITEL_VAN_TAAK

rmdir $DIRECTORY_NAME

# OEFENING 3:
# De archieven van de studenten hebben volgende filenames: {TITEL VAN TAAK}_{VOORNAAM}.{ACHTERNAAM}.s.ua poging_{DATUM (yyyy-mm-dd)}. Pak vervolgens deze archieven ook uit en zorg dat de files van een student in een map {VAK}/{TITEL VAN TAAK}/{ACHTERNAAM}.{VOORNAAM} opgeslagen worden. Verwijder alle spaties in de namen van de studenten.
tar -xvzf "$1"  #archief uitpakken
FILENAME=$1
METADATA="${FILENAME##assignment_UA_}"
VAK=$(cut -d'_' -f1 <<<$METADATA)
TITEL_VAN_TAAK=$(cut -d'_' -f2 <<<$METADATA)
DEADLINE=$(cut -d'_' -f3 <<<$METADATA)
DEADLINE=$(cut -d'.' -f1 <<<$DEADLINE)

mkdir "$VAK"
mkdir "$VAK/$TITEL_VAN_TAAK"


DIRECTORY_NAME=$(cut -d'.' -f1 <<<$FILENAME)

mv $DIRECTORY_NAME/* $VAK/$TITEL_VAN_TAAK

rmdir $DIRECTORY_NAME


cd $VAK/$TITEL_VAN_TAAK
tar -xvzf *.tgz


ls > "ls.txt"
while read -r line
do
  if [ "$line" != "ls.txt" ]
  then
    tar -xvzf "$line"
    UNPACKED=$(echo "$line" | sed "s/\.tgz//")
    TAAKNAAM=$(cut -d'_' -f1 <<<$line)
    NAAM=$(cut -d'_' -f2 <<<$line)
    VOORNAAM=$(cut -d'.' -f1 <<<$NAAM)
    ACHTERNAAM=$(cut -d'.' -f2 <<<$NAAM)
    VOORNAAM=$(echo "$VOORNAAM" | sed s/[[:space:]]//g)
    ACHTERNAAM=$(echo "$ACHTERNAAM" | sed s/[[:space:]]//g)
    mkdir "$ACHTERNAAM.$VOORNAAM"

    mv "$UNPACKED"/* $ACHTERNAAM.$VOORNAAM
    rm "$line"
    rm -r "$UNPACKED"
fi
done < "ls.txt"
rm "ls.txt"


#OEFENING 5:
# In het geval dat de submissie-datum later is dan de deadline-datum voeg je een leeg bestand late_inzending toe aan de folder van de student.
#
# Kopieer en vul je commando's uit de vorige oefening aan om dit op te lossen. Om deze opdracht tot een goed einde te brengen kan het zijn dat je ook je oplossing voor de eerste oefening moet aanpassen.
tar -xvzf "$1"  #archief uitpakken
FILENAME=$1
METADATA="${FILENAME##assignment_UA_}"
VAK=$(cut -d'_' -f1 <<<$METADATA)
TITEL_VAN_TAAK=$(cut -d'_' -f2 <<<$METADATA)
DEADLINE=$(cut -d'_' -f3 <<<$METADATA)
DEADLINE=$(cut -d'.' -f1 <<<$DEADLINE)

deadline_jaar=$(cut -d'-' -f1 <<<$DEADLINE)
deadline_maand=$(cut -d'-' -f2 <<<$DEADLINE)
deadline_dag=$(cut -d'-' -f3 <<<$DEADLINE)

mkdir "$VAK"
mkdir "$VAK/$TITEL_VAN_TAAK"


DIRECTORY_NAME=$(cut -d'.' -f1 <<<$FILENAME)

mv $DIRECTORY_NAME/* $VAK/$TITEL_VAN_TAAK

rmdir $DIRECTORY_NAME


cd $VAK/$TITEL_VAN_TAAK
tar -xvzf *.tgz


ls > "ls.txt"
while read -r line
do
  if [ "$line" != "ls.txt" ]
  then
    tar -xvzf "$line"
    UNPACKED=$(echo "$line" | sed "s/\.tgz//")
    TAAKNAAM=$(cut -d'_' -f1 <<<$line)
    NAAM=$(cut -d'_' -f2 <<<$line)
    VOORNAAM=$(cut -d'.' -f1 <<<$NAAM)
    ACHTERNAAM=$(cut -d'.' -f2 <<<$NAAM)
    VOORNAAM=$(echo "$VOORNAAM" | sed s/[[:space:]]//g)
    ACHTERNAAM=$(echo "$ACHTERNAAM" | sed s/[[:space:]]//g)
    mkdir "$ACHTERNAAM.$VOORNAAM"


    mv "$UNPACKED"/* $ACHTERNAAM.$VOORNAAM
    inzendingsdatum=$(cut -d'_' -f4 <<<$line)
    inzendingsdatum=$(cut -d'.' -f1 <<<$inzendingsdatum)
    inzending_jaar=$(cut -d'-' -f1 <<<$inzendingsdatum)
    inzending_maand=$(cut -d'-' -f2 <<<$inzendingsdatum)
    inzending_dag=$(cut -d'-' -f3 <<<$inzendingsdatum)

    if [ $inzending_jaar -gt $deadline_jaar ]
    then
    touch $ACHTERNAAM.$VOORNAAM/late_inzending
    elif [ $inzending_maand -gt $deadline_maand ]
    then
    touch $ACHTERNAAM.$VOORNAAM/late_inzending
    elif [ $inzending_dag -gt $deadline_dag ]
    then
    touch $ACHTERNAAM.$VOORNAAM/late_inzending
    fi


    rm "$line"
    rm -r "$UNPACKED"



fi
done < "ls.txt"
rm "ls.txt"



# OEFENING 7:
# Zorg er nu voor dat er in de mappen van de studenten geen andere mappen zitten, door alle files uit deze mappen te verplaatsen naar de hoofdmap van de studenten zelf. En de overbodige mappen vervolgens te verwijderen. Geef een gebruiker ook de mogelijkheid om een extensie mee te geven aan het script, enkel files die voldoen aan deze extensie blijven behouden. Als je het voorbeeld archief download en laat uitpakken door je script waarbij je filtert op de extensie .py dan krijg je onderstaande mappen-structuur:

tar -xvzf "$1"  #archief uitpakken
FILENAME=$1
METADATA="${FILENAME##assignment_UA_}"
VAK=$(cut -d'_' -f1 <<<$METADATA)
TITEL_VAN_TAAK=$(cut -d'_' -f2 <<<$METADATA)
DEADLINE=$(cut -d'_' -f3 <<<$METADATA)
DEADLINE=$(cut -d'.' -f1 <<<$DEADLINE)

deadline_jaar=$(cut -d'-' -f1 <<<$DEADLINE)
deadline_maand=$(cut -d'-' -f2 <<<$DEADLINE)
deadline_dag=$(cut -d'-' -f3 <<<$DEADLINE)

mkdir "$VAK"
mkdir "$VAK/$TITEL_VAN_TAAK"


DIRECTORY_NAME=$(cut -d'.' -f1 <<<$FILENAME)

mv $DIRECTORY_NAME/* $VAK/$TITEL_VAN_TAAK

rmdir $DIRECTORY_NAME


cd $VAK/$TITEL_VAN_TAAK
tar -xvzf *.tgz


ls > "ls.txt"
while read -r line
do
  if [ "$line" != "ls.txt" ]
  then
    tar -xvzf "$line"
    UNPACKED=$(echo "$line" | sed "s/\.tgz//")
    TAAKNAAM=$(cut -d'_' -f1 <<<$line)
    NAAM=$(cut -d'_' -f2 <<<$line)
    VOORNAAM=$(cut -d'.' -f1 <<<$NAAM)
    ACHTERNAAM=$(cut -d'.' -f2 <<<$NAAM)
    VOORNAAM=$(echo "$VOORNAAM" | sed s/[[:space:]]//g)
    ACHTERNAAM=$(echo "$ACHTERNAAM" | sed s/[[:space:]]//g)
    mkdir "$ACHTERNAAM.$VOORNAAM"


    mv "$UNPACKED"/* $ACHTERNAAM.$VOORNAAM

    cd $ACHTERNAAM.$VOORNAAM
    find . -mindepth 2 -type f -exec mv {} . \;
	# Delete hidden files

	# Delete empty directories
	  find . -type d -empty -delete

    if [[ "$2" != "" ]];
    then
    directory=$(pwd)
    for file in "$directory"/*;
    do
        if [ -f "$file" ] && [[ "$file" != *".$2" ]] && [ "$file" != "late_inzending" ]; then
        echo "Deleting $file"
        rm "$file"
        fi
    done
    fi
    echo "checking inzendingsdatum! ----"
    inzendingsdatum=$(cut -d'_' -f4 <<<$line)
    inzendingsdatum=$(cut -d'.' -f1 <<<$inzendingsdatum)
    inzending_jaar=$(cut -d'-' -f1 <<<$inzendingsdatum)
    inzending_maand=$(cut -d'-' -f2 <<<$inzendingsdatum)
    inzending_dag=$(cut -d'-' -f3 <<<$inzendingsdatum)
    echo $inzendingsdatum

    if [ $inzending_jaar -gt $deadline_jaar ]
    then
    touch "late_inzending"
    elif [ $inzending_maand -gt $deadline_maand ]
    then
    touch "late_inzending"
    elif [ $inzending_dag -gt $deadline_dag ]
    then
    touch "late_inzending"
    fi



    cd ..
    rm "$line"
    rm -r "$UNPACKED"



fi

done < "ls.txt"
rm "ls.txt"



