from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', running=app.lights_running)

@app.route('/on')
def on():
    app.lights_running = True
    return redirect('/')

@app.route('/off')
def off():
    app.lights_running = False
    return redirect('/')

if __name__ == '__main__':
    app.lights_running = False
    app.run(host='0.0.0.0')