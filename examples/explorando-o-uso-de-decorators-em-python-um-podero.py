# Explorando o uso de Decorators em Python: um poderoso e elegante recurso que permite modificar o comportamento de funções e métodos. Este tópico incluirá a introdução à terminologia, o processo de criação e casos de uso específicos.

def decorator_example(function):
    def wrapper():
        print('Before function execution')
        function()
        print('After function execution')
    return wrapper


@decorator_example
def my_function():
    print('Executing my function')

my_function() # The output will be: Before function execution, Executing my function, After function execution