[[Week 1 - C Basics]]


|   |   |
|---|---|
|Created|@August 14, 2023 8:48 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture07/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture07/singlepage.html)[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture08/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture08/singlepage.html)|

> Process: a program under execution, the “animated” existence of a program, an identifiable entity executed on a processor by the OS.

2 Views:

- The processor’s POV: only role is to execute the machine instructions from main memory, executes the sequence of instructions indicated by the program counter (PC)

- The process’s POV: either being executed by the processor or is waiting to be processed

Process Transitions:

1. newly created processes are created and marked as READY and are queued to run

2. only ever a single process in the RUNNING state. It will either:
    
    1. complete its execution and terminate
    
    2. be suspended

Process Creation:

- must allocate resources for both process and OS

- the process will require a portion of available memory to contain its instructions and initial data requirements

- the OS will need to maintain some internal control structures to support migration of the process between states

- where do they come from:
    
    - take new processes from batch queue
    
    - user created
    
    - existing process calls new process
    
    - OS makes process after request

Process Termination:

- why:
    
    - normal
    
    - execution time-limit
        - a hardware timer will periodically generate an interrupt, processor will look for interrupt, when a timer interrupt occurs, the processor will begin execution of interrupt handler, moving it from running to ready, a maximum time for a process is called time quantum
    
    - resource is unavailable
    
    - arithmetic error
    
    - memory access violation
    
    - invalid request
    
    - OS or parent process request
    
    - parent process terminated

Blocked states are when a process is waiting for an event to occur before executing. (the processes in the blocked states are in the event queues, waiting for the event to occur in order for it to be executed again)

[![](Untitled%2029.png)](Week%204%20-%20Processes%20&%20Raw%20I%20O%2064ae4935941a41c583ea2f9e12c9c41e/Untitled.png)

5-State Model:

[![](Untitled%2030.png)](CITS2002%20Notes%2018117552e59346edbe8a09638bb4df5b/Untitled.png)

# Raw Input & Output

Reading From A File & Writing To A File:

```
#include  <stdio.h>
#include  <fcntl.h>
#include  <stdlib.h>
#include  <unistd.h>

#define  MYSIZE      10000

int copy_file(char destination[], char source[])        
{
//  ATTEMPT TO OPEN source FOR READ-ONLY ACCESS
    int fd0    = open(source, O_RDONLY);
//  ENSURE THE FILE COULD BE OPENED
    if(fd0 == -1) {
        return -1;
    }

//  ATTEMPT TO OPEN destination FOR WRITE-ONLY ACCESS
    int fd1    = open(destination, O_WRONLY);
//  ENSURE THE FILE COULD BE OPENED
    if(fd1 == -1) {
        close(fd0);
        return -1;
    }

//  DEFINE A CHARACTER ARRAY TO HOLD THE FILE'S CONTENTS
    char   buffer[MYSIZE];
    size_t got;

//  PERFORM MULTIPLE READs OF FILE UNTIL END-OF-FILE REACHED  
    while((got = read(fd0, buffer, sizeof buffer)) > 0) {  
        if(write(fd1, buffer, got)) != got) {  
            close(fd0); close(fd1);
            return -1;
        }
    }

    close(fd0); close(fd1);
    return 0;
}
```

**************************************Reading & Writing Text Files:**************************************

```
#include <stdio.h>

#define DICTIONARY      "/usr/share/dict/words"

....
//  ATTEMPT TO OPEN THE FILE FOR READ-ACCESS
    FILE   *dict = fopen(DICTIONARY, "r");

//  CHECK IF ANYTHING WENT WRONG
    if(dict == NULL) {
        printf( "cannot open dictionary '%s'\n", DICTIONARY);
        exit(EXIT_FAILURE);
    }

//  READ AND PROCESS THE CONTENTS OF THE FILE
    ....

//  WHEN WE'RE FINISHED, CLOSE THE FILE
    fclose(dict);
```

- If fopen() returns NULL, the file may not exist or the operating system is not giving permission for the user to access it.

- r = open for reading

- r+ = reading and writing

- w = create or truncate file, then open for writing

- w+ = create or truncate file then open for reading and writing

- a = create if necessary then open for appending

- a+ = create if necessary then open for reading and appending

- all future operations are checked against the initial file access mode, and will fail if they do not match the initial declaration.