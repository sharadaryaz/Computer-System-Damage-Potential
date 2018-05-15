#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 10:55:35 2018

@author: sharadsharad
"""
import pandas as pd
import numpy as ny                                                                        
import networkx as nx                                                                     
                                                                                          
import matplotlib.pyplot as plt                                                           
                                                                                          
df = pd.DataFrame({'from': ['D','A','B'], 'to' :['A','D','A']})                           
                                                                                          
                                                                                          
                                                                                          
df                                                                                        
G = nx.from_pandas_dataframe(df, 'from','to',create_using=nx.DiGraph())                   
nx.draw(G, with_labels = True, node_size=1500, alpha=0.3, arrows=True)                    
plt.title("Un-Directed")