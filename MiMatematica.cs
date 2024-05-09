using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Matematica
{
    public class calculo
    {

        // Método para calcular el máximo común divisor (MCD)
        public static int Calculo_MCD(int nroA, int nroB)
        {
            int mcd = 1;
            int divisor = 1;
            bool valor = false;
            List<int> MCD = new List<int>();

            while (valor == false)
            {
                // Dividiremos por el divisor común para ambos números
                divisor += 1;

                // Entra si se dividen en divisores comunes
                if (nroA % divisor == 0 && nroB % divisor == 0)
                {
                    nroA /= divisor;
                    nroB /= divisor;
                    MCD.Add(divisor);
                }
                else
                {
                    valor = true;
                }
            }

            // Imprime los números finales
            Console.WriteLine(nroA + " " + nroB);

            // Calcula el MCD multiplicando los factores comunes
            foreach (int numero in MCD)
            {
                mcd *= numero;
            }
            Console.WriteLine("El máximo común divisor es : " + mcd);

            return mcd;
        }
    }
}