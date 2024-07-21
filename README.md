# Mateus_Javelin_Alpha_01_0

# Scrapper do Memów

## Cel projektu

Celem tego projektu jest stworzenie narzędzia do scrappowania memów z najpopularniejszej strony z memami, **JebzDzidy**, oraz wysyłania ich do określonej grupy ludzi przez Messengera. Projekt ma na celu automatyzację procesu zbierania i udostępniania memów, co może być przydatne dla osób zarządzających grupami lub fanpage'ami.

## Problemy napotkane podczas realizacji projektu

Podczas pracy nad projektem napotkałem kilka problemów, które wpływały na działanie aplikacji, zwłaszcza w środowisku Linuxowym:

1. **Problemy z przestrzenią dyskową na Linuxie**:
   Program generuje nadmierną ilość danych, co prowadzi do zajmowania całej przestrzeni dyskowej. Ten problem jest szczególnie zauważalny na systemach Linux, gdzie nieoptymalne zarządzanie plikami może szybko prowadzić do pełnego dysku.

2. **Błędne ścieżki katalogowe na Linuxie**:
   W kodzie pojawiły się problemy związane z niepoprawnymi ścieżkami katalogowymi, które działają poprawnie na Windowsie, ale powodują błędy na Linuxie. Różnice w systemach plików i separatorach ścieżek sprawiają, że kod wymaga dostosowania.

3. **Brak testowania w środowisku Linux**:
   Program został pierwotnie testowany tylko na systemie Windows, gdzie działał poprawnie.

## Jak uruchomić projekt

### Wymagania

- Python 3.x
- Biblioteki Python: `requests`, `beautifulsoup4`, `selenium` (zainstaluj za pomocą `pip install -r requirements.txt`) - Reszta będzie dopisana niedługo

### Instrukcja uruchamiania na Windowsie

1. Klonuj repozytorium:
   ```sh
   git clone https://github.com/Mateus_Javelin_Alpha_01_0
