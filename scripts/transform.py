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

# moving total row to the end
df = df.append(df.iloc[0]).iloc[1:]
df = df.reset_index(drop=True)

# # creating a dictionary for the region names mapping
cyrillic_to_english = {
    'Абай': 'Abai Region',
    'Акмолинская': 'Akmolinskaya Region',
    'Актюбинская': 'Aktobe Region',
    'Алматинская': 'Almaty Region',
    'Атырауская': 'Atyrau Region',
    'Западно-Казахстанская': 'West Kazakhstan Region',
    'Жамбылская': 'Jambyl Region',
    'Жетісу': 'Jetisu Region',
    'Карагандинская': 'Karaganda Region',
    'Костанайская': 'Kostanay Region',
    'Кызылординская': 'Kyzylorda Region',
    'Мангистауская': 'Mangystau Region',
    'Северо-Казахстанская': 'North Kazakhstan Region',
    'Павлодарская': 'Pavlodar Region',
    'Туркестанская': 'Turkistan Region',
    'Ұлытау': 'Ulytau Region',
    'Восточно-Казахстанская': 'East Kazakhstan Region',
    'г. Астана': 'Astana',
    'г. Шымкент': 'Shymkent',
    'г. Алматы': 'Almaty',
    'Республика Казахстан': 'All regions'
}
df['Region'] = df['Region'].map(cyrillic_to_english)
df['Region'] = df['Region'].astype(str)

# # Saving the data
df.to_csv('../data/water.csv', index=False)