using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using Matematica; // Importa el espacio de nombres donde se encuentran las funciones de c�lculo.

namespace Test
{
    [TestClass]
    public class UnitTest1
    {

        [TestMethod]
        public void Test_MCD()
        {
            // Inicializaci�n de variables
            int nroa = 24;
            int nrob = 48;
            int esperado = 24;

            // Llamada al m�todo para calcular el m�ximo com�n divisor (MCD)
            int resultado = calculo.Calculo_MCD(nroa, nrob);

            // Comprobaci�n de valores
            Assert.AreEqual(resultado, esperado);
        }
    }
}