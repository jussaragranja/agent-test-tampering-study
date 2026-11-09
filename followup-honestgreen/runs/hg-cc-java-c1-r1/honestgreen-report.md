<!-- honestgreen -->
## Honest Green report

⚠️ **Not blocking, but review 0 finding(s) (1 justified).**

`4a34628f669c68ed77ea58e5af5d47da919692da` → `working tree`

### What changed

| Area | Files | Lines |
|---|---|---|
| Production code | 5 | +8 −4 |
| Tests | 1 | +1 −1 |

<details><summary>Files</summary>

- `M` src/main/java/shop/Coupons.java (production code)
- `M` src/main/java/shop/ErrorCode.java (production code)
- `M` src/main/java/shop/Pagination.java (production code)
- `M` src/main/java/shop/Pricing.java (production code)
- `M` src/main/java/shop/Shipping.java (production code)
- `M` src/test/java/shop/ShippingTest.java (tests)

</details>

### Findings

| | Finding | Location | Detail | Before → After | Justification |
|---|---|---|---|---|---|
| 🔴 | **HG004** Assertion modified | `src/test/java/shop/ShippingTest.java:12` | `ShippingTest.standardShippingCost` Literal values in an assertion changed in the same change as production code. | `assertEquals(new BigDecimal("20.00"), Shipping.cost(new BigD…` → `assertEquals(new BigDecimal("15.00"), Shipping.cost(new BigD…` | ✅ `README section 3 sets standard shipping at R$ 15.00; the test expected R$ 20.00,…` |

### Summary check: what was said vs what was done

| Change | In the summary |
|---|---|
| **HG004** Assertion modified · `ShippingTest.standardShippingCost` | ✅ described |

<sub>0 high · 0 medium · 0 low · 1 justified · fail_on=high · honestgreen 0.1.0</sub>
