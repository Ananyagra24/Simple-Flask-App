from flask import Flask, render_template, request, redirect, url_for, flash

app =Flask(__name__)
app.secret_key = 'Ananya'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods =["GET","POSt"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"New message from {name} ({email}): {message}")

        flash ("Thank you for contatcing me")
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)