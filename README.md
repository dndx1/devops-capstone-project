# Customer Accounts Microservice

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)
[![CI Build](https://github.com/dndx1/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/dndx1/devops-capstone-project/actions/workflows/ci-build.yaml)

## Overview
This project is a Customer Accounts microservice built using Flask and Python. It provides RESTful APIs for managing customer accounts including Create, Read, Update, Delete, and List operations.

## Project layout

```text
├── service         <- microservice package
│   ├── common/     <- common log and error handlers
│   ├── config.py   <- Flask configuration object
│   ├── models.py   <- code for the persistent model
│   └── routes.py   <- code for the REST API routes
├── setup.cfg       <- tools setup config
└── tests
    ├── factories.py
    ├── test_models.py
    └── test_routes.py
```

## Running Tests
```bash
nosetests
```

## License
Licensed under the Apache License. See [LICENSE](LICENSE)
