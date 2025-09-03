from flask import Flask

app = Flask(__name__)

@app.route('/')
def create_app():
    """Initialize the Flask application. Create and configure the app."""
    app = Flask(__name__,instance_relative_config=True)
    
    @app.route('/health')
    def health_check():
        return "AegisPhishDetector system status: Nominal!"
    return app