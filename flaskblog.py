from flask import Flask, render_template, url_for
app = Flask(__name__)




posts = [
    {
        'author': 'Vy Truong',
        'title': '1. Download Files',
        'content': 'Basic instructions on typesets and redrawing comic images in general, using the GNU Image Manipulation Program.',
        'date_posted': 'August 20, 2021'
    },
    {
        'author': 'Vy Truong',
        'title': '2. Languages + Themes',
        'content': 'Basic instructions on typesets and redrawing comic images in general, using the GNU Image Manipulation Program.',
        'date_posted': 'August 20, 2021'
    },
    
    {
        'author': 'Vy Truong',
        'title': '3. Export Files',
        'content': 'Basic instructions on typesets and redrawing comic images in general, using the GNU Image Manipulation Program.',
        'date_posted': 'August 20, 2021'
    }
    ,
    
    {
        'author': 'Vy Truong',
        'title': '4. Fonts List',
        'content': 'Basic instructions on typesets and redrawing comic images in general, using the GNU Image Manipulation Program.',
        'date_posted': 'August 22, 2021'
    }
    ,
    
    {
        'author': 'Vy Truong',
        'title': '5. Redraw',
        'content': 'Basic instructions on typesets and redrawing comic images in general, using the GNU Image Manipulation Program.',
        'date_posted': 'August 22, 2021'
    }
    ,
    
    {
        'author': 'Vy Truong',
        'title': '6. Heal Selection',
        'content': 'Basic instructions on typesets and redrawing comic images in general, using the GNU Image Manipulation Program.',
        'date_posted': 'August 23, 2021'
    }
    ,
    
    {
        'author': 'Vy Truong',
        'title': '1. Fishing, Gathering, Shop',
        'content': 'My personal game development diary to describe certain game mechanics.',
        'date_posted': 'April 8, 2022'
    },
        {
        'author': 'Vy Truong',
        'title': '2. 3D Experiment',
        'content': 'My personal game development diary to describe certain game mechanics.',
        'date_posted': 'April 9, 2022'
    },
        {
        'author': 'Vy Truong',
        'title': '3. UI Design',
        'content': 'My personal game development diary to describe certain game mechanics.',
        'date_posted': 'April 15, 2022'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



@app.route("/index")
def index():
    return render_template('index.html', title='Index')


import os
picFolder = os.path.join('static', 'upload')
app.config['UPLOAD_FOLDER'] = picFolder
@app.route("/port")
def show_image():
    imageList = os.listdir('static/upload')
    imagelist = ['upload/' + image for image in imageList]
    return render_template("port.html", imagelist=imagelist)





if __name__ == '__main__':
    app.run(debug=True)






