# Użyj oficjalnej wersji Pythona jako obrazu bazowego
FROM python:3.12-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki projektu do katalogu roboczego
COPY . .

# Zainstaluj zależności z requirements.txt
RUN pip install pytest

# Domyślne polecenie – uruchom testy
CMD ["pytest"]
