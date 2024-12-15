# Final Project
## Project Overview

### This project scrapes restaurant delivery data from the Fantuan website using Playwright, processes the data with pandas and serves it through a Flask web application. The application provides a paginated interface to explore the delivery data.

#### Install required Python packages:
pip install playwright pandas flask

#### Install Playwright browsers:
playwright install

#### File Structure: 
fantuan-project/

├── app.py                  # Flask application

├── fantuan_data.csv        # Processed delivery data

├── scrape_fantuan.ipynb    # Jupyter notebook for scraping and processing

├── templates/

│   └── fantuan.html        # HTML template for the web app

#### Running the Project

1. Scrape and Process Data

Open the Project.ipynb Jupyter notebook.

Run all cells to:

Scrape the data from Fantuan using Playwright.

Process the data into a structured format using pandas and save the output to fantuan_data.csv.

2. Start the Flask App

Navigate to the project directory in the terminal

Run the Flask app: python app.py

Open your browser and visit https://final-project-m6rs.onrender.com/fantuan to access the web application.
