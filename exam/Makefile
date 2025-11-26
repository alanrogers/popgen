final.dvi : final.aux
	latex final

final.aux : final.tex
	latex final

html : dummy
	rm -rf html/*
	latex2html -antialias_text -no_math -html_version 3.2,math \
           -show_section_numbers \
           -dir html -split +0 -toc_depth 0 -no_navigation final

clean :
	rm -rf html/* *.log *~

dummy :

