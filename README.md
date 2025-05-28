# 🌱 Django CRUD API - Hydroponic System

## 📌 Opis projektu
Ten projekt to aplikacja Django z REST API umożliwiająca zarządzanie systemami hydroponicznymi, czujnikami oraz ich pomiarami. Pozwala użytkownikom na rejestrację, autoryzację oraz operacje CRUD (Create, Read, Update, Delete) na danych.

---

## 🚀 Instalacja

1️⃣ **Klonowanie repozytorium**
```sh
git clone https://github.com/maksblink/coding_task_luna.git
cd django_crud
```

2️⃣ **Utworzenie i aktywacja środowiska wirtualnego**
```sh
python -m venv .venv
source .venv/bin/activate # macOS/Linux
source .venv\Scripts\activate # Windows
```

3️⃣ **Instalacja zależności**
```sh
pip install -r requirements.txt
```

4️⃣ **Migracje bazy danych**
```sh
python manage.py migrate
```

5️⃣ **Tworzenie użytkownika administratora** (opcjonalnie)
```sh
python manage.py createsuperuser
```

---

## 🛠 Uruchamianie aplikacji

```sh
python manage.py runserver
```
Aplikacja będzie dostępna pod adresem: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🐟 Populate DB i Random
Aby zasilić bazę danych przykładowymi danymi, 

---

## 🌀 Endpoints API

### 🔑 Autoryzacjamożna skorzystać z polecenia:
```sh
python populate_db
```
Następnie aby generować losowe dane od czujników, można skorzystać z polecenia:
```sh
python random_generator.py
```

---

## 🌀 Endpoints API

### 🔑 Autoryzacja
| Metoda | Endpoint | Opis | Autoryzacja |
|-|-|-|-|
| `POST` | `/api/register/` | Rejestracja użytkownika | Nie wymagana ❌ |
| `POST` | `/api/token/` | Pobranie tokenu autoryzacji | Nie wymagana ❌ |

📝 Rejestracja użytkownika (Metoda `POST`)
-
📩 Body (przykładowe):
```sh
{
    "username": "testuser77",
    "email": "test@example.com",
    "password": "securepassword123"
}
```

🔄 Odpowiedź (przykładowa):

```sh
{
    "token": "3da872696b0c61812328d0602867df7090811b06",
    "message": "Rejestracja zakończona sukcesem"
}
```
📝 Pobieranie tokenu
-
📩 Body (przykładowe):
```sh
{
    "username": "testuser77",
    "password": "securepassword123"
}
```

🔄 Odpowiedź (przykładowa):
```sh
{
    "token": "3da872696b0c61812328d0602867df7090811b06"
}
```

### 🌱 Systemy hydroponiczne
| Metoda | Endpoint | Opis | Autoryzacja |
|-|-|-|-|
| `GET` | `/api/hydroponic_system/` | Pobranie listy systemów hydroponicznych | Wymagana ✅ |
| `POST` | `/api/hydroponic_system/` | Dodanie nowego systemu hydroponicznego | Wymagana ✅ |
| `PUT` | `/api/hydroponic_system/<int>` |  Edycja systemu hydroponicznego | Wymagana ✅ |
| `PATCH` | `/api/hydroponic_system/<int>` | Częściowa aktualizacja systemu hydroponicznego | Wymagana ✅ |
| `DELETE` | `/api/hydroponic_system/<int>` | Usunięcie systemu hydroponicznego | Wymagana ✅ |

📝 Dodanie nowego systemu hydroponicznego
-
📩 Body (przykładowe):
```sh
{
  "name": "HydroSystem A",
  "description": "Opis A"
}
```
Pamiętaj o autoryzacji (token).

🔄 Odpowiedź (przykładowa):

```sh
{
    "id": 91,
    "name": "HydroSystem A",
    "description": "Opis A",
    "created_at": "2025-03-05T15:17:34.989539Z",
    "updated_at": "2025-03-05T15:17:34.989539Z",
    "sensors": [
        "sensor_type = pH, hydroponic_system = HydroSystem A",
        "sensor_type = temperature, hydroponic_system = HydroSystem A",
        "sensor_type = TDS, hydroponic_system = HydroSystem A"
    ]
}
```

📝 Edycja systemu hydroponicznego
-
📩 Body (przykładowe):
```sh
{
  "name": "HydroSystem A",
  "description": "Opis A"
}
```
Pamiętaj o autoryzacji (token).

🔄 Odpowiedź (przykładowa):

```sh
{
    "id": 91,
    "name": "HydroSystem A",
    "description": "Opis A",
    "created_at": "2025-03-05T15:17:34.989539Z",
    "updated_at": "2025-03-05T15:17:34.989539Z",
    "sensors": [
        "sensor_type = pH, hydroponic_system = HydroSystem A",
        "sensor_type = temperature, hydroponic_system = HydroSystem A",
        "sensor_type = TDS, hydroponic_system = HydroSystem A"
    ]
}
```

### 💽 Czujniki
| Metoda | Endpoint | Opis | Autoryzacja |
|-|-|-|------------|
| `GET`  | `/api/sensors/` | Pobranie listy czujników | Wymagana ✅ |
| `POST` | `/api/sensors/` | Dodanie nowego czujnika | Wymagana ✅ |

📝 Dodanie nowego czujnika
-
📩 Body (przykładowe):
```sh
{
    "sensor_type": "temperature",
    "hydroponic_system": 91
}
```
Pamiętaj o autoryzacji (token).

🔄 Odpowiedź (przykładowa):

```sh
{
    "id": 240,
    "hydroponic_system": 91,
    "sensor_type": "temperature",
    "measurements": []
}
```

### 📊 Pomiary
| Metoda | Endpoint | Opis | Autoryzacja |
|-|-|-|------------|
| `GET`  | `/api/measurements/` | Pobranie listy pomiarów | Wymagana ✅ |
| `POST` | `/api/measurements/` | Dodanie nowego pomiaru | Wymagana ✅ |

📝 Dodanie  nowego pomiaru
-
📩 Body (przykładowe):
```sh
{
    "sensor": 221,
    "value": 22.5,
    "timestamp": "2024-03-05T12:00:00Z"
}
```
Pamiętaj o autoryzacji (token).

🔄 Odpowiedź (przykładowa):

```sh
{
    "id": 15621,
    "sensor": 221,
    "value": 22.5,
    "timestamp": "2025-03-05T15:25:19.487315Z"
}
```

---

## 🛠 Technologie
✅ **Python 3.12**  
✅ **Django REST Framework**  
✅ **PostgreSQL**  

---

## 👨‍💻 Autorzy
👤 **Maksymilian Moskwytyn**

📧 **Email: moskwytyn.maksymilian@gmail.com**

🔗 **GitHub: https://github.com/maksblink/**

---

## 📚 Licencja
Projekt udostępniany na licencji MIT.
