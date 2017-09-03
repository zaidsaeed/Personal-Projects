class OrderedListGenericsTest{
	public static void main(String args[]){
		OrderedLists <Integer> t = new OrderedLists<Integer>();
		System.out.println(t.size());
		t.add(5);
		t.add(6);
		System.out.println(t.size());
		System.out.println(t.get(0));
	}
}