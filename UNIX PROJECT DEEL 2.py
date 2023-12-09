# OEFENING 1:
# Als input krijg je een .tgz archief (assignment-archief) waarin meerdere archieven zitten, die telkens een inzending van een student bevatten (student-archieven). Het assignment-archief heeft een filename volgens het volgende patroon: assignment_UA_{VAK}_{TITEL VAN TAAK}_{DEADLINE (yyyy-mm-dd)}.
#
# Je script wordt als volgt opgeroepen:
#
# extract_tasks.sh archive-with-student-submissions.tgz
# In Inginious moet je je script geen aparte naam geven, Inginious doet dit reeds voor jou.
#
# Pak dit archief uit en bewaar de inhoud in de volgende directory: {VAK}/{TITEL VAN TAAK}, zodat deze directory al de originele student-archieven bevat. Merk op dat het lastig is om te werken met whitespaces in filenames. Zet alle whitespaces in de directory naam om naar _.

echo $1


SOL_PATH=$1
OPL_DIR="./${SOL_PATH}/Oplossingen"
mkdir $OPL_DIR

for subdirectory in "$1"/*/; do
  if [ -d "$subdirectory" ]; then
    subdirectory_name=$(basename "$subdirectory")

    VOORNAAM=$(echo "$subdirectory_name" | sed 's/\(.*\)\.\(.*\)/\1/' | tr -d '[:space:]')
    ACHTERNAAM=$(echo "$subdirectory_name" | sed 's/\(.*\)\.\(.*\)/\2/' | tr -d '[:space:]')

    echo $VOORNAAM
    echo $ACHTERNAAM


    OUTPUT_PATH="$ACHTERNAAM.$VOORNAAM_output.txt"
    ERROR_PATH="$ACHTERNAAM.$VOORNAAM_error.txt"

    python3"$line" >> $ACHTERNAAM.$VOORNAAM_output.txt 2>> $ACHTERNAAM.$VOORNAAM_error.txt

  fi
done


# OEFENING 3:
# De archieven van de studenten hebben volgende filenames: {TITEL VAN TAAK}_{VOORNAAM}.{ACHTERNAAM}.s.ua poging_{DATUM (yyyy-mm-dd)}. Pak vervolgens deze archieven ook uit en zorg dat de files van een student in een map {VAK}/{TITEL VAN TAAK}/{ACHTERNAAM}.{VOORNAAM} opgeslagen worden. Verwijder alle spaties in de namen van de studenten.

tar - xvzf
"$1"  # archief uitpakken
FILENAME =$1
METADATA = "${FILENAME##assignment_UA_}"
VAK =$(cut - d'_' -f1 << < $METADATA)
TITEL_VAN_TAAK =$(cut - d'_' -f2 << < $METADATA)
DEADLINE =$(cut - d'_' -f3 << < $METADATA)
DEADLINE =$(cut - d'.' -f1 << < $DEADLINE)

deadline_jaar =$(cut - d'-' -f1 << < $DEADLINE)
deadline_maand =$(cut - d'-' -f2 << < $DEADLINE)
deadline_dag =$(cut - d'-' -f3 << < $DEADLINE)

mkdir
"$VAK"
mkdir
"$VAK/$TITEL_VAN_TAAK"

DIRECTORY_NAME =$(cut - d'.' -f1 << < $FILENAME)

mv $DIRECTORY_NAME / * $VAK /$TITEL_VAN_TAAK

rmdir $DIRECTORY_NAME



cd $VAK /$TITEL_VAN_TAAK

tar - xvzf *.tgz

ls > "ls.txt"

mkdir
"oplossingen"

while read - r line
do
if ["$line" != "ls.txt"]
    then
tar - xvzf
"$line"
UNPACKED =$(echo "$line" | sed "s/\.tgz//")
TAAKNAAM =$(cut - d'_' -f1 << < $line)
NAAM =$(cut - d'_' -f2 << < $line)
VOORNAAM =$(cut - d'.' -f1 << < $NAAM)
ACHTERNAAM =$(cut - d'.' -f2 << < $NAAM)
VOORNAAM =$(echo "$VOORNAAM" | sed s/[[:space:]] // g)
ACHTERNAAM =$(echo "$ACHTERNAAM" | sed s/[[:space:]] // g)
LOCAL_DIR =$ACHTERNAAM.$VOORNAAM

mkdir $LOCAL_DIR

mv
"$UNPACKED" / * $ACHTERNAAM.$VOORNAAM

cd $ACHTERNAAM.$VOORNAAM
find. - mindepth
2 - type
f - exec
mv
{}. \;
# Delete hidden files

# Delete empty directories
find. - type
d - empty - delete

if [["$2" != ""]];
then
directory =$(pwd)
for file in "$directory" / *;
do
if [-f "$file"] & & [["$file" != *".$2"]] & & ["$file" != "late_inzending"]; then
echo
"Deleting $file"
rm
"$file"
fi
done
fi
echo
"checking inzendingsdatum! ----"
inzendingsdatum =$(cut - d'_' -f4 << < $line)
inzendingsdatum =$(cut - d'.' -f1 << < $inzendingsdatum)
inzending_jaar =$(cut - d'-' -f1 << < $inzendingsdatum)
inzending_maand =$(cut - d'-' -f2 << < $inzendingsdatum)
inzending_dag =$(cut - d'-' -f3 << < $inzendingsdatum)
echo $inzendingsdatum

if [ $inzending_jaar -gt $deadline_jaar]
then
touch
"late_inzending"
elif [ $inzending_maand - gt $deadline_maand]
then
touch
"late_inzending"
elif [ $inzending_dag - gt $deadline_dag]
then
touch
"late_inzending"
fi

for file in * .py;
do
filename_without_extension = "${file%.py}"  # chatgpt

OUTPUT_PATH = "${ACHTERNAAM}.${VOORNAAM}_${filename_without_extension}_output.txt"
ERROR_PATH = "${ACHTERNAAM}.${VOORNAAM}_${filename_without_extension}_error.txt"

touch $OUTPUT_PATH
touch $ERROR_PATH

python3 $file >> $OUTPUT_PATH
2 >> $ERROR_PATH
mv $OUTPUT_PATH
"../oplossingen"
mv $ERROR_PATH
"../oplossingen"

done
cd..
rm
"$line"
rm - r
"$UNPACKED"

fi

done < "ls.txt"
rm
"ls.txt"
cd.. /../

DIR = "${VAK}/${TITEL_VAN_TAAK}"

