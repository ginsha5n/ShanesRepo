package Adapter;
import Strategy.*;

public class Main {
    public static void main(String[] args) {

        Turkey turkey = new WildTurkey();
        duck mallard = new MallardDuck();

        duck turkeyToDuckAdapter = new TurkeyAdapter(turkey);
        Turkey duckToTurkeyAdapter = new DuckAdapter(mallard);

        turkey.gobble();
        System.out.println("This is a turkey \n");

        mallard.preformQuack();
        System.out.println("This is a duck \n");

        turkeyToDuckAdapter.preformQuack();
        System.out.println("This is a duck pretending to be a turkey \n");

        duckToTurkeyAdapter.gobble();
        System.out.println("This is a turkey pretending to be a duck \n");






        
    }
    
}
