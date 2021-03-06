#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int BemFormada (char s[]) {
    char *p; int t;
    int n, i;
    n = strlen (s);
    p = malloc (n * sizeof (char));
    t = 0;
    for (i = 0; s[i] != '\0'; i++) {
    /* p[0..t-1] ? uma pilha */
        switch (s[i]) {
            case ')': if (t != 0 && p[t-1] == '(') --t;
                      else return 0;
                      break;
            case '}': if (t != 0 && p[t-1] == '{') --t;
                      else return 0;
                      break;
            default: p[t++] = s[i];
        }
    }
    free (p);
    return t == 0;
}

int main (void) {
    //char expr [10] = "((){()})";
    //char expr [10] = "({)}";
    char expr [10] = ")})}}}";
    //char expr [10] = "({({{{";
    printf ("%s\n", BemFormada (expr) ? "Bem formada" : "Mal formada");
    system ("pause");
}
