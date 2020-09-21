import numpy as np

class NormalGen():

    """A normal generator class

    An instance of the class represents a particluar normal distribution.
    The draw method takes a sample of a desired size from this distribution.
    """

    def __init__(self, mu, sd):
        if not isinstance(mu,(int,float)):
            raise TypeError("mu must be an int or a float!")
        if not isinstance(sd,(int,float)):
            raise TypeError("sd must be an int or a float!")
        self.mu = mu
        self.sd = sd
            
    # instance method to generate random numbers
    # prints out summary of numbers as default
    def draw(self, size=1, printSummary=False):

        values = np.random.normal(loc=self.mu, scale=self.sd, size=size)
        
        if printSummary:
            self.summarise(values)

        return values
    
    # class method to print out a summary of a set of random numbers
    # can be used from outside the class to summarise any set of numbers
    @classmethod
    def summarise(cls,values):
         print("Summary statistics:"+
              "\n  Count:   "+ str(len(values))+
              "\n  Max:     "+ str(max(values))+
              "\n  Min:     "+ str(min(values))+
              "\n  Mean:    "+ str(np.mean(values))+
              "\n  Std dev: "+ str(np.std(values)))


class PoissonGen():

    """A poisson generator class

    An instance of the class represents a particluar poisson distribution.
    The draw method takes a sample of a desired size from this distribution.
    """

    def __init__(self, lam):
        if not isinstance(lam,(int,float)):
            raise TypeError("lam must be an int or a float!")

        self.lam = lam
            
    # instance method to generate random numbers
    # prints out summary of numbers as default
    def draw(self, size=1, printSummary=False):

        values = np.random.poisson(lam=self.lam, size=size)
        
        if printSummary:
            self.summarise(values)

        return values
    
    # class method to print out a summary of a set of random numbers
    # can be used from outside the class to summarise any set of numbers
    @classmethod
    def summarise(cls, values):
        print("Summary statistics:"+
              "\n  Count:   "+ str(len(values))+
              "\n  Max:     "+ str(max(values))+
              "\n  Min:     "+ str(min(values))+
              "\n  Mean:    "+ str(np.mean(values))+
              "\n  Std dev: "+ str(np.std(values)))


class BinomialGen():

    """A binomial generator class

    An instance of the class represents a particluar binomial distribution.
    The draw method takes a sample of a desired size from this distribution.
    """

    def __init__(self, n, p):
        if not isinstance(n,int):
            raise TypeError("n must be an int!")
        if not isinstance(p,(int,float)):
            raise TypeError("p must be an int or float!")

        self.n = n
        self.p = p
            
    # instance method to generate random numbers
    # prints out summary of numbers as default
    def draw(self, size=1, printSummary=False):

        values = np.random.binomial(n=self.n, p=self.p, size=size)
        
        if printSummary:
            self.summarise(values)

        return values
    
    # class method to print out a summary of a set of random numbers
    # can be used from outside the class to summarise any set of numbers
    @classmethod
    def summarise(cls, values):
        print("Summary statistics:"+
              "\n  Count:   "+ str(len(values))+
              "\n  Max:     "+ str(max(values))+
              "\n  Min:     "+ str(min(values))+
              "\n  Mean:    "+ str(np.mean(values))+
              "\n  Std dev: "+ str(np.std(values)))