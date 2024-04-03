def filter_data(data):
    """This function manually filters out keys and values based on elements that do not appear consistently"""
    filtered_data = {
        "Oferta od": data.get("Oferta od", ""),
        "Pokaż oferty z numerem VIN": data.get("Pokaż oferty z numerem VIN", ""),
        "Ma numer rejestracyjny": data.get("Ma numer rejestracyjny", ""),
        "Marka pojazdu": data.get("Marka pojazdu", ""),
        "Model pojazdu": data.get("Model pojazdu", ""),
        "Wersja": data.get("Wersja", ""),
        "Generacja": data.get("Generacja", ""),
        "Rok produkcji": data.get("Rok produkcji", ""),
        "Przebieg": data.get("Przebieg", ""),
        "Pojemność skokowa": data.get("Pojemność skokowa", ""),
        "Rodzaj paliwa": data.get("Rodzaj paliwa", ""),
        "Moc": data.get("Moc", ""),
        "Skrzynia biegów": data.get("Skrzynia biegów", ""),
        "Napęd": data.get("Napęd", ""),
        "Spalanie Poza Miastem": data.get("Spalanie Poza Miastem", ""),
        "Spalanie W Mieście": data.get("Spalanie W Mieście", ""),
        "Typ nadwozia": data.get("Typ nadwozia", ""),
        "Emisja CO2": data.get("Emisja CO2", ""),
        "Liczba drzwi": data.get("Liczba drzwi", ""),
        "Liczba miejsc": data.get("Liczba miejsc", ""),
        "Kolor": data.get("Kolor", ""),
        "Rodzaj koloru": data.get("Rodzaj koloru", ""),
        "Kraj pochodzenia": data.get("Kraj pochodzenia", ""),
        "Data pierwszej rejestracji w historii pojazdu": data.get("Data pierwszej rejestracji w historii pojazdu", ""),
        "Numer rejestracyjny pojazdu": data.get("Numer rejestracyjny pojazdu", ""),
        "Zarejestrowany w Polsce": data.get("Zarejestrowany w Polsce", ""),
        "Bezwypadkowy": data.get("Bezwypadkowy", ""),
        "Serwisowany w ASO": data.get("Serwisowany w ASO", ""),
        "Stan": data.get("Stan", "")
    }
    return filtered_data
