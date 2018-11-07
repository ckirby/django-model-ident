import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-model-ident',
    version=model_ident.__version__,
    description="Django app to provide classes quick pk only lookups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chaim Kirby',
    author_email='chaim.kirby@gmail.com',
    url='https://github.com/ckirby/django-model-ident',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)