#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

/* Este programa crea una cadena de procesos. Es decir el padre  */
/* crea un hijo, este a su vez crea otro y asi en forma sucesiva */
/* Ejm 2.5 del libro UNIX Programacion Practica - Kay Robbins    */
/*                                                Steve Robbins  */
/* Modificado por Alejandro Bello Ruiz - Informática PUCP        */

int main(int narg, char *argv[]){
  int i,status,n;
  pid_t child;    /* pid_t es un tipo definido en types.h */

  n = atoi(argv[1]);
  for (i=0;i<n;++i) if((child=fork())) break;
  wait(&status);
  return 0;
}  
