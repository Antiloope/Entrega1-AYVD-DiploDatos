# Si, existe una correlación lineal entre las columnas Salario Bruto y Neto. Se propone eliminar de la encuesta la columna de Salario Bruto para que la encuesta sea mas simple.
# Se utiliza el **coeficiente de Pearson** para determinar la correlación. Esté tiene un valor de **0,83** lo que indica una alta correlación positiva entre las columnas.

#  Crear subconjunto de df.
df_s = df[["salary_monthly_BRUTO","salary_monthly_NETO"]]
df_s.head()

# Eliminar Nan
df_s = df_s.dropna(how='all')

# Coeficiente de Pearson
df_s["salary_monthly_BRUTO"].corr(df_s["salary_monthly_NETO"])

# Esta correlación positiva entre las dos variables se puede apreciar también por medio del siguiente grafico:
max_age = 99
seaborn.pairplot(data=df[df.profile_age < max_age], y_vars=['salary_monthly_BRUTO'],
                 x_vars=['salary_monthly_NETO'],
                 aspect=3, height=4, dropna= True)
