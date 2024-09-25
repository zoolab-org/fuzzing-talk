
PROGS	= program

all: program

program: program.c
	clang -fsanitize=address -g -o $@ $<

clean:
	rm -rf $(PROGS) ./*.dSYM

