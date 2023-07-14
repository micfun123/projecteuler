//find the biggest palindrome made from the product of two 3-digit numbers
#include <stdio.h>

int isPalindrome(int n)
{
    int temp = n;
    int rev = 0;
    while (temp != 0)
    {
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    if (rev == n)
        return 1;
    else
        return 0;
}

int main()
{
    for (int i = 1000; i >= 100; i--)
    {
        for (int j = 1000; j >= 100; j--)
        {
            if (isPalindrome(i * j))
            {
                printf("%d\n", i * j);
                return 0;
            }
        }
    }

}