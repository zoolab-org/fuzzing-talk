#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
    /* Create an array with 100 bytes, initialized with 42 */
    char *buf1 = malloc(100), *buf2 = malloc(100);
    memset(buf1, 42, 100); memset(buf2, 43, 100);

    /* Read the N-th element, with N being the first command-line argument */
    int index = atoi(argv[1]);
    char val = buf1[index];

    /* Clean up memory so we don't leak */
    free(buf1); free(buf2);
    return val;
}
    
