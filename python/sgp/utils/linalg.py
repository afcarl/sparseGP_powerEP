import numpy as np
import scipy.linalg   as spla
from scipy.spatial.distance import cdist

def chol2inv(chol):
    return spla.cho_solve((chol, False), np.eye(chol.shape[ 0 ]))

def matrixInverse(M):
    return chol2inv(spla.cholesky(M, lower=False))