import pandas as pd

MODEL_PATH = "../models/modelo_Kmeans.joblib"




def get_features_num(dataframe):
    features_num = list(dataframe.columns[dataframe.dtypes != "object"])
    return features_num


def get_features_cat(dataframe):
    features_cat = (list(dataframe.select_dtypes(include = ['object']).columns))
    return features_cat

def card_tipo(df,umbral_categoria = 20, umbral_continua = 30):
    # Primera parte: Preparo el dataset con cardinalidades, % variación cardinalidad, y tipos
    df_temp = pd.DataFrame([(round(df.isnull().sum() * 100 / len(df), 2)), df.nunique(), df.nunique()/len(df) * 100, df.dtypes]) # Cardinaliad y porcentaje de variación de cardinalidad
    df_temp = df_temp.T # Como nos da los valores de las columnas en columnas, y quiero que estas sean filas, la traspongo
    df_temp = df_temp.rename(columns = {0: "Missing%", 1:"Card", 2: "%_Card", 3:"Tipo"}) 
    # Cambio el nombre de la transposición anterior para que tengan más sentido, y uso asignación en vez de inplace = True (esto es arbitrario para el tamaño de este dataset)

    # Corrección para cuando solo tengo un valor
    df_temp.loc[df_temp.Card == 1, "%_Card"] = 0.00

    # Creo la columna de sugerencia de tipo de variable, empiezo considerando todas categóricas pero podría haber empezado por cualquiera, siempre que adapte los filtros siguientes de forma correspondiente
    df_temp["tipo_sugerido"] = "Categorica"
    df_temp.loc[df_temp["Card"] == 2, "tipo_sugerido"] = "Binaria"
    df_temp.loc[df_temp["Card"] >= umbral_categoria, "tipo_sugerido"] = "Numerica discreta"
    df_temp.loc[df_temp["%_Card"] >= umbral_continua, "tipo_sugerido"] = "Numerica continua"

    return df_temp

def data_report(df):
    '''Esta funcion describe los campos de un dataframe de pandas de forma bastante clara, crack'''
    # Sacamos los NOMBRES
    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])

    # Sacamos los TIPOS
    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])

    # Sacamos los MISSINGS
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns=["MISSINGS (%)"])

    # Sacamos los VALORES UNICOS
    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])
    
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(percent_cardin.values, columns=["CARDIN (%)"])

    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)

    return concatenado.T


def education_level(education):
        ''''
        Función para clasificar la variable Education
        '''
        if education in ['2n Cycle', 'PhD', 'Master']:
            return 'High'
        elif education in ['Graduation']:
            return 'Medium'
        else:
            return 'Basic'
        
def family_status(row):
        ''''
        Función para clasificar según TotalSons y Marital_Status
        '''
        if row['TotalSons'] == 0 and row['Marital_Status'] in ['Absurd', 'Alone', 'Yolo', 'Single', 'Widow', 'Divorced']:
            return 'AloneNoKids'
        elif row['TotalSons'] == 0:
            return 'InPartneringNoKids' #DINK - Double Income No Kids
        elif row['Marital_Status'] in ['Absurd', 'Alone', 'Yolo', 'Single', 'Widow', 'Divorced']:
            return 'AloneWithKids' 
        else:
            return 'InPartneringWhitKids'

def preprocesado_df_marketing_campaign(df):
    
    #df_model=df.copy
    #Elimina duplicados si los hay

    #Elimina columnas
    df.drop(['ID', 'Z_CostContact', 'Z_Revenue'], axis=1, inplace=True)

    #Elimino valores de Income superiores a 15000
    df = df[df['Income'] < 150000 ].copy()
    df['Income'].fillna(df['Income'].median(), inplace=True) #relleno con la mediana si aparecen valores NaN

    # Crear características derivadas
    ##Age_group
    df['Age'] = 2015 - df['Year_Birth']
    cut_labels_Age = ['<35', '35-50', '50-65', '+65']
    cut_bins = [0, 35, 50, 65, 120]
    df['Age_group'] = pd.cut(df['Age'], bins=cut_bins, labels=cut_labels_Age)
    
    #Elimino valores de Age superiores a 100
    df = df[df['Age'] < 100 ].copy()


    ## Income_group
    cut_labels_Income = ['Low income', 'Low to medium income', 'Medium to high income', 'High income']
    df['Income_group'] = pd.qcut(df['Income'], q=4, labels=cut_labels_Income)

    ##TotalSons
    df['TotalSons'] = df['Kidhome'] + df['Teenhome']

    ## Education Level 
    df['Education_Level'] = df['Education'].apply(education_level)
    
    ## Family Status
    df['Family_Status'] = df.apply(family_status, axis=1)

    #Creacion Feature Total gastado sumando todos los gastos en los distintos productos
    df['Total_Spend']=df['MntWines']+df['MntFruits']+df['MntMeatProducts']+df['MntFishProducts']+df['MntSweetProducts']+df['MntGoldProds']
    
    #Creacion Feature que suma los resultados de todas las campañas realizadas
    df['Total_Campañas_Aceptadas']=df['AcceptedCmp1']+df['AcceptedCmp2']+df['AcceptedCmp3']+df['AcceptedCmp4']+df['AcceptedCmp5']+df['Response']

    #Creacion Feature suma de todas las compras realizadas en los distintos canales
    df['Total_Compras']=df['NumDealsPurchases']+df['NumWebPurchases']+df['NumStorePurchases']+df['NumCatalogPurchases']
    
    #Creacion Feature Madeia por compra
    df['MediaXcompra'] = df['Total_Spend'] / (df['Total_Compras']+1)

    
    return df