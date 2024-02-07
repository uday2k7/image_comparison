# Create Virtual Environment
py -3 -m venv venv_image
source venv_image/Scripts/activate

# Dependency Details
pip install flask
pip install validate_email

# Run Application
flask run

# Create requirements.txt file
pip3 freeze > requirements.txt

# Run requirements.txt file
pip install -r requirements.txt