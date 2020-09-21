# This script uses the distributions package to demonstrate a few relationships between the normal, poisson, and binomial distributions.
import numpy as np
from distributions.draw import draw
from distributions.generator import NormalGen
from distributions.generator import PoissonGen
from distributions.generator import BinomialGen

# show that binomial distribution with large n approaches the normal distribution of mu = np, and sd = sqrt(np(1-p))
n = 1000
p = 0.3
b = BinomialGen(n=n, p=p)
sample = b.draw(10000)
print("demo 1 ----------------------------------")
print("mean of sample:               ",np.mean(sample))
print("normal approx of mean:        ",n*p)
print("standard deviation of sample: ",np.std(sample))
print("normal approx of sd:          ",np.sqrt(n*p*(1-p)))

# show that poisson distribution with large lambda approaches the normal distribution of mu = lambda, and sd = sqrt(lambda)
lam =100
p = PoissonGen(lam)
sample = p.draw(10000)
print("demo 2 ----------------------------------")
print("mean of sample:               ",np.mean(sample))
print("normal approx of mean:        ",lam)
print("standard deviation of sample: ",np.std(sample))
print("normal approx of sd:          ",np.sqrt(lam))

# show that poisson distribution with large lambda approaches the normal distribution of mu = lambda, and sd = sqrt(lambda)
# show that a binomial distribution with large n and small p approaches a poisson distribution of lambda = np
n = 1000
p = 0.02
b = BinomialGen(n,p)
sample = b.draw(10000)
print("demo 3 ----------------------------------")
print("mean of sample:               ",np.mean(sample))
print("poisson approx of mean:       ",n*p)
print("standard deviation of sample: ",np.std(sample))
print("square root of lambda:        ",np.sqrt(n*p))
