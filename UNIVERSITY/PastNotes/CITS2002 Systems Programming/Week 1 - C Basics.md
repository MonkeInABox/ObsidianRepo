

|   |   |
|---|---|
|Created|@July 24, 2023 8:51 AM|
|Class|Systems Programming|
|Reviewed||

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* Compile this program with:
   cc -std=c11 -Wall -Werror -o rotate rotate.c
 */

#define ROT 13

static char rotate(char c)
{
    c = c + ROT;
    .....
    return c;
}

int main(int argcount, char *argvalue[])
{
    // check the number of arguments
    if(argcount != 2) {
        ....
        exit(EXIT_FAILURE);
    }
    else {
        ....
        exit(EXIT_SUCCESS);
    }
    return 0;
}
```

- Characters such as space, tab, new line etc. are ignored by the compiler

- keywords (in orange)

- # are processed by C processor, preprocessor statements

- <> enclose a file name in a #include directive

- every complete C program requires a main() function

********************Variables:********************

- A C program will use 4 bytes to hold a single integer value, 8 to hold a floating-point

- Variable names must commence with an alphabetic or underscore character & followed by zero or more alphabetic, underscore or digit chars
    
    - is case sensitive
    
    - older compilers may be limited to say 8 unique characters

********************Datatypes:********************

- bool, char, int, float, double

- for int size (sizeof())
    - char ≤ short ≤ int ≤ long

**********************************************Scope of Variables:**********************************************

- global scope: var declared outside of all functions or statement blocks

- block scope: var declared in a specific function or statement block