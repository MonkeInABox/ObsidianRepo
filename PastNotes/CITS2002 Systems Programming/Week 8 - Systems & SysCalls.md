

|   |   |
|---|---|
|Created|@September 18, 2023 9:00 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture15/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture15/singlepage.html)[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture16/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture16/singlepage.html)|

**********************Organisation of File Systems:**********************

- fields: the smallest logical item of data understood by a file-system, a single integer or string

- records: one or more fields, treated as a single unit

- files: familiar collections of identically represented records and are accessed by unique names, deleting a file deletes its component records

- databases: one or more files whose contents are strongly (logically) related

|   |   |
|---|---|
|**File-Based Activity**|**System-Calls**|
|File Creation, Deletion|open(), creat(), close(), truncate(), unlink()|
|Accessing A File’s Contents|read(), write(), lseek()|
|Accessing A File’s Attribute|chmod(), chown(), stat()|
|Some Directory Ops|mkdir(), rmdir()|

******************************File Information Structures (INODES):******************************

- each information structure is accessed by a unique key, and the role of the directory is to provide <filename, inode> pairs.

- A distinct file-entry is identified by a <major-device-number, minor-device-number, inode> tuple.

- Each inode typically includes:
    
    - files type
    
    - files size
    
    - limits on file size
    
    - primary owner of file
    
    - information about other potential users of the file
    
    - access constraints on different users
    
    - dates and times of creation, last access, last modification
    
    - pointers to the files actual data blocks

- As a consequence, multiple file names may refer to the same file. These are file-system links.
    
    - Individual processes access open files through their file descriptor table
    
    - This table indexes the kernels global file table
    
    - This table indexes the devices inode table

[![](Untitled%2032.png)](Week%208%20-%20Systems%20&%20SysCalls%2019a4e1b76efc479a9e2ff4af766c8120/Untitled.png)

********************************************File Allocation Methods (CONTIGUOUS):********************************************

- The simplest policy is the use of a fixed or contiguous allocation. This requires that a files maximum size is determined when the file is created and that file cannot grow beyond that limit.

- The file allocation table stores, for each file, its starting block and length.

- Like simple memory allocation schemes, this method suffers from internal and external fragmentation.

- A compaction scheme is required to reduce fragmentation.

********************************************************************File Allocation Methods (CHAINED):********************************************************************

- Here the blocks allocated to a file form a linked list (chain) and as a files length is extended, a new block is allocated and linked to the last block in the file.

- A small pointer is allocated within each file data block to indicate the next block.

**********************File Allocation Methods (INDEXED):**********************

- The file-allocation table (FAT) contains a multi-level index for each file - just as we have seen in the use of inodes, which contain direct pointers to data blocks and pointers to indirection blocks.

- Indirection blocks are introduced each time the total number of blocks overflows the previous index allocation.

- The indices are neither stored with the file-allocation table or with the file and are retained in memory when the file is opened.

# SYSTEM CALLS:

- We can use & to get the pointer, to put into a function with a *variable to be passed through.

- We can use the → operator to access the fields via a pointer:

```
#include  <stdio.h>
#include  <time.h>

void greeting(void)
{
    time_t      NOW     = time(NULL);
    struct tm   *tm     = localtime(&NOW);

    printf("Today's date is %i/%i/%i\n",
             tm->tm_mday, tm->tm_mon + 1, tm->tm_year + 1900);

    if(tm->tm_hour < 12) {
        printf("Good morning\n");
    }
    else if(tm->tm_hour < 17) {
        printf("Good afternoon\n");
    }
    else {
        printf("Good evening\n");
    }
}
```

```
#include  <stdio.h>
#define __USE_XOPEN_EXTENDED
#include <sys/types.h>
#include <pwd.h>

#if 0
The header file <pwd.h> declares:

   struct passwd {
       char   *pw_name;       /* username */
       char   *pw_passwd;     /* user password */
       uid_t   pw_uid;        /* user ID */
       gid_t   pw_gid;        /* group ID */
       char   *pw_gecos;      /* user information */
       char   *pw_dir;        /* home directory */
       char   *pw_shell;      /* shell program */
   };

   struct passwd *getpwent(void);
#endif

int main(int argc, char *argv[])
{
    struct passwd *pwd;

    while((pwd = getpwent()) != NULL) {
        printf("%20s\t%-30s\t%s\n",
                pwd->pw_name, pwd->pw_dir, pwd->pw_shell);
    }
    return 0;
}
```

We can define our own data-types and use pointers to reference particular parts of them:

```
//  DEFINE THE LIMITS ON PROGRAM'S DATA-STRUCTURES
#define MAX_TEAMS               24
#define MAX_TEAMNAME_LEN        30
....

typedef struct {
    char    teamname[MAX_TEAMNAME_LEN+1];        // +1 for null-byte        
    ....
    int     played;
    ....
} TEAM;

TEAM    team[MAX_TEAMS];

//  PRINT EACH TEAM'S RESULTS, ONE-PER-LINE, IN NO SPECIFIC ORDER
for(int t=0 ; t<nteams ; ++t) {
    TEAM    *tp = &team[t];

    printf("%s %i %i %i %i %i %i %.2f %i\n", // %age to 2 decimal-places
            tp->teamname,
            tp->played, tp->won, tp->lost, tp->drawn,
            tp->bfor, tp->bagainst,
            (100.0 * tp->bfor / tp->bagainst),      // calculate percentage
            tp->points);
}
```