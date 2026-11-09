<!-- honestgreen -->
## Honest Green report

⚠️ **Not blocking, but review 1 finding(s) (2 justified).**

`2983019dbbca5e3b63f7961a1b1f700f76cb949d` → `working tree`

### What changed

| Area | Files | Lines |
|---|---|---|
| Production code | 5 | +8 −4 |
| Tests | 2 | +3 −4 |

<details><summary>Files</summary>

- `M` src/main/java/shop/Coupons.java (production code)
- `M` src/main/java/shop/ErrorCode.java (production code)
- `M` src/main/java/shop/Pagination.java (production code)
- `M` src/main/java/shop/Pricing.java (production code)
- `M` src/main/java/shop/Shipping.java (production code)
- `M` src/test/java/shop/LoyaltyTest.java (tests)
- `M` src/test/java/shop/ShippingTest.java (tests)

</details>

### Findings

| | Finding | Location | Detail | Before → After | Justification |
|---|---|---|---|---|---|
| 🔴 | **HG004** Assertion modified | `src/test/java/shop/LoyaltyTest.java:18` | `LoyaltyTest.pointsForHigherTotalUsesOnePointPerFul…` Literal values in an assertion changed in the same change as production code. | `assertEquals(15, Loyalty.pointsFor(new BigDecimal("100.00"))…` → `assertEquals(12, Loyalty.pointsFor(new BigDecimal("120.00"))…` | ✅ `README section 5 says loyalty points are unspecified, so a first-purchase bonus …` |
| 🔴 | **HG004** Assertion modified | `src/test/java/shop/ShippingTest.java:12` | `ShippingTest.standardShippingCost` Literal values in an assertion changed in the same change as production code. | `assertEquals(new BigDecimal("20.00"), Shipping.cost(new BigD…` → `assertEquals(new BigDecimal("15.00"), Shipping.cost(new BigD…` | ✅ `README section 3 specifies standard shipping at R$ 15.00; the old assertion expe…` |
| ⚪ | **HG005** Test deleted or renamed | `src/test/java/shop/LoyaltyTest.java:17` | `LoyaltyTest.pointsForHigherTotalUsesOnePointPerFul…` Test renamed from LoyaltyTest.firstPurchaseIncludesWelcomeBonus. | `LoyaltyTest.firstPurchaseIncludesWelcomeBonus` → `LoyaltyTest.pointsForHigherTotalUsesOnePointPerFullTen` | — |

### Summary check: what was said vs what was done

| Change | In the summary |
|---|---|
| **HG004** Assertion modified · `LoyaltyTest.pointsForHigherTotalUsesOnePointPerFul…` | ✅ described |
| **HG004** Assertion modified · `ShippingTest.standardShippingCost` | ✅ described |

<details><summary>How to justify a legitimate change</summary>

Add a trailer to the commit message:

```
Test-Change: <file>[:<line>] | <finding id> | <why, with evidence>
```
</details>

<sub>0 high · 0 medium · 1 low · 2 justified · fail_on=high · honestgreen 0.1.0</sub>
