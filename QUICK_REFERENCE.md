# SecureIoT Dashboard - Quick Reference Guide

## 🚀 60-Second Setup

```bash
# 1. Install Python (if not already installed)
# Download from https://www.python.org/downloads/

# 2. Create project folder
mkdir SecureIoT-Dashboard && cd SecureIoT-Dashboard

# 3. Copy all provided files to this folder

# 4. Create virtual environment
python -m venv venv

# 5. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 6. Install dependencies
pip install flask flask-cors numpy

# 7. Terminal 1: Start backend
python backend_server.py
# Should show: Running on http://0.0.0.0:5000

# 8. Terminal 2: Start frontend
python -m http.server 8000
# Should show: Serving HTTP on port 8000

# 9. Open browser: http://localhost:8000
# Login: admin / admin123
```

---

## 📁 File Structure

```
SecureIoT-Dashboard/
├── index.html              # Main web application
├── app.js                  # Frontend logic (original)
├── ml_backend.py           # ML/AI implementation
├── backend_server.py       # Flask REST API
├── README_GUIDE.md         # Complete user guide
├── INSTALLATION.md         # Installation instructions
├── ARCHITECTURE.md         # Technical architecture
├── PROJECT_SUMMARY.md      # Project overview
└── QUICK_REFERENCE.md      # This file
```

---

## 🔑 Default Credentials

```
Username: admin
Password: admin123
```

**⚠️ IMPORTANT**: Change password immediately in production!

---

## 🌐 URL Guide

| Component | URL | Port |
|-----------|-----|------|
| Frontend | http://localhost:8000 | 8000 |
| Backend API | http://localhost:5000 | 5000 |
| API Health | http://localhost:5000/api/health | 5000 |
| Devices API | http://localhost:5000/api/devices | 5000 |

---

## 📋 Dashboard Pages

| Page | Purpose | Key Features |
|------|---------|--------------|
| Dashboard | Overview | Stats, devices, threats, timeline |
| Devices | Management | Add, remove, edit, refresh, search |
| Topology | Network | Visual diagram, device status, connections |
| Attacks | Reference | Attack types, descriptions, success rates |
| Simulator | Testing | Run attacks, select targets, get results |
| AI Training | ML | Train FGSM/PGD, validate, download models |
| Mitigations | Defense | Strategy comparison, effectiveness %, techniques |
| Insights | Analytics | Trends, heatmap, recommendations, risks |
| History | Timeline | Refresh events, status changes, audit log |
| Admin | Control | Device management, settings, logs, export |

---

## 🎮 How to Run Your First Attack

1. **Login**: admin / admin123
2. **Go to Attack Simulator** (left sidebar)
3. **Select Attack Type**: e.g., "FGSM Attack"
4. **Select Target Device**: e.g., "Camera"
5. **Select Mitigation**: e.g., "AI-Powered Detection"
6. **Click "Launch Simulation"**
7. **Watch 2-minute simulation**
8. **Review results**: success rate, detection time, recommendations

---

## 🧠 How to Train ML Models

1. **Go to AI Training** (left sidebar)
2. **Choose Model Type**: FGSM or PGD
3. **Configure Parameters**:
   - Epsilon: 0.3 (default)
   - Epochs: 50 (default)
   - Dataset Size: 1000 (default)
4. **Click "Start Training"**
5. **Monitor Progress**: Watch loss/accuracy curves
6. **View Results**: Final accuracy, training time
7. **Download Model**: Save for later use

---

## 📊 Attack Types & Success Rates

```
CRITICAL Severity:
  • DDoS: 85% success rate
  • Man-in-the-Middle: 65%
  • Ransomware: 58%
  • Zero-Day Exploit: 42%
  • Firmware Injection: 51%

HIGH Severity:
  • Malware: 78%
  • FGSM Attack: 72%
  • PGD Attack: 78%
  • Botnet: 68%
  • SQL Injection: 68%

MEDIUM Severity:
  • Spoofing: 72%
  • Brute Force: 45%
```

---

## 🛡️ Mitigation Effectiveness

```
Effectiveness Levels:
  0%   → No Mitigation (baseline)
  35%  → Proactive Monitoring
  52%  → Network Segmentation
  68%  → Adversarial Training
  71%  → Zero Trust Architecture
  76%  → AI-Powered Detection ⭐ BEST
  84%  → Multi-Layered Defense
  92%  → Full Defense Suite (optimal)
```

**Recommendation**: Use "Multi-Layered Defense" for most scenarios (84% effective)

---

## 🔧 Common Commands

```bash
# Start Backend
python backend_server.py

# Start Frontend
python -m http.server 8000

# Test API Health
curl http://localhost:5000/api/health

# Get All Devices
curl http://localhost:5000/api/devices

# Add New Device
curl -X POST http://localhost:5000/api/devices \
  -H "Content-Type: application/json" \
  -d '{"name":"Sensor-1","type":"Sensor"}'

# Run Attack Simulation
curl -X POST http://localhost:5000/api/simulate/attack \
  -H "Content-Type: application/json" \
  -d '{"attack_type":"DDoS","target_device":"Server","mitigation_strategy":"AI-Powered Detection"}'
```

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version

# Verify dependencies
pip list | grep -E "flask|numpy"

# Check if port 5000 is free
netstat -ano | findstr :5000  # Windows
lsof -i :5000                 # macOS/Linux
```

### Frontend not loading
```bash
# Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
# Try incognito/private mode
# Check http://localhost:8000 in browser
```

### API connection error
```bash
# Test connection
curl http://localhost:5000/api/health

# Verify backend running on correct port
ps aux | grep backend_server.py  # macOS/Linux
tasklist | findstr python        # Windows
```

### Virtual environment issues
```bash
# Recreate venv
rmdir venv /s  # Windows
rm -rf venv    # macOS/Linux

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 📈 Key Metrics to Monitor

| Metric | Interpretation |
|--------|-----------------|
| **Attack Success Rate** | % of attacks that bypass defenses (lower is better) |
| **Detection Time** | Seconds to detect attack (lower is better) |
| **False Positive Rate** | % of normal activity flagged as threat (lower is better) |
| **Recovery Time** | Seconds to restore after attack (lower is better) |
| **Security Score** | Overall defense effectiveness 0-100 (higher is better) |

---

## ⚙️ Configuration Quick Tips

### Adjust Simulation Duration
```
Default: 120 seconds (2 minutes)
Can adjust: 1-300 seconds
Shorter: Faster results, less detail
Longer: More comprehensive simulation
```

### Change Refresh Interval
```
Device refresh: 30 minutes (configurable)
Dashboard update: 30 seconds
Chart update: 5 seconds
```

### Modify FGSM Parameters
```
Epsilon: 0.1-1.0 (default: 0.3)
  Lower: Smaller perturbations
  Higher: Larger perturbations
```

### Adjust PGD Settings
```
Iterations: 10-100 (default: 20)
Alpha: 0.001-0.1 (default: 0.01)
More iterations: Better attack quality
Larger alpha: Faster convergence
```

---

## 📱 Mobile Access

To access from mobile devices on same network:

```bash
# Find your machine IP
ipconfig  # Windows
ifconfig  # macOS/Linux

# Access from mobile
http://<YOUR_IP>:8000
```

---

## 🔐 Security Best Practices

✅ **Before Production**
- [ ] Change admin password
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall
- [ ] Set up logging
- [ ] Enable monitoring
- [ ] Create backups
- [ ] Test disaster recovery

✅ **Regular Maintenance**
- [ ] Update Python packages monthly
- [ ] Review security logs weekly
- [ ] Backup data daily
- [ ] Test API endpoints
- [ ] Monitor system performance

---

## 📚 Documentation Quick Links

| Document | Best For |
|----------|----------|
| README_GUIDE.md | Feature overview & user guide |
| INSTALLATION.md | Setup & deployment |
| ARCHITECTURE.md | Technical deep dive |
| PROJECT_SUMMARY.md | Project overview |
| QUICK_REFERENCE.md | This file - quick answers |

---

## 🎯 Getting Help

### Level 1: Self-Service
- Check README_GUIDE.md
- Review INSTALLATION.md
- Check browser console (F12)
- Review terminal output

### Level 2: Debugging
- Enable debug mode
- Check application logs
- Test API endpoints manually
- Review browser network tab

### Level 3: Advanced
- Review ARCHITECTURE.md
- Check backend logs
- Test database connection
- Verify system resources

---

## ⏱️ Performance Quick Start

| Operation | Typical Time |
|-----------|--------------|
| Login | <1 second |
| Load Dashboard | 1-2 seconds |
| Add Device | <1 second |
| Run 2-min Simulation | 2 minutes |
| Train Model (50 epochs) | 1-3 minutes |
| Export Data | <1 second |

---

## 🚀 Next Steps

1. **Complete Initial Setup** (5 minutes)
   - Install dependencies
   - Start backend & frontend
   - Login with default credentials

2. **Explore Dashboard** (5 minutes)
   - Review all pages
   - Add sample devices
   - Review attack library

3. **Run First Simulation** (5 minutes)
   - Select attack type
   - Choose target
   - Run simulation
   - Review results

4. **Train ML Model** (5 minutes)
   - Select FGSM training
   - Configure parameters
   - Start training
   - Monitor progress

5. **Customize** (ongoing)
   - Add real devices
   - Create custom attacks
   - Develop defenses
   - Integrate with systems

---

## 📞 Quick Support Checklist

Before contacting support, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] All files present
- [ ] Dependencies installed
- [ ] Backend running (port 5000)
- [ ] Frontend running (port 8000)
- [ ] Browser cache cleared
- [ ] No port conflicts
- [ ] Firewall allows connections
- [ ] Network connection active

---

## 💡 Pro Tips

🎯 **Tip 1**: Use "Multi-Layered Defense" (84% effective) as default mitigation strategy

🎯 **Tip 2**: FGSM attacks are faster (3.2s detection) than PGD (5.8s detection)

🎯 **Tip 3**: Server devices are most vulnerable (100+ success rate combined)

🎯 **Tip 4**: Run simulations with no mitigation first to understand baseline

🎯 **Tip 5**: Train models with larger datasets (2000+) for better accuracy

🎯 **Tip 6**: Export simulation results regularly for compliance

🎯 **Tip 7**: Check device refresh history for audit trail

🎯 **Tip 8**: Use topology view to identify critical devices

---

## 🎓 Learning Path

**Beginner** (1-2 hours)
1. Read this quick reference
2. Set up system
3. Login and explore
4. Run one simulation
5. Review results

**Intermediate** (2-4 hours)
1. Read README_GUIDE.md
2. Add multiple devices
3. Run multiple simulations
4. Compare results
5. Train ML model

**Advanced** (4+ hours)
1. Read ARCHITECTURE.md
2. Customize backend code
3. Integrate external data
4. Deploy to production
5. Set up monitoring

---

**You're ready to go! Happy securing! 🔐**

---

### Version
- **Quick Reference v1.0**
- **Last Updated**: November 10, 2025
- **Compatible With**: SecureIoT Dashboard v1.0+
