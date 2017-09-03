/**
 * ITI 1121. Introduction à l'informatique II (Hiver 2008).
 * ITI 1521. Introduction to Computer Science II (Winter 2008).
 *
 * @author Marcel Turcotte, Université d'Ottawa/University of Ottawa
 */
import java.lang.String.*;

public class Balanced {
    static Stack<Character> t;

    public static boolean algo1( String s ) {

        int curly = 0;
        int square = 0;
        int round = 0;

        for ( int i=0; i<s.length(); i++ ) {

            char c = s.charAt( i );

            switch ( c ) {
            case '{':
                curly++;
                break;
            case '}':
                curly--;
                break;
            case '[':
                square++;
                break;
            case ']':
                square--;
                break;
            case '(':
                round++;
                break;
            case ')':
                round--;
            }
        }
        return curly == 0 && square == 0 && round == 0;
    }
    @SuppressWarnings( "unchecked" )
    public static boolean algo2( String s ){
        t = new ArrayStack<Character>(100);
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == '{'){
                t.push('{');
             }
             else if(s.charAt(i) == '['){
                t.push('[');
             }
             else if(s.charAt(i) == '('){
                t.push('(');
             }
             else if(s.charAt(i) == ')' && t.peek() == '('){
                t.pop();
             }
             else if(s.charAt(i) == ']' && t.peek() == '['){
                t.pop();
             }
             else if(s.charAt(i) == '}' && t.peek() == '{'){
                t.pop();
             }


        }
        return t.isEmpty();
    }



    public static void main( String[] args ) {
        for ( int i=0; i<args.length; i++ ) {
            System.out.println( "algo1( \"" + args[ i ] + "\" ) -> " + algo2( args[ i ] ) );
        }
    }
}