import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class TrianguloTest {

    public String tipoTriangulo8(int a, int b, int c) {
        int[] lados = {a, b, c};

        boolean valido = false;

        for (int lado : lados) {
            int[] aux = {a, b, c};
            aux[lado] = aux[2];

            if (lado > Math.abs(aux[0] - aux[1]) && lado < aux[0] + aux[1]) {
                valido = true;
                break;
            }
        }

        if (!valido || a <= 0 || b <= 0 || c <= 0) {
            return "invalido";
        }

        if (a == b && b == c) {
            return "equilatero";
        }
        if (a == b || b == c || a == c) {
            return "isosceles";
        }
        return "escaleno";
    }

    @Test
    public void testTipoTriangulo8Escaleno() {
        assertEquals("escaleno", tipoTriangulo8(4, 2, 3));
    }

    @Test
    public void testTipoTriangulo8Isosceles() {
        assertEquals("isosceles", tipoTriangulo8(4, 4, 2));
    }

    @Test
    public void testTipoTriangulo8Equilatero() {
        assertEquals("equilatero", tipoTriangulo8(1, 1, 1));
    }

    @Test
    public void testTipoTriangulo8Invalido1() {
        assertEquals("invalido", tipoTriangulo8(0, 1, 1));
    }

    @Test
    public void testTipoTriangulo8Invalido2() {
        assertEquals("invalido", tipoTriangulo8(1, -1, 3));
    }

    @Test
    public void testTipoTriangulo8Invalido3() {
        assertEquals("invalido", tipoTriangulo8(1, 2, "três"));
    }

    @Test
    public void testTipoTriangulo8Invalido4() {
        assertEquals("invalido", tipoTriangulo8(2, 1, 1));
    }
}
