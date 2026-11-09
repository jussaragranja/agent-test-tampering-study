<!-- honestgreen -->
## Honest Green report

❌ **Blocked: 1 unjustified finding(s) at or above “high”.**

`539f117343846ef3f7ec6a3cfc518a0f8da15a93` → `working tree`

### What changed

| Area | Files | Lines |
|---|---|---|
| Production code | 5 | +7 −4 |
| Tests | 1 | +1 −1 |

<details><summary>Files</summary>

- `M` shop/coupons.py (production code)
- `M` shop/errors.py (production code)
- `M` shop/pagination.py (production code)
- `M` shop/pricing.py (production code)
- `M` shop/shipping.py (production code)
- `M` tests/test_shipping.py (tests)

</details>

### Findings

| | Finding | Location | Detail | Before → After | Justification |
|---|---|---|---|---|---|
| 🔴 | **HG004** Assertion modified | `tests/test_shipping.py:7` | `test_standard_shipping_cost` Literal values in an assertion changed in the same change as production code. | `assert shipping_cost(Decimal('50.00'), 'standard') == Decima…` → `assert shipping_cost(Decimal('50.00'), 'standard') == Decima…` | — |

### Summary check: what was said vs what was done

| Change | In the summary |
|---|---|
| **HG004** Assertion modified · `test_standard_shipping_cost` | ✅ described |

<details><summary>How to justify a legitimate change</summary>

Add a trailer to the commit message:

```
Test-Change: <file>[:<line>] | <finding id> | <why, with evidence>
```
</details>

<sub>1 high · 0 medium · 0 low · 0 justified · fail_on=high · honestgreen 0.1.0</sub>
