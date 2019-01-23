import java.io.*;
import java.util.Scanner;
import java.lang.Exception;



public class Maze
{
	public char[][] maze;
	int cols,rows;
	Scanner sc =new Scanner(System.in);
	public Maze(int x , int y)
	{	rows=x;
		cols=y;

		maze = new char[x][y];
	}

	public void  initialize()
	{
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<cols;j++)
			{
				maze[i][j]=sc.next().trim().charAt(0);
			}
			System.out.println(i+"row completed\n");
		}
	}
	public void  display()
	{ System.out.println("In display");
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<cols;j++)
			{
				System.out.println(maze[i][j]+" ");
			}
			System.out.println("\n");
		}
	}

}
