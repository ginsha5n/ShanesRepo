package Strategy;

import Strategy.Flying.FlyNoWay;
import Strategy.Quack.Squeak;

public class RubberDuck extends duck{

    public RubberDuck(){
        flybehaviour = new FlyNoWay();
        quackbehaviour = new Squeak();
    }

    public void display(){
        System.out.println("I'm a rubber duck");
        
    }
}