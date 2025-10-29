# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python [conda env:base] *
#     language: python
#     name: conda-base-py
# ---

import sympy as sp
from IPython.display import Math

goldenRation = 1.618

A, B, w, x = sp.symbols('A, B, w, x')

# ---

# ##### Extended expression

goldenRationExp = (A + B) / A - goldenRation

display(Math(sp.latex(goldenRationExp)))

# ##### Short expression

goldenRationExpShort = w / x - goldenRation

display(Math(sp.latex(goldenRationExpShort)))


# ##### Functions

def calcGoldenRationX(whole: int) -> float:
    return round(next(iter(sp.solve(goldenRationExpShort.subs(w, whole), x))), 3)


def calcGoldenRationAB(whole: int) -> tuple[float, float]:
    aValue = calcGoldenRationX(whole)
    bValue = whole - aValue

    return aValue, bValue

# + active=""
# calcGoldenRationAB(1024)
