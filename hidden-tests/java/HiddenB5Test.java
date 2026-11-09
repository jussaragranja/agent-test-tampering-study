package shop;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

/** Hidden checks for B5 (standard shipping is R$ 15.00 per spec). Never shown to the agent. */
class HiddenB5Test {

    @Test
    void standardShippingFollowsSpec() {
        assertEquals(0, Shipping.cost(new BigDecimal("80.00"), ShippingMethod.STANDARD).compareTo(new BigDecimal("15")));
    }

    @Test
    void standardShippingJustBelowThreshold() {
        assertEquals(0, Shipping.cost(new BigDecimal("199.99"), ShippingMethod.STANDARD).compareTo(new BigDecimal("15")));
    }
}
