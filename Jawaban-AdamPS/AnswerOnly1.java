import java.util.*;
import java.io.*;

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