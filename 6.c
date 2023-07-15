#include <stdio.h>
#include <math.h>

int sumofsquares(int n){
    int sum = 0;
    for (int i = 0; i < n+1; i++)
    {
        sum += i * i; 
    }
    return sum;
}

int squareofsum(int n){
    int sum = 0;
    for (int i = 0; i < n+1; i++)
    {
        sum += i;
    }
    sum = sum * sum;
    return sum;


}

int main()
{
    int j = squareofsum(100)-sumofsquares(100);
    printf("%d",j);
    return 0;
}
