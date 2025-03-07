# Plagiarism Detector
The Plagiarism Detector is a user-friendly web application built with Flask that helps identify text similarities between two uploaded .txt files. Utilizing Python's SequenceMatcher module, it calculates and displays the percentage of plagiarism, providing an efficient way to compare documents for originality. The application features a simple interface for easy file uploads and quick results viewing, making it an ideal tool for educators, writers, and anyone concerned with content authenticity.

markdown
This is a Flask-based web application that detects plagiarism between two uploaded text files. It uses the `SequenceMatcher` module to compare text similarity and provides a plagiarism percentage.

## Features
- Upload two text files (.txt) for comparison.
- Calculates and displays the plagiarism percentage.
- Simple web interface using Flask.

## Installatio

### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.7)
- Flask

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/plagiarism-detector.git
   cd plagiarism-detector
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python plagiarism_detector/app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`.

## Usage
1. Upload two `.txt` files.
2. Click "Compare" to analyze the similarity.
3. View the plagiarism percentage on the results page.

## Project Structure
```
plagiarism_detector/
│── static/
│   └── styles.css
│── templates/
│   ├── upload.html
│   ├── result.html
│── app.py
│── requirements.txt (to be created)
└── README.md
```

## Requirements File
Create a `requirements.txt` with the following:
```
Flask
```

## License
This project is licensed under the MIT License.
```

