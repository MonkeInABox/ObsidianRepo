[[Week 1 - C Basics]]


|   |   |
|---|---|
|Created|@August 7, 2023 9:02 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture05/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture05/singlepage.html)[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture06/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture06/singlepage.html)|

**********CPU:********** undertakes arithmetic and logical computation and directs most I/O services

********RAM:******** used to store both instructions and data, read and write items

******Secondary Storage/Peripheral Devices:****** move data to and from other components, to provide longer-term, persistent storage

**********Communications Bus:********** connects the processor(s), main memory and I/O devices together

The role of the OS in managing the flow of data to and from its CPU and I/O devices, attempts to attain maximum throughput of its computation and data transfer.

**************************Processor Registers:**************************

- memory locations, can be read and written very rapidly (10-500x faster than main memory)

- all data to be processed by the CPU must first be copied into registers, the operation is then performed in the registers and the result is copied back to the RAM

- two types:
    
    - user-accessible registers: are accessible to programs, programs are able to read and write these registers
        
        - data registers hold values before execution and results after
        
        - address registers hold addresses of memory locations
    
    - control and status registers: hold data the processor maintains in order to execute programs

**********************************Memory Hierarchy:**********************************

- having too much can be wasteful if it is not all required: trade-off (cost, capacity, access time)

[![](Untitled%2027.png)](Week%203%20-%20Computer%20Hardware%20&%20Arrays%20&%20Structures%2033f95e81c2fe4283aa46f66cf52652e3/Untitled.png)

# Arrays:

- 1-dimensional == vectors

- 2-dimensional == matrices

- 3-dimensional == volumes

```
#define N 20

int myarray[N];                     //one dimens. array
int evensum;                        //myarray[N] = {0, 1, 2, 3, ...};

evensum = 0;
for(int i = 0 ; i < N ; ++i) {      //arrays start at 0, not 1
		myarray[i] = i * 2;
    evensum = evensum + myarray[i];
}
```

- we may need variable length arrays:

```
void function2(int array_size,charvla[ ]) {
		for(int i=0 ; i < array_size ; ++i) {
				// access vla[i] ...
        //....
    }
}

void function1(void) {
		int size = //read an integer from keyboard or a file;
		char vla[size];
    function2(size, vla);
}
```

- a string in C is actually an array of characters

```
char month[] = "August"; //valid, compiler counts length for us
```

- strings are terminated by a special character, the ****************null byte**************** (\0)
    - means strings always have an extra byte of memory

- we may want our output to be written to a character array:

```
#include  <stdio.h>

char chess_outcome[64];
if(winner == WHITE) {
		sprintf(chess_outcome, "WHITE with %i", nwhite_pieces);
}
else {
		sprintf(chess_outcome, "BLACK with %i", nblack_pieces);
}
printf("The winner: %s\n", chess_outcome);

//OR

char chess_outcome[64];

//  FORMAT, AT MOST, A KNOWN NUMBER OF CHARACTERS
if(winner == WHITE) {
    snprintf(chess_outcome, 64, "WHITE with %i", nwhite_pieces);
}

//  OR, GREATLY PREFERRED:
if(winner == WHITE) {
    snprintf(chess_outcome, sizeof(chess_outcome), "WHITE with %i", nwhite_pieces);
}
```

# Structures:

- collect data into a single structure

```
//  DEFINE THE LIMITS ON PROGRAM'S DATA-STRUCTURES
#define MAX_TEAMS               24
#define MAX_TEAMNAME_LEN        30
....

struct {
		char    teamname[MAX_TEAMNAME_LEN+1];      // +1 for null-byte
   //  STATISTICS FOR THIS TEAM, INDEXED BY EACH TEAM'S 'TEAM NUMBER'
		int     played;
		int     won;
		int     lost;
		int     drawn;
		int     bfor;
		int     bagainst;
		int     points;
} 

team[MAX_TEAMS];       //  DEFINE A 1-DIMENSIONAL ARRAY NAMED team

//  PRINT EACH TEAM'S RESULTS, ONE-PER-LINE, IN NO SPECIFIC ORDER
for(int t=0 ; t<nteams ; ++t) {
    printf("%s %i %i %i %i %i %i %.2f %i\n", 
		// %age to 2 decimal-places
            team[t].teamname,
            team[t].played, team[t].won, team[t].lost, team[t].drawn,
            team[t].bfor, team[t].bagainst,
            (100.0 * team[t].bfor / team[t].bagainst),      
						// calculate percentage
            team[t].points);
}
```