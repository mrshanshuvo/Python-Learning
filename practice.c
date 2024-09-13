#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);

    for (int row = 1; row <= n; row++)
    {
        for (int sp = 1; sp <= n - row; sp++)
        {
            printf(" ");
        }
        for (int star = 1; star <= row; star++)
        {
            printf("*");
        }
        for (int star = 1; star <= row - 1; star++)
        {
            printf("*");
        }
        printf("\n");
    }

    // for (int row = 1; row <= n; row++)
    // {
    //     for (int sp = 1; sp <= row - 1; sp++)
    //     {
    //         printf(" ");
    //     }
    //     for (int star = 1; star <= n - row + 1; star++)
    //     {
    //         printf("*");
    //     }
    //     printf("\n");
    // }
}
