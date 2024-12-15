# Data Diary

## Data Collection Process
Objective: Extract restaurant delivery details (name, location, delivery time, delivery fees, rating, average price, etc) from Fantuan's website.
Tool: Playwright for dynamic web scraping.
Challenge: Many restaurants were hidden behind a "Load More" button.
Solution: Used Playwright to continuously click "Load More" until all content was loaded.

## Data Processing
Tool: pandas
Process: Extracted structured information using regex.
Saved the structured data to fantuan_data.csv.

## Web Application Implementation
Tool: Flask
Features:
Reads the processed CSV data and renders it in an HTML table.
Paginates and allows navigation between pages.

## Future Improvements
Data Cleaning: Cleane null or missing data.
Search and Filter: Enable users to filter restaurants by name, location, average price or food type.
