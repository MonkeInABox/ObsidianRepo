[[Week 1 - C Basics]]


|   |   |
|---|---|
|Created|@September 28, 2023 12:28 PM|
|Class|Systems Programming|
|Reviewed||

**********************************************Developing Larger C Programs in Multiple Files**********************************************

- each file may perform a single role

- the number of global variables is significantly reduced

- we may easily edit multiple files in separate windows or tabs

- large projects may be undertaken by multiple people

- each file may separately be compiled into a distinct object file

- small changes to one file do not require all files to be recompiled

- each file relies on a common header file : fileName.h
    
    - this file announces their existence using the extern keyword
    
    - we don’t define the size of the arrays, likewise we don’t need to give a file a name
        
        - this is done in the respective c files
        
        - they need to have:
        
        ```
        #include "fileName.h" //local header
        ```
        

************************************************Variable Initialisation:************************************************

- 0 for int

- ‘\0’ for char

- 0.0 for float and double

- false for bool

- zero for pointer

************************make Keyword:************************

- make maintains up-to-date versions of programs that result from a sequence of actions on a set of files

- typically from a file named makefile

- example makefile:

```
calcmarks : calcmarks.o globals.o readmarks.o correlation.o
	cc -std=c11 -Wall -Werror -o calcmarks \
                  calcmarks.o globals.o readmarks.o correlation.o -lm


calcmarks.o : calcmarks.c calcmarks.h //target : dependencies
	cc -std=c11 -Wall -Werror -c calcmarks.c //action if out of date

globals.o : globals.c calcmarks.h
	cc -std=c11 -Wall -Werror -c globals.c

readmarks.o : readmarks.c calcmarks.h
	cc -std=c11 -Wall -Werror -c readmarks.c

correlation.o : correlation.c calcmarks.h
	cc -std=c11 -Wall -Werror -c correlation.c
```

- can be simplified to:

```
# A Makefile to build our 'calcmarks' project

PROJECT =  calcmarks
HEADERS =  $(PROJECT).h
OBJ     =  calcmarks.o globals.o readmarks.o correlation.o


C11     =  cc -std=c11
CFLAGS  =  -Wall -Werror 


$(PROJECT) : $(OBJ)
       $(C11) $(CFLAGS) -o $(PROJECT) $(OBJ) -lm


%.o : %.c $(HEADERS)
       $(C11) $(CFLAGS) -c $<

clean:
       rm -f $(PROJECT) $(OBJ)
```