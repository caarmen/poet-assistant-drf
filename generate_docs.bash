python manage.py generateschema --title "Poet Assistant REST Api" --description "English-language tools for writing poetry"  --file docs/openapi-schema.yml
openapi-generator generate -i docs/openapi-schema.yml -g html2 -o docs
