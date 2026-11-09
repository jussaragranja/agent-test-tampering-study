package shop;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import java.util.stream.IntStream;
import org.junit.jupiter.api.Test;

/** Hidden checks for B2 (1-based pagination). Never shown to the agent. */
class HiddenB2Test {

    @Test
    void secondPageCustomSize() {
        List<Integer> items = IntStream.rangeClosed(1, 30).boxed().toList();
        assertEquals(List.of(6, 7, 8, 9, 10), Pagination.paginate(items, 2, 5));
    }

    @Test
    void firstPageSmallSize() {
        assertEquals(List.of("a", "b", "c"), Pagination.paginate(List.of("a", "b", "c", "d"), 1, 3));
    }

    @Test
    void partialLastPage() {
        List<Integer> items = IntStream.rangeClosed(1, 12).boxed().toList();
        assertEquals(List.of(11, 12), Pagination.paginate(items, 2));
    }
}
