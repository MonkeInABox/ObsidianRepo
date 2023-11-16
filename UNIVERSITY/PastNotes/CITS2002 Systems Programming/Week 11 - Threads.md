
|   |   |
|---|---|
|Created|@October 9, 2023 8:39 AM|
|Class|Systems Programming|
|Reviewed||
|Materials|[https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture20/singlepage.html](https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/lecture20/singlepage.html)|

> **************Thread:************** Includes → a sequence of instructions to be executed, a set of local variables that belong to the thread, a set of shared global variables that all threads can read and write.

- Threads allow us to deal with asynchronous events synchronously and efficiently

- And allow us to get parallel performance on a shared-memory multiprocessor

4 Core Benefits to Multi-Threading:

1. Responsiveness

2. Resource sharing

3. Efficiency

4. Scalability

Difference Between Processes and Threads:

- The degree of independence between processes/threads
    
    - Standard C program is a process with just one thread
    
    - Thread library allows us to write a program defining multiple threads within a single process

|   |   |
|---|---|
|**PROCESSES**|**THREADS**|
|IDs|registers|
|environment variables|stack pointer|
|working directory|scheduling properties|
|program instructions|set of pending and blocked signals|
|registers|thread specific data|
|file descriptors||
|asynchronous signal actions||
|libraries||
|inter-process comm channels||

********Creating & Terminating POSIX threads:********

pthread_create(thread, attr, start_routine, arg);

```
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS     5

void *hello_world(void *threadid)
{
  printf("Hello World, from thread #%li!\n", (long)threadid);
  pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
  pthread_t threads[NUM_THREADS];

  for(long tid=0 ; tid < NUM_THREADS ; tid++) {
    printf("In main(): creating thread %li\n", tid);

    int err = pthread_create(&threads[tid], NULL, hello_world, (void *)tid);

    if(err != 0) {
      printf("ERROR; return code from pthread_create() is %d\n", err);
      exit(EXIT_FAILURE);
    }
  }

  pthread_exit(NULL);       // as main() is a thread, too
  return 0;
}
```

```
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *worker(void *threadarg)
{
    ....
    printf("thread #%li terminating.\n", (long)threadarg);
    pthread_exit((void*) threadarg);
}

int main(int argc, char *argv[])
{
    ....
    pthread_attr_t attr;

//  INITIALIZE AND SET THREAD DETACHED ATTRIBUTE
    pthread_attr_init(&attr);
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);  

    err = pthread_create(&thread[tid], &attr, worker, (void *)tid);
    ....

//  BLOCK main() UNTIL THE worker() THREAD TERMINATES
    err = pthread_join(thread[t], &status);
    ....

    printf("main() resumes execution\n");
    ....
}
```

**************************************Synchronisation:**************************************

- If multiple threads are simply reading the same variable, there is no problem

- however, if they update the same variable, the order in which it occurs is important

> MUTEX : an abbreviation of mutual exclusion, acts like a lock protecting access to a shared data resource, only one thread can lock (or own) a mutex variable at any given time. The threads take turns accessing protected data

- Mutex sequence:
    
    - create and initialise mutex variable
    
    - several threads attempt to lock mutex
    
    - only one thread succeeds, owns the mutex
    
    - owner performs actions
    
    - unlocks mutex
    
    - another thread acquires mutex and the sequence is repeated
    
    - mutex is destroyed
    
    ```
    #include <stdio.h>
    #include <stdlib.h>
    #include <pthread.h>
    
    int balance = 0;
    
    pthread_mutex_t mutexbalance = PTHREAD_MUTEX_INITIALIZER;
    
    void deposit(int amount)
    {
        pthread_mutex_lock(&mutexbalance);
        {
            int currbalance = balance;      // read shared balance
            currbalance    += amount;
            balance         = currbalance;  // write shared balance
        }
        pthread_mutex_unlock(&mutexbalance);
    }
    
    void withdraw(int amount)
    {
        pthread_mutex_lock(&mutexbalance);
        {
            int currbalance = balance;       // read shared balance
            if(currbalance >= amount) {
                currbalance -= amount;
                balance      = currbalance;  // write shared balance
            }
        }
        pthread_mutex_unlock(&mutexbalance);
    }
    
        create threads...
    ....
        deposit(200);      // thread 1
        withdraw(100);     // thread 2
        deposit(500);      // thread 1
        withdraw(200);     // thread 3
    ```
    

******************************************************************Producer/Consumer Threads Example******************************************************************

```
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <pthread.h>

#define MAX_ITEMS     10

pthread_cond_t cond_recv    = PTHREAD_COND_INITIALIZER;
pthread_cond_t cond_send    = PTHREAD_COND_INITIALIZER;

pthread_mutex_t cond_mutex  = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;

bool full=false;
int  count=0;

void *producer(void *thread_id)
{
    while(true) {
	pthread_mutex_lock(&cond_mutex);
        while(full) {
            pthread_cond_wait(&cond_recv, &cond_mutex) ;
        }

        pthread_mutex_unlock(&cond_mutex);
        pthread_mutex_lock(&count_mutex);

        ++count;
        full = true;
        printf("producer(%li):%i\n", pthread_self() , count);

        pthread_cond_broadcast(&cond_send);
        pthread_mutex_unlock(&count_mutex);

        if((count >= MAX_ITEMS) {
            break;
        }
    }
}
void *consumer(void *thread_id)
{
    while(true) {
        pthread_mutex_lock(&cond_mutex);

        while(!full) {
            pthread_cond_wait(&cond_send , &cond_mutex) ;
        }

        pthread_mutex_unlock(&cond_mutex);
        pthread_mutex_lock(&count_mutex);

        --count;
        full = false;
        printf("consumer(%li):%i\n", pthread_self(), count);

        pthread_cond_broadcast(&cond_recv);
        pthread_mutex_unlock(&count_mutex);

        if((count >= MAX_ITEMS) {
            break;
        }
    }
}
```