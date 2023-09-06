/**************************************************/
/**   Autor : Prof. Alejandro T. Bello Ruiz      **/
/**   Curso : Sistemas Operativos - Laboratorio  **/
/**   Año   : 2019-2                             **/  
/**************************************************/

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

void arbol(int);
int pp;

int main(int narg, char *argv[]){
	char orden[30];
	int n;
	
	if( narg != 2) {
		fprintf(stderr,"Usage: %s <num_procesos>\n",argv[0]);
		exit(1);
	}	
	pp = getpid();	
	n = atoi(argv[1]); 		
	arbol(n);
	sleep(1);	
	sprintf(orden,"pstree -p %d",pp);
	system(orden);
	exit(0);
}

void arbol(int n) {
	int i,k,mpid,npid,final;
	for(k=0; k< n;k++) 
		 if(!(mpid=fork())) {
			final =  k==0 || k== n-1 ? n-1:n-2;			
		    for(i=0;i<final;i++)		        
				if((npid=fork())) break;
		    break;		 
	     }
	if(pp != getpid()) {
	   sleep(2);
	   exit(0);
	}	 	
}
