
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_ip_location(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    return {
        "ip": ip,
        "country": data.get("country"),
        "regionName": data.get("regionName"),
        "city": data.get("city"),
        "lat": data.get("lat"),
        "lon": data.get("lon")
    }

@app.route('/get_location', methods=['GET'])
def get_location():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "IP address is required"}), 400
   
    location = get_ip_location(ip)
    return jsonify(location)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
