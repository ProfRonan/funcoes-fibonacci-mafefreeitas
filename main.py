    def fibonacci(n):
        if n < 0:
            raise ValueError("não existe fibonacci com n negativo!")
        if type(n) != int:
            raise ValueError("só serve com números inteiros")
        fibonacci =[0,1]
        if n ==0:
            return fibonacci[0]
        for i in range(2, n+1):
            fibonacci.append(fibonacci[-1]+ fibonacci[-2])
        return fibonacci.pop()
