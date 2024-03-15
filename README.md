# `fundpy_test_3_final`

Brief overview of your project.

```{warning}
Where this documentation refers to the root folder we mean where this README.md is
located.
```

## Getting started / Setting up 

To start using this project, [first make sure your system meets its
requirements](#requirements).

In order to setup your project, in a *bash terminal*,
navigate to the root directory and run 

```shell
bash setup_project.bat
```
This will perform a number of steps for you, including:
* Setting up a [virtual environment](#virtual-environments)
* Installing [pre-commit hooks](#pre-commit-hooks)
* Initalising a git repository 

## Virtual environments

In programming we might work on several projects concurrently, each project depending on different packages of different versions. For example, our `project1` might require version `2.0.1` of `packageA`, and `project2` might require version `3.2.2` of that same `packageA`. If these versions are different enough, our `project1` and `project2` may not run with the wrong version of `packageA` installed. We use virtual environments so that all our projects can have separate, isolated environments with all their required dependencies inside, so working on one project does not disrupt our workflow in another.

Documentation on virtual environments in Python is available [here][python-venv-tutorial]

Running the `setup_project.bat` file will create and environment for you called `fundpy-test-3-final-env` using the `environment.yml` file in the root directory of this project.

This environment contains all the packages needed to run the example code and the pre-commit-hooks

* To activate this virtual environment, run `conda`: `conda activate fundpy-test-3-final-env`.
* When you are finished with this project, run: `conda deactivate`.

## Required secrets and credentials PLACEHOLDER

To run this project, [you need a `.env` file with secrets/credentials as
environmental variables](docs/user_guide/loading_environment_variables.md). The
secrets/credentials should have the following environment variable name(s):git

| Secret/credential | Environment variable name | Description                                |
|-------------------|---------------------------|--------------------------------------------|
| Secret 1          | `SECRET_VARIABLE_1`       | Plain English description of Secret 1.     |
| Credential 1      | `CREDENTIAL_VARIABLE_1`   | Plain English description of Credential 1. |

Once you've added, [load these environment variables using
`.env`](docs/user_guide/loading_environment_variables.md).


## Pre-commit hooks

Git-hooks are scripts that can identify simple issues in code. Pre-commit hooks are run on every commit to ensure issues are identified before code is pushed to a repository hosting platform such as GitHub. If you have run `setup_project.bat` then pre-commit hooks will run automatically. 

[*Note*] if you try to make a commit in an environment that does not have access to the pre-commit hook packages the hooks will fail. Activate your environment with `conda`: `conda activate fundpy-test-3-final-env` and commit your changes again. 

For more information see the [pre-commit hooks section in the user guide](docs/user_guide/pre_commit_hooks.md)

## Running the pipeline 

The entry point for the example pipeline is stored in the root directory and called `main.py`. This scripts imports and runs the pipline located within the src folder. 
To run the pipeline, run the following code in the terminal (whilst in the root directory of the
project).

```shell
python main.py
```

Alternatively, most Python IDE's allow you to run the code directly from the IDE using a `run` button.


## Documentation

All functions contained in `.py` scripts in the `src` folder should have docstrings explaining what they do, what parameters are passed to the function, what errors the function can raise, and what the function outputs. The [Google style][google-docstrings] of formatting docstrings is recommended. Scripts as a whole can contain their own docstrings, in much the same way as a function - simply contain a description of the module inside triple quotation marks `"""` at the top of the script. Examples of such documentation are contained in the `src` modules and submodules.

Having documentation in this way is crucial to meet the minimum requirments of a Reproducible Analytical Pipeline.


## Code of Conduct

Please note that the fundpy_test_3_final project is released with a [Contributor Code of Conduct][contributing-code] . By contributing to this project, you agree to abide by its terms.

## License

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `fundpy_test_3_final`, view our
contributing guidelines](docs/CONTRIBUTING.md).

### Requirements

[```Contributors have some additional requirements!```](docs/CONTRIBUTING.md)

- Python 3.6.1+ installed

- a `.env` file with the [required secrets and
  credentials](#required-secrets-and-credentials)
- [able to load environment variables](docs/user_guide/loading_environment_variables.md) from `.env`

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].

[contributing-code]: https://contributor-covenant.org/version/2/1/CODE_OF_CONDUCT.html 
[google-docstrings]: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[python-venv-tutorial]: https://docs.python.org/3/tutorial/venv.html

