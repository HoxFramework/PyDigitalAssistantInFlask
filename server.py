from flask import Flask, render_template, request
#from flask_cors import CORS
import importlib
import os 
app = Flask(__name__)
#CORS(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        post = request.form.get('post')
        #print(str(post))
        q = str(post)
        import redline
        importlib.reload(redline)
        from redline import red_line
        line = red_line(q)
        from redline import solution
        solution = str(solution[1])
        print(solution)
        return render_template('index.html', solution=solution)

    #os.system("dir > dir.txt") - OK so our dir is okay.
    
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run(debug=True, host="YOUR IP",port =80)
