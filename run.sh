# exit when any command fails
set -e

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT
echo "running pdfminer"
python pdfminer_pdf_to_text.py
echo "computing counts"
python 2_deg_new.py
echo "running binary_predictions.py"
python binary_predications.py
# to get json from pdf
# java -jar science-parse-cli-assembly-2.0.3.jar pdf -o pdf2json
