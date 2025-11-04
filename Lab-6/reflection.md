# Lab 6: Fuzz Testing Reflection

## What did you learn from Hypothesis fuzz testing?

- Hypothesis automatically generated edge-case inputs (like `None`, empty strings), which revealed real bugs in my functions that simple manual testing did not catch.

## Bugs revealed by fuzz testing

- `parse_int_list` crashed on `None` input and when trying to convert empty strings to int.
- `reverse_words` failed when given `None` instead of a string.

## How did you fix them?

- Added type and value checks at the start of each function.
- Used a `try/except` to skip non-integer values in `parse_int_list`.
- Ensured `reverse_words` returns an empty string for `None` or non-str input.

## Importance of fuzz testing in CI/CD

- Fuzz testing should be integrated into CI pipelines to automatically catch rare, unexpected input cases before code reaches production.
- It makes software much more robust and reliable.

## Observations from the experiment

- The lab shows that even simple code may have hidden bugs that only property-based (automated) testing can reveal.
