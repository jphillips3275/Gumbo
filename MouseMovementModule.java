//information for how Robot works: https://www.javatpoint.com/java-robot
//used for moving the mouse
import java.awt.AWTException;
import java.awt.Robot;

//used for determining mouse position
import java.awt.MouseInfo;
import java.awt.Point;

public class MouseMovementModule {
    public static void main(String... args) throws AWTException {
        Robot robot = new Robot();
        robot.mouseMove(400, 400); //moves the mouse to the given coordinates

        Point p = MouseInfo.getPointerInfo().getLocation();
        int x = p.x;
        int y = p.y;
        System.out.println("Mouse x = " + x + " Mose y = " + y);
    }
}