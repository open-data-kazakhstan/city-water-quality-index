import pandas as pd

# loading the excel sheet named '7.1' from source.xls
df = pd.read_excel('../archive/source.xls', sheet_name='7.1')

# cleaning and preparing the data
df = df.drop(df.index[0:3])
df.columns = ['Region', 'total', 'residential', 'communal_enterprises', 'industrial_enterprises', 'other_consumers']

# changeing all columns except region to numeric
df['total'] = pd.to_numeric(df['total'], errors='coerce')
df['residential'] = pd.to_numeric(df['residential'], errors='coerce')
df['communal_enterprises'] = pd.to_numeric(df['communal_enterprises'], errors='coerce')
df['industrial_enterprises'] = pd.to_numeric(df['industrial_enterprises'], errors='coerce')
df['other_consumers'] = pd.to_numeric(df['other_consumers'], errors='coerce')

# moving first row to the end of the dataframe
df = pd.concat([df.iloc[1:], df.iloc[:1]])

# # creating a dictionary for the region names mapping
cyrillic_to_english = {
     "Республика Казахстан": "The Republic of Kazakhstan",
    "Абай": "Abai Region",
    "Акмолинская": "Akmola Region",
    "Актюбинская": "Aktobe Region",
    "Алматинская": "Almaty Region",
    "Атырауская": "Atyrau Region",
    "Западно-Казахстанская": "West Kazakhstan Region",
    "Жамбылская": "Jambyl Region",
    "Жетісу": "Jetisu Region",
    "Карагандинская": "Karaganda Region",
    "Костанайская": "Kostanay Region",
    "Кызылординская": "Kyzylorda Region",
    "Мангистауская": "Mangystau Region",
    "Павлодарская": "Pavlodar Region",
    "Северо-Казахстанская": "North Kazakhstan Region",
    "Туркестанская": "Turkistan Region",
    "Ұлытау": "Ulytau Region",
    "Восточно-Казахстанская": "East Kazakhstan Region",
    "г. Астана": "Astana city",
    "г. Алматы": "Almaty city",
    "г. Шымкент": "Shymkent city"
}

df['Region'] = df['Region'].map(cyrillic_to_english)
df['Region'] = df['Region'].astype(str)

# # Saving the data
df.to_csv('../data/water.csv', index=False)