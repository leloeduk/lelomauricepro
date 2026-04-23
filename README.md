# LeloMaurice - Portfolio Django

le lien du cahier de charge : https://docs.google.com/document/d/1xVARwAPwePw5rOB9-UnNwxImFUKPzf0f/edit?usp=drive_link&ouid=115566819801026079981&rtpof=true&sd=true

Un portfolio professionnel moderne construit avec Django 6, conçu pour présenter vos projets, compétences et services.

## 🚀 Fonctionnalités

- **Portfolio de projets** — Showcase de vos réalisations avec détails
- **Section compétences** — Affichage visuel de vos compétences techniques
- **Module de contact** — Formulaire de contact fonctionnel
- **Tableau de bord CRM** — Gestion des contacts et leads
- **Assistant IA** — Intégration d'un chatbot IA
- **Analytics** — Suivi des visiteurs et statistiques
- **API REST** — Endpoints API pour integrations externes

## 🛠️ Tech Stack

| Technologie | Version |
|-------------|---------|
| Python | 3.12+ |
| Django | 6.0.4 |
| Gunicorn | 25.3.0 |
| PostgreSQL | - |
| Docker | - |

### Dépendances principales

```
asgiref==3.11.1
Django==6.0.4
gunicorn==25.3.0
pillow==12.2.0
psycopg2-binary==2.9.11
whitenoise==6.12.0
```

## 📋 Prérequis

- Python 3.12 ou supérieur
- Docker et Docker Compose (optionnel)
- PostgreSQL (pour production)

## ⚡ Installation Locale

### 1. Cloner le projet

```bash
git clone <repo-url>
cd lelomaurice
```

### 2. Créer l'environnement virtuel

```bash
python -m venv venv
```

### 3. Activer l'environnement

**Windows :**
```powershell
.\venv\Scripts\Activate
```

**Linux/Mac :**
```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Configuration

Copiez le fichier `.env.example` en `.env` et configurez vos variables d'environnement :

```bash
cp .env.example .env
```

### 6. Appliquer les migrations

```bash
python manage.py migrate
```

### 7. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 8. Lancer le serveur

```bash
python manage.py runserver
```

Le site sera accessible à `http://127.0.0.1:8000`

## 🐳 Docker

### Build et lancement

```bash
docker-compose up --build
```

### Commandes utiles

```bash
# Arrêter les containers
docker-compose down

# Rebuild sans cache
docker-compose build --no-cache

# Logs en temps réel
docker-compose logs -f
```

## 📁 Structure du projet

```
lelomaurice/
├── apps/
│   ├── ai/          # Module chatbot IA
│   ├── analytics/   # Suivi et statistiques
│   ├── api/         # API REST
│   ├── contact/    # Formulaire de contact
│   ├── core/       # Pages principales
│   ├── crm/        # Gestion clients
│   ├── projects/   # Portfolio projets
│   └── skills/     # Compétences
├── config/         # Configuration Django
├── static/         # Fichiers statiques
├── templates/      # Templates HTML
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

## 🔧 Commandes Django

```bash
# Créer une app
python manage.py startapp <app_name>

# Appliquer migrations
python manage.py migrate

# Créer migrations
python manage.py makemigrations

# Collecter fichiers statiques
python manage.py collectstatic

# Shell Django
python manage.py shell
```

## 📄 Admin

Accédez à l'interface d'administration : `/admin`

## 🌐 Déploiement

### Variables d'environnement recommandées

| Variable | Description |
|----------|-------------|
| `DEBUG` | False en production |
| `ALLOWED_HOSTS` | Domaines autorisés |
| `SECRET_KEY` | Clé secrète Django |
| `DATABASE_URL` | URL de connexion BDD |

### Production avec Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## 📝 License

MIT License — Voir le fichier `LICENSE` pour plus de détails.

---

Developped by ❤️ par LeloMaurice