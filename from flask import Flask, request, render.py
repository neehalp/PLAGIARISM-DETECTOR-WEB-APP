from flask import Flask, request, render_template
from difflib import SequenceMatcher

app = Flask(__name__)

def calculate_plagiarism(file1_content, file2_content):
    """Calculate the plagiarism percentage between two texts."""
    matcher = SequenceMatcher(None, file1_content, file2_content)
    return matcher.ratio() * 100

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        # Check if files are uploaded
        if 'file1' not in request.files or 'file2' not in request.files:
            return "No file part"
        
        file1 = request.files['file1']
        file2 = request.files['file2']

        if file1.filename == '' or file2.filename == '':
            return "No selected file"

        # Read the contents of the files
        file1_content = file1.read().decode('utf-8')
        file2_content = file2.read().decode('utf-8')

        # Calculate plagiarism
        plagiarism_percentage = calculate_plagiarism(file1_content, file2_content)

        return render_template('result.html', plagiarism_percentage=plagiarism_percentage)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)