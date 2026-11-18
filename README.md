# Real-Time Weather Web Application

A dynamic full-stack weather and Air Quality Index (AQI) lookup web application built with **Python**, **FastAPI**, **Jinja2**, **HTML**, and the **Requests** library. The application integrates with **WeatherAPI** to fetch real-time meteorological conditions and air quality metrics for user-submitted locations via multi-step HTML forms.

---

## Features

- **Real-Time Weather & AQI Lookup:** Fetches live temperature, weather conditions, humidity, wind speed, and Air Quality Index (AQI) data from WeatherAPI.
- **Multi-Step HTML Form Workflow:** Implements sequential form handling across `/login` and `/weather_data` routes to process user sessions and location queries.
- **Dynamic Server-Side Rendering:** Uses Jinja2 templates and HTML to render clean, location-specific weather dashboards.
- **External REST API Integration:** Uses the Python `requests` library to query external WeatherAPI endpoints and parse JSON meteorological payloads.

---

## Tech Stack

- **Backend Framework:** Python, FastAPI
- **Frontend & Templating:** HTML5, CSS, Jinja2 Templates
- **HTTP Client & External API:** Python `requests`, WeatherAPI
- **Server:** Uvicorn

---

## Project Structure

```text
weather_fastapi_application/
├── main.py                   # FastAPI application, WeatherAPI integration, and route handlers
├── templates/                # Jinja2 HTML templates for login, location input, and weather output
├── .gitignore                # Git ignore rules for virtual environments and cache files
└── README.md                 # Project documentation
```

---

## Web Routes

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` / `POST` | `/login` | Handles initial user login / entry form submission |
| `GET` / `POST` | `/weather_data` | Processes submitted city/location queries, calls WeatherAPI, and renders live weather & AQI results |

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/varshitha17041943/](https://github.com/varshitha17041943/)<your-weather-repo-name>.git
cd <your-weather-repo-name>
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn jinja2 requests python-multipart
```

### 4. Configure WeatherAPI Key
1. Sign up for a free API key at [WeatherAPI.com](https://www.weatherapi.com/).
2. Add your API key in `main.py` (or set it as an environment variable `WEATHER_API_KEY`):
   ```python
   API_KEY = "YOUR_WEATHER_API_KEY"
   ```

### 5. Run the Application
```bash
uvicorn main:app --reload
```

Open your browser and navigate to:
- **Web App:** `http://127.0.0.1:8000/login`
- **Swagger API Docs:** `http://127.0.0.1:8000/docs`

---

## Author

**Varshitha Reddy**  
- GitHub: [@varshitha17041943](https://github.com/varshitha17041943)  
- LinkedIn: [N Varshitha](https://www.linkedin.com/in/n-varshitha)
