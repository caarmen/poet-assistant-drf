mkdir -p reports
pylint --load-plugins=pylint_json2checkstyle.checkstyle_reporter,pylint_json2html  --output-format=jsonextended:reports/pylint.json,checkstyle poetassistant > reports/pylint-checkstyle.xml
has_lint_errors=$?
pylint-json2html -f jsonextended -o reports/pylint.html reports/pylint.json
flake8 --format=checkstyle poetassistant > reports/flake8-checkstyle.xml
if [ $? != 0 ]
then
  has_lint_errors=$?
fi
exit $has_lint_errors
