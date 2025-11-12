# Flask REST API Server for SecureIoT Dashboard
# Run: python backend_server.py

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import numpy as np
from datetime import datetime
import json
from ml_backend import (
    FGSMAttackSimulator,
    PGDAttackSimulator,
    AdversarialTrainingModel,
    AttackFlowSimulator
)
import uuid

app = Flask(__name__)
CORS(app)

# In-memory data storage
trained_models = {}
simulations_log = []
devices_db = {}
refresh_history = []

# ============================================
# AUTHENTICATION ROUTES
# ============================================

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Authenticate admin user"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Simple authentication (hardcoded for demo)
    if username == 'admin' and password == 'admin123':
        session_token = str(uuid.uuid4())
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'token': session_token,
            'admin_name': 'Administrator',
            'timestamp': datetime.now().isoformat()
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid credentials'
        }), 401


@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """Logout admin user"""
    return jsonify({
        'success': True,
        'message': 'Logout successful'
    }), 200


# ============================================
# DEVICE MANAGEMENT ROUTES
# ============================================

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Get all devices"""
    devices_list = list(devices_db.values())
    return jsonify({
        'success': True,
        'devices': devices_list,
        'total': len(devices_list),
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/devices', methods=['POST'])
def add_device():
    """Add new device"""
    data = request.json
    device_id = f"DEV-{str(uuid.uuid4())[:8].upper()}"
    
    device = {
        'device_id': device_id,
        'name': data.get('name', f'Device-{device_id}'),
        'type': data.get('type', 'Sensor'),
        'status': 'online',
        'vulnerability_level': data.get('vulnerability_level', 'medium'),
        'ip_address': data.get('ip_address', f'192.168.1.{len(devices_db) + 1}'),
        'last_seen': datetime.now().isoformat(),
        'created_at': datetime.now().isoformat()
    }
    
    devices_db[device_id] = device
    
    # Log refresh event
    refresh_history.append({
        'timestamp': datetime.now().isoformat(),
        'action': 'device_added',
        'device_id': device_id,
        'details': f"Added {data.get('type')} device"
    })
    
    return jsonify({
        'success': True,
        'message': 'Device added successfully',
        'device': device
    }), 201


@app.route('/api/devices/<device_id>', methods=['DELETE'])
def remove_device(device_id):
    """Remove device"""
    if device_id in devices_db:
        removed_device = devices_db.pop(device_id)
        
        refresh_history.append({
            'timestamp': datetime.now().isoformat(),
            'action': 'device_removed',
            'device_id': device_id,
            'details': f"Removed {removed_device['type']} device"
        })
        
        return jsonify({
            'success': True,
            'message': 'Device removed successfully'
        }), 200
    
    return jsonify({
        'success': False,
        'message': 'Device not found'
    }), 404


@app.route('/api/devices/<device_id>', methods=['PUT'])
def update_device(device_id):
    """Update device"""
    data = request.json
    
    if device_id in devices_db:
        devices_db[device_id].update(data)
        devices_db[device_id]['last_seen'] = datetime.now().isoformat()
        
        return jsonify({
            'success': True,
            'message': 'Device updated successfully',
            'device': devices_db[device_id]
        }), 200
    
    return jsonify({
        'success': False,
        'message': 'Device not found'
    }), 404


@app.route('/api/devices/refresh', methods=['POST'])
def refresh_devices():
    """Refresh device status"""
    refresh_event = {
        'refresh_id': str(uuid.uuid4())[:8],
        'timestamp': datetime.now().isoformat(),
        'devices_updated': len(devices_db),
        'online_devices': sum(1 for d in devices_db.values() if d['status'] == 'online'),
        'offline_devices': sum(1 for d in devices_db.values() if d['status'] == 'offline')
    }
    
    refresh_history.append(refresh_event)
    
    return jsonify({
        'success': True,
        'message': 'Devices refreshed',
        'refresh_event': refresh_event
    }), 200


# ============================================
# ATTACK SIMULATION ROUTES
# ============================================

@app.route('/api/attacks/fgsm', methods=['POST'])
def execute_fgsm_attack():
    """Execute FGSM attack simulation"""
    data = request.json
    
    simulator = FGSMAttackSimulator(
        epsilon=data.get('epsilon', 0.3)
    )
    
    attack_result = simulator.execute_attack(
        np.random.randn(28, 28),
        data.get('target_label', 0)
    )
    
    simulations_log.append(attack_result)
    
    return jsonify({
        'success': True,
        'attack_type': 'FGSM',
        'result': attack_result
    }), 200


@app.route('/api/attacks/pgd', methods=['POST'])
def execute_pgd_attack():
    """Execute PGD attack simulation"""
    data = request.json
    
    simulator = PGDAttackSimulator(
        epsilon=data.get('epsilon', 0.3),
        alpha=data.get('alpha', 0.01),
        iterations=data.get('iterations', 20)
    )
    
    attack_result = simulator.execute_attack(
        np.random.randn(28, 28),
        data.get('target_label', 0)
    )
    
    # Remove iteration logs from response (too large)
    attack_result.pop('iteration_logs', None)
    simulations_log.append(attack_result)
    
    return jsonify({
        'success': True,
        'attack_type': 'PGD',
        'result': attack_result
    }), 200


@app.route('/api/simulate/attack', methods=['POST'])
def simulate_full_attack():
    """Simulate complete attack flow"""
    data = request.json
    
    flow_simulator = AttackFlowSimulator()
    
    simulation_result = flow_simulator.simulate_attack_flow(
        attack_type=data.get('attack_type', 'DDoS'),
        target_device=data.get('target_device', 'Server'),
        mitigation_strategy=data.get('mitigation_strategy', 'AI-Powered Detection'),
        duration_seconds=data.get('duration_seconds', 120)
    )
    
    simulations_log.append(simulation_result)
    
    return jsonify({
        'success': True,
        'simulation': simulation_result
    }), 200


@app.route('/api/simulations', methods=['GET'])
def get_simulations():
    """Get all attack simulations"""
    return jsonify({
        'success': True,
        'simulations': simulations_log,
        'total': len(simulations_log),
        'timestamp': datetime.now().isoformat()
    }), 200


# ============================================
# ML TRAINING ROUTES
# ============================================

@app.route('/api/train/fgsm', methods=['POST'])
def train_fgsm_model():
    """Train FGSM adversarial robust model"""
    data = request.json
    
    model_name = data.get('model_name', 'FGSM_Model_Auto')
    model = AdversarialTrainingModel(model_name)
    
    training_result = model.train_fgsm_robust_model(
        dataset_size=data.get('dataset_size', 1000),
        epochs=data.get('epochs', 50),
        batch_size=data.get('batch_size', 32),
        epsilon=data.get('epsilon', 0.3)
    )
    
    # Store model
    model_id = training_result['model_id']
    trained_models[model_id] = {
        'model': model,
        'training_result': training_result,
        'type': 'FGSM'
    }
    
    return jsonify({
        'success': True,
        'message': 'FGSM model training completed',
        'model_id': model_id,
        'training_info': {
            'epochs': training_result['epochs'],
            'final_accuracy': training_result['epoch_logs'][-1]['robust_accuracy'] if training_result['epoch_logs'] else 0
        }
    }), 200


@app.route('/api/train/pgd', methods=['POST'])
def train_pgd_model():
    """Train PGD adversarial robust model"""
    data = request.json
    
    model_name = data.get('model_name', 'PGD_Model_Auto')
    model = AdversarialTrainingModel(model_name)
    
    training_result = model.train_pgd_robust_model(
        dataset_size=data.get('dataset_size', 1000),
        epochs=data.get('epochs', 50),
        batch_size=data.get('batch_size', 32),
        epsilon=data.get('epsilon', 0.3),
        pgd_iterations=data.get('pgd_iterations', 20)
    )
    
    # Store model
    model_id = training_result['model_id']
    trained_models[model_id] = {
        'model': model,
        'training_result': training_result,
        'type': 'PGD'
    }
    
    return jsonify({
        'success': True,
        'message': 'PGD model training completed',
        'model_id': model_id,
        'training_info': {
            'epochs': training_result['epochs'],
            'final_accuracy': training_result['epoch_logs'][-1]['robust_accuracy'] if training_result['epoch_logs'] else 0
        }
    }), 200


@app.route('/api/models/validate/<model_id>', methods=['POST'])
def validate_model(model_id):
    """Validate trained model"""
    data = request.json
    
    if model_id not in trained_models:
        return jsonify({
            'success': False,
            'message': 'Model not found'
        }), 404
    
    model_obj = trained_models[model_id]['model']
    validation_result = model_obj.validate_model(
        test_dataset_size=data.get('test_dataset_size', 500)
    )
    
    return jsonify({
        'success': True,
        'model_id': model_id,
        'validation': validation_result
    }), 200


@app.route('/api/models', methods=['GET'])
def get_trained_models():
    """Get all trained models"""
    models_list = []
    
    for model_id, model_info in trained_models.items():
        model = model_info['model']
        summary = model.get_model_summary()
        models_list.append({
            'model_id': model_id,
            'name': summary['model_name'],
            'type': model_info['type'],
            'created_at': summary['created_at'],
            'training_sessions': summary['training_sessions'],
            'latest_accuracy': summary['latest_accuracy']
        })
    
    return jsonify({
        'success': True,
        'models': models_list,
        'total': len(models_list)
    }), 200


# ============================================
# ANALYTICS & INSIGHTS ROUTES
# ============================================

@app.route('/api/analytics/overview', methods=['GET'])
def get_analytics_overview():
    """Get system analytics overview"""
    online_devices = sum(1 for d in devices_db.values() if d['status'] == 'online')
    critical_vulnerabilities = sum(1 for d in devices_db.values() if d['vulnerability_level'] == 'critical')
    
    return jsonify({
        'success': True,
        'analytics': {
            'total_devices': len(devices_db),
            'online_devices': online_devices,
            'offline_devices': len(devices_db) - online_devices,
            'critical_vulnerabilities': critical_vulnerabilities,
            'total_simulations': len(simulations_log),
            'total_models_trained': len(trained_models),
            'attack_success_rate': np.mean([s.get('success_rate', 0) for s in simulations_log]) if simulations_log else 0,
            'average_detection_time': np.mean([s.get('detection_time', 0) for s in simulations_log]) if simulations_log else 0
        }
    }), 200


@app.route('/api/history/refresh', methods=['GET'])
def get_refresh_history():
    """Get device refresh history"""
    limit = request.args.get('limit', 50, type=int)
    
    return jsonify({
        'success': True,
        'refresh_history': refresh_history[-limit:],
        'total': len(refresh_history)
    }), 200


# ============================================
# EXPORT ROUTES
# ============================================

@app.route('/api/export/simulations', methods=['GET'])
def export_simulations():
    """Export simulations as JSON"""
    format_type = request.args.get('format', 'json')
    
    if format_type == 'json':
        return jsonify({
            'success': True,
            'data': simulations_log,
            'exported_at': datetime.now().isoformat()
        }), 200
    
    return jsonify({
        'success': False,
        'message': 'Unsupported format'
    }), 400


@app.route('/api/export/devices', methods=['GET'])
def export_devices():
    """Export devices as JSON"""
    return jsonify({
        'success': True,
        'data': list(devices_db.values()),
        'exported_at': datetime.now().isoformat()
    }), 200


# ============================================
# HEALTH CHECK
# ============================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'devices': len(devices_db),
        'models': len(trained_models),
        'simulations': len(simulations_log)
    }), 200


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'Resource not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'message': 'Internal server error'
    }), 500


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    # Initialize with sample devices
    sample_devices = [
        {'name': 'Gateway-01', 'type': 'Gateway', 'vulnerability_level': 'high'},
        {'name': 'Sensor-01', 'type': 'Sensor', 'vulnerability_level': 'medium'},
        {'name': 'Camera-01', 'type': 'Camera', 'vulnerability_level': 'high'},
        {'name': 'Server-01', 'type': 'Server', 'vulnerability_level': 'critical'},
    ]
    
    for device_data in sample_devices:
        device_id = f"DEV-{str(uuid.uuid4())[:8].upper()}"
        device = {
            'device_id': device_id,
            'name': device_data['name'],
            'type': device_data['type'],
            'status': 'online',
            'vulnerability_level': device_data['vulnerability_level'],
            'ip_address': f'192.168.1.{len(devices_db) + 1}',
            'last_seen': datetime.now().isoformat(),
            'created_at': datetime.now().isoformat()
        }
        devices_db[device_id] = device
    
    print("=" * 50)
    print("SecureIoT Backend Server Starting...")
    print("=" * 50)
    print("API Documentation:")
    print("  POST   /api/auth/login - Admin login")
    print("  GET    /api/devices - Get all devices")
    print("  POST   /api/devices - Add device")
    print("  POST   /api/simulate/attack - Run attack simulation")
    print("  POST   /api/train/fgsm - Train FGSM model")
    print("  POST   /api/train/pgd - Train PGD model")
    print("  GET    /api/models - Get trained models")
    print("  GET    /api/health - Health check")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
