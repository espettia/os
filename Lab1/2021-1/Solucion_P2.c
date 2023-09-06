/* Codigo: 20172665
 * Nombre: Christian Andre Carhuancho Rodriguez
 * Fecha:  23/04/2021
 */

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
int main(int argc,  char *argv[ ]) {
   pid_t padre = getpid();
   pid_t childpid;
   char buff[50];              /* indicates process should spawn another     */
   unsigned long long num1,num2;
   int error;                  /* return value from dup2 call                */
   int fd[2];                  /* file descriptors returned by pipe          */
   int i;                      /* number of this process (starting with 1)   */
   int nprocs;                 /* total number of processes in ring          */
           /* check command line for a valid number of processes to generate */
   if ( (argc != 2) || ((nprocs = atoi (argv[1])) <= 0) ) {
       fprintf (stderr, "Usage: %s nprocs\n", argv[0]);
       return 1;
   }
   if (pipe (fd) == -1) {      /* connect std input to std output via a pipe */
      perror("Failed to create starting pipe");
      return 1;
   }
   if ((dup2(fd[0], STDIN_FILENO) == -1) ||(dup2(fd[1], STDOUT_FILENO) == -1)) {
      perror("Failed to connect pipe");
      return 1;
   }
   if ((close(fd[0]) == -1) || (close(fd[1]) == -1)) {
      perror("Failed to close extra descriptors");
      return 1;
   }
   for (i = 1; i < nprocs;  i++) {         /* create the remaining processes */
      if (pipe (fd) == -1) {
         fprintf(stderr, "[%ld]:failed to create pipe %d: %s\n", (long)getpid(), i, strerror(errno));
         return 1;
      }
      if ((childpid = fork()) == -1) {
         fprintf(stderr, "[%ld]:failed to create child %d: %s\n", (long)getpid(), i, strerror(errno));
         return 1;
      }
      if (childpid > 0)               /* for parent process, reassign stdout */
          error = dup2(fd[1], STDOUT_FILENO);
      else                              /* for child process, reassign stdin */
          error = dup2(fd[0], STDIN_FILENO);
      if (error == -1) {
         fprintf(stderr, "[%ld]:failed to dup pipes for iteration %d: %s\n", (long)getpid(), i, strerror(errno));
         return 1;
      }
      if ((close(fd[0]) == -1) || (close(fd[1]) == -1)) {
         fprintf(stderr, "[%ld]:failed to close extra descriptors %d: %s\n", (long)getpid(), i, strerror(errno));
         return 1;
      }
      if (childpid) break;
   }                
   
    if(getpid() == padre){
	  strcpy(buff,"1 1");
	  write(STDOUT_FILENO,buff,sizeof(buff));
	  wait(NULL);
	  read(STDIN_FILENO,buff,sizeof(buff));
	  sscanf(buff,"%llu %llu",&num1,&num2);
	  fprintf(stderr,"%llu\n",num1);
	}
	else{
		read(STDIN_FILENO,buff,sizeof(buff));
		sscanf(buff,"%llu %llu",&num1,&num2);
		unsigned long long c = num1 + num2;
		sprintf(buff,"%llu %llu",num2,c);
		write(STDOUT_FILENO,buff,sizeof(buff));
		wait(NULL);
	}
    return 0;
}
