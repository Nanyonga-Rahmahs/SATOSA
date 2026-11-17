"""
setup.py
"""

from setuptools import setup, find_packages

dev = [

    "autopep8",
    "black",
    "build",
    "commitizen",
    "id",
    "ipdb",
    "isort",
    "jedi",
    "matplotlib",
    # https://github.com/executablebooks/mdit-py-plugins/pull/65
    "mdit-py-plugins>0.3.4",
    "myst-parser[linkify,rtd]",
    "pip-tools",
    "pre-commit",
    "pystemmer",
    "rinohtype",
    "sphinxcontrib-bibtex",
    "sphinxcontrib-svg2pdfconverter[CairoSVG]",
    "sphinx-autodoc2[cli]",
    # https://github.com/ResearchDataCom/templates/issues/11
    "sphinx-book-theme==1.2.0",
    "sphinx-intl",
    "sphinx-js",
    "sphobjinv",
    "twine",
    "yapf",
    "yq",
    # Keep the list of flake8 plugins in sync with
    # .pre-commit-config.yaml.
    "dlint",
    "flake8-bandit",
    "flake8-bugbear",
    "flake8-comprehensions",
    "flake8-docstrings",
    "flake8-eradicate",
    "flake8-fixme",
    "flake8-future-import",
    "flake8-pytest-style",
    "flake8-requirements",

]

setup(
    name='SATOSA',
    version='8.6.0',
    description='Protocol proxy (SAML/OIDC).',
    author='DIRG',
    author_email='satosa-dev@lists.sunet.se',
    license='Apache 2.0',
    url='https://github.com/SUNET/SATOSA',
    packages=find_packages('src/'),
    package_dir={'': 'src'},
    python_requires=">=3.11",
    install_requires=[
        "pyop >= v3.4.0",
        "pysaml2 >= 6.5.1",
        "pycryptodomex",
        "requests",
        "PyYAML",
        "gunicorn",
        "Werkzeug",
        "click",
        "chevron",
        "cookies-samesite-compat",
    ],
    extras_require={
        "ldap": ["ldap3"],
        "pyop_mongo": ["pyop[mongo]"],
        "pyop_redis": ["pyop[redis]"],
        "idpy_oidc_backend": ["idpyoidc >= 2.1.0"],
        "dev": dev,
    },
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    entry_points={
        "console_scripts": ["satosa-saml-metadata=satosa.scripts.satosa_saml_metadata:construct_saml_metadata"]
    }
)
