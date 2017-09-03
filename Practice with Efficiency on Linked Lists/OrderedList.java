class OrderedList implements OrderedStructure{
	
	public Node head;

	private static class Node{
		private Comparable payload;
		private Node previous;
		private Node next;
		private Node(Comparable payload, Node previous, Node next){
			this.payload = payload;
			this.previous = previous;
			this.next = next;
		}
	}

	

	public OrderedList(){
		head = new Node(null, null, null); //This is the dummy node
		head.next = head;
		head.previous = head;
	}

	public int size(){
		int c = 0;
		Node p = head;
		while(p.next != head){
			c++;
			p = p.next;	
		}
		return c;
	}

	public boolean add(Comparable element) throws IllegalArgumentException{
		if(element == null){
			throw new IllegalArgumentException();
		}

		boolean complete;
		Node temp = new Node(element, null, null);
		if(head.next == head || head.previous.payload.compareTo(element) <= 0){
			head.previous.next = temp;
			temp.previous = head.previous;
			head.previous = temp;
			temp.next = head;
			complete = true;
		}else{
			complete = false;
		}
		return complete;
	}

	public Object get(int pos) throws IndexOutOfBoundsException{
		Node p = head; //placed on the dummy node right now
		for(int i = 0; i < pos; i++){
			if(p.next == head){    //this implies that the poistion that you asked for does not exist unfortunately
				return null; 
			}else{
				p = p.next;
			}
		}

		return p.payload;
	}

	public void remove(int pos) throws IndexOutOfBoundsException{
		Node p =head; //placed on the dummy node
		if(pos == 0 ){
			throw new Error("Cannot remove dummy node");
		}
		for(int i = 0; i<pos; i++){
			if(p.next == head){
				throw new Error();
			}else{
				p = p.next;
			}
		}
		//If we've gotten to this part, then we are ON the node that we want to remove
		p.previous.next = p.next;
		p.next.previous = p.previous;
		p.next= null;
		p.previous = null; 

	}

	public void merge(OrderedList other){
		Comparable t1 = other.head.next.payload;
		Comparable t2 = head.next.payload;
		if(t2.compareTo(t1) <= 0 ){
			Node p = other.head.next;
			while(p != other.head){
				Node toAdd = new Node(p.payload, head.previous, head);
				head.previous.next = toAdd;
				head.previous = toAdd;
				p = p.next;
				
			}
		}else{
			Node p = head.next;
			while(p != head){
				Node toAdd = new Node(p.payload, other.head.previous, other.head);
				other.head.previous.next = toAdd;
				other.head.previous = toAdd;
				p = p.next;
			}
		}
	}



}