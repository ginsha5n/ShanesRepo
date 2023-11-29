package Strategy;

public class DuckSim {

    public static void main(String[] args) {

        duck mallard = new MallardDuck();
        duck robot = new RobotDuck();
        duck rubberDuck = new RubberDuck();

        mallard.display();
        mallard.preformFly();
        mallard.preformQuack();

        robot.display();
        robot.preformFly();
        robot.preformQuack();

        rubberDuck.display();
        rubberDuck.preformFly();
        rubberDuck.preformQuack();
        rubberDuck.swim();
    }
    
}
