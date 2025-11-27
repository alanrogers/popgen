TARGETS = prob.pdf
INSTALLDIR = $(HOME)/public_html/ant4221

all : $(TARGETS)

main.pass1 : main.tex
	pdflatex main
	touch $@

main.pass2 : main.tex
	pdflatex main
	touch $@

main.pdf : main.pass2
	pdflatex main

prob.pdf : main.pdf
	cp main.pdf prob.pdf

install : $(TARGETS)
	cp -a $(TARGETS) $(INSTALLDIR)
	chmod go+r $(INSTALLDIR)/*

clean :
	rm -rf $(TARGETS) *.aux *.pdf *.dvi *.log *~
	rm -rf *.pass1 *.pass2

.PHONY : clean install all

