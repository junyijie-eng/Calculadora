import doctest

class Calculos:

    def suma(self,a, b):
        """
        >>> calculos(1,2)
        3
        >>> calculos(3,4)
        6

        :param a:
        :param b:
        :return:
        """
        return a + b
    def resta(self,a, b):
        """
        >>> calculos(4,3)
        1
        >>> calculos(9,4)
        5
        :param a:
        :param b:
        :return:
        """
        return a - b

    def multiplicacion(self,a, b):
        """
        >>> multiplicacion(2,3)
        6
        >>> multiplicacion(3,4)
        12

        :param a:
        :param b:
        :return:
        """
        return a * b

    def division(self,a, b):
        """
        >>> division(3,0)
        ZeroDivisionError: division by zero
        >>> division(8,4)
        2
        """
        try:
            return a / b
        except ZeroDivisionError:
            return "division by zero"




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)