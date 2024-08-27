#include <stdio.h>
#include <math.h>

int main() {
    
    long double valor_verdadero, valor_aproximado;
    
    printf("Ingrese el valor verdadero: ");
    scanf("%Lf", &valor_verdadero); 

    printf("Ingrese el valor aproximado: ");
    scanf("%Lf", &valor_aproximado);

    long double error_verdadero = fabsl(valor_verdadero - valor_aproximado); 
    long double error_relativo = error_verdadero / valor_verdadero;
    long double error_relativo_porcentual = error_relativo * 100;
    
    
    printf("Error verdadero: %Lf\n", error_verdadero); 
    printf("Error relativo: %.8Lf\n", error_relativo);  
    printf("Error relativo porcentual: %Lf %%\n", error_relativo_porcentual); 
    
    return 0;
}