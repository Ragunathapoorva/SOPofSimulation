# SecureIoT Dashboard - Complete Installation & Deployment Guide

## Table of Contents
1. System Requirements
2. Installation Steps
3. Configuration
4. Running the Application
5. Backend Server Setup
6. Database Setup (Optional)
7. Docker Deployment
8. Troubleshooting
9. Performance Tuning

---

## 1. System Requirements

### Hardware Requirements
- **Minimum**:
  - CPU: 2-core processor
  - RAM: 2GB
  - Storage: 500MB free space
  
- **Recommended**:
  - CPU: 4-core processor
  - RAM: 8GB
  - Storage: 2GB free space

### Software Requirements
- **Operating System**: Windows, macOS, or Linux
- **Web Browser**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Python**: 3.8 or higher
- **Node.js**: 14+ (optional, for build tools)

### Network Requirements
- Stable internet connection (for initial setup)
- Ports: 8000 (frontend), 5000 (backend), 3000 (optional)

---

## 2. Installation Steps

### 2.1 Windows Installation

#### Step 1: Install Python
```bash
# Download Python 3.8+ from https://www.python.org/downloads/
# Run installer and ensure "Add Python to PATH" is checked
# Verify installation
python --version
pip --version
```

#### Step 2: Clone/Download Project
```bash
# Create project directory
mkdir SecureIoT-Dashboard
cd SecureIoT-Dashboard

# Copy all provided files to this directory
```

#### Step 3: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### Step 4: Install Dependencies
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install required packages
pip install flask flask-cors numpy

# Verify installations
pip list
```

#### Step 5: Verify Files
```bash
# Check that all files are present
dir

# Expected files:
# - index.html
# - app.js (original)
# - ml_backend.py
# - backend_server.py
# - README_GUIDE.md
```

---

### 2.2 macOS Installation

#### Step 1: Install Python
```bash
# Using Homebrew
brew install python@3.9

# Verify installation
python3 --version
pip3 --version
```

#### Step 2: Project Setup
```bash
# Create project directory
mkdir SecureIoT-Dashboard
cd SecureIoT-Dashboard

# Copy all project files here
```

#### Step 3: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### Step 4: Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install flask flask-cors numpy

# Verify
pip list
```

---

### 2.3 Linux Installation (Ubuntu/Debian)

#### Step 1: Install Python
```bash
# Update package manager
sudo apt update
sudo apt upgrade

# Install Python
sudo apt install python3.9 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

#### Step 2: Project Setup
```bash
# Create project directory
mkdir SecureIoT-Dashboard
cd SecureIoT-Dashboard

# Copy all project files
```

#### Step 3: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### Step 4: Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install flask flask-cors numpy

# Verify
pip list
```

---

## 3. Configuration

### 3.1 Frontend Configuration (Optional)

Edit the application constants in the web app for customization:

```javascript
// Application Configuration
const CONFIG = {
    API_BASE_URL: 'http://localhost:5000/api',
    AUTO_REFRESH_INTERVAL: 30 * 60 * 1000, // 30 minutes
    SIMULATION_DEFAULT_DURATION: 120, // 120 seconds
    DEVICE_SYNC_INTERVAL: 30000, // 30 seconds
    CHART_UPDATE_INTERVAL: 5000, // 5 seconds
    THEME: 'dark' // 'dark' or 'light'
};
```

### 3.2 Backend Configuration

Edit `backend_server.py` for customization:

```python
# Flask Configuration
FLASK_ENV = 'development'  # or 'production'
DEBUG = True  # Set to False for production
HOST = '0.0.0.0'
PORT = 5000

# Database Configuration (if using database)
DB_HOST = 'localhost'
DB_PORT = 27017
DB_NAME = 'secureiot'

# ML Model Configuration
ML_FGSM_EPSILON = 0.3
ML_PGD_ITERATIONS = 20
TRAINING_BATCH_SIZE = 32
```

### 3.3 Security Configuration

**Important**: For production deployment, change default credentials.

```python
# backend_server.py - Change default admin credentials
ADMIN_CREDENTIALS = {
    'admin': 'your_new_secure_password_here'
}

# Implement proper authentication:
# - Use bcrypt for password hashing
# - Implement JWT tokens
# - Use HTTPS only
# - Enable CORS selectively
```

---

## 4. Running the Application

### 4.1 Basic Setup (Frontend Only)

```bash
# Windows
cd C:\Path\To\SecureIoT-Dashboard
python -m http.server 8000

# macOS/Linux
cd /path/to/SecureIoT-Dashboard
python3 -m http.server 8000

# Open browser to: http://localhost:8000
```

### 4.2 Full Setup (Frontend + Backend)

#### Terminal 1: Run Backend Server
```bash
# Windows
venv\Scripts\activate
python backend_server.py

# macOS/Linux
source venv/bin/activate
python3 backend_server.py

# Expected output:
# ================================================== 
# SecureIoT Backend Server Starting...
# ==================================================
# API Documentation:
#   POST   /api/auth/login - Admin login
#   GET    /api/devices - Get all devices
#   ...
# ==================================================
# Running on http://0.0.0.0:5000
```

#### Terminal 2: Run Frontend Server
```bash
# Windows
python -m http.server 8000

# macOS/Linux
python3 -m http.server 8000

# Open browser to: http://localhost:8000
```

### 4.3 Login Credentials

```
Username: admin
Password: admin123
```

---

## 5. Backend Server Setup

### 5.1 Understanding the Backend

The backend provides REST API endpoints for:
- Authentication
- Device management
- Attack simulation
- ML model training
- Analytics and reporting

### 5.2 API Endpoints Reference

```
=== AUTHENTICATION ===
POST   /api/auth/login          - Login admin user
POST   /api/auth/logout         - Logout admin user

=== DEVICE MANAGEMENT ===
GET    /api/devices             - Get all devices
POST   /api/devices             - Add new device
PUT    /api/devices/<id>        - Update device
DELETE /api/devices/<id>        - Delete device
POST   /api/devices/refresh     - Refresh device status

=== ATTACK SIMULATION ===
POST   /api/attacks/fgsm        - Execute FGSM attack
POST   /api/attacks/pgd         - Execute PGD attack
POST   /api/simulate/attack     - Full attack simulation
GET    /api/simulations         - Get all simulations

=== ML TRAINING ===
POST   /api/train/fgsm          - Train FGSM model
POST   /api/train/pgd           - Train PGD model
GET    /api/models              - Get trained models
POST   /api/models/validate/<id> - Validate model

=== ANALYTICS ===
GET    /api/analytics/overview  - System analytics
GET    /api/history/refresh     - Refresh history

=== EXPORT ===
GET    /api/export/simulations  - Export simulations
GET    /api/export/devices      - Export devices

=== HEALTH ===
GET    /api/health              - Health check
```

### 5.3 Testing API Endpoints

Using curl:

```bash
# Test login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

# Get devices
curl http://localhost:5000/api/devices

# Add device
curl -X POST http://localhost:5000/api/devices \
  -H "Content-Type: application/json" \
  -d '{"name":"TestDevice","type":"Sensor","vulnerability_level":"medium"}'

# Run simulation
curl -X POST http://localhost:5000/api/simulate/attack \
  -H "Content-Type: application/json" \
  -d '{
    "attack_type":"FGSM Attack",
    "target_device":"Camera",
    "mitigation_strategy":"AI-Powered Detection",
    "duration_seconds":120
  }'
```

---

## 6. Database Setup (Optional)

### 6.1 MongoDB Setup

For persistent data storage, integrate MongoDB:

```bash
# Install MongoDB
# Windows: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
# macOS: brew install mongodb-community
# Linux: sudo apt install mongodb

# Start MongoDB
# Windows: mongod --config "C:\Program Files\MongoDB\Server\config.conf"
# macOS: brew services start mongodb-community
# Linux: sudo systemctl start mongod

# Verify MongoDB is running
mongo --version
```

### 6.2 Update Backend for MongoDB

```python
# In backend_server.py
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['secureiot']
devices_collection = db['devices']
simulations_collection = db['simulations']
```

---

## 7. Docker Deployment

### 7.1 Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000 8000

CMD ["python", "backend_server.py"]
```

### 7.2 Create requirements.txt

```
flask==2.3.0
flask-cors==4.0.0
numpy==1.24.0
werkzeug==2.3.0
```

### 7.3 Build and Run Docker

```bash
# Build image
docker build -t secureiot-dashboard .

# Run container
docker run -p 5000:5000 -p 8000:8000 secureiot-dashboard

# Using Docker Compose
docker-compose up
```

### 7.4 Docker Compose File

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: production
      DEBUG: false
    volumes:
      - ./logs:/app/logs

  frontend:
    image: nginx:alpine
    ports:
      - "8000:80"
    volumes:
      - ./index.html:/usr/share/nginx/html/index.html:ro
    depends_on:
      - backend
```

---

## 8. Troubleshooting

### Issue: "Port already in use"
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :5000
kill -9 <PID>
```

### Issue: "Module not found"
```bash
# Ensure virtual environment is activated
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Reinstall packages
pip install -r requirements.txt
```

### Issue: "Connection refused"
```bash
# Check if backend is running
curl http://localhost:5000/api/health

# Check firewall settings
# Windows: Check Windows Defender Firewall
# macOS/Linux: Check iptables/firewall
```

### Issue: "CORS error"
```bash
# Ensure backend has CORS enabled
# In backend_server.py:
from flask_cors import CORS
CORS(app)
```

### Issue: "ML training fails"
```bash
# Check numpy version
pip list | grep numpy

# Reinstall numpy
pip install --upgrade numpy

# Check available RAM
# Reduce training dataset size if insufficient memory
```

---

## 9. Performance Tuning

### 9.1 Frontend Optimization

```javascript
// Lazy load charts
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            initChart(entry.target);
            observer.unobserve(entry.target);
        }
    });
});

// Optimize DOM manipulation
const fragment = document.createDocumentFragment();
// Add elements to fragment
document.body.appendChild(fragment);
```

### 9.2 Backend Optimization

```python
# Use caching
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_operation():
    return compute_result()

# Use batch processing
def batch_process(items, batch_size=32):
    for i in range(0, len(items), batch_size):
        yield items[i:i+batch_size]
```

### 9.3 Database Optimization

```python
# Create indexes
db.devices.create_index('device_id')
db.simulations.create_index('timestamp')

# Use aggregation pipeline
pipeline = [
    {'$match': {'status': 'online'}},
    {'$group': {'_id': '$type', 'count': {'$sum': 1}}}
]
```

---

## 10. Production Deployment

### 10.1 Security Checklist
- [ ] Change default admin credentials
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall rules
- [ ] Implement rate limiting
- [ ] Enable audit logging
- [ ] Set up monitoring and alerts
- [ ] Configure backups
- [ ] Implement authentication/authorization
- [ ] Use environment variables for secrets
- [ ] Regular security updates

### 10.2 Recommended Production Stack

```
Frontend:
  - Nginx as reverse proxy
  - Let's Encrypt for SSL
  - CDN for static files
  - Web Application Firewall

Backend:
  - Gunicorn as WSGI server
  - Redis for caching
  - PostgreSQL for database
  - Elasticsearch for logging
  - Prometheus for monitoring

Infrastructure:
  - Docker containers
  - Kubernetes orchestration
  - AWS/GCP/Azure cloud platform
  - RDS for managed database
  - S3 for backup storage
```

### 10.3 Production Environment Variables

```bash
# .env file
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@host/db
REDIS_URL=redis://localhost:6379/0
LOG_LEVEL=INFO
ADMIN_PASSWORD=secure_password_hash
API_RATE_LIMIT=100/hour
CORS_ORIGINS=https://yourdomain.com
```

---

## 11. Monitoring & Maintenance

### 11.1 Health Checks

```bash
# Monitor backend health
curl -s http://localhost:5000/api/health | python -m json.tool

# Monitor device status
curl -s http://localhost:5000/api/devices | python -m json.tool
```

### 11.2 Logging

```python
# Configure logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info('Application started')
```

### 11.3 Backup Strategy

```bash
# Backup database
mongodump --db secureiot --out ./backups/

# Backup files
tar -czf backup-$(date +%Y%m%d).tar.gz /path/to/app/

# Schedule with cron (Linux/macOS)
# 0 2 * * * /path/to/backup.sh
```

---

## Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (Flask, NumPy)
- [ ] All project files copied to directory
- [ ] Backend server started (port 5000)
- [ ] Frontend server started (port 8000)
- [ ] Logged in with admin/admin123
- [ ] Created test devices
- [ ] Ran test attack simulation
- [ ] Reviewed simulation results
- [ ] Changed admin password (production)
- [ ] Configured backup strategy

---

**You're ready! Start exploring SecureIoT Dashboard now!**
