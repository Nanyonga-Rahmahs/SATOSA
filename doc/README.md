## Building the documentation

The documentation is built with [Sphinx](https://www.sphinx-doc.org/) from the files in `doc/`. API pages are generated from the docstrings in `src/satosa`.

### Build

```bash
make setup    # creates the .venv virtual environment and installs the documentation tools
make html     # builds the documentation
```

The output is written to `build/html/`. Open `build/html/index.html` in a browser.