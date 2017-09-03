public class Iterative{

	public static BitList complement(BitList in){
		Iterator iter = in.iterator();
		BitList out = new BitList();
		while(iter.hasNext()){
			int toAdd = iter.next();
			if(toAdd == 0){
				out.addFirst(1);
			}else{
				out.addFirst(0);
			}
		}

		return out;
	}

	public static BitList or(BitList a , BitList b){
		if(a == null || b ==null || a.length()!= b.length()){
			throw new IllegalArgumentException();
		}
		if(a.length() != b.length()){
			throw new IllegalArgumentException();
		}
		BitList toReturn = new BitList();
		Iterator toReturnIt = toReturn.iterator();
		Iterator ait = a.iterator();
		Iterator bit = b.iterator();
		while(ait.hasNext()){
			int abit = ait.next();
			int bbit = bit.next();
			if(abit == 1 || bbit == 1){
				toReturnIt.add(1);
			}else{
				toReturnIt.add(0);
			}
			
		}
		return toReturn;
	}

	public static BitList and(BitList a, BitList b){
		if(a == null || b == null){
			throw new IllegalArgumentException();
		}

		if(a.length() != b.length()){
			throw new IllegalArgumentException();
		}

		Iterator aIt = a.iterator();
		Iterator bIt = b.iterator();
		BitList c = new BitList();
		Iterator cIt = c.iterator();
		while(	aIt.hasNext()	){
			int aINT = aIt.next();
			int bINT = bIt.next();
			if(aINT == 1 && bINT == 1){
				cIt.add(1);
			}else{
				cIt.add(0);
			}
		}
		return c;
	}

	public static void main(String args[]){
		BitList test = new BitList("10001");
		BitList test1 = new BitList("00011");
		BitList answer = and(test, test1);
		System.out.println(answer);
	}

	}

