# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate-attraction', methods=['GET', 'POST'])
def calculate_attraction():
    if request.method == 'POST':
        lilac_bouquet = int(request.form.get('lilac_bouquet', 0))
        blue_bouquet = int(request.form.get('blue_bouquet', 0))
        red_bouquet = int(request.form.get('red_bouquet', 0))
        attraction_bowl = int(request.form.get('attraction_bowl', 0))
        attraction_bottle = int(request.form.get('attraction_bottle', 0))
        attraction_box = int(request.form.get('attraction_box', 0))
        
        total_attraction = (lilac_bouquet * 5 + 
                            blue_bouquet * 2 + 
                            red_bouquet * 1 + 
                            attraction_bowl * 2.5 + 
                            attraction_bottle * 6.5 + 
                            attraction_box * 27)
        
        return render_template('calculate_attraction.html', total_attraction=total_attraction)
    
    return render_template('calculate_attraction.html', total_attraction=None)

if __name__ == '__main__':
    app.run(debug=True)
