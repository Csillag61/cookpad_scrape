from flask import request, Flask
from cookpad_recipe_only import recipe

app = Flask(__name__) #create Flask app

@app.route('/', methods=['GET','POST']) #allow get and post requests
def cookpad_form(): # sending via forms as a post request (behind the scenes)

    #--- Check if its a post or get request: ---#
    if request.method == 'POST': #this block is only entered if the form is submitted
        url = request.form.get('recipe')
        user = request.form['name']
        recipe(url)
        return '''<h1>Thanks {},</h1> your request has been submitted'''.format(user)

    #--- Make the form ---#
    return '''<form method = "POST">
                    What is the cookpad recipe page? <input type="text" name="recipe"><br>
                    What is your name? <input type="text" name="name"><br>
                    <input type="submit" value="Submit"><br>
                </form>'''
                # The form makes a post request to the same route that made the form

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')