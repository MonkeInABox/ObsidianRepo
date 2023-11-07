[[Week 1 - C Basics]]


|   |   |
|---|---|
|Created|@September 11, 2023 8:49 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture13/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture13/singlepage.html)[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture14/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture14/singlepage.html)|

Memory plays a role from two perspectives:

- The operating system’s perspective of how to allocate and manage all memory fairly and efficiently

- The process’ perspective of how to access the memory allocated to it and how to obtain more

Requirements of Memory Management:

- Logical Organisation:
    
    - Although processes often occupy linear sequences of addresses, this is rarely how they are written or executed
    
    - Ideally all references from one module to another are resolved at run time, maintaining their independence (late binding)

- Sharing:
    - Processes need to be allowed to share memory

- Relocation:
    
    - Execution of a single process is often unrelated to others. It is difficult to know where a process’ image is placed when loaded into physical memory
    
    - When a process is swapped-out, it is unlikely that the process will be swapped-in back to exactly the same memory location

- Protection:
    
    - Each process must be protected from accidental or deliberate interference from other processes
    
    - Memory references must be checked at run-time to ensure they lie within the bounds of memory allocated

- Physical Organisation:
    
    - The relationship between RAM and disk is straightforward, however, overlays permitted reuse of a systems memory but today are unnecessarily complex
    
    - Programmer cannot predict the size nor location of a process’ memory, this task of moving information is the responsibility of the operating system

Initial Memory Allocation Using Partitioning:

- Two choices of fixed-size partitions:
    
    - equal-sized partitions
        - Two problems: process’ requirements may exceed partition size, and a small process still occupies a full partition (internal memory fragmentation)
    
    - unequal-sized partitions
        - still has internal memory fragmentation

- So we want to use dynamic memory partitioning. 3 algorithms that can be used to do this:
    
    - First-fit: find first unused block of memory that can contain the process
    
    - Best-fit: find smallest unused block that can contain the process
    
    - Next-fit: remember where the last process was put, find first unused usable block from that process

Address Relocation:

- Logical address: a reference to a memory location independent of any current assignment of data to main memory

- Relative address: a logical address expressed relative to a fixed location, such as the beginning of a process’ image

- Physical address: an actual location in main (physical) memory

Paging of Memory:

- A hardware base register indicates the beginning of the process’ partition, and a hardware bounds register to indicate the partition’s extent

- We term small, equal sized chunks of a process’ image _____pages_____, and place them in equal sized chunks of main memory called _______frames/page frames_______.

- We can also remove the restriction that a process’ section of memory must be contiguous

- So the OS maintains a set of page registers, or a page table
    
    - holds the physical frame location for each page
    
    - a logical address now consists of a page number and an offset within the page’s frame

The Principle of Referential Locality:

- Memory references cluster in certain parts of the program: over long periods, the centers of clusters move, but over shorter periods they are fairly static.
    
    - except for infrequent branches and function/procedure invocation, program execution is sequential
    
    - programs operate at the same depth of function-invocation, references cluster around a small collection of functions

Paging vs. Partitioning:

- Two benefits to paging:
    
    - As processes are frequently swapped out/in they occupy different regions of physical memory, hardware translates logical address to new physical address
    
    - A process is broken up into pages and these need not be contiguous in physical memory

- Execution of a process can continue provided that the instruction it next wants to execute is in physical memory
    
    - if not it must be loaded from the swapping or paging space before it can continue
    
    - paging request forces the process to be blocked until the required page of memory is available
    
    - This means:
        
        - More processes may be maintained in main physical memory (ready or running)
        
        - If the swapping space is larger than physical memory, then any single process may now demand more memory than the amount of physical memory installed → virtual memory.

Virtual Memory:

- Principle of referential locality tells us that at any one time, only a small subset of data will be required

- A process’ set of pages in physical memory is its RESIDENT (or working) MEMORY SET

- Page table entries must include control information. At least:
    
    - if the table is present in physical memory (P bit)
    
    - if the page has been modified since being brought into physical memory (M bit)

- When a running process requests a page not in memory, __________page fault__________
    - To make room for the required page, one or more existing pages must move to swap space

Implementation Considerations:

- When should a process’ page be fetched?
    - A process first requires the first page containing its starting address, then a VM system can employ demand paging in which a page is allocated only when a reference to it is made, or predictive pre-paging where it intelligently adds pages before required

- Where in physical memory should pages be allocated?
    - Should we use first-fit, best-fit or next-fit?

- Which existing blocks should be replaced?
    
    - To avoid page-thrashing, we wish to replace only pages unlikely to be required soon
    
    - first-in first-out and least-recently-used are commonly used algorithms

- How many process to admit to Ready and Running states?
    - The degree of multi-programming permitted must balance processor utilisation against utility