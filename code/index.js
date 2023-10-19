/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 * 
 * 
 * Creado por Laura Ortega - 04/09/2023
 */









//crea una funcion para invertir un string

const inverse = (string) => {
    stringReverse = ''
    for(let i = string.length-1;i>=0;i--){
        stringReverse += string[i]
    }
    return stringReverse
}

// crea una funcion que convierta de deciaml a binario

const binario = (numero) => {
    let numeroBinario = []
    
    while (numero > 0){
        const residuo = numero % 2
        numeroBinario.push(residuo)
        numero = Math.floor(numero/2)

    }


    //invertir numero
    let numeroBinarioInvertido = []
    for(let i = numeroBinario.length-1;i>=0;i--){
        numeroBinarioInvertido.push(numeroBinario[i])

    }
    return numeroBinarioInvertido

}

