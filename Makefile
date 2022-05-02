all:
	@(echo $(DIVIDER); cd cs21; $(MAKE) -k)
	@(echo $(DIVIDER); cd corrStudents; $(MAKE) -k)
	@(echo $(DIVIDER); cd physics; $(MAKE) -k)
	python3 join.py
clean:
	@(echo $(DIVIDER); cd csAndTech; $(MAKE) -k clean)
	rm *.html
