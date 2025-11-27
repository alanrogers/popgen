website=$(HOME)/website/ant5221/lectures
handoutpdf = lactase-2x3.pdf
projectpdf = lactase.pdf

.SUFFIXES:
.SUFFIXES: .tex .aux .ps .pdf

# rule for making a file to project
project : $(projectpdf)

# Rule for making .aux from .tex
%.aux : %.tex
	-latex $<

# Rule for making .dvi from .aux and .tex
%.dvi : %.aux
	-latex `basename $< .aux`

# Rule for making .ps from .dvi
%.ps : %.dvi
	dvips -t letter -Ppdf -o `basename $< .dvi`.ps `basename $< .dvi`

## Rule for making .pdf from .ps
#%.pdf : %.ps FORCE
#	ps2pdf $<

# Rule for making .pdf from .dvi
%.pdf : %.dvi FORCE
	dvipdf $<

# Rule for making 4-up handouts
%-2x2.pdf : %.pdf FORCE
	pdfnup --nup 2x2 --frame true --orient landscape --paper letterpaper $<

# Rule for making 6-up handouts
%-2x3.pdf : %.pdf FORCE
	pdfnup --nup 2x3 --frame true --orient portrait --paper letterpaper $<

# Rule for making handouts
handout : $(handoutpdf)

install : $(handoutpdf)
	cp $(handoutpdf) $(website)

FORCE:

.PHONY : handout install project

