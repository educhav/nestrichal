CC := gcc

LFLAGS := `sdl2-config --libs --cflags` -O0 --std=c99 -Wall -lSDL2_image -lm
CFLAGS := -O0 --std=c99 -Wall 

SRCS := src/main.c src/game.c
HDRS := src/const.h
OBJS := $(SRCS:.c=.o)
EXEC := nestrichal

all: $(EXEC)
 
$(EXEC): $(OBJS) $(HDRS) Makefile
	$(CC) -o $(EXEC) $(OBJS) $(LFLAGS)

$(OBJS): $(SRCS) $(HDRS) Makefile
	$(CC) $(SRCS) -c $(CFLAGS)

clean:
	rm -f $(EXEC) $(OBJS)
