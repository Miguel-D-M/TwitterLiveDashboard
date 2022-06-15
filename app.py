from flask import Flask , render_template
from twitter_dumper import main

app = Flask ( __name__ )


@app.route ( '/' )
def index() :
    main.main()
    return render_template ( "index.html" )


if __name__ == '__main__' :
    app.run ( debug=True )
