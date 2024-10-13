import os
import zipfile

import pytest

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "file")


@pytest.fixture(scope="function", autouse=True)
def create_archive():
    with zipfile.ZipFile(f"{FILE}/archive.zip", "w") as zip_file:
        for file in ["test_csv.csv", "test_pdf.pdf", "test_xlsx.xlsx"]:
            add_file = os.path.join(FILE, file)
            zip_file.write(add_file, os.path.basename(add_file))
    yield
    os.remove(f"{FILE}/archive.zip")
