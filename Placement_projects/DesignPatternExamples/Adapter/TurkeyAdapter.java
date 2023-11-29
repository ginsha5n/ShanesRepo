package Adapter;
import Strategy.*;
import Strategy.Flying.*;
import Strategy.Quack.*;

// This adapts a duck to behave like a turkey
public class TurkeyAdapter extends duck {
    Turkey turkey;
    

    public void display(){
        
    }
    public TurkeyAdapter(Turkey turkey){
        this.turkey = turkey;
        flybehaviour = new FlyWithWings();
        quackbehaviour = new DuckQuack();
        
    }

    public void preformQuack(){
        turkey.gobble();
    }
    public void preformFly(){
        turkey.fly();
    }

    public void swim(){
        turkey.swim();
    }
    

    


}