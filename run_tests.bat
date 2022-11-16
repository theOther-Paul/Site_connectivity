set dt=%DATE:~6,4%_%DATE:~3,2%_%DATE:~0,2%__%TIME:~0,2%_%TIME:~3,2%_%TIME:~6,2%
set dt=%dt: =0%
SET file_name="Pytest Report at "
SET complete_name=%file_name%%dt%
venv\Scripts\python -m pytest --html=testing_reports/%complete_name%.html --self-contained-html --css=testing_reports/theme.css test_functionality.py