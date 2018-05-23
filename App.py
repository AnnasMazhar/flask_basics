from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def helloworld():
    return 'Hello World'

@app.route('/new/')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return  '<h1>The greeting is  : {0}</h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='Annas'):
    return '<h1>Hello there {}</h1>'.format(name)

@app.route('/text/<string:newname>')
def string(newname='Saad'):
    return '<h2>Hello your name is {}</h2>'.format(newname)

# Numbers
@app.route('/number/<int:num>')
def numbers(num):
    return '<h1>Hello the number you picked is:' +str(num)+ '</h1>'

# Adding
@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return '<h2>the sum is : {}'.format(num1 + num2)+'<h2>'

# floats
@app.route('/floats/<float:num3>/<float:num4>')
def float(num3, num4):
    return '<h3>the sum of the floats is: {}'.format(num3 + num4)+'</h3>'

@app.route('/tempelate')
def tempelate():
    return render_template('hello.html')

@app.route('/watch')
def movies():
    movie = ['Black panther', 'Avengers: Infinity war', 'Deadpool','Ice age 4']
    return render_template('movies.html', movie=movie, name='Annas')

@app.route('/movieduration')
def movie_duration():
    movie_dict = {"Black Panther": 2, "Avengers":2.5, "The matrix": 1.7, "Venom": 1.5, "Inception": 3}
    return render_template('duration.html', movie=movie_dict, name ="Misbah")

@app.route('/filters')
def filter_data():
    more_movies = {"The Amazing Spiderman": 2.4, "Thor: Ragnarok": 2.6,"Murder on the Orient Express":2.3, "Wolverine": 1.9}
    return render_template('filter.html', movie=more_movies, name=None, film='A Chrristmas Carol')

@app.route('/macros')
def macros():
    my_movies = {"The Amazing Spiderman": 2.4, "Thor: Ragnarok": 2.6, "Murder on the Orient Express": 2.3, "Wolverine": 1.9}
    return  render_template('macros.html', movie=my_movies)


if __name__ == '__main__':
    app.run(debug=True)
