import os
from flask import Flask, request

app = Flask(__name__)

# Ορίζουμε πού βρίσκεται ο φάκελος storage
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'storage')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Αυτή είναι η HTML εμφάνιση της σελίδας μας (Φόρμα για Upload)
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>CodeShare Local</title>
</head>
<body>
    <h2>📤 Ανέβασμα Αρχείου Κώδικα</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file_to_upload">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
'''

# 1. Η Αρχική Σελίδα που δείχνει τη φόρμα
@app.route('/')
def home():
    return HTML_PAGE

# 2. Η "κρυφή" διαδρομή που επεξεργάζεται το αρχείο όταν πατάς το κουμπί Upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Ελέγχουμε αν ο χρήστης έβαλε όντως αρχείο
    if 'file_to_upload' not in request.files:
        return 'Καμία επιλογή αρχείου'
    
    file = request.files['file_to_upload']
    
    if file.filename == '':
        return 'Δεν επέλεξες αρχείο'
    
    if file:
        # Βρίσκουμε το όνομα του αρχείου και το αποθηκεύουμε μέσα στον φάκελο storage
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f'<h3>Το αρχείο {file.filename} ανέβηκε επιτυχώς!</h3> <a href="/">Πίσω στην αρχική</a>'

if __name__ == '__main__':
    app.run(debug=True)