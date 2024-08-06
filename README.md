# VE3---Python-Developer-Task-1

# CSV Analysis Project

This Django-based web application allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Features

- **File Upload**: Users can upload CSV files.
- **Data Processing**: The application reads the uploaded CSV files and performs basic data analysis such as displaying the first few rows, calculating summary statistics, and identifying missing values.
- **Data Visualization**: Generates histograms for numerical columns and displays them on the web page.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rushideshmukh3620/VE3---Python-Developer-Task-1
    cd VE3---Python-Developer-Task-1
    ```

2. **Create a virtual environment and activate it**:(If necessary)
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create necessary directories**:(If not present)
    ```bash
    mkdir uploaded_files
    mkdir -p static/plots
    ```

5. **Run the Django migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000/`

## Sample CSV File

A sample CSV file named `iris.csv` is included in the repository for testing purposes.

## Project Structure

