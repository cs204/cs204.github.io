res: doc/cs204.pdf  index.html 


index.html: src/main.nw 
	notangle -Rindex.html src/main.nw > index.html 




doc/cs204.pdf: src/cs204.tex  tmp/main.tex
	pdflatex -output-directory=doc src/cs204.tex
	pdflatex -output-directory=doc src/cs204.tex

# Утилита noweave генерирует файл main.tex из отдельных файлов 
# формата noweb.
tmp/main.tex: src/main.nw  src/Makefile.nw
	noweave -n -latex -index -autodefs c  src/main.nw \
	       	src/Makefile.nw > tmp/main.tex

# Эту команду выполняем в случае, если были изменения в файле 
#Makefile.nw, notangle генерирует новый Makefile

new: src/Makefile.nw
	notangle -t8 -RMakefile src/Makefile.nw > Makefile


view:
	evince doc/cs204.pdf &
	
clean:
	rm doc/cs204.pdf *.html  

