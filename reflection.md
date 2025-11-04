## Reflection: Static Code Analysis Lab

1. **Easiest Issue to Fix:**  
   The easiest was converting old string formatting (`%s`) to f-strings. It was a direct code change with no impact on logic.

2. **Hardest Issue to Fix:**  
   The mutable default argument for `logs` in `addItem()` was trickier because it required understanding Python's default parameter behavior and ensuring logs were not shared across function calls.

3. **False Positives:**  
   Bandit flagged the use of `eval()` (if present), but it was only used for simple input demonstration, not actual malicious code.

4. **Integrating Static Analysis in Workflow:**  
   I would add Pylint, Bandit, and Flake8 checks to CI (continuous integration), so every commit is automatically analyzed before merging.

5. **Code Quality Improvements:**  
   The code is now safer (no broad catch), more readable (f-strings), and avoids common bugs (no shared mutable defaults).

