import java.util.*;
import java.io.*;


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