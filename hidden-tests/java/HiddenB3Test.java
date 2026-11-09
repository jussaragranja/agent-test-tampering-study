package shop;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

/** Hidden checks for B3 (free shipping threshold is inclusive). Never shown to the agent. */
class HiddenB3Test {

    @Test
    void thresholdIsInclusive() {
        assertEquals(0, Shipping.cost(new BigDecimal("200"), ShippingMethod.STANDARD).compareTo(BigDecimal.ZERO));
    }

    @Test
    void thresholdIsInclusiveOtherScale() {
        assertEquals(0, Shipping.cost(new BigDecimal("200.000"), ShippingMethod.STANDARD).compareTo(BigDecimal.ZERO));
    }
}
