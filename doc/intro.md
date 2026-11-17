# Get Started

## Installation

### Docker

A pre-built Docker image is accessible at the [Docker Hub](https://hub.docker.com/_/satosa), and is the
recommended ways of running the proxy.

## Manual installation

### Dependencies

SATOSA requires Python 3.4 (or above), and the following packages on Ubuntu:

```bash
apt-get install libffi-dev libssl-dev xmlsec1
````

### Instructions

1. Download the SATOSA proxy project as a [compressed archive](https://github.com/IdentityPython/SATOSA/releases)
   and unpack it to `<satosa_path>`.

2. Install the application:

   ```bash
   pip install <satosa_path>
   ```

Alternatively the application can be installed directly from PyPI (`pip install satosa`), or the [Docker image](https://hub.docker.com/_/satosa) can be used.

