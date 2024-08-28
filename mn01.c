#include <stdio.h>
#include <math.h>

long double obtener_cifras_significativas(long double numero) {
    int exponent;
    long double mantissa;
    if (numero < 1 && numero > 0) {
        exponent = floor(log10(numero));
        mantissa = numero / pow(10, exponent);
        mantissa = roundl(mantissa * 1000) / 1000; 
        numero = mantissa * pow(10, exponent);
    } else if (numero >= 1) {
        exponent = floor(log10(numero)) - 2; 
        mantissa = numero / pow(10, exponent);
        mantissa = roundl(mantissa) / 100; 
        numero = mantissa * pow(10, exponent);
    }
    return numero;
}

int main() {
    long double valor_verdadero, valor_aproximado;
    
    printf("Bienvenido:\n");
    printf("Ingrese el valor verdadero: ");
    scanf("%Lf", &valor_verdadero); 

    printf("Ingrese el valor aproximado: ");
    scanf("%Lf", &valor_aproximado);

    long double error_verdadero = fabsl(valor_verdadero - valor_aproximado); 
    long double error_relativo = error_verdadero / valor_verdadero;
    long double error_relativo_porcentual = error_relativo * 100;
    
    printf("\n");
    printf("Calculos normales:\n");
    printf("Error verdadero: %Lf\n", error_verdadero); 
    printf("Error relativo: %Lf\n", error_relativo);  
    printf("Error relativo porcentual: %Lf %%\n", error_relativo_porcentual);
    
    printf("\n");
    printf("Con 3 cifras significativas:\n");
    printf("Error verdadero: %.9Lf\n", obtener_cifras_significativas(error_verdadero));
    printf("Error relativo: %.9Lf\n", obtener_cifras_significativas(error_relativo));
    printf("Error relativo porcentual: %.9Lf %%\n", obtener_cifras_significativas(error_relativo_porcentual));

    return 0;
}