class OrderedLists <T extends Comparable<T>> implements OrderedStructures <T> {

	private static class Node<T>{
		T payload;
		Node<T> previous;
		Node<T> next;
		public Node(T payload, Node<T> previous, Node<T> next){
			this.payload = payload;
			this.previous = previous;
			this.next = next;
		}
	}

	Node<T> head; 

	public OrderedLists(){

		head = new Node<T>(null,null,null);  //This is my dummmy node right here
		head.previous = head;
		head.next = head;

	}

	public int size(){
		int c = 0;
		Node<T> p = head;
		while(p.next != head){ //we get to reach all the way until the last element here
			c++;
			p = p.next;
		}
		return c;
	}

    public boolean add(T elem) throws IllegalArgumentException{
    	boolean completed = false;
    	if(head.next == head || head.previous.payload.compareTo(elem) <= 0){ //taking into account both cases for where one should add
    		Node<T> newElem = new Node<T>(elem, head.previous, head); //adding to the end of the end of the list here
    		head.previous.next = newElem;
    		head.previous = newElem; //making the correct new ties in these last two steps
    		completed = true;
    	}else{
    		throw new IllegalArgumentException();
    	}
    	return completed;
    	
    }


    public T get(int pos) throws IndexOutOfBoundsException{
    	Node<T> p = head;
    	for(int i =0; i<pos; i++){
    		p = p.next;
    		if(p==head){
    			throw new IndexOutOfBoundsException();
    		}
    	}
    	return p.payload;
    } 
    
    public void remove(int pos) throws IndexOutOfBoundsException{
    	Node<T> p = head;
    	for(int i = 0; i=pos; i++){
    		p = p.next;
    		if(p == head){
    			throw new IndexOutOfBoundsException();
    		}
    	}
    	///Now we should be on the element that we want to remove
    	p.previous.next = p.next;
    	p.next.previous = p.previous; 
    	p.next = null; //severing ties here
    	p.previous = null; //severing ties here
    }
}