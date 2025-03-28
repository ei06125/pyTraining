# pyTraining

A series of projects in Python to practice my skills

## Requirements

We advise to create a virtual environment with:

```bash
python -m venv </PATH/TO/INSTALL/DIR>
# example: python -m venv DotFiles/.pyvenv
source </PATH/TO/INSTALL/DIR>/bin/activate
# example source DotFiles/.pyvenv/bin/activate
```

Or use your Code Editor to create one for you.

### Test Requirements

#### pytest

To install, run:

```bash
# to install pytest
python -m pip install pytest
# to install the dependencies
python -m pip install -r requirements.txt
```

### PYTHONPATH

In order to import modules from within the `modules/` folder next to the `tests/` folders,
we use `direnv` and its `envrc` file to load into `PYTHONPATH` the value of `pwd`.
That way, you only need to run `pytest` to run your tests and `python` should be able to import all your modules.

For more information about `direnv`, check its official page in the references.

## Version

This project uses a versioning guideline similar to semantic versioning:

### MAJOR

The main version of this project. This number should never change.
An update to the MAJOR is an ABI breaking change and it should be so drastic that
it should require a new repository.

### MINOR

The MINOR component of the VERSION is to define the progress of the current MAJOR.
Everytime a new Feature, Module, API function, etc is ADDED to the current version,
the MINOR should be incremented. I will repeat:

> MINOR is updated when new things are ADDED (not removed) to the code.

### PATCH

The PATCH component of the VERSION is incremented when changes are done to the code.
This includes bug fixes, refactoring and other non-additive patches.
It should exclude fine-tuning changes. For example, if you have implemented a function,
and now, you are only tweaking a default value between 10 and 15 - that is a TWEAK.

### TWEAK

The TWEAK component of the VERSION is incremented with every commit by the pre-commit hook.
This means that a MAJOR, MINOR or PATCH update will probably start always on X.Y.Z.1.

## References

- <https://direnv.net/>
