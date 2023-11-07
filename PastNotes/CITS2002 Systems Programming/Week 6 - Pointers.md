[[Week 1 - C Basics]]


|   |   |
|---|---|
|Created|@August 28, 2023 8:55 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/schedule.php](https://teaching.csse.uwa.edu.au/units/CITS2002/schedule.php)|

> Pointers: allow a program to access its own memory, each byte in the memory has a location, an _______address_______ and the action of identifying an address is called addressing.

****************Pointers:****************

- Variables that hold the address of a memory location

- Point to memory locations

- Point to memory locations being used to hold the variables’ values/contents

******************************The & Operator:******************************

- address of

```
int total;
int *p;
...
&total //gives the address of total
...
p = &total; //p stores the address of a memory location
...
printf(" value of pointer p is: %p/n", (void *)p);
...
```

******************De referencing a Pointer:******************

- If the contents change, it will still point to the same variable

- Does not change the pointer

****************Address:****************

- When requiring the address of an array, we’re really asking for the address of the first element of that array

```
#define N 5
int totals[N];

int *first = &totals[0]; //equals int *p = totals;
int *second = &totals[1];
int *third = &totals[2];
```

********************************Pointer Arithmetic:********************************

```
#define  N     5

int totals[N];
int *p = totals; // p points to the first/leftmost element of totals   

    for(int i=0 ; i<N ; ++i) {
        *p = 0;  // set what p points to to zero   
        ++p;     // advance/move pointer p "right" to point to the next integer   
    }

    for(int i=0 ; i<N ; ++i) {
        printf("address of totals[%i] is:  %p\n", i, (void *)&totals[i] );
				printf("  value of totals[%i] is:  %i\n", i,          totals[i] );
    }
```

- in reference to the size of the data type, i.e. a subtraction of two ints: 2024-2000 = 6 as an int is of byte size 4

************************************************Passing Pointers to Functions:************************************************

```
#include <stdio.h>

void swap(int *ip, int *jp)
{
    int temp;

    temp  = *ip;    // swap's temp is now 3
    *ip   = *jp;    // main's variable a is now 5
    *jp   = temp;   // main's variable b is now 3
}

int main(int argc, char *argv[])
{
    int a=3, b=5;

    printf("before a=%i, b=%i\n", a, b);

    swap(&a, &b);   // pass pointers to our local variables  

    printf("after  a=%i, b=%i\n", a, b);

    return 0;
}

//before a=3, b=5
//after  a=5, b=3
```

- The swap() function needs to deal with the original variables, rather than new copies of their values

- A function may permit another function to modify its variables, by passing pointers to those variables

# Allocating New Memory

- We often do not know how much memory we will need, so we must dynamically request some new memory at runtime to hold our desired result

```
#include <stdlib.h>

extern void *malloc( size_t nbytes );
```

- returns a pointer, it is a generic pointer, “void star” or “void pointer”

- needs to be informed the number of bytes required

- we need to return malloc() to check if it is succeeded (if there is enough memory to allocate)

```
#include <stdlib.h>

  size_t bytes_wanted   = 1000000 * sizeof(int);

  int    *huge_array    = malloc( bytes_wanted );

  if(huge_array == NULL) {   // DID malloc FAIL?
      printf("Cannot allocate %i bytes of memory\n", bytes_wanted);    
      exit( EXIT_FAILURE );
  }
```

- i.e. to duplicate a string:

```
#include <stdlib.h>
#include <string.h>

char *my_strdup2(char *str)
{
    char *new = malloc( strlen(str) + 1 );

    if(new != NULL) {
        strcpy(new, str);  // ENSURES THAT DUPLICATE WILL BE NUL-TERMINATED 
    }
    return new;
}
```

- Clearing the memory:

```
include <stdlib.h>

extern void *calloc( size_t nitems, size_t itemsize );
    ....
    int  *intarray = calloc(N, sizeof(int));
```

- De allocating memory:

```
extern void free( void *pointer );
```

- Reallocating memory (shrinking or growing the allocated memory space):

```
extern void *realloc( void *oldpointer, size_t newsize );
```

Comparing Integer Values:

```
#include <stdio.h>
#include <stdlib.h>

#define  N    10

int main(int argc, char *argv[])
{
    int values[N];

// FILL OUR ARRAY WITH N INTEGERS BETWEEN 0 and 99
    srand( time(NULL) );
    for(int i=0 ; i<N ; i++) {
        values[i] = rand() % 100;
    }
// PRINT THE ARRAY BEFORE SORTING
    for(int i=0 ; i<N ; i++) {
        printf("%i  ", values[i]);
    }
    printf("\n\n");

// SORT THE ARRAY USING qsort
    qsort(values, N, sizeof(values[0]), compareints);   

// PRINT THE ARRAY AFTER SORTING
    for(int i=0 ; i<N ; i++) {
        printf("%i  ", values[i]);
    }
    printf("\n");

    return 0;
}
```