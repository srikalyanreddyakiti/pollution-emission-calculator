from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        power_rating = float(request.form['power_rating'])
        hours_of_use = float(request.form['hours_of_use'])
        emissions_intensity = float(request.form['emissions_intensity'])
        total_emissions = power_rating * hours_of_use * emissions_intensity
        carbon_credits = total_emissions / 1000
        return render_template('results.html', total_emissions=total_emissions, carbon_credits=carbon_credits)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
