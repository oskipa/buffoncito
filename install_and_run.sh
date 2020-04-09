echo ">> Checking for pipenv"

if brew ls --versions pipenv > /dev/null; then
  echo ">> pipenv is installed"
else
  echo ">> pipenv installing"
  brew install pipenv
  echo ">> pipenv has been installed"
fi

echo ">> Installing dependencies"
pipenv run pipenv install

echo ">> Migrating the database"
pipenv run python manage.py migrate

echo ">> Running"
pipenv run python manage.py runserver
