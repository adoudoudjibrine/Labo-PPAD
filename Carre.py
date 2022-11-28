#Importation du module multiprossing 
from multiprocessing import Pool

#Declaration de la fonction Carre
def f(x):
    return x*x

#Appel de la fonction principal
if __name__ == '__main__' :
    with Pool(5) as p :
        print(p.map(f, [1,2,3,4,5]))



