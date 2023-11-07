 

|   |   |
|---|---|
|Created|@October 2, 2023 8:53 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture18/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture18/singlepage.html)[cdecl.org](https://www.notion.socdecl.org)|

> argv - an array of pointers to characters

- We assume that each value of argv[i] is a pointer that we’ll treat as a string

- The argv array is guaranteed to be terminated by a NULL pointer

****************OPTLIST:****************

```
#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>

#include <getopt.h>

#define	OPTLIST		"d"

int main(int argc, char *argv[])
{
    int		opt;

    .....
    opterr	= 0;
    while((opt = getopt(argc, argv, OPTLIST)) != -1) {
	if(opt == 'd')
            dflag = !dflag;
        else
            argc = -1;
    }
    if(argc < 0) {
        fprintf(stderr, "Usage: %s [-d] [filename]\n", progname);  
        exit(EXIT_FAILURE);
    }
    while(optind < argc) {
        process( argv[optind] );
        ++optind;
    }
    .....
    return 0;
}
```

```
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <getopt.h>

#define	OPTLIST		"df:n:" //colon means that there is some value after

int main(int argc, char *argv[])
{
    int  opt;
    bool dflag   = false;
    char *filenm = NULL;
    int  value   = DEFAULT_VALUE;

    opterr	= 0;
    while((opt = getopt(argc, argv, OPTLIST)) != -1)   {  
//  ACCEPT A BOOLEAN ARGUMENT
	if(opt == 'd') {
            dflag  =  !dflag;
        }
//  ACCEPT A STRING ARGUMENT
	else if(opt == 'f') {
            filenm  =  strdup(optarg);
        }
//  ACCEPT A INTEGER ARGUMENT
	else if(opt == 'n') {
            value  =  atoi(optarg);
        }
//  OOPS - AN UNKNOWN ARGUMENT
        else {
            argc = -1;
        }
    }

    if(argc <= 0) {    //  display program's usage/help   
        usage(1);
    }
    argc  -= optind;
    argv  += optind;
    .....
    return 0;
}
```

********************************************************Inter-Process Communication:********************************************************

- asynchronous signals

- unidirectional anonymous pipes
    - communicates in one direction

- named pipes
    - representation of the internal buffers have a name on file

- in-memory message-queues

- shared memory blocks, permitting processes to “share” an array or other data-structure
    
    - two processes: one creates memory block, exports so another process can attach to it
    
    - two page table entries that point to the same page

- sockets, to communicate with local or remote processes across a network

************Pipes:************

- pipe()

```
#include  <unistd.h>

int  thepipe[2];
char data[1024];
int  datasize, nbytes;

if(pipe(thepipe) != 0) {
    perror("cannot create pipe");
    exit(EXIT_FAILURE);
}

datasize = ...
nbytes   = write( thepipe[0], data, datasize);       // write to the pipe

nbytes   =  read( thepipe[1], data, sizeof(data));   // read from the pipe
```

- a newly created pipe is empty

- data written to the writing end is added to pipe

- if more than fits, it will be blocked until there is enough space

- data read from the reading end is removed from the pipe

# Dynamic Data Structures

Stacks: (first in last out structure)

```
typedef struct _s { //containers value and pointer (next)
    int         value;
    struct _s   *next;
}  STACKITEM;

STACKITEM    *stack = NULL; //stack points to a stack of items
```

Lists:

```
typedef struct _l {
     char        *string;
     struct _l   *next;
 } LISTITEM;

 LISTITEM   *list  =  NULL;
```

General Purpose Queue:

```
typedef struct _e {
    void        *data;
    size_t      datalen;
    struct _e   *next;
} ELEMENT;

typedef struct {
    ELEMENT     *head;
    ELEMENT     *tail;
} QUEUE;
```