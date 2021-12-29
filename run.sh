echo "running pdfminer"
python pdfminer_pdf_to_text.py
echo "computing counts"
python 2_deg_new.py
echo "running binary_predications.py.py"
python binary_predications.py