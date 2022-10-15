python -m pytest --cov=poetassistant --cov-report=xml --cov-report=html --junitxml="reports/junit.xml"
mkdir -p reports
mv coverage.xml htmlcov reports/.
