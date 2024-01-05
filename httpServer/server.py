from flask import Flask
import socket

app = Flask(__name__)

@app.route('/root2/', methods=['GET'])
def hello_world(value):
    return "Hello, World!" + value

@app.route('/get/Ip')
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

@app.route('/data2/<string:name>/')
def hello(name):
    return "Hello " + name
@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 418

if __name__ == '__main__':
   app.run(host='0.0.0.0')