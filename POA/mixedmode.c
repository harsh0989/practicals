#include <stdio.h>

int main(void) {
    int num1 = 10, num2 = 15, sum = 0;
    __asm__ __volatile__(
        "addl %%ebx,%%eax"
        : "=a"(num1)
        : "a"(num1), "b"(num2));
    printf("num1 + num2=%d\n", num1);
    __asm__ __volatile__(
        "movl %%eax, %%ecx"
        : "=c"(sum)
        : "a"(num1));
    printf("num1 + num2=%d\n", sum);
    return 0;
}