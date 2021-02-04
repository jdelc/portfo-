import os, csv
from flask import Flask, render_template, send_from_directory, request, url_for, redirect
app = Flask(__name__)

print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # if request.method == 'POST':
    # 	data = request.form.to_dict()
    # 	print(data)
    # 	return 'form submitted'
    # else:
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to data base'
    else:
        return 'something went wrong. Try Again'



# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/components')
# def components():
#     return render_template('components.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/work')
# def work():
#     return render_template('work.html')

# @app.route('/works')
# def works():
#     return render_template('work.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
