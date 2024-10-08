#include <stdio.h>
#include <string.h>

void reverse_string(char *str) {
    int length = strlen(str);
    int i, j;
    char temp;

    for (i = 0, j = length - 1; i < j; i++, j--) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

int main() {
    int n;
    printf("Enter the length of the string: ");
    scanf("%d",&n);
    char str[n];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    reverse_string(str);
    printf("Reversed string: %s\n", str);
    return 0;
}