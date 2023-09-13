import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class TrianguloTest {

    static String tipotriangulo4(int a, int b, int c){
        if (a <= 0 && b <= 0 && c <= 0){
            return "invalido";
        }
        if(a+b > c || a+c > b || b+c > a){
            if(a==b && b==c){
                return "equilatero";
            }
            if(a==b || a==c || b==c){
                return "isoceles";
            }
            return "escaleno";
        }
        return "invalido";
    }

    @Test
    public void testTipoTriangulo4Escaleno() {
        assertEquals("escaleno", tipotriangulo4(4, 2, 3));
    }

    @Test
    public void testTipoTriangulo4Isosceles() {
        assertEquals("isosceles", tipotriangulo4(4, 4, 2));
    }

    @Test
    public void testTipoTriangulo4Equilatero() {
        assertEquals("equilatero", tipotriangulo4(1, 1, 1));
    }

    @Test
    public void testTipoTriangulo4Invalido1() {
        assertEquals("invalido", tipotriangulo4(0, 1, 1));
    }

    @Test
    public void testTipoTriangulo4Invalido2() {
        assertEquals("invalido", tipotriangulo4(1, -1, 3));
    }

    @Test
    public void testTipoTriangulo4Invalido3() {
        assertEquals("invalido", tipotriangulo4(1, 2, "três"));
    }

    @Test
    public void testTipoTriangulo4Invalido4() {
        assertEquals("invalido", tipotriangulo4(2, 1, 1));
    }
}
