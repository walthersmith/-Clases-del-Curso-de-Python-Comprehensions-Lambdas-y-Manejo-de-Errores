  Curso de Python: Comprehensions, Lambdas y Manejo de Errores

  **[List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)**

  |element|for element in interable|if condition|
  |:---:|:---:|:---:|
  |Representa a cada uno delos elementos a poner en la nueva lista| ciclo a aprtir del cual se extraeran elementos de otra lista o cualquier iterable | Condicion opcional para filtrar los elementos del ciclo|


 **[Dictionary comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)**
 |key:value|for element in interable|if condition|
  |:---:|:---:|:---:|
  |Representa a cada una de las llaves y alores a poner en el nuevo diccionario| ciclo a aprtir del cual se extraeran elementos de otra lista o cualquier iterable | Condicion opcional para filtrar los elementos del ciclo|

  
  **[Lambda](https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions)**
  
Small anonymous functions can be created with the lambda keyword.
```python
  palindrome = lambda string: string == string[::-1]
  print(palindrome('ana'))
```
  
