# Random Password Generator

Random password generator using Flask.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Kennylalek/Random-Password-Generator.git
    cd Random-Password-Generator
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```


## Usage

1. **Run the application:**
    ```sh
    flask run
    ```

2. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000
    ```

3. **Enter the password length in the specified input, and check the boxes for the desired features.**

## Project Structure
```plaintext
.
├── app.py                  # Main application file
├── password_generator.py   # Contains utility function
├── templates
│   └── index.html          # HTML template for the website
├── static
│   ├── css
│   │   └── style.css       # CSS styles
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Dependencies

- Flask

Make sure to install all dependencies listed in the `requirements.txt` file.
