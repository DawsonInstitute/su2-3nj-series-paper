import sympy as sp
import numpy as np

def _build_K_symbolic(xs):
    """
    Build antisymmetric adjacency matrix K (4×4) for the 6-j example.
    xs: sequence of two sympy numbers [x1, x2].
    """
    x1, x2 = xs
    K = sp.zeros(4)
    K[0,1] = x1; K[1,0] = -x1
    K[1,2] = x2; K[2,1] = -x2
    K[2,3] = x1; K[3,2] = -x1
    return K

def _build_K_numeric(xs):
    """
    Build numeric adjacency matrix K (4×4) for the 6-j example.
    xs: sequence of two floats [x1, x2].
    """
    x1, x2 = xs
    K = np.zeros((4,4))
    K[0,1] = x1; K[1,0] = -x1
    K[1,2] = x2; K[2,1] = -x2
    K[2,3] = x1; K[3,2] = -x1
    return K

def G_exact(xs):
    """
    Exact (symbolic) evaluation of G({x_e}) = 1/√det(I – K).
    xs: list of two sympy.Rational or sympy objects.
    """
    K = _build_K_symbolic(xs)
    I = sp.eye(4)
    return 1/sp.sqrt((I - K).det())

def G_numeric(xs):
    """
    Numeric evaluation of G({x_e}).
    xs: list of two floats.
    """
    K = _build_K_numeric(xs)
    I = np.eye(4)
    return 1/np.sqrt(np.linalg.det(I - K))
