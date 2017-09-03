class OrderedListsNoDummmyNode <T extends Comparable<T>> implements OrderedStructures<T>{
	Node<T> head;

	private class Node<T>{
		T payload;
		Node<T> next;
		Node<T> previous;
		public Node(T payload, Node<T> next, Node<T> previous){
			this.payload = payload;
			this.previous = previous;
			this.next = next;
		}	
	}

	public OrderedListsNoDummmyNode(){
		head = null;
	}

	public int size(){
		int c;
		Node<T> p = head;
		if(p == null){
			c = 0;
		}else if(p.next == head){
			c= 1;
		}else{
			c=1;
			while(p.next != head){ //the orderedlist should still be circular
				c++;
				p = p.next;
			}
		}

		return c;
	}

    public boolean add(T elem) throws IllegalArgumentException{
    	//only two special cases here 
    	boolean completed = false;
    	if(head == null){
    		head = new Node<T>(elem, head, head);
    		head.previous = head;
    		head.next = head;
    		completed = true;
    	}else{
    		if(head.previous.payload.compareTo(elem) <= 0){
    			Node<T> toAdd = new Node<T>(elem, head.previous, head);
    			head.previous.next = toAdd;
    			head.previous = toAdd;
    			completed = true;
    		}
    	}
    	return completed;	
    }

    //I stopped here
    public T get(int pos) throws IndexOutOfBoundsException{
    	Node<T> p = head;
    	if(p == null){
    		throw new IndexOutOfBoundsException();
    	}else if(pos == 1){
    		return p.next.payload;
    	}else{
    		for(int i =0; i<pos; i++){
    			p = p.next;
    			if(p==head){
    				throw new IndexOutOfBoundsException();
    		}
    		}

    	}

    	return p.payload;
    } 
    
    public void remove(int pos) throws IndexOutOfBoundsException{
    	Node<T> p = head;
    	for(int i = 0; i<pos; i++){
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