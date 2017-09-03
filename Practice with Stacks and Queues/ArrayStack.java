/**
 * ITI 1121. Introduction à l'informatique II (Hiver 2008).
 * ITI 1521. Introduction to Computer Science II (Winter 2008).
 *
 * @author Marcel Turcotte, Université d'Ottawa/University of Ottawa
 */


public class ArrayStack<E> implements Stack<E> {

    // Instance variables

    private E[] elems;  // Used to store the elements of this ArrayStack
    private int top;    // Designates the first free cell
    public static final int DEFAULT_INC = 25;
    private E[] elems1;

    @SuppressWarnings( "unchecked" )

    // Constructor

    public ArrayStack( int d ) {
        elems = (E[]) new Object[ d ];
        top = 0;
    }

    // Returns true if this ArrayStack is empty

    public boolean isEmpty() {

        // Same as:
        // if ( top == 0 ) {
        //     return true;
        // } else {
        //     return false;
        // }

        return ( top == 0 );
    }

    // Returns the top element of this ArrayStack without removing it

    public E peek() {

        // pre-conditions: ! isEmpty()
        if(!isEmpty()){
         return elems[ top-1 ];   
        }
        return elems[0];
    }

    // Removes and returns the top element of this stack

    @SuppressWarnings( "unchecked" )
    public E pop() {
        int c = 0;
        int index = 0;
        // pre-conditions: ! isEmpty()
        
        // *first* decrements top, then access the value!
        E saved = elems[ --top ];

        elems[ top ] = null; // scrub the memory!
       if((elems.length) - (top+1) == DEFAULT_INC){
           elems1 = (E[]) new Object[elems.length - DEFAULT_INC];
           for(int i =0; i<elems1.length; i++){
                elems1[i] = elems[i];
           }
           elems = elems1; 
       }        

        return saved;
    }


    public void printStack(){
        for(int i =0; i<elems.length; i++){
            System.out.println(elems[i]);

        }
        System.out.println(elems.length);
    }

    // Puts the element onto the top of this stack
    @SuppressWarnings( "unchecked" )
    public void push( E element ) {

        // Pre-condition: the stack is not full

        // *first* stores the element at position top, then increments top

        elems[ top++ ] = element;

          if(top == elems.length){
            elems1 = (E[]) new Object[elems.length + DEFAULT_INC];
            for(int i = 0; i<elems.length; i++){
                elems1[i] = elems[i];
            }
            elems = elems1;
        }

    }

    public void clear(){
        for(int i =0; i<elems.length; i++){
            elems[i] = null;
        }
    }



}