public class BinarySearchTree< E extends Comparable<E> > {

    // A static nested class used to store the elements of this tree

    private static class Node<E> {
        private E value;
        private Node<E> left;
        private Node<E> right;
        private Node( E value ) {
            this.value = value;
            left = null;
            right = null;
        }
    }

    private Node<E> root = null;
    
    /**
     * Inserts an object into this BinarySearchTree.
     *
     * @param obj item to be added
     * @return true if the object has been added and false otherwise
     */

    public boolean add( E obj ) {

        // pre-condtion:

        if ( obj == null ) {
            throw new IllegalArgumentException( "null" );
        }

        // special case:

        if ( root == null ) {
            root = new Node<E>( obj );
            return true;
        }

        // general case:

        return add( obj, root );
    }

    private boolean add( E obj, Node<E> current ) {

        boolean result;
        int test = obj.compareTo( current.value );

        if ( test == 0 ) {
            result = false;
        } else if ( test < 0 ) {
            if ( current.left == null ) {
                current.left = new Node<E>( obj );
                result = true;
            } else {
                result = add( obj, current.left );
            }
        } else {
            if ( current.right == null ) {
                current.right = new Node<E>( obj );
                result = true;
            } else {
                result = add( obj, current.right );
            }
        }
        return result;
    }

    /**
     * Looks up for obj in this BinarySearchTree, returns true
     * if obj is found and false otherwise.
     *
     * @param obj value to look for
     * @return true if the object has been found and false otherwise
     */

    public boolean contains( E obj ) {

        // pre-condtion:

        if ( obj == null ) {
            throw new IllegalArgumentException( "null" );
        }

        return contains( obj, root );
    }

    private boolean contains( E obj, Node<E> current ) {

        boolean result;

        if ( current == null ) {

            result = false;

        } else {

            int test = obj.compareTo( current.value );

            if ( test == 0 ) {

                result = true;

            } else if ( test < 0 ) {

                result = contains( obj, current.left );

            } else {

                result = contains( obj, current.right );

            }
        }
        return result;
    }

    // Implement the method max()
    public E max() {

        if (root == null){
            throw new NullPointerException();
        }

        return max(root);
    }

    private E max(Node<E> current){
        //base case
        E result;
        if(current.right == null){
            result = current.value;
        }else{
            result = max(current.right);
        }
        return result;
    }

    public static void main(String args[]){
        BinarySearchTree test = new BinarySearchTree();
        test.add(6);
        test.add(2);
        test.add(0);
        test.add(5);
        test.add(10);
        test.add(7);
        test.add(15);
        System.out.println( test.isTwoTree() );
    }
    
    // Implement the method min()
    public E min(){
        if (root == null){
            throw new NullPointerException();
        }
        return min(root);
    }


    private E min(Node<E> current){
        E result;
        if(current.left == null){
            result = current.value;
        }else{
            result = min(current.left);
        }
        return result;
    }
    
    // Implement the method depth()
    public int depth() {
        if (root == null){
            throw new NullPointerException();
        }
        return depth(root);
    }

    private int depth(Node<E> current){
        int count = 0;
        if(current.left == null && current.right == null){
            return count;
        }
        else if(current.left == null && current.right != null){
            count = 1 + depth(current.right);
        }else if(current.left != null && current.right == null){
            count = 1 + depth(current.left);
        }else{
            int a = 1 + depth(current.left);
            int b = 1 + depth(current.right);
            if(a > b){
                count = a;
            }else{
                count = b;
            }
        }
        return count;

    }
    
    // Implement the method isTwoTree()
    public boolean isTwoTree() {
        return isTwoTree(root);
    }

    private boolean isTwoTree(Node<E> current){
        boolean retina;
        if(current == null){
            retina = true;
        }else if( (current.right != null && current.left ==null) || (current.right ==null && current.left != null)   ){
            retina = false;
        }else{
            boolean a = isTwoTree(current.left);
            boolean b = isTwoTree(current.right);
            if(a && b){
                retina = true;
            }else{
                retina = false;
            }
        }
        return retina;

    }

    
    public String toString() {
        return toString( root );
    }

    private String toString( Node<E> current ) {

        if ( current == null ) {
            return "()";
        }

        return "(" + toString( current.left ) + current.value + toString( current.right ) + ")";
    }

}