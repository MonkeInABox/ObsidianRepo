[[Week 1 - C Basics]]


|   |   |
|---|---|
|Created|@July 31, 2023 8:51 AM|
|Class|Systems Programming|
|Reviewed||

************************************Operating Systems:************************************

- A piece of systems software that provides a convenient, efficient environment for the execution of user programs

- Why?
    
    - the user (UI, command interpreter, executing programs)
    
    - programming environment (utility programs, I/O)
    
    - efficiency (schedule, store and retrieve)
    
    - economic (to allow simultaneous use and scheduling of resources)

- Operating system ≠ User/Computer Interface

- Operating system == Resource Manager

- Operating systems must be extensible:
    
    - new hardware is introduced
    
    - new application programs
    
    - fixes and patches are released

****************************************Operating System Services:****************************************

- CPU scheduling

- Memory management

- Swapping

- I/O support

- File system

- Utility programs

- Command interface

- System calls

- Protection

- Communication

************************C Functions:************************

5 Primary Motivations:

- allow us to group together statements
    - provides convenience and readability, by giving them a common name

- have a repeated sequence that can be grouped together
    - minimises total memory required to hold repeated statements

- entry points from code to kernel (system calls), read, open, etc

- libraries

- shared libraries, such as `printf()`

****************************Role of main()****************************

- don’t place all statements in `main()`

- should constrained to:
    
    - receive and checking command-line arguments
    
    - report errors detected, call exit(EXIT_FAILURE)
    
    - call functions
    
    - finally call exit(EXIT_SUCCESS)

```
#include <stdio.h>
#include <stdlib.h>

int main(int argcount,char *argvalue[]) {
		// check the number of argumentsif(argcount != 2) {
        .... //function called
        exit(EXIT_FAILURE);
    }
		else {
        .... //function called
        exit(EXIT_SUCCESS);
    }
		return 0;
}
```

****************************************Accessing Libraries and Their Functions:****************************************

- `#include <stdlib.h>`

- `extern double sqrt(double x);`

************static************

- signifies the variable is only visible from within that file

- variable retains its value between calls to the function