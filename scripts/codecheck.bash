mkdir -p reports
PYTHONPATH=scripts pylint --load-plugins=checkstyle_reporter,pylint_json2html  --output-format=jsonextended:reports/pylint.json,checkstyle poetassistant > reports/pylint.xml
has_lint_errors=$?
pylint-json2html -f jsonextended -o reports/pylint.html reports/pylint.json
exit $has_lint_errors