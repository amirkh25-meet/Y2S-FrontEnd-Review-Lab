from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '''<html>
                    <style>
                        .food_page_redirect{
                        position : absolute;
                        bottom : 0;
                        }
                        /* Dropdown Button */
                        .dropbtn {
                          background-color: #04AA6D;
                          color: white;
                          padding: 16px;
                          font-size: 16px;
                          border: none;
                        }

                        /* The container <div> - needed to position the dropdown content */
                        .dropdown {
                          position: relative;
                          display: inline-block;
                        }

                        /* Dropdown Content (Hidden by Default) */
                        .dropdown-content {
                          display: none;
                          position: absolute;
                          background-color: #f1f1f1;
                          min-width: 160px;
                          box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                          z-index: 1;
                        }

                        /* Links inside the dropdown */
                        .dropdown-content a {
                          color: black;
                          padding: 12px 16px;
                          text-decoration: none;
                          display: block;
                        }

                        /* Change color of dropdown links on hover */
                        .dropdown-content a:hover {background-color: #ddd;}

                        /* Show the dropdown menu on hover */
                        .dropdown:hover .dropdown-content {display: block;}

                        /* Change the background color of the dropdown button when the dropdown content is shown */
                        .dropdown:hover .dropbtn {background-color: #3e8e41;}
                    </style>
                    <body>
                    <header>
                        <h1>Amir's Gallery</h1>
                    <header>
                    <div>    
                        <p>Welcome User to Amir's Gallery ! Here you can find the best photos of food, pets and outer space</p>
                    </div>
                    <div class="dropdown">
                    <button class="dropbtn">Dropdown</button>
                        <div class="dropdown-content">
                            <a href="/pet1">pet1</a>
                            <a href="/pet2">pet2</a>
                            <a href="/pet3">pet3</a>
                            <a href="/space1">space1</a>
                            <a href="/space2">space2</a>
                            <a href="/space3">space3</a>
                            <a href="/food1">food1</a>
                            <a href="/food2">food2</a>
                            <a href="/food3">food3</a>
                          </div>
                    </div>

                    <div class="dropdown-content">

                    </div>
                    <footer class="food_page_redirect">
                        <a href="/food1" >go to the first food photo</a><br><br>
                        <a href="/space1" >go to the first space photo</a><br><br>
                        <a href="/pet2" >go to the second pet photo</a>


                    </footer>
                    </body>
                </html>'''

@app.route('/food1')
def food1():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Food 1</h1>

                        <div class="first-food-image">
                            <img src="https://www.southernliving.com/thmb/3x3cJaiOvQ8-3YxtMQX0vvh1hQw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/2652401_QFSSL_SupremePizza_00072-d910a935ba7d448e8c7545a963ed7101.jpg" alt="alternatetext" width="700x">
                        </div><br>
                        <a href="/food2">Go to the second picture</a>
                    </body>
                </html>''')

@app.route('/food2')
def food2():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Food 2</h1>

                        <div class="first-food-image">
                            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzPqUeen82WrUFOosBOuRcK9rdj32r_-wwzg&s" width="500">
                        </div><br>
                        <a href="/food3">Go to the third picture</a>
                        </div>
                    </body>
                </html>''')

@app.route('/food3')
def food3():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Food 3</h1>

                        <div >
                            <img src="https://www.foodandwine.com/thmb/XE8ubzwObCIgMw7qJ9CsqUZocNM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/MSG-Smash-Burger-FT-RECIPE0124-d9682401f3554ef683e24311abdf342b.jpg" width="500">
                        </div><br>
                        <a href="/home">Go to the main page</a>
                    </body>
                </html>''')

@app.route('/space1')
def space1():
    return ('''<html>
                    <style>
                    </style>

                    <body>
                    <h1>Room of Space 1</h1>

                        <div >
                            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJpaWTviBwKxlBCAQujz_Jr3Fb2baDw7eRrg&s" width="500">
                        </div><br>
                        <a href="/home">Go to the main page</a><br>
                        <a href="/space2">Go to the second picture</a><br>
                        <a href="/space3">Go to the third picture</a><br>

                    </body>
                </html>''')

@app.route('/space2')
def space2():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Space 2</h1>

                        <div >
                            <img src="https://c02.purpledshub.com/uploads/sites/48/2020/04/Things-never-knew-astronomy-e454e5d.jpg" width="500">
                        </div><br>
                        <a href="/space1">Go to the first picture</a><br>
                        <a href="/space3">Go to the third picture</a><br>
                    </body>
                </html>''')

@app.route('/space3')
def space3():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Space 3</h1>

                        <div >
                            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Webb%27s_First_Deep_Field.jpg/1200px-Webb%27s_First_Deep_Field.jpg" width="500">
                        </div><br>
                        <a href="/space1">Go to the first picture</a><br>
                        <a href="/space2">Go to the second picture</a><br>
                    </body>
                </html>''')

@app.route('/pet1')
def pet1():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Pet 1</h1>

                        <div >
                            <img src="https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg" width="500">
                        </div><br>
                        <a href="/pet2">Go to the first picture</a><br>
                    </body>
                </html>''')


@app.route('/pet2')
def pet2():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Pet 2</h1>

                        <div >
                            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/1200px-Cat_August_2010-4.jpg" width="500">
                        </div><br>
                        <a href="/pet1">Go to the first picture</a><br>
                        <a href="/pet3">Go to the third picture</a><br>
                    </body>
                </html>''')


@app.route('/pet3')
def pet3():
    return ('''<html>
                    <style>
                    </style>
                    <body>
                    <h1>Room of Pet 3</h1>
                        <div >
                            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgSYizW8hXwnYJM08O7eRSW2UiVkrkHntOBA&s" width="500">
                        </div><br>
                        <a href="/pet2">Go to the second picture</a><br>
                        <div class="dropdown">
                          <button class="dropbtn">Dropdown</button>
                        </div>
                    </body>
                </html>''')

if __name__ == '__main__':
    app.run(debug=True)