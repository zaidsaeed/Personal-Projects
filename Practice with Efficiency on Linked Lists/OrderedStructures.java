public interface OrderedStructures <T extends Comparable<T>> { 
    int size(); 
    boolean add(T elem) throws IllegalArgumentException; 
    T get(int pos) throws IndexOutOfBoundsException; 
    void remove(int pos) throws IndexOutOfBoundsException; 
}