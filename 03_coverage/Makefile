
PROGS	= cgidecode

all: cgidecode

cgidecode: cgidecode.c
	gcc --coverage -o $@ $<

coverage: cgidecode
	rm -rf cgidecode.gcda cgidecode.gcno cgidecode.c.gcov
	./cgidecode '1+1'
	gcov cgidecode.c

clean:
	rm -rf $(PROGS) cgidecode.gcda cgidecode.gcno cgidecode.c.gcov

