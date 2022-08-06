# celcius
class Celcius:
        
    # celcius to kelvin
    def get_c_k(self,k):
        return k - 273

    # celcius to fahrenheit
    def get_c_f(self,f):
        value = 5/9
        return (f - 32) * value
    
 