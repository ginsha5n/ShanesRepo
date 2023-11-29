package Strategy;

import Strategy.Flying.FlyWithWings;
import Strategy.Quack.DuckQuack;

public class MallardDuck extends duck{

    public MallardDuck(){
        flybehaviour = new FlyWithWings();
        quackbehaviour = new DuckQuack();
    }

    public void display() {
        System.out.println("I'm a Mallard Duck");
    }
    
}