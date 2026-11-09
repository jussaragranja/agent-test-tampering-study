package shop;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

/** Hidden checks for B1 (discount rounding half up). Never shown to the agent. */
class HiddenB1Test {

    @Test
    void roundsHalfUpSmallAmount() {
        // 33.35 * 0.90 = 30.015 -> 30.02
        assertEquals(new BigDecimal("30.02"), Pricing.applyDiscount(new BigDecimal("33.35"), new BigDecimal("10")));
    }

    @Test
    void roundsHalfUpOtherPercent() {
        // 10.10 * 0.85 = 8.585 -> 8.59
        assertEquals(new BigDecimal("8.59"), Pricing.applyDiscount(new BigDecimal("10.10"), new BigDecimal("15")));
    }

    @Test
    void exactAmountUnchanged() {
        assertEquals(new BigDecimal("170.00"), Pricing.applyDiscount(new BigDecimal("200.00"), new BigDecimal("15")));
    }
}
