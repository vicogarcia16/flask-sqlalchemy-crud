
from app import app
from routes.login import csrf
from utils.db import db
from routes.login import status_401, status_404, status_405

with app.app_context():
    db.create_all()
    
    
if __name__ == '__main__':
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.register_error_handler(405, status_405)
    app.run(debug=True)