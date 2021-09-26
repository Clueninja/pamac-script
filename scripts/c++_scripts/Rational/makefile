src = $(wildcard *.cpp)
obj = $(src:.c=.o)

LDFLAGS = -lGL -lglut -lpng -lz -lm

myprog: $(obj) $(CC) -o $@ $^ $(LDFLAGS)

.PHONY: clean
clean: rm -f $(obj) myprog
