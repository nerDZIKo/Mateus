# Mateus_Javelin_Alpha_01_0

# Scrapper do Memów z JEBZDZIDY

## Cel projektu

Celem tego projektu jest stworzenie narzędzia do scrappowania memów z najpopularniejszej strony z memami, **JebzDzidy**, oraz wysyłania ich do określonej grupy ludzi przez Messengera. Projekt ma na celu automatyzację procesu zbierania i udostępniania memów, co może być przydatne dla osób zarządzających grupami lub fanpage'ami.

## Problemy napotkane podczas realizacji projektu

Podczas pracy nad projektem napotkałem kilka problemów, które wpływały na działanie aplikacji, zwłaszcza w środowisku Linuxowym:

1. **Problemy z przestrzenią dyskową na Linuxie**: Program w trakcie działania generuje nadmierną ilość danych, co prowadzi do zajmowania całej przestrzeni dyskowej. Problem ten może być związany z nieoptymalnym zarządzaniem danymi lub błędami w kodzie, które prowadzą do nadmiernego zapisywania plików.

2. **Błędne ścieżki katalogowe na Linuxie**: Napotkałem problemy związane z niepoprawnymi ścieżkami katalogowymi w środowisku Linux. Ścieżki, które działają na Windowsie, mogą nie działać poprawnie na Linuxie z powodu różnic w systemie plików i separatorach ścieżek.

3. **Brak testowania w środowisku Linux**: Projekt był testowany głównie na Windowsie, gdzie działał poprawnie. Dopiero po przeniesieniu na środowisko Linux pojawiły się problemy. Brak wcześniejszego testowania na Linuxie spowodował, że wiele problemów zostało zauważonych dopiero w późnym etapie rozwoju.


## Jak uruchomić projekt

### Wymagania

- Python 3.x
- Biblioteki Python: `requests`, `beautifulsoup4`, `selenium` (zainstaluj za pomocą `pip install -r requirements.txt`) - Reszta będzie dopisana niedługo

### Instrukcja uruchamiania na Windowsie

1. Klonuj repozytorium:
   ```sh
   git clone https://github.com/Mateus_Javelin_Alpha_01_0
