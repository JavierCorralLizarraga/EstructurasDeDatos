package CifradoCesar;

public interface QueueADT <T>{
     public void enqueue(T dato); 
     public T dequeue(); 
     public T first(); 
     public boolean isEmpty(); 
}
