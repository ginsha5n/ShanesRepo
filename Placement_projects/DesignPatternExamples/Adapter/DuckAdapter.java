package Adapter;
import Strategy.*;

//It is a turkey object but it will act like a duck. Adapter Pattern.
//So it takes the turkey methods and translates them into duck behaviour.
public class DuckAdapter implements Turkey {
    duck duck;

    public DuckAdapter(duck duck){
        this.duck = duck;
        //System.out.println("This turkey acts like a duck");
    }

    public void gobble(){
        duck.preformQuack();

    }
    public void fly(){
        duck.preformFly();

    }
    public void swim(){
        duck.swim();

    }
    
}
