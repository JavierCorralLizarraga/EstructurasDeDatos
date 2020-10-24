package CifradoCesar;

public class EmptyCollectionException extends RuntimeException {
    public EmptyCollectionException(){
        super("La colección está vacía");
    }
    public EmptyCollectionException(String mensaje){
        super("La colección está vacía: " + mensaje); // para que es este constructor?
    }
}
