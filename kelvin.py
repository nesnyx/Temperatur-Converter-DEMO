# celcius
class Kelvin:
        
    # celcius to kelvin
    def get_k_c(self,c):
        return c + 273

    # celcius to fahrenheit
    def get_k_f(self,k):
        value = 9/5
        value2 = 273
        return (k - 273) * value + 32
    
 