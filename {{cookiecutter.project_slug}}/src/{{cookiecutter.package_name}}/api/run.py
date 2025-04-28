import uvicorn
from {{cookiecutter.package_name}}.api.app import app

def main():
    """Run the FastAPI application."""
    uvicorn.run(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main() 