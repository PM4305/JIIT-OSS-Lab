#include <stdio.h>

int main()
{
    int n;
    printf("Enter the number of elements in the array: ");
    scanf("%d",&n);
    int a[n],sum=0;
    for(int i=0;i<n;i++)
    {
        printf("\nEnter element %d: ",i+1);
        scanf("%d",&a[i]);
        sum=sum+a[i];
    }
    printf("\nAverage of the numbers is: %0.2f",sum/n);

}