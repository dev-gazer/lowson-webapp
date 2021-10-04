from io import StringIO, BytesIO
from flask import Flask, request, render_template, make_response
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from functions import Lowson
import base64
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html', image='/static/placeholder.png', c="0.15", s="0.498", U="60", I="0.04", Lambda="0.009", r_e="1.2", alpha="0", phi="90", theta="90")

@app.route('/', methods=['POST'])
def my_form_post():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    f_vec = np.array([10, 12.5, 16, 20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000, 20000])
    A_filter = np.array([-70.4, -63.4, -56.7, -50.5, -44.7, -39.4, -34.6, -30.2, -26.2, -22.5, -19.1, -16.1, -13.4, -10.9, -8.6, -6.6, -4.8, -3.2, -1.9, -0.8, 0, 0.6, 1, 1.2, 1.3, 1.2, 1, 0.5, -0.1, -1.1, -2.5, -4.3, -6.6, -9.3])
    c = float(request.form['c'])
    s = float(request.form['s'])
    U = float(request.form['U'])
    I = float(request.form['I'])
    Lambda = float(request.form['Lambda'])
    alpha = float(request.form['alpha'])
    phi = float(request.form['phi'])
    theta = float(request.form['theta'])
    r_e = float(request.form['r_e'])
    SPL = Lowson(f_vec, c, s, alpha, U, I, Lambda, r_e, phi, theta)
    SPL_A = SPL + A_filter
    axis.plot(f_vec, SPL_A)
    axis.set_title('Lowson Method')
    axis.set_xscale('log')
    axis.set_xlabel('Frequency [Hz]')
    axis.set_ylabel('SPL [dBA]')
    axis.grid(linestyle='--', which='both', axis='both', linewidth=0.5)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    buf = BytesIO()
    fig.savefig(buf, format="png")
    #fig.savefig('/static/placeholder.png')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template('index.html', image=f'data:image/png;base64,{data}', c=str(c), s=str(s), U=str(U), I=str(I), Lambda=str(Lambda), r_e=str(r_e), alpha=str(alpha), phi=str(phi), theta=str(theta))

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)