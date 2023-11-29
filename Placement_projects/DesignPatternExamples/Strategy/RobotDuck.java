package Strategy;

import Strategy.Flying.FlyNoWay;
import Strategy.Quack.beep;

public class RobotDuck extends duck{

    public RobotDuck(){
        flybehaviour = new FlyNoWay();
        quackbehaviour = new beep();
    }

    

    public void display(){
        System.out.println("I AM A ROBOT DUCK");
    }
}





