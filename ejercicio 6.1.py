import unittest

# Función para calcular el mínimo común múltiplo (MCM) de dos números
def calculo_MCM(nro1, nro2):
    divisor = 1
    valor = 'true'
    MCM = []

    while (nro1 != 1 or nro2 != 1):
        valor = 'false'

        while (valor == 'false'):
            divisor += 1

            while (nro1 % divisor == 0 and nro2 % divisor == 0):
                nro1 /= divisor
                nro2 /= divisor
                MCM.append(divisor)

            while (nro1 % divisor == 0):
                nro1 /= divisor
                MCM.append(divisor)

            while (nro2 % divisor == 0):
                nro2 /= divisor
                MCM.append(divisor)

            valor = 'true'

        valor = 'false'
    print(nro1, " ", nro2)

    print(MCM)
    mcm = 1

    # Calcula el MCM multiplicando todos los elementos de MCM
    for i in range(len(MCM)):
        mcm *= MCM[i]

    print("El mínimo común múltiplo es : ", mcm)
    return mcm

# Función para calcular el máximo común divisor (MCD) de dos números
def calculo_MCD(nro1, nro2):
    divisor = 1
    valor = 'false'
    MCD = []
    mcd = 1

    while (valor == 'false'):

        divisor += 1
        if (nro1 % divisor == 0 and nro2 % divisor == 0):
            nro1 /= divisor
            nro2 /= divisor

            MCD.append(divisor)
        else:
            valor = 'true'

    # Calcula el MCD multiplicando todos los elementos de MCD
    for i in range(len(MCD)):
        mcd *= MCD[i]
    print("El máximo común divisor es : ", mcd)
    return mcd


# Clase de prueba para las funciones calculo_MCM y calculo_MCD
class TestCalculoDeMCM_MCD(unittest.TestCase):
    
    # Prueba para la función calculo_MCD
    def test_calcular_MCD(self):
        esperado = 24
        nro1 = 24
        nro2 = 48
        self.assertEqual(calculo_MCD(nro1, nro2), esperado)
    
    # Prueba para la función calculo_MCM
    def test_calcular_MCM(self):
        esperado = 272
        nro1 = 34
        nro2 = 16
        self.assertEqual(calculo_MCM(nro1, nro2), esperado)


if __name__ == "__main__":
    unittest.main()