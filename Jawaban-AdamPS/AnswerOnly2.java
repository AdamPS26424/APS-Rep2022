import java.util.*;
import java.io.*;


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