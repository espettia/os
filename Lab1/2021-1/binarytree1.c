/* *************************************************************/
/* binarytree.c (c) 2021 Alejandro T. Bello Ruiz, GPL-like      */
/* *********** *********************************************** */
#include <stdio.h>
#include <unistd.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>

double final;

void crea_arbol(int);

int main(int narg, char *argv[])
{  
   final=atoi(argv[1]);   
   crea_arbol(0);
   return 0;
}

void crea_arbol(int nivel)
{  int k;
	   
   nivel++;       
   for(k=0;k<2;k++) 
      if(!fork()) {
         if(nivel < final) crea_arbol(nivel);
         else pause(); 
      }      
   wait(NULL);
   wait(NULL);
     
} 
