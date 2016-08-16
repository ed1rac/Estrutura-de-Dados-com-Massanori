#include <stdio.h>
#include <stdlib.h>

int buscaBinaria(int x, int lista[], int n);
int main(){
    int x;
    int vetor[7] = {1,2,3,4,5,6,7};

    x = buscaBinaria(0, vetor, 7);
    printf("Busca: 0 Encontrado: %d\n", x);

    x = buscaBinaria(1, vetor, 7);
    printf("Busca: 0 Encontrado: %d\n", x);

    x = buscaBinaria(2, vetor, 7);
    printf("Busca: 1 Encontrado: %d\n", x);

    x = buscaBinaria(3, vetor, 7);
    printf("Busca: 2 Encontrado: %d\n", x);

    x = buscaBinaria(4, vetor, 7);
    printf("Busca: 3 Encontrado: %d\n", x);

    x = buscaBinaria(5, vetor, 7);
    printf("Busca: 4 Encontrado: %d\n", x);

    system("pause");
    return 0;
}

int buscaBinaria(int x, int lista[],int n){
    /*
    Função de Busca Binária
    Pesquisa um numero em uma lista ordenada
    Tempo de O(Log(n)) e espaço de O(n)
    Input:: int x, int lista[], int n
    Output:: local do item buscado
    */
    int inicio = 0;
    int fim = n-1;
    int meio = fim/2;
    while(fim-inicio>1){
        if(x <= lista[meio] ){
            fim -= meio;
            meio = fim/2;
        }
        else{
            inicio += fim - meio;
            meio = inicio+((fim-inicio)/2);
        }
        if(x==lista[meio])  return meio;   // Contigência de Acerto ou mutiplos
    }
    if (x <= lista[inicio]){
        return inicio;
    }
    else{
        return fim;
    }
}
