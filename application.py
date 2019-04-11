
from src.flaskbasic import application ,db
from src.flaskbasic.form import *
from src.flaskbasic.models import *
db.create_all()
if __name__ == '__main__':
	application.run(debug=True)
