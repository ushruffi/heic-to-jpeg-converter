

all: package distribute-dev distribute-prod

package:
	@python setup.py sdist bdist_wheel

distribute-dev:
	@TWINE_NON_INTERACTIVE=1 TWINE_USERNAME=${TWINE_USERNAME} TWINE_PASSWORD=${TWINE_PASSWORD} twine upload --repository testpypi --skip-existing dist/*

distribute-prod:
	@TWINE_NON_INTERACTIVE=1 TWINE_USERNAME=${TWINE_USERNAME} TWINE_PASSWORD=${TWINE_PASSWORD} twine upload --skip-existing dist/*

test-pip:
	pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple heic-to-jpeg-converter==1.0.1