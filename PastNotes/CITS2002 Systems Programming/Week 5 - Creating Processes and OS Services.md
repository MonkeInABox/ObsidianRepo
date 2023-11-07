[[Week 1 - C Basics]]


|   |   |
|---|---|
|Created|@August 21, 2023 8:45 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture09/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture09/singlepage.html)[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture10/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture10/singlepage.html)|

************************************************************************Creating a new process using fork()************************************************************************

- it returns values in existing parent process and new child process

- value in parent process will be the process-identifier of the child process

- value returned by the child will be 0, fork didn’t fail

```
#include  <stdio.h>
#include  <unistd.h>

void function(void)
{
    int  pid;                 // some systems define a pid_t

    switch (pid = fork()) {
    case -1 :
        printf("fork() failed\n");     // process creation failed
        exit(EXIT_FAILURE);
        break;

    case 0:                   // new child process
        printf("c:  value of pid=%i\n", pid);
        printf("c:  child's pid=%i\n", getpid());
        printf("c:  child's parent pid=%i\n", getppid());
        break;

    default:                  // original parent process
        sleep(1);
        printf("p:  value of pid=%i\n", pid);
        printf("p:  parent's pid=%i\n", getpid());
        printf("p:  parent's parent pid=%i\n", getppid());
        break;
    }
    fflush(stdout); //forces output to appear
}
```

- Produces:
    
    c: child's value of pid=0 c: child's pid=5642 c: child's parent pid=5641 p: parent's value of pid=5642 p: parent's pid=5641 p: parent's parent pid=3244
    

******************************************************************************Where Does the First Process Come From?******************************************************************************

- The last internal action of booting a Unix-based operating system results in the first single “true” process, named ____init____.

- _____init_____ has the process-ID of 1

[![](Untitled%2031.png)](Week%205%20-%20Creating%20Processes%20and%20OS%20Services%2042be2c625c7842bf882fc9ee8d9c811a/Untitled.png)

**************************************Waiting for a Process to Terminate:**************************************

- The parent process typically lets the child process execute, but wants to know when the child has terminated and whether the child terminated successfully or otherwise

- Parent process calls the ______wait()______ system call to suspend its own execution and to wait for any of its child processes to terminate

- _______&status_______ permits the system call to modify the calling function’s variable, allowing it to receive information about how the child terminated

```
#include  <stdio.h>
#include  <stdlib.h>
#include  <unistd.h>
#include  <sys/wait.h>

void function(void)
{
    switch ( fork() ) {
    case -1 :
        printf("fork() failed\n"); // process creation failed
        exit(EXIT_FAILURE);
        break;

    case 0:                       // new child process
        printf("child is pid=%i\n", getpid() );

        for(int t=0 ; t<3 ; ++t) {
            printf("  tick\n");
            sleep(1);
        }
        exit(EXIT_SUCCESS);
        break;

    default: {                    // original parent process
        int child, status;

        printf("parent waiting\n");
        child = wait( &status );

        printf("process pid=%i terminated with exit status=%i\n",
                child, WEXITSTATUS(status) );
        exit(EXIT_SUCCESS);
        break;
    }

    }
}
```

**************Memory:**************

- Parent process memory is copied from parent to child, a copy

- Newer computers, child does not receive a full copy of the memory, only when the child is trying to edit the memory

- “copy-on-write”

e************xecv:************

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char *program_arguments[] = {
    "ls",
    "-l",
    "-F",
    NULL
};

    ....
    execv( "/bin/ls", program_arguments );
    // A SUCCESSFUL CALL TO exec() DOES NOT RETURN
		// typically will be made in a child process

    exit(EXIT_FAILURE);  // IF WE GET HERE, THEN exec() HAS FAILED
```

# Operating System Services

- System calls, system traps or syscalls

- Kernel time isn’t added until the system call has executed

- The syscall interfaces of modern OSs are presented as an API of C prototypes

- Syscalls need to be paranoid to protect the kernel from memory access violations.

```
#include <syscall.h>
#include <unistd.h>
.....

int write(int fd,void *buf, size_t len) {
	if (any_errors_in_arguments) {
      errno = EINVAL;
			return (-1);
   }
		returnsyscall(SYS_write, fd, buf, len);
}
```

****************************Status Values:****************************

- Minimal return-value interface is supported

- Most return an integer value (0 for success, or non-zero on failure)

```
#define EPERM     1     /* Operation not permitted */
#define ENOENT    2     /* No such file or directory */
#define ESRCH     3     /* No such process */
#define EINTR     4     /* Interrupted system call */
#define EIO       5     /* I/O error */
#define ENXIO     6     /* No such device or address */
#define E2BIG     7     /* Arg list too long */
#define ENOEXEC   8     /* Exec format error */
#define EBADF     9     /* Bad file number */
#define ECHILD   10     /* No child processes */
```

- These are the errno error list

```
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
    
...
    if(chdir("/Users/someone") != 0) {
       printf("cannot change directory, why: %s\n", 
								sys_errlist[errno]);
       exit(EXIT_FAILURE);
    }
...
```

- Syscalls are often written in C-pre-process code (an assembly language)

**********************************************************************Execution Environment of a Process:**********************************************************************

[![](Untitled%201%208.png)](Week%205%20-%20Creating%20Processes%20and%20OS%20Services%2042be2c625c7842bf882fc9ee8d9c811a/Untitled%201.png)

- The stack grows downwards, heap is what grows upwards if more memory is required.

- When they collide, we get a stack overflow

**************************************************Environment Variables:**************************************************

- NULL-terminated character strings

- They allow us to pass additional information into our programs

```
#include <stdio.h>
#include <stdlib.h>
   ...

//  A POINTER TO A VECTOR OF POINTERS TO CHARACTERS - OUCH, LATER!
//  (LET'S CALL IT AN ARRAY OF STRINGS, FOR NOW)
extern char **environ;

int main(int argc, char *argv[])
{
    putenv("ANIMAL=budgie");

    for(int i=0 ; environ[i] != NULL ; ++i) {
        printf("%s\n", environ[i]);
    }
    return 0;
}
```