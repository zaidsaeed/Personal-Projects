//                              -*- Mode: Java -*- 
// BitList.java --- data structure to store a sequence of bits (ints)
// Author          : Marcel Turcotte
// Created On      : Fri Apr  9 09:00:27 2004
// Last Modified By: Marcel Turcotte
// Last Modified On: Fri Mar 24 10:00:36 2006

// Unlike the list of the current assignment, this one 1) does not
// detect concurrent modifications and 2) does not start with a dummmy
// node.

import java.util.NoSuchElementException;

// Stores the bits in reverse order!

public class BitList {

    // useful constants

    public static final int ZERO = 0;
    public static final int ONE = 1;

    // instance variables

    private Node first;

    // constructors

    public BitList() {  
        first = null;
    }

    public BitList( String s ) {
        Iterator iter = iterator();
        String input = s;
        if(s == null){
            throw new NullPointerException();
        }
        char[] charachters = input.toCharArray();
        for(int i =(charachters.length-1); i>=0; i-- ){
            char c = charachters[i];
            int x = Character.getNumericValue(c);
            //System.out.println(x);
            if(x != 0 && x!= 1 ){
                throw new IllegalArgumentException();
            }
            iter.add(x);
        }
    }

    public int length(){
        int length = 0;
        Iterator iter = this.iterator();
        while( iter.hasNext() ){
            length++;
            iter.next();
        }
        return length;
    }


    public static void main(String args[]){
        BitList test = new BitList("1001");
        System.out.println(test.length());
    }

    public void addFirst( int bit ) {

        if ( ( bit != ZERO ) && ( bit != ONE ) ) {
            throw new IllegalArgumentException( Integer.toString( bit ) );
        }

        first = new Node( bit, first );
    }

    public int removeFirst() {

        if ( first == null ) {
            throw new NoSuchElementException();
        }

        int saved = first.bit;

        first = first.next;

        return saved;
    }

    public Iterator iterator() {
        return new BitListIterator();
    }

    public String toString() {

        String str = "";

        if ( first == null ) {

            str += ZERO;

        } else {

            Node p = first;

            while ( p!=null ) {
                str = p.bit + str; // reverses the order!
                p = p.next;
            }

        }
        return str;
    }

    // The implementation of the nodes (static nested class)

    private static class Node {

        private int bit; // <- NEW
        private Node next;

        private Node( int bit, Node next ) { // <- ACCORDINGLY ...
            this.bit = bit;
            this.next  = next;
        }
    }

    // The implementation of the iterators (inner class)

    private class BitListIterator implements Iterator {

        private Node current = null;

        private BitListIterator() {
            current = null;
        }

        public boolean hasNext() {
            return ( ( current == null && first != null )   ||
                     ( current != null && current.next != null ) );
        }

        public int next() {

            if ( current == null ) {
                current = first ;
            } else {
                current = current.next ; // move the cursor forward
            }

            if ( current == null ) {
                throw new NoSuchElementException() ;
            }

            return current.bit ;
        }

        public void add( int bit ) {

            if ( ( bit != ZERO ) && ( bit != ONE ) ) {
                throw new IllegalArgumentException( Integer.toString( bit ) );
            }

            Node newNode;

            if ( current == null ) {
                first = new Node( bit, first );
                current = first;
            } else {
                current.next = new Node( bit, current.next );
                current = current.next;
            }
        }
    }
}