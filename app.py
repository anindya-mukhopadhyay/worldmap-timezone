from flask import Flask, render_template, jsonify
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML file

@app.route('/get_time/<float:lat>/<float:lon>', methods=['GET'])
def get_time(lat, lon):
    # Use TimezoneFinder to get the timezone based on lat/lon
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lng=lon, lat=lat)
    
    if timezone_str:
        local_timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(local_timezone)
        return jsonify({
            "time": local_time.strftime('%Y-%m-%d %H:%M:%S'),
            "timezone": timezone_str
        })
    else:
        return jsonify({"error": "No timezone found for this location"}), 404

if __name__ == '__main__':
    app.run(debug=True)
