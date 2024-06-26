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
        turquoise_note = int(request.form.get('turquoise_note', 0))
        indigo_note = int(request.form.get('indigo_note', 0))
        crimson_note = int(request.form.get('crimson_note', 0))
        golden_note = int(request.form.get('golden_note', 0))
        
        total_attraction = round(lilac_bouquet * 5 + 
                            blue_bouquet * 2 + 
                            red_bouquet * 1 + 
                            attraction_bowl * 2.5 + 
                            attraction_bottle * 6.5 + 
                            attraction_box * 27 +
                            turquoise_note * 1 +
                            indigo_note * 2 +
                            crimson_note * 5 +
                            golden_note * 25)
        
        return render_template('calculate_attraction.html', total_attraction=total_attraction)
    
    return render_template('calculate_attraction.html', total_attraction=None)

@app.route('/calculate-intimacy', methods=['GET', 'POST'])
def calculate_intimacy():
    if request.method == 'POST':
        luxurious_gift = int(request.form.get('luxurious_gift', 0))
        large_gift = int(request.form.get('large_gift', 0))
        regular_gift = int(request.form.get('regular_gift', 0))
        intimacy_bag = int(request.form.get('intimacy_bag', 0))
        intimacy_sack = int(request.form.get('intimacy_sack', 0))
        intimacy_box = int(request.form.get('intimacy_box', 0))
        
        total_intimacy = round(luxurious_gift * 5 + 
                          large_gift * 2 + 
                          regular_gift * 1 + 
                          intimacy_bag * 2.5 + 
                          intimacy_sack * 6.5 + 
                          intimacy_box * 27)
        
        return render_template('calculate_intimacy.html', total_intimacy=total_intimacy)
    
    return render_template('calculate_intimacy.html', total_intimacy=None)

if __name__ == '__main__':
    app.run(debug=True)
