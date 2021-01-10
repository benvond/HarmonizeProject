from flask import Flask, render_template, redirect
import os, subprocess, signal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', running=app.lights_running)

@app.route('/on')
def on():
    if not lights_running:
        os.system('sudo python3 harmonize.py -v &')
    app.lights_running = True
    return redirect('/')

@app.route('/off')
def off():
    if lights_running:
        pid = subprocess.check_output('ps aux | grep "python3 harmonize.py -v" | grep -v grep | grep -v sudo | awk \'{print $2}\'', shell=True)
        os.kill(int(pid.decode('utf-8').rstrip('\n')), signal.SIGINT)
    app.lights_running = False
    return redirect('/')

if __name__ == '__main__':
    app.lights_running = False
    app.run(host='0.0.0.0')