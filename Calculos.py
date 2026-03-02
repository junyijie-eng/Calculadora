import doctest
### https://www.pythonguis.com/installation/install-qt-designer-standalone/ ###
### pyside 6

class Calculos:

    def suma(self,a, b):
        """
        >>> c = Calculos()
        >>> c.suma(1, 2)
        3
        >>> c.suma(2, 4)
        6

        :param a:
        :param b:
        :return:
        """
        return a + b
    def resta(self,a, b):
        """
        >>> c = Calculos()
        >>> c.resta(4, 3)
        1
        >>> c.resta(9, 4)
        5
        """
        return a - b

    def multiplicacion(self,a, b):
        """
        >>> c = Calculos()
        >>> c.multiplicacion(2, 3)
        6
        >>> c.multiplicacion(3, 4)
        12
        """
        return a * b

    def division(self,a, b):
        """

        >>> c = Calculos()
        >>> c.division(8, 4)
        2.0
        >>> c.division(3, 0)
        'division by zero'
        """
        try:
            return a / b
        except ZeroDivisionError:
            return "division by zero"

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)