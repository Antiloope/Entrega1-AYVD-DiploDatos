## a) Densidad conjunta
# Que herramientas visuales y modelos puede utilizar para estudiar la distribución y comportamiento de sus datos? 
# Elija tres variables numéricas y 2 variables categóricas. Visualice la base según varias de las variables elegidas. Puede describir de alguna forma el comportamiento de sus datos? Que herramientas utilizaría? Describa

import io
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_context('talk')
sns.set_style("ticks")

# Lectura del dataset

url = 'https://cs.famaf.unc.edu.ar/~mteruel/datasets/diplodatos/sysarmy_survey_2020_processed.csv'
df = pd.read_csv(url)

# Filtro valores extremos

selected_df = df.filter(items=["work_province","profile_age", "profile_years_experience", "work_role", "salary_monthly_BRUTO"])
selected_df = selected_df[selected_df['profile_age'] < 100]
selected_df = selected_df[selected_df['profile_age'] > 10]
selected_df = selected_df[selected_df['profile_years_experience'] < 70]
selected_df = selected_df[selected_df['salary_monthly_BRUTO'] < df.salary_monthly_BRUTO.quantile(0.98)]
selected_df = selected_df[selected_df['salary_monthly_BRUTO'] > df.salary_monthly_BRUTO.quantile(0.02)]

# Descripción de los datos

description = selected_df.groupby(by=['work_province']).mean().round(2).rename(columns={'profile_age': "age_mean",'profile_years_experience': "experience_mean",'salary_monthly_BRUTO': "salary_mean"})
description = description.sort_values(by='age_mean')
description

# Se puede ver que no cambia mucho el sueldo con la edad. El promeido es de 100K aprox y las edades rondan los 32 años.

sns.jointplot(data=selected_df, x="profile_age", y="salary_monthly_BRUTO", height=10)

# En todas las provincias el sueldo tiende a la suba y tienen un pico máximo entre los 30 y los 40 años

most_populated_provinces = ['Ciudad Autónoma de Buenos Aires', 'Provincia de Buenos Aires', 'GBA', 'Santa Fe', 'Córdoba', 'Mendoza']

selected_provinces_df = selected_df[selected_df['work_province'].isin(most_populated_provinces)]

g = seaborn.lmplot(x="profile_age", y="salary_monthly_BRUTO", col="work_province", data=selected_provinces_df, col_wrap=2, height=7)

