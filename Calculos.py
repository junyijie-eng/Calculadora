import doctest



>>> division(3,0)
ZeroDivisionError: division by zero
>>> division(8,4)
2
>>> raiz(25,2)
5

class Calculos:

    def suma(self,a, b):
        """
        >>> suma(1,2)
        3
        >>> suma(3,4)
        6

        :param a:
        :param b:
        :return:
        """
        return a + b
    def resta(self,a, b):
        return a - b
        """
        >>> resta(4,3)
        1
        >>> resta(9,4)
        5
        :param a: 
        :param b: 
        :return: 
        """
    def multiplicacion(self,a, b):
        return a * b
        """
        >>> multiplicacion(2,3)
        6
        >>> multiplicacion(3,4)
        12
        
        :param a: 
        :param b: 
        :return: 
        """
    def division(self,a, b:
        try:
            return a / b
        except ZeroDivisionError:
            return "division by zero"




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)