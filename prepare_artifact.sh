python3.9 -m poetry build
python3.9 -m poetry run pip install --upgrade -t package dist/*.whl
cd package ; zip -r ../artifact.zip . -x '*.pyc'
