# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

def safe_path(path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.normpath(os.path.join(base_dir, path))
        if base_dir != os.path.commonpath([base_dir, filepath]):
            return None
        return filepath
class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        if not path:
            pass

        safe_path_result = safe_path(path)
        if safe_path_result is None:
            return None

        with open(safe_path_result, 'rb') as pic:
            picture = bytearray(pic.read())

        return safe_path_result


    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        if not path:
            raise Exception("Error: Tax form is required for all users")

        safe_path_result = safe_path(path)
        if safe_path_result is None:
            return None

        with open(safe_path_result, 'rb') as form:
            tax_data = bytearray(form.read())

        return safe_path_result
