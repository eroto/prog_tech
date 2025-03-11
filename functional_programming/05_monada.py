#!/usr/bin/python3

#design pattern "Monada"

class MyFunctor:
    def __init__(self,value):
        self.value = value
    
    '''
    Type:   functor, high-order function
    Def:    map applies a function (func) to the value
            inside the Monad (self.value) map works with
            functions that return regular values and
            returns a new Monad with the result
    '''
    def map(self, func):
        return MyFunctor(func(self.value))
    
    def __repr__(self):
        return f"Functor({self.valye})"

#A Maybe monada
class MaybeMonad: 
    def __init__(self, value=None):
        self.value = value
    
    def is_empty(self): #return a bool. In python "is" function is a comparator
        return self.value is None
    
    def get(self):
        if self.is_empty():
            print("No value to return. get() return nothing")
        return self.value
        
    
    '''
    Applicative
    '''
    def apply(self,maybe_func):
        if self.is_empty() or maybe_func.is_empty():
            return MaybeMonad()
        else:
            return MaybeMonad(maybe_func.get()(self.value))
        
    '''
    Type: functor, high-order function
    Def: bind applies a function (func) that returns a Monad to the
    value inside the Monad, effectively chaining operations
    Usage: To chain multiple operations to function that returns a monad
    '''
    def bind(self, func):
        if self.is_empty():
            return self
        else:
            return func(self.value)
        
    
    '''
    Type:   functor, high-order function
    Def:    map applies a function (func) to the value
            inside the Monad (self.value) map works with
            functions that return regular values and
            returns a new Monad with the result
    '''
    def map(self, func):
        if self.is_empty():
            return self
        else:
            print(f"mapping {func} to self.value{self.value}")
            return MaybeMonad(func(self.value))
    
    def __repr__(self):
        return f'MaybeMonad({self.value})'


def suma(a):
    print(f"a:{a}")
    return a+37
    
def SafeDiv(a, b):
    return MaybeMonad(a/b) if b != 0 else MaybeMonad()

def mult(a,b):
    print(f"a:{a}")
    print (f"b:{b}")
    return MaybeMonad(a*b)            

if __name__ == "__main__":
    numero = MaybeMonad(5)

    print(f"numero = {numero}")
    print(f"numero.value = {numero.value}")
    resultado = numero.map(lambda x: x * 2)
    resultado1 = numero.map(suma)
    print(f"numero.map(lambda x: x * 2) = {resultado.get()}")
    print(f"numero.map(lambda x: suma(x,5))= {resultado1.get()}")
    result = MaybeMonad(100).bind(lambda x: SafeDiv(x,4)).bind(lambda x: mult(x,50))
    print(f"return of first monad.bind(): result {result}")
    result2 = MaybeMonad(40).bind(lambda x: mult(x,2))
    print(f"return of monad.bind(): resultado mult {result2.get()}")

    maybe_func = MaybeMonad(lambda x: x**3)
    maybe_value = MaybeMonad(45)
    result3 = maybe_value.apply(maybe_func)
    print(f"result3 = {result3}")
    print(f"maybe_func.get():{maybe_func}")
