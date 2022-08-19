# -*- coding: UTF-8 -*-
from app import app


@app.route('/')
def index():
    return 'Flask API started'

if __name__ == '__main__':
    app.run(host='192.168.50.134',port = 3000,debug=False)
    
