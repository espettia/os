#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

/* Author: Alejandro Bello Ruiz - Informática PUCP        */
/* Laboratorio 1 - 2023-1 PUCP                                   */ 

int main(int narg, char *argv[]){
  int i,n,mypid;
  
  n = atoi(argv[1]);
  for(i=0;i<2;i++) 
     if(!fork()) {
		 /* Hijos */
		 int *ptr;
		 
		 ptr = (int *)calloc(n,sizeof(int));
		 srand(getpid());
		 for(i=0; i<n; i++) {
               ptr[i] = rand() % 50;
		 }
		 mypid = getpid();
		 for(i=0; i<n; i++) {
				printf("My pid=%d my number=%d\n",mypid,ptr[i]);
		 }
		  	 
     } 		  
}  
