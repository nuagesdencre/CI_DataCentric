import os
from amphora import app

if __name__ == '__main__':
    app.run(host='IP',
            port=int(os.environ.get('PORT', 5000)))
