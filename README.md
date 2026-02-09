# 🧠 AbuDhabi-LifeGuide-SmartCity

**AbuDhabi-LifeGuide** is an AI-powered platform designed to enhance the everyday life of Abu Dhabi residents by leveraging public **open data**, predictive analytics, and intelligent recommendations.

[![Django](https://img.shields.io/badge/Django-5.1.4-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌍 Purpose

The platform aims to bridge the gap between **open government data** and **citizen empowerment**. By making data digestible and actionable, AbuDhabi-LifeGuide supports smarter living, better planning, and more sustainable choices for residents, urban developers, and policymakers.

---

## 🚀 Features

- 📊 **Open Data Integration**  
  Pulls live and historical data from Abu Dhabi's open data portals (transport, health, education, safety, housing, etc.)

- 🧠 **AI-Powered Recommendations**  
  Uses machine learning models to suggest optimal residential areas based on user preferences and real-time data.

- 🗺️ **Interactive Smart Map**  
  View neighborhoods ranked by safety, air quality, affordability, education, and healthcare access.

- 📍 **Location Comparison Tool**  
  Compare two or more regions based on lifestyle KPIs.

- 📈 **Trend Forecasting**  
  See future predictions in traffic congestion, housing prices, or pollution levels using time-series modeling.

- 🔔 **Personalized Alerts**  
  Get updates about neighborhood developments, policy changes, or environmental warnings.

- 🕌 **Worship Places Finder**  
  Discover mosques and churches in the UAE with AI-powered recommendations.

- 🛍️ **Shopping & Tourism**  
  Get personalized recommendations for shopping destinations and tourist sites.

- 🎉 **Events & Entertainment**  
  Find cultural events and entertainment venues in Abu Dhabi.

- 🅿️ **Smart Parking**  
  Book parking spots using real-time availability data.

---

## 🏗️ System Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Frontend  │ ───> │    Django    │ ───> │   Azure     │
│  HTML/CSS/JS│      │   Backend    │      │  OpenAI API │
└─────────────┘      └──────────────┘      └─────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │  SQLite DB   │
                     │ (or Postgres)│
                     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │  Abu Dhabi   │
                     │  Open Data   │
                     └──────────────┘
```

---

## 🧰 Tech Stack

| Component          | Technology Used                  | Version |
|--------------------|----------------------------------|---------|
| 🖥 Frontend         | HTML, CSS, JavaScript, Leaflet.js | 1.9.4   |
| ⚙️ Backend          | Django, Django REST Framework     | 5.1.4   |
| 🧠 AI/ML            | Python, scikit-learn, pandas      | 1.5.2   |
| 🤖 AI Integration   | OpenAI (Azure)                   | 1.57.0  |
| 🌐 Data Ingestion   | REST APIs, CSV Parsers            | -       |
| 🗄️ Database         | SQLite (dev), PostgreSQL (prod)   | -       |
| 🚀 Web Server       | Gunicorn                          | 23.0.0  |

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Git

### 1. Clone the repository
```bash
git clone https://github.com/pamone74/AbuDhabi-LifeGuide-SmartCity.git
cd AbuDhabi-LifeGuide-SmartCity
```

### 2. Create and activate virtual environment
```bash
# On macOS/Linux
python -m venv env
source env/bin/activate

# On Windows
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys and configuration
# Required for Azure OpenAI features:
# AZURE_OPENAI_API_KEY=your_key_here
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
```

**Note:** The application will work without Azure OpenAI configured, but AI-powered recommendation features will not be available.

### 5. Run migrations
```bash
cd AbuDhabiLifeGuide
python manage.py migrate
```

### 6. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Collect static files
```bash
python manage.py collectstatic --noinput
```

### 8. Run the development server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the application.

---

## 🌐 Deployment

### Deploy to Azure Web Apps

1. **Procfile** is already configured for Gunicorn
2. Set environment variables in Azure Portal:
   - `SECRET_KEY`: Django secret key
   - `DEBUG`: Set to `False` for production
   - `ALLOWED_HOSTS`: Your Azure domain
   - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI key
   - `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint
3. Deploy using Git or GitHub Actions

### Environment Variables for Production
```
SECRET_KEY=your-long-random-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.azurewebsites.net
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
DATABASE_URL=postgres://user:pass@host/dbname  # Optional for PostgreSQL
```

---

## 🧪 Running Tests

```bash
cd AbuDhabiLifeGuide
python manage.py test
```

---

## 📖 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/api/parking-data/` | GET | Fetch parking data from Abu Dhabi Open Data |
| `/recommend-worship-church/` | POST | Get church recommendations |
| `/recommend-worship-mosque/` | POST | Get mosque recommendations |
| `/recommend-shopping-places/` | POST | Get shopping recommendations |
| `/recommend-tourist-sites/` | POST | Get tourist site recommendations |
| `/recommend-events/` | POST | Get event recommendations |
| `/booking/` | GET | View parking booking page |
| `/book_parking_spot/<id>/` | POST | Book a parking spot |

---

## 🔧 Troubleshooting

### Common Issues

#### 1. ModuleNotFoundError: No module named 'environ'
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

#### 2. Azure OpenAI API errors
**Solution:** Check your environment variables
- Verify `.env` file exists and contains correct values
- Ensure `AZURE_OPENAI_API_KEY` and `AZURE_OPENAI_ENDPOINT` are set
- Check API key permissions in Azure Portal

#### 3. Static files not loading
**Solution:** Collect static files
```bash
python manage.py collectstatic --noinput
```

#### 4. Database migration errors
**Solution:** Reset migrations
```bash
python manage.py migrate --run-syncdb
```

#### 5. Port already in use
**Solution:** Use a different port
```bash
python manage.py runserver 8001
```

---

## 📂 Project Structure

```
AbuDhabi-LifeGuide-SmartCity/
├── AbuDhabiLifeGuide/          # Main Django project
│   ├── AbuDhabiLifeGuide/      # Project settings
│   │   ├── settings.py         # Django settings
│   │   ├── urls.py             # Root URL configuration
│   │   └── wsgi.py             # WSGI configuration
│   ├── SmartRoute/             # Main application
│   │   ├── models.py           # Database models
│   │   ├── views.py            # View functions
│   │   ├── urls.py             # URL routing
│   │   └── templates/          # HTML templates
│   ├── static/                 # Static files (CSS, JS, images)
│   └── manage.py               # Django management script
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── Procfile                    # Gunicorn configuration for deployment
└── README.md                   # This file
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Patrick Amone** - [pamone74](https://github.com/pamone74)

---

## 🙏 Acknowledgments

- Abu Dhabi Open Data Portal
- Azure OpenAI Service
- Django Community
- OpenStreetMap Contributors

---

## 📞 Contact

For questions or support, please open an issue on GitHub or contact the maintainers.

---

## 🔐 Security

- **Never commit API keys or secrets** to the repository
- Use environment variables for sensitive configuration
- Keep dependencies up to date
- Report security vulnerabilities privately to the maintainers

---

**Made with ❤️ for Abu Dhabi residents**
