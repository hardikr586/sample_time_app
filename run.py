from flask import Flask
import time
app = Flask(__name__)


@app.route('/time')
def show_time():
 
	seconds = time.time()
	local_time = time.ctime(seconds)
	localtime = "Local time:"+ local_time
	return localtime

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
