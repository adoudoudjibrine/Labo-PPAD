#include <stdio.h>
#include <stdlib.h>
#include <time.h>    // for clock_t, clock()
#define BILLION  1000000000.0


/** Programme qui modifie une matrice */

int main (int argc, char **argv)

{
    int a[2][2] = {{1,5},{0,3}};
    struct timespec start, end;


    printf("Matrice de depart : ");

    for(int i = 0; i<2;i++)
    {
        printf("\n");
        for(int j=0;j<2;j++)
        {
            printf("%4d",a[i][j]);
        }
    }
    printf("\n");

    clock_gettime(CLOCK_REALTIME, &start);

    for(int i = 0; i<2; i++)
    {
        for(int j=0; j<2;j++)
        {
            a[i][j] = (i+2)*j;
        }
    }
    clock_gettime(CLOCK_REALTIME, &end);
    // time_spent = end - start
    double time_spent = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) ;


    printf("Voici le resultat : ");

    for(int i = 0; i<2;i++)
    {
        printf("\n");
        for(int j=0;j<2;j++)
        {
            printf("%4d",a[i][j]);
        }
    }
    printf("\nLe programme s\'execute en : %f ms\n",time_spent);

}