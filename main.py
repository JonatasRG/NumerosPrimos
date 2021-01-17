class NumerosPrimos():

    def __init__(self):
        self.lista_de_primos = [2]

    def divisivel_pela_lista(self, numero):#, lista_divisores):

        resultado = True
        maior_divisor_possivel = numero

        for divisor in self.lista_de_primos:

            if divisor >= maior_divisor_possivel:
                break
            if (numero % divisor) == 0:
                resultado = False
                break
            else:
                maior_divisor_possivel = numero // divisor + 1

        return resultado

    def gera_lista_de_primos(self,numero):
        for testar in range(self.lista_de_primos[-1] + 1 , numero + 1):
            if self.divisivel_pela_lista(testar): #    , self.lista_de_primos ):
                self.lista_de_primos.append(testar)

    def verifica_se_e_primo(self,numero):
        if numero >= self.lista_de_primos[-1]:
            self.gera_lista_de_primos( numero)
        return numero in self.lista_de_primos

teste= NumerosPrimos()


if __name__ == '__main__':

    teste = NumerosPrimos()
    print(teste.lista_de_primos)
    teste.gera_lista_de_primos(40)

    print(teste.verifica_se_e_primo(311))
    print(teste.verifica_se_e_primo(391))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#teste