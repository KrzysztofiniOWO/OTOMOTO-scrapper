import pandas as pd
from pymongo import MongoClient

# wpisujemy klienta

client = MongoClient(
    'mongodb+srv://molakrzysztof:<haslo>@cars.uwewuw1.mongodb.net/?retryWrites=true&w=majority&appName=Cars')
# nasza superancka baza
db = client['car_info']
collection = db["cars_info"]
# co za debil przechowuje te dane po polsku, czy ktos widzial zeby funkcje operowaly na polskich nazwach.
# anyway, tutaj cos co dobierze nam angielski odpowiednik
month_mapping = {
    'stycznia': 'January',
    'lutego': 'February',
    'marca': 'March',
    'kwietnia': 'April',
    'maja': 'May',
    'czerwca': 'June',
    'lipca': 'July',
    'sierpnia': 'August',
    'września': 'September',
    'października': 'October',
    'listopada': 'November',
    'grudnia': 'December'
}

# nasza kolekcja ładowana do pandasa
df = pd.DataFrame(list(collection.find()))

df['Pokaż oferty z numerem VIN'] = df['Pokaż oferty z numerem VIN'].map({'Tak': True, 'Nie': False})
df['Ma numer rejestracyjny'] = df['Ma numer rejestracyjny'].map({'Tak': True, 'Nie': False})
df['Serwisowany w ASO'] = df['Pokaż oferty z numerem VIN'].map({'Tak': True, 'Nie': False})
df['Marka pojazdu'] = df['Marka pojazdu'].astype('category')
df['Rok produkcji'] = df['Rok produkcji'].astype(int)
df['Przebieg'] = pd.to_numeric(df['Przebieg'].str.replace(' ', '').str.strip(' km'), errors='coerce')
df['Pojemność skokowa'] = pd.to_numeric(df['Pojemność skokowa'].str.replace(' ', '').str.strip(' cm3'), errors='coerce')
df['Rodzaj paliwa'] = df['Rodzaj paliwa'].astype('category')
df['Moc'] = df['Moc'].str.strip(' KM').astype(int)
df['Skrzynia biegów'] = df['Skrzynia biegów'].astype('category')
df['Spalanie Poza Miastem'] = pd.to_numeric(df['Spalanie Poza Miastem'].str.replace(' ', '').str.strip(' l/100km'),
                                            errors='coerce')
df['Spalanie W Mieście'] = pd.to_numeric(df['Spalanie W Mieście'].str.replace(' ', '').str.strip(' l/100km'),
                                         errors='coerce')
df['Typ nadwozia'] = df['Typ nadwozia'].astype('category')
df['Emisja CO2'] = pd.to_numeric(df['Emisja CO2'].str.replace(' ', '').str.strip(' g/km'), errors='coerce')
df['Liczba drzwi'] = pd.to_numeric(df['Liczba drzwi'], errors='coerce').astype('Int64')
df['Liczba miejsc'] = pd.to_numeric(df['Liczba miejsc'], errors='coerce').astype('Int64')

df['Data pierwszej rejestracji w historii pojazdu'] = df['Data pierwszej rejestracji w historii pojazdu'].str.replace(
    '.', '').str.split()
df['Data pierwszej rejestracji w historii pojazdu'] = df['Data pierwszej rejestracji w historii pojazdu'].apply(
    lambda x: ' '.join([month_mapping[elem] if elem in month_mapping else elem for elem in x]))
df['Data pierwszej rejestracji w historii pojazdu'] = pd.to_datetime(
    df['Data pierwszej rejestracji w historii pojazdu'])
# nawet nie pytajcie mi co tu sie wydarzylo
# po prostu to dziala

df['Zarejestrowany w Polsce'] = df['Zarejestrowany w Polsce'].map({'Tak': True, 'Nie': False})
df['Bezwypadkowy'] = df['Bezwypadkowy'].map({'Tak': True, 'Nie': False})
df['Serwisowany w ASO'] = df['Serwisowany w ASO'].map({'Tak': True, 'Nie': False})
df['Stan'] = df['Stan'].astype('category')
