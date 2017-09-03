class OrderedListTest{

	public static void main(String args[]){
		OrderedList test1;
		test1 = new OrderedList();
		OrderedList test2;
		test2= new OrderedList();
		test1.add("C");
		System.out.println(test1.add("D"));
		test2.add("B");
		test1.merge(test2);
		//test1.get(2);
		//test.remove(1);
		//st.remove(1);
		System.out.println(test2.get(3));
	}
		
}