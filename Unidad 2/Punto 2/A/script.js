function sumaElementos(listaNumeros) {
  let suma = 0;

  for (let i = 0; i < listaNumeros.length; i++) {
      suma += listaNumeros[i];
  }

  return suma;
}

const numeros = [2, 4, 6, 8, 10];
const resultado = sumaElementos(numeros);


const resultadoElement = document.getElementById('resultado');
resultadoElement.textContent = `El resultado es: ${resultado}`;