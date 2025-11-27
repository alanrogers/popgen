This directory contains the source code for the main syllabus. The academic
calendar is in `acadcal.txt`, and the assignments are in `syllabus.in`.
To make `syllabus.tex`, use my program `mksyll` like this:

    mksyll -l -n, mon,wed,fri > syllabus.tex

Then `pdflatex main` will generate a syllabus in file `main.pdf`.
