### Title04_01
1. Circle
````java

public class Circle {
 	private	double radius;
 	
	public void setRadius(double _radius) {
		radius = _radius;
	}
	public double getRadius() {
		return radius;
	}
	public double getArea() {
		return radius*radius*3.141926;
	}
	public double getPerimeter() {
		return radius*2*3.1415926;
	}	
}
````
2. Rectangle
````java

public class Rectangle {
	private double length;
	private double width;
	public void setLength(double _length) {
		length = _length;
	}
	public double getLength() {
		return length;
	}
	public void setWidth(double _width) {
		width = _width;
	}
	public double getwidth() {
		return width;
	}
	public double getArea() {
		return length*width;
	}
	public double getPerimeter() {
		return (length+width)*2;
	}
}
````
3. Square
````java

public class Square {
	private double  sideLength;
	public void setSideLength(double _sideLength) {
		sideLength = _sideLength;
	}
	public double getSideLength() {
		return sideLength;
	}
	public double getArea() {
		return sideLength*sideLength;
	}
	public double getPerimeter() {
		return sideLength*4;
	}
}
````
4. Test
````java

public class Test {

	public static void main(String[] args) {
		Circle a1 = new Circle();
		a1.setRadius(2);
		System.out.println(a1.getArea());
		System.out.println(a1.getPerimeter());
		
		Square a2 = new Square();
		a2.setSideLength(2);
		System.out.println(a2.getArea());
		System.out.println(a2.getPerimeter());
		
		Rectangle a3 = new Rectangle();
		a3.setWidth(1); 
		a3.setLength(2);
		System.out.println(a3.getArea());
		System.out.println(a3.getPerimeter());
		
	}
}
````
### Title_03
1. Point
````java

public class Point {
	private double x;
	private double y;
	public Point(double x,double y) {
		this.x = x;
		this.y = y;
	}
	public double getX() {
		return x;
	}
	public void setX(double x) {
		this.x = x;
	}
	public double getY() {
		return y;
	}
	public void setY(double y) {
		this.y = y;
	}
//	相等为1不等为0；
	public int equals(Point b) {
		if (this.x == b.x && this.y == b.y ) {
			return 1;
		}else {
			return 0;
		}		
	}
}
````
2. Line 
````java
public class Line {
	private Point a;
	private Point b;
	public Line(Point _a,Point _b) {
		this.a = _a;
		this.b = _b;
	}
	public Point getA() {
		return a;
	}
	public void setA(Point a) {
		this.a = a;
	}
	public void setA(double x,double y) {
		a.setX(x);
		a.setY(y);
	}
	public Point getB() {
		return b;
	}
	public void setB(Point b) {
		this.b = b;
	}
	public void setB(double x,double y) {
		b.setX(x);
		b.setY(y);
	}
	public double getLength() {
		return Math.sqrt((a.getX()-b.getX())*(a.getX()-b.getX())+(a.getY()-b.getY())*(a.getY()-b.getY()));
	}
//	两线平行或重合为1，其余为0
	public int collinear(Line l2) {
		if((this.a.getX()-this.b.getX()) * (l2.a.getY()-l2.b.getY() ) == 
				(this.a.getY()-this.b.getY())*(l2.a.getX()-l2.b.getX())) {
			return 1;
		}else {
			return 0;
		}
	}
}
````
3. Triangle
````java

public class Triangle {
	private Line l1;
	private Line l2;
	public Triangle(Point p1,Point p2,Point p3) {
			Line l1 = new Line(p1,p2);
			Line l2 = new Line(p1,p3);
			if(l1.collinear(l2)==1){
				System.out.println("Two line collinear");
			}else if(l1.getA().equals(l2.getA())==1||l1.getA().equals(l2.getB())==1||l1.getB().equals(l2.getA())==1||l1.getB().equals(l2.getB())==1) {
				this.l1 = l1;
				this.l2 = l2;
			}else {
				System.out.println("Wrong Example");
			}	
	}
	public Triangle(Line l1,Line l2) {
		if(l1.collinear(l2)==1){
			System.out.println("Two line collinear");
		}else if(l1.getA().equals(l2.getA())==1||l1.getA().equals(l2.getB())==1||l1.getB().equals(l2.getA())==1||l1.getB().equals(l2.getB())==1) {
			this.l1 = l1;
			this.l2 = l2;
		}else {
			System.out.println("Wrong Example");
		}
	}
	public Triangle() {
		Point p1 = new Point(0,0);
		Point p2 = new Point(1,1);
		Point p3 = new Point(0,1);
		Line l1 = new Line(p1,p2);
		Line l2 = new Line(p1,p3);
		this.l1 = l1;
		this.l2 = l2;
	}
	
	public Line getL1() {
		return l1;
	}
	public void setL1(Line l1) {
		this.l1 = l1;
	}
	public Line getL2() {
		return l2;
	}
	public void setL2(Line l2) {
		this.l2 = l2;
	}
	public double L3Length() {
		if(l1.getA().getX()==l2.getA().getX()&&l1.getA().getY()==l2.getA().getY()) {
//			System.out.println("l1.start==l2.start");
			return Math.sqrt((l1.getB().getX()-l2.getB().getX())*(l1.getB().getX()-l2.getB().getX())+(l1.getB().getY()-l2.getB().getY())*(l1.getB().getY()-l2.getB().getY()));
		}else if(l1.getB().getX()==l2.getB().getX()&&l1.getB().getY()==l2.getB().getY()){
//			System.out.println("l1.end==l2.end");
			return Math.sqrt((l1.getA().getX()-l2.getA().getX())*(l1.getA().getX()-l2.getA().getX())+(l1.getA().getY()-l2.getA().getY())*(l1.getA().getY()-l2.getA().getY()));
		}else if(l1.getA().getX()==l2.getB().getX()&&l1.getA().getY()==l2.getB().getY()) {
//			System.out.println("l1.start==l2.end");
			return Math.sqrt((l1.getB().getX()-l2.getA().getX())*(l1.getB().getX()-l2.getA().getX())+(l1.getB().getY()-l2.getA().getY())*(l1.getB().getY()-l2.getA().getY()));
		}else {
//			System.out.println("l1.end==l2.start");
			return Math.sqrt((l1.getA().getX()-l2.getA().getX())*(l1.getA().getX()-l2.getA().getX())+(l1.getB().getY()-l2.getB().getY())*(l1.getB().getY()-l2.getB().getY()));
		}			
	}
	public double getCircumference() {
		return l1.getLength()+l2.getLength()+L3Length();
	}
}

````
4.Test
````java

public class Title04_3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Point p1 = new Point(0,0);
		Point p2 = new Point(1,1);
		Point p3 = new Point(0,1);
		Line l1 = new Line(p1,p2);
		Line l2 = new Line(p1,p3);
		System.out.println("有1个接收3个点类对象作为参数的构造方法");
		Triangle t1 = new Triangle(p1,p2,p3);
		System.out.println(t1.getCircumference());
		System.out.println("有1个接收2个线段类对象作为参数的构造方法");
		Triangle t2 = new Triangle(l1,l2);	
		System.out.println(t2.getCircumference());
		System.out.println("有1个无参构造方法:");
		Triangle t3 = new Triangle();
		System.out.println(t3.getCircumference());

	}

}
````

