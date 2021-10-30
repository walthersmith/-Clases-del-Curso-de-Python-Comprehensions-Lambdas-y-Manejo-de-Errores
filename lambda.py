#solo se pyuede tener una linea de codigo
#lambda es una funcion anonima que se puede pasar como parametro a otra funcion

if __name__ == '__main__':
    palindrome = lambda string: string == string[::-1]
    print(palindrome('ana'))