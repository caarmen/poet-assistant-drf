mkdir -p reports
pip install --index-url https://test.pypi.org/simple/ pylint_json2checkstyle-caarmen
pylint --load-plugins=pylint_json2checkstyle.checkstyle_reporter,pylint_json2html  --output-format=jsonextended:reports/pylint.json,checkstyle poetassistant > reports/pylint.xml
has_lint_errors=$?
pylint-json2html -f jsonextended -o reports/pylint.html reports/pylint.json
exit $has_lint_errors
