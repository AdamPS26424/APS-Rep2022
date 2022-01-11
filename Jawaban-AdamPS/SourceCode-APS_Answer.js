import java.util.*;
import java.io.*;
//Question 1
class Student {
  public String name;
  public List<Sport> sports;
}
enum Sport {
  BASKETBALL,
  SOCCER, 
  SWIMMING, 
  E_SPORT, 
  CHESS,
  OTHER
}
//Question 2 with 5x+2y = 7 so the answer is = 5(1) + 2(1) = 7
class Param {
  public int x;
  public int y;
  //Part of answer 2
  public Param(){
	  x = 0;
	  y = 0;
  }
  public Param (int X, int Y){
	  x = X;
	  y = Y;
  }
}
//Question 3
class Node
{
  public int value;
  public Node next;
  public Node(int value)
  {
    this.value = value;
    next = null;
  }
}
class OurList
{
  Node head;
  int length;
  public OurList()
  {
    head = null;
    length = 0;
  }
  //Logic is (10,20,30,40) -> (40,10,20,30)
  public void rotateRight() {
		//Answer 3
		if (head == null)
		{return;}
		Node tmp = head;
		while (tmp.next != null){
			tmp = tmp.next;
		}
		Node temp = tmp;
		tmp.next = head;
		head = tmp;
		tmp = head;
		while (tmp.next != temp){
			tmp = tmp.next;
		}
		tmp.next = null;
  }
}

public class Main {
//Answer 1
  public List<Student> getStudentsWhoLoveBasketballAndSoccer(List<Student> students) {
  List<Student> answer = new ArrayList<Student>();
  for (int i = 0; i < students.size(); i++){
	  if (students.get(i).sports.contains(Sport.BASKETBALL) && students.get(i).sports.contains(Sport.SOCCER))
		{answer.add(students.get(i));}
  }
  return answer;
}
  public List<Student> getStudentsWhoLoveBasketballOrSwimming(List<Student> students) {
  List<Student> answer = new ArrayList<Student>();
  for (int i = 0; i < students.size(); i++){
	  if (students.get(i).sports.contains(Sport.BASKETBALL) || students.get(i).sports.contains(Sport.SWIMMING))
		{answer.add(students.get(i));}
  }
  return answer;
}
  public List<Student> getStudentsWhoOnlyLoveSoccer(List<Student> students) {
  List<Student> answer = new ArrayList<Student>();
  for (int i = 0; i < students.size(); i++){
	  if (students.get(i).sports.contains(Sport.SOCCER) && students.get(i).sports.size() == 1)
		{answer.add(students.get(i));}
  }
  return answer;
}
//End of Answer 1
//Answer 2
public Param getParamFor5x2y7() {
  int minX = -5;
  int maxX = 5;
  int minY = -5;
  int maxY = 5;
  
  int ansX = -6;
  int ansY = -6;
  for (int i = minX; i <= maxX; i++){
	  ansX = i;
	  for (int j = minY; j <= maxY; j++){
		  ansY = j;
		  if ((5*ansX + 2*ansY) == 7){
		  return new Param(ansX,ansY);}
	  }
  }
	return new Param(ansX,ansY);
}
//End of Answer 2
	public static void main(String[] args){
		// Prints "Hello, World" to the terminal window.
		System.out.println("Hello, World");
	}
}