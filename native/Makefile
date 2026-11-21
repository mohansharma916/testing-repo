# Build validation for the native sources: cc -c on each translation unit.
CFLAGS ?= -Wall -std=c11

all: parse_header.o conn.o alloc.o

%.o: %.c demo.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f *.o
