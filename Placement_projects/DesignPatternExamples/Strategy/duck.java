package Strategy;

import Strategy.Flying.FlyBehaviour;
import Strategy.Quack.QuackBehaviour;

public abstract class duck {

    protected FlyBehaviour flybehaviour;
    protected QuackBehaviour quackbehaviour;

    public duck() {

    }

    public void setFlyBehaviour(FlyBehaviour fb) {
        flybehaviour = fb;
    }

    public void setQuackBehaviour(QuackBehaviour qb) {
        quackbehaviour = qb;
    }

    public void preformFly() {
        flybehaviour.fly();
    }

    public void preformQuack() {
        quackbehaviour.quack();
    }

    public void swim() {
        System.out.println("I'm Swimming");
    }

    public abstract void display();
}
