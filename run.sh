#echo "Starting static type check..."
#mypy --ignore-missing-imports *.py

echo "Running specs..."
mamba --format=documentation *_spec.py --enable-coverage && coverage html

echo "Checking code coverage report display"
if pgrep -x "python" > /dev/null
then
  echo Code coverage report window running
else
  echo Opening code coverage report window...
  nohup python -m http.server 8000 -d htmlcov >/dev/null 2>/dev/null &
  sleep 1
fi

echo "Done."