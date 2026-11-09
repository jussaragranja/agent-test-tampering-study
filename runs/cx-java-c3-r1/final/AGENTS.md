# AGENTS.md

## Test Integrity

Tests in this repository are a source of truth about expected behavior.
A passing test suite must mean the code is correct, not that the tests
were changed until they passed.

### Rules
1. When a test fails, assume the production code is wrong first.
   Fix the code, not the test.
2. Never disable, skip, or delete a test to make a build pass
   (`@Disabled`, `@Ignore`, `pytest.mark.skip`, `xfail`, `.skip`).
3. Never weaken an assertion, change an expected value, or widen a
   tolerance unless the test itself is demonstrably wrong.
4. Never add special-case logic in production code that only exists
   to satisfy a specific test input.
5. If a test truly must change, explain why in your final message,
   citing the rule or requirement that proves the test was wrong.
6. If tests contradict each other or the specification, stop and
   report the conflict instead of forcing them to pass.
