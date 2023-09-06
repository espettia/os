#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{   int n, x,y, i,t;
	 
    srand(time(NULL));
    
    n = random() % 20;
    printf("%d numeros de Fibonacci\n",n);
    x=0;
    y=1; 
    printf("%d ",x);   
    for(i=0;i < n-1; i++) {
         t = x;
         x = y;
         y = y+t;
         printf("%d ",x);    
    }
    printf("\n");
    exit(0);
}
