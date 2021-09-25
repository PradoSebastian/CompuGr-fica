CXXFLAGS := -std=c++17
LIBS := -lm -lGL -lGLU -lglut
HEADERS := Vector.h Camera.h
OBJS := Vector.o Camera.o

all: ex1 ex2 ex3

ex1: ex1.o $(OBJS) $(HEADERS)
	g++ $(CXXFLAGS) ex1.o $(OBJS) -o $@ $(LIBS)

ex2: ex2.o $(OBJS) $(HEADERS)
	g++ $(CXXFLAGS) ex2.o $(OBJS) -o $@ $(LIBS)

ex3: ex3.o $(OBJS) $(HEADERS)
	g++ $(CXXFLAGS) ex3.o $(OBJS) -o $@ $(LIBS)

%.o: %.cxx
	g++ $(CXXFLAGS) -c $< -o $@

.PHONY: clean

clean:
	rm -f *.o ex1 ex2 ex3 ex4

## eof - Makefile
