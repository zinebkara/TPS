#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Exercice 1 : Creating and Modifying Series
import pandas as pd

# Création de la série à partir du dictionnaire
exo1_series = pd.Series({'a': 100, 'b': 200, 'c': 300})
print(exo1_series)




# In[4]:


# Exercice 2 : Creating DataFrames
# Création du DataFrame
df_exo2 = pd.DataFrame({'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]})
print(df_exo2)

# Ajout de la colonne D
df_exo2['D'] = [10, 11, 12]
print(df_exo2)

# Suppression de la colonne B
df_exo2 = df_exo2.drop(columns=['B'])
print(df_exo2)



# In[5]:


# Exercice 3 : DataFrame Indexing and Selection
df_exo3 = pd.DataFrame({'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]})

# Sélection de la colonne B
colonneB = df_exo3['B']
print(colonneB)

# Sélection des colonnes A et C
colonnesAC = df_exo3[['A', 'C']]
print(colonnesAC)

# Sélection de la ligne d'index 1
row_1 = df_exo3.loc[1]
print(row_1)



# In[6]:


# Exercice 5 : Merging DataFrames
left = pd.DataFrame({'key': [1, 2, 3], 'A': ['A1', 'A2', 'A3'], 'B': ['B1', 'B2', 'B3']})
right = pd.DataFrame({'key': [1, 2, 3], 'C': ['C1', 'C2', 'C3'], 'D': ['D1', 'D2', 'D3']})

# Jointure externe avec ajout de la colonne E
right['E'] = ['E1', 'E2', 'E3']
merged = pd.merge(left, right, on='key', how='outer')
print(merged)



# In[7]:


# Exercice 6 : Data Cleaning
df_exo6 = pd.DataFrame({'A': [1.0, np.nan, 7.0], 'B': [np.nan, 5.0, 8.0], 'C': [3.0, 6.0, np.nan]})

# Remplacer NaN par 0
df_zero = df_exo6.fillna(0)
print(df_zero)

# Remplacer NaN par la moyenne de chaque colonne
df_filled_mean = df_exo6.fillna(df_exo6.mean())
print(df_filled_mean)

# Supprimer les lignes contenant des NaN
df_dropped = df_exo6.dropna()
print(df_dropped)



# In[8]:


# Exercice 7 : Grouping and Aggregation
df_exo7 = pd.DataFrame({'Category': ['A', 'B', 'A', 'B', 'A', 'B'], 'Value': [1, 2, 3, 4, 5, 6]})

# Moyenne par catégorie
grouped_mean = df_exo7.groupby('Category')['Value'].mean()
print(grouped_mean)

# Somme par catégorie
grouped_sum = df_exo7.groupby('Category')['Value'].sum()
print(grouped_sum)

# Comptage par catégorie
grouped_count = df_exo7.groupby('Category').size()
print(grouped_count)



# In[9]:


# Exercice 8 : Pivot Tables
df_exo8 = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Tableau croisé dynamique avec la somme
pivot_sum = df_exo8.pivot_table(values='Value', index='Category', columns='Type', aggfunc='sum', margins=True)
print(pivot_sum)



# In[10]:


# Exercice 9 : Time Series Data
date_rng = pd.date_range(start='2023-01-01', periods=6, freq='D')
df_time = pd.DataFrame({'Date': date_rng, 'Value': np.random.randint(1, 100, size=(6,))})
df_time.set_index('Date', inplace=True)

# Resampler par période de 2 jours (somme)
df_resampled = df_time.resample('2D').sum()
print(df_resampled)



# In[11]:


# Exercice 10 : Handling Missing Data
df_exo10 = pd.DataFrame({'A': [1.0, 2.0, np.nan], 'B': [np.nan, 5.0, 8.0], 'C': [3.0, np.nan, 9.0]})

# Interpolation
df_interpolated = df_exo10.interpolate()
print(df_interpolated)

# Suppression des lignes avec NaN
df_dropped = df_exo10.dropna()
print(df_dropped)



# In[12]:


# Exercice 11 : DataFrame Operations
df_exo11 = pd.DataFrame({'A': [1, 4, 7], 'B': [2, 5, 8], 'C': [3, 6, 9]})

# Cumul de la somme
df_cumsum = df_exo11.cumsum()
print(df_cumsum)

# Cumul du produit
df_cumprod = df_exo11.cumprod()
print(df_cumprod)

# Soustraction de 1 à chaque élément
df_subtracted = df_exo11.applymap(lambda x: x - 1)
print(df_subtracted)


# In[ ]:




