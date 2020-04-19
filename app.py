import ZODB
from src import app

db = ZODB(app)

if __name__ == '__main__':
    app.run()