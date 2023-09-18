all:
#	@(echo $(DIVIDER); cd cs21; $(MAKE) -k)
	@(echo $(DIVIDER); cd python23; $(MAKE) -k)
	@(echo $(DIVIDER); cd cs23; $(MAKE) -k)
	@(echo $(DIVIDER); cd modeling; $(MAKE) -k)
#	@(echo $(DIVIDER); cd corrStudents; $(MAKE) -k)
#	@(echo $(DIVIDER); cd physics; $(MAKE) -k)
	@(echo $(DIVIDER); cd psets; $(MAKE) -k)
	python3 join.py
clean:
	@(echo $(DIVIDER); cd csAndTech; $(MAKE) -k clean)
	@(echo $(DIVIDER); cd python23; $(MAKE) -k clean)
	@(echo $(DIVIDER); cd cs21; $(MAKE) -k clean)
	@(echo $(DIVIDER); cd psets; $(MAKE) -k clean)
	@(echo $(DIVIDER); cd physics; $(MAKE) -k clean)
	@(echo $(DIVIDER); cd corrStudents; $(MAKE) -k clean)
	@(echo $(DIVIDER); cd modeling; $(MAKE) -k clean)

	rm -f *.html
