# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt
s=pd.Series(np.random.randn(10), index=np.arange(0,100,10))
s.plot()
plt.show()

