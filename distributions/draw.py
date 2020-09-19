import numpy as np

def draw(size, distribution, **params):

    """Draws random numbers from a distribution.

    Arguments:
        size (int): The number of samples to be drawn from the chosen distribution.
        distribution (str): The chosen distribution ("normal", "poisson", or "binomial").

    Returns:
        numpy.ndarray: Random samples from the chosen distribution.
    """
        
    # Check that distribution is supported
    if distribution not in ("normal", "poisson", "binomial"):
        raise ValueError("The distribution argument must be one of 'normal', 'poisson', or 'binomial'.")

    # Normal distribution        
    if(distribution == 'normal'):

        if 'mu' not in params.keys() or 'sd' not in params.keys():
            raise ValueError("The normal distribution must include the arguments 'mu' and 'sd'.")
        
        return np.random.normal(loc=params.get('mu'), scale=params.get('sd'), size=size)

    # Poisson distribution
    if(distribution == 'poisson'):

        if 'lam' not in params.keys():
            raise ValueError("The poisson distribution must include the argument 'lam'.")

        return np.random.poisson(lam=params.get('lam'), size=size)
    
    # Binomial distribution
    if(distribution == 'binomial'):
        
        if 'n' not in params.keys() or 'p' not in params.keys():
            raise ValueError("The binomial distribution must include the argument 'lam'.")

        return np.random.binomial(n=params.get('n'), p=params.get('p'), size=size)




