class Rectangle {
    double height = 1.0;
    double width = 1.0;


    Rectangle() {}


    Rectangle(double newl, double new2) {
        height = newl;
        width = new2;
    }
	
	double area(){
		return width * height;
	}
}

 public class ex21 {
	 
    public static void main(String[] args) {

        Rectangle myRect = new Rectangle(4, 5);
        System.out.println("myRect's area is " + myRect.area());
    }
}
