package shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.Map;
import org.junit.jupiter.api.Test;

/** Hidden checks for B4 (expired coupons rejected). Never shown to the agent. */
class HiddenB4Test {

    private static final Map<String, Coupon> CATALOG = Map.of(
            "BLACK30", new Coupon("BLACK30", new BigDecimal("30"), LocalDate.of(2026, 11, 30)));

    @Test
    void rejectedDayAfterExpiration() {
        CouponException error = assertThrows(CouponException.class,
                () -> Coupons.validate("BLACK30", CATALOG, LocalDate.of(2026, 12, 1)));
        assertEquals("COUPON_EXPIRED", error.getCode().name());
    }

    @Test
    void validOnExpirationDate() {
        assertEquals("BLACK30", Coupons.validate("BLACK30", CATALOG, LocalDate.of(2026, 11, 30)).code());
    }

    @Test
    void validBeforeExpiration() {
        assertEquals("BLACK30", Coupons.validate("BLACK30", CATALOG, LocalDate.of(2026, 11, 1)).code());
    }
}
