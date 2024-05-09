using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using Matematica; // Importa el espacio de nombres donde se encuentran las funciones de cálculo.

namespace Test
{
    [TestClass]
    public class UnitTest1
    {

        [TestMethod]
        public void Test_MCD()
        {
            // Inicialización de variables
            int nroa = 24;
            int nrob = 48;
            int esperado = 24;

            // Llamada al método para calcular el máximo común divisor (MCD)
            int resultado = calculo.Calculo_MCD(nroa, nrob);

            // Comprobación de valores
            Assert.AreEqual(resultado, esperado);
        }
    }
}