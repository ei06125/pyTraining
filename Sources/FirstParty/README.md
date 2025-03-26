# First Party

## Testing

### pytest

To run `ImportSystem` tests:

```bash
# navigate to the ImportSystem/packages folder
cd /**/ImportSystem/packages
# run pytest with PYTHONPATH defined as
PYTHONPATH=$(pwd) pytest
# or
python -m pytest # which will add the pwd to the sys.path
```
