# SecureIoT Dashboard - Technical Architecture Document

## 1. System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Web Browser (Frontend)                  │  │
│  │  HTML5 | CSS3 | Vanilla JavaScript                  │  │
│  │  ┌─────────────────────────────────────────────┐    │  │
│  │  │  • Dashboard & Analytics                    │    │  │
│  │  │  • Device Management UI                     │    │  │
│  │  │  • Network Topology Visualization           │    │  │
│  │  │  • Attack Simulator UI                      │    │  │
│  │  │  • AI/ML Training Interface                 │    │  │
│  │  │  • Real-time Charts & Graphs                │    │  │
│  │  └─────────────────────────────────────────────┘    │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                  │
│                          │ HTTP/REST                        │
│                          ▼                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  API GATEWAY LAYER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Authentication & Authorization                      │  │
│  │  Request Validation                                 │  │
│  │  Rate Limiting & Throttling                         │  │
│  │  CORS & Security Headers                            │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Flask REST API Server                   │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Authentication Module                        │  │  │
│  │  │  Device Management Module                     │  │  │
│  │  │  Attack Simulation Module                     │  │  │
│  │  │  ML Training Module                           │  │  │
│  │  │  Analytics Module                             │  │  │
│  │  │  Export/Import Module                         │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    BUSINESS LOGIC LAYER                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  ML & AI Module (ml_backend.py)                      │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  FGSM Attack Simulator                        │  │  │
│  │  │  PGD Attack Simulator                         │  │  │
│  │  │  Adversarial Training Model                   │  │  │
│  │  │  Attack Flow Simulator                        │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │  Device Management Logic                           │  │
│  │  Security Analytics Engine                        │  │  │
│  │  Report Generation                                │  │  │
│  └──────────────────────────────────────────────────────┘  │
│                          │                                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      DATA LAYER                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  In-Memory Storage                                  │  │
│  │  ├── Devices Database                              │  │
│  │  ├── Simulations Log                               │  │
│  │  ├── Trained Models                                │  │
│  │  └── Refresh History                               │  │
│  │                                                    │  │
│  │  Optional: MongoDB/PostgreSQL Integration          │  │
│  │  Optional: Redis Caching                           │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Component Architecture

### 2.1 Frontend Components

```
index.html
├── Header/Navigation
│   ├── Sidebar Navigation
│   ├── User Profile
│   └── Logout Button
│
├── Page Components
│   ├── Login Page
│   ├── Dashboard
│   ├── Devices Management
│   ├── Network Topology
│   ├── Attacks Library
│   ├── Attack Simulator
│   ├── AI Training
│   ├── Mitigations
│   ├── Security Insights
│   ├── Refresh History
│   └── Admin Control Panel
│
├── Utility Components
│   ├── Charts & Graphs
│   ├── Data Tables
│   ├── Modal Dialogs
│   ├── Toast Notifications
│   └── Loading Indicators
│
└── JavaScript (app.js)
    ├── State Management
    ├── API Communication
    ├── Event Handling
    ├── DOM Manipulation
    └── Data Processing
```

### 2.2 Backend Components

```
backend_server.py (Flask Application)
├── Authentication Routes
│   ├── /api/auth/login
│   └── /api/auth/logout
│
├── Device Management Routes
│   ├── /api/devices (GET, POST)
│   ├── /api/devices/<id> (PUT, DELETE)
│   └── /api/devices/refresh
│
├── Attack Simulation Routes
│   ├── /api/attacks/fgsm
│   ├── /api/attacks/pgd
│   ├── /api/simulate/attack
│   └── /api/simulations (GET)
│
├── ML Training Routes
│   ├── /api/train/fgsm
│   ├── /api/train/pgd
│   ├── /api/models (GET)
│   └── /api/models/validate/<id>
│
├── Analytics Routes
│   ├── /api/analytics/overview
│   └── /api/history/refresh
│
└── Export Routes
    ├── /api/export/simulations
    └── /api/export/devices

ml_backend.py (Python Modules)
├── FGSMAttackSimulator
│   ├── __init__()
│   ├── generate_perturbation()
│   └── execute_attack()
│
├── PGDAttackSimulator
│   ├── __init__()
│   └── execute_attack()
│
├── AdversarialTrainingModel
│   ├── __init__()
│   ├── train_fgsm_robust_model()
│   ├── train_pgd_robust_model()
│   ├── validate_model()
│   └── get_model_summary()
│
└── AttackFlowSimulator
    ├── simulate_attack_flow()
    ├── _get_stage_description()
    └── _generate_recommendations()
```

---

## 3. Data Flow Diagrams

### 3.1 Attack Simulation Flow

```
User Interface
    │
    ├─ Select Attack Type
    ├─ Select Target Device
    ├─ Select Mitigation Strategy
    └─ Launch Simulation
         │
         ▼
    API Request (POST /api/simulate/attack)
         │
         ▼
    Flask Backend (Route Handler)
         │
         ▼
    AttackFlowSimulator.simulate_attack_flow()
         │
         ├─ Calculate Metrics
         │  ├─ Base Success Rate
         │  ├─ Mitigation Effectiveness
         │  ├─ Detection Time
         │  └─ Recovery Time
         │
         ├─ Generate Attack Stages
         │  ├─ Reconnaissance
         │  ├─ Exploitation
         │  ├─ Payload Delivery
         │  ├─ Detection
         │  └─ Recovery
         │
         └─ Return Results
              │
              ▼
         JSON Response (success_rate, detection_time, etc.)
              │
              ▼
         Update Frontend UI
              │
              ├─ Display Progress Bar
              ├─ Show Metrics
              ├─ Visualize Stages
              └─ Generate Report
```

### 3.2 ML Training Flow

```
User Configures Training
    ├─ Select Model Type (FGSM/PGD)
    ├─ Set Parameters (epsilon, epochs, etc.)
    └─ Submit Training Job
         │
         ▼
    API Request (POST /api/train/fgsm or /api/train/pgd)
         │
         ▼
    Flask Backend Instantiates Model
         │
         ▼
    AdversarialTrainingModel Class
         │
         ├─ For each Epoch:
         │  ├─ Generate Synthetic Data
         │  ├─ Create Adversarial Examples (FGSM/PGD)
         │  ├─ Calculate Loss & Accuracy
         │  └─ Log Epoch Results
         │
         ├─ Training Complete
         │  ├─ Store Model
         │  ├─ Generate Model ID
         │  └─ Save Training History
         │
         └─ Return Training Results
              │
              ▼
         JSON Response (epoch_logs, final_accuracy, etc.)
              │
              ▼
         Frontend Visualization
              ├─ Plot Loss Curve
              ├─ Plot Accuracy Curve
              └─ Show Training Progress
```

### 3.3 Device Management Flow

```
Admin Interface
    │
    ├─ View Devices
    ├─ Add Device
    ├─ Edit Device
    └─ Delete Device
         │
         ▼
    API Requests
         │
         ├─ GET /api/devices
         ├─ POST /api/devices
         ├─ PUT /api/devices/<id>
         └─ DELETE /api/devices/<id>
              │
              ▼
         Flask Backend Routes
              │
              ├─ Validate Input
              ├─ Update In-Memory Database
              ├─ Log Action
              ├─ Record Refresh Event
              └─ Return Response
                   │
                   ▼
              Update Frontend
                   │
                   ├─ Refresh Device List
                   ├─ Update Topology
                   ├─ Update Statistics
                   └─ Show Confirmation
```

---

## 4. Database Schema (In-Memory)

### 4.1 Devices Table

```python
{
    'device_id': 'DEV-ABC123',
    'name': 'Gateway-01',
    'type': 'Gateway',  # Gateway, Sensor, Camera, Actuator, Server, Router, Thermostat
    'status': 'online',  # online, offline, warning, critical
    'vulnerability_level': 'high',  # critical, high, medium, low
    'ip_address': '192.168.1.1',
    'mac_address': '00:11:22:33:44:55',
    'last_seen': '2025-11-10T14:30:00Z',
    'created_at': '2025-11-01T08:00:00Z',
    'updated_at': '2025-11-10T14:30:00Z',
    'metrics': {
        'cpu_usage': 45.2,
        'memory_usage': 62.1,
        'network_traffic': 1024,
        'threat_level': 'medium'
    }
}
```

### 4.2 Simulations Table

```python
{
    'simulation_id': 'SIM-ABC123',
    'timestamp': '2025-11-10T14:30:00Z',
    'attack_type': 'DDoS',
    'target_device': 'Server',
    'mitigation_strategy': 'AI-Powered Detection',
    'duration_seconds': 120,
    'attack_success': True,
    'success_rate': 42.5,
    'detection_time': 3.2,
    'false_positive_rate': 1.2,
    'recovery_time': 25.4,
    'security_score': 68.5,
    'stages': [
        {
            'stage': 'Reconnaissance',
            'duration': 24,
            'status': 'completed',
            'description': '...'
        },
        # ... more stages
    ],
    'recommendations': ['...', '...']
}
```

### 4.3 Trained Models Table

```python
{
    'model_id': 'MDL-ABC123',
    'model_name': 'IoT_Defense_V1',
    'type': 'FGSM',  # FGSM, PGD
    'created_at': '2025-11-10T10:00:00Z',
    'training_sessions': 1,
    'epochs': 50,
    'batch_size': 32,
    'dataset_size': 1000,
    'final_accuracy': 92.5,
    'validation_accuracy': 89.3,
    'epoch_logs': [
        {
            'epoch': 1,
            'clean_loss': 2.1,
            'adversarial_loss': 1.9,
            'clean_accuracy': 50.2,
            'adversarial_accuracy': 45.1,
            'robust_accuracy': 47.65
        },
        # ... more epochs
    ],
    'status': 'ready_for_deployment'
}
```

### 4.4 Refresh History Table

```python
{
    'refresh_id': 'REF-ABC123',
    'timestamp': '2025-11-10T14:30:00Z',
    'action': 'device_added',  # device_added, device_removed, device_updated, status_changed
    'device_id': 'DEV-XYZ789',
    'details': 'Added Gateway device',
    'devices_updated': 25,
    'online_devices': 22,
    'offline_devices': 3
}
```

---

## 5. API Contract Specifications

### 5.1 Authentication API

```
POST /api/auth/login
Request:
{
    "username": "admin",
    "password": "admin123"
}

Response (200):
{
    "success": true,
    "message": "Login successful",
    "token": "550e8400-e29b-41d4-a716-446655440000",
    "admin_name": "Administrator",
    "timestamp": "2025-11-10T14:30:00Z"
}

Response (401):
{
    "success": false,
    "message": "Invalid credentials"
}
```

### 5.2 Device Management API

```
GET /api/devices
Response (200):
{
    "success": true,
    "devices": [...],
    "total": 25,
    "timestamp": "2025-11-10T14:30:00Z"
}

POST /api/devices
Request:
{
    "name": "Sensor-05",
    "type": "Sensor",
    "vulnerability_level": "medium",
    "ip_address": "192.168.1.15"
}

Response (201):
{
    "success": true,
    "message": "Device added successfully",
    "device": {...}
}
```

### 5.3 Attack Simulation API

```
POST /api/simulate/attack
Request:
{
    "attack_type": "FGSM Attack",
    "target_device": "Camera",
    "mitigation_strategy": "AI-Powered Detection",
    "duration_seconds": 120
}

Response (200):
{
    "success": true,
    "simulation": {
        "simulation_id": "SIM-ABC123",
        "attack_success": true,
        "success_rate": 42.5,
        "detection_time": 3.2,
        "stages": [...],
        "recommendations": [...]
    }
}
```

### 5.4 ML Training API

```
POST /api/train/fgsm
Request:
{
    "model_name": "IoT_Defense_V2",
    "dataset_size": 2000,
    "epochs": 100,
    "batch_size": 32,
    "epsilon": 0.3
}

Response (200):
{
    "success": true,
    "message": "FGSM model training completed",
    "model_id": "MDL-XYZ789",
    "training_info": {
        "epochs": 100,
        "final_accuracy": 94.2
    }
}
```

---

## 6. Security Architecture

### 6.1 Authentication Flow

```
┌─────────────────────────────────────────────┐
│         Login Credentials                   │
│    username: admin, password: ***          │
└─────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│    Validate Credentials                    │
│    (Compare with secure hash)               │
└─────────────────────────────────────────────┘
           │
    ┌──────┴──────┐
    │             │
    ▼             ▼
 Valid      Invalid
    │             │
    ▼             ▼
Generate    Return 401
 Token      Unauthorized
    │
    ▼
┌─────────────────────────────────────────────┐
│    Store Session Token                      │
│    Set Session Timeout                      │
└─────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────┐
│    Return JWT Token to Client              │
│    Send to Frontend                        │
└─────────────────────────────────────────────┘
```

### 6.2 Authorization Checks

```
Request with Token
    │
    ▼
Extract Token from Header
    │
    ▼
Validate Token
    │
    ├─ Token Exists?
    ├─ Token Valid?
    ├─ Token Expired?
    └─ User Has Permission?
         │
    ┌────┴────────┐
    │             │
    ▼             ▼
 Allowed      Denied
    │             │
    ▼             ▼
Proceed      Return 403
Route        Forbidden
```

---

## 7. Performance Considerations

### 7.1 Optimization Strategies

| Aspect | Optimization |
|--------|--------------|
| **Frontend** | Lazy loading, virtual scrolling, CSS animations, debouncing |
| **Backend** | Caching, batch processing, async operations, indexing |
| **Database** | Connection pooling, query optimization, replication |
| **Network** | Compression, CDN, request batching, WebSocket for real-time |
| **Memory** | Garbage collection, memory pooling, efficient data structures |

### 7.2 Caching Strategy

```
L1: Browser Cache (Frontend)
    ├─ Static files (HTML, CSS, JS)
    ├─ Images and assets
    └─ Session data (IndexedDB)

L2: Server Cache (Backend)
    ├─ Query results (Redis)
    ├─ Computed metrics
    └─ Device status

L3: Database Cache
    ├─ Query caching
    ├─ Materialized views
    └─ Replication
```

---

## 8. Deployment Topology

### 8.1 Single Server Deployment

```
Internet
    │
    ▼
┌─────────────────────────────────┐
│    Reverse Proxy (Nginx)        │
│    ├─ SSL/TLS Termination       │
│    ├─ Load Balancing            │
│    └─ Static File Serving       │
└─────────────────────────────────┘
    │
    ├─────────────────────┬─────────────────────┐
    │                     │                     │
    ▼                     ▼                     ▼
┌─────────────┐  ┌──────────────────┐  ┌────────────┐
│  Frontend   │  │  Flask Backend   │  │  Database  │
│  (Port 80)  │  │  (Port 5000)     │  │ (MongoDB)  │
└─────────────┘  └──────────────────┘  └────────────┘
```

### 8.2 Distributed Deployment (Future)

```
Internet
    │
    ▼
┌──────────────────────────────────┐
│   Load Balancer                  │
│   (AWS ELB / Azure LB)           │
└──────────────────────────────────┘
    │
    ├─────────┬─────────┬─────────┐
    │         │         │         │
    ▼         ▼         ▼         ▼
┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
│ API │  │ API │  │ API │  │ API │
│ #1  │  │ #2  │  │ #3  │  │ #4  │
└─────┘  └─────┘  └─────┘  └─────┘
    │         │         │         │
    └─────────┼─────────┴─────────┘
              │
              ▼
    ┌─────────────────────────┐
    │  Database Cluster       │
    │  (MongoDB Replica Set)  │
    │  ┌─────┬─────┬─────┐   │
    │  │ #1  │ #2  │ #3  │   │
    │  └─────┴─────┴─────┘   │
    └─────────────────────────┘
```

---

## 9. Error Handling & Recovery

### 9.1 Error Codes

```
HTTP Status Codes:
  200 OK - Request successful
  201 Created - Resource created
  400 Bad Request - Invalid input
  401 Unauthorized - Authentication failed
  403 Forbidden - Authorization failed
  404 Not Found - Resource not found
  500 Internal Server Error - Server error
  503 Service Unavailable - Service down

Application Error Codes:
  ERR_AUTH_001 - Invalid credentials
  ERR_AUTH_002 - Session expired
  ERR_DEVICE_001 - Device not found
  ERR_SIM_001 - Simulation failed
  ERR_ML_001 - Training failed
  ERR_DB_001 - Database connection error
```

### 9.2 Recovery Strategies

```
Failure Scenario           Recovery Strategy
─────────────────────────  ───────────────────────────────
Backend Down               Retry logic, circuit breaker
Database Down              Fallback to in-memory cache
Network Timeout            Exponential backoff retry
Training Crash             Save checkpoint, resume
Data Corruption            Restore from backup
Session Timeout            Re-authenticate
Rate Limit Exceeded        Queue and retry later
Out of Memory              Garbage collection, scaling
```

---

## 10. Monitoring & Observability

### 10.1 Key Metrics

```
Application Metrics:
  ├─ Request latency (ms)
  ├─ Throughput (req/sec)
  ├─ Error rate (%)
  ├─ Active users
  └─ Model accuracy (%)

System Metrics:
  ├─ CPU usage (%)
  ├─ Memory usage (%)
  ├─ Disk usage (%)
  ├─ Network I/O (Mbps)
  └─ Connection count

Business Metrics:
  ├─ Total devices
  ├─ Active threats
  ├─ Attacks detected
  ├─ Mean time to detect (MTTD)
  └─ Mean time to recover (MTTR)
```

### 10.2 Logging Strategy

```
Log Levels:
  DEBUG   - Development information
  INFO    - General application events
  WARNING - Potential issues
  ERROR   - Error events
  CRITICAL - System-critical events

Log Destinations:
  ├─ File System (local.log)
  ├─ Centralized Logging (ELK Stack)
  ├─ Cloud Logging (CloudWatch, Stackdriver)
  └─ Real-time Alerts (Slack, PagerDuty)
```

---

This architecture document provides a comprehensive blueprint for the SecureIoT Dashboard system design, implementation, and deployment.
