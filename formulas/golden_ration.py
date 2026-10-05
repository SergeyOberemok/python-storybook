#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sympy as sp
from IPython.display import Math, display


# In[ ]:


golden_ration = 1.618


# In[25]:


A, B, w, x = sp.symbols('A, B, w, x')


# ---

# ##### Extended expression

# In[ ]:


golden_ration_exp = (A + B) / A - golden_ration


# In[ ]:


display(Math(sp.latex(golden_ration_exp)))


# ##### Short expression

# In[ ]:


golden_ration_exp_short = w / x - golden_ration


# In[ ]:


display(Math(sp.latex(golden_ration_exp_short)))


# ##### Functions

# In[ ]:


def calc_golden_ration_x(whole: int) -> float:
    return round(float(next(iter(sp.solve(golden_ration_exp_short.subs(w, whole), x)))), 3)


# In[ ]:


def calc_golden_ration_ab(whole: int) -> tuple[float, float]:
    a_value = calc_golden_ration_x(whole)
    b_value = whole - a_value

    return a_value, b_value


# calc_golden_ration_ab(1024)
