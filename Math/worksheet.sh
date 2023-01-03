# /bin/sh

python3 ./worksheet.py > ./worksheet.tex
pdflatex ./worksheet.tex
xdg-open ./worksheet.pdf

