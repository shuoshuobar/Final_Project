from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Default route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Fantuan route with pagination
@app.route("/fantuan")
def fantuan():
    # Read the Fantuan CSV file
    df = pd.read_csv("fantuan_data.csv")  
    fantuan_data = df.to_dict('records')  # Convert the dataframe to a list of dictionaries

    # Pagination parameters
    PER_PAGE = 10  # Set number of records per page to 10
    current_page = int(request.args.get('page', 1))  # Get current page from query parameter, default is 1
    start = (current_page - 1) * PER_PAGE  # Start index
    end = start + PER_PAGE  # End index

    # Paginate the data
    paginated_data = fantuan_data[start:end]

    # Calculate total pages
    total_pages = (len(fantuan_data) + PER_PAGE - 1) // PER_PAGE  # Total pages for navigation

    # Render the template with paginated data and pagination info
    return render_template(
        'fantuan.html',
        fantuan_data=paginated_data,
        current_page=current_page,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(debug=True)
