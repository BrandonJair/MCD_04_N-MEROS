import unittest

def calculo_MCD(nroA,nroB):
    divisor = 1
    valor = 'false'
    MCD = []
    mcd = 1
    #Dividiremos solo el divisor que sea comun para ambos numeros 
    while (valor=='false'):
        #prueba de divisor para comparar
        divisor +=1
        if ( nroA%divisor==0 and nroB%divisor==0 ) :
            nroA/=divisor
            nroB/=divisor
            #Se registrar valor en el MCD
            MCD.append(divisor)
        else: 
            #Si no hay divisores comunes sale del bucle
            valor = 'true'
## MCD de ambos numeros 
    for i in range(len(MCD)):
        mcd *=MCD[i]
    print("El maximo comun divisor es : ",mcd)
    return mcd
  

class TestCalculoDeMCM_MCD(unittest.TestCase):
    
    def test_calcular_MCD(self):
        esperado = 24
        nroa = 24
        nrob = 48
        self.assertEqual(calculo_MCD(nroa,nrob),esperado)
   
        


if __name__ == "_main_":
    unittest.main()