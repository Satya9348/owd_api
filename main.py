from flask import Flask, render_template_string, send_file
import os
app = Flask(__name__)
# Define the route to display the PDF
@app.route('/pdf/<category>/<id>')
def show_pdf(category, id):
    if category=='All' or id=='All':
        return ''
    else:
        return send_file('pdf\sample.pdf', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)

