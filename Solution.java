public class Solution extends Maze
{	int startx,starty,endx=-1,endy=-1;
	public Solution(int x,int y)
	{
		super(x,y);
	}

	public void findStart()
	{	System.out.println("In findStart");
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<cols;j++)
			{
				if(maze[i][j]=='e')
				{
					startx=i;
					starty=j;
					break;
				}

			}
		}
	}
	public void findEnd()
	{System.out.println("In findEnd\n");
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<cols;j++)
			{
				if(maze[i][j]=='x')
				{
					endx=i;
					endy=j;
					break;
				}

			}
		}
	}

	public void findPath()
	{System.out.println("In find path");
		String sol[][] ={};
		int i=startx,j=starty;
		if((endx!=-1))
		{
		while(maze[i][j]!=maze[endx][endy])
		{	//top
			try{
			if(maze[i-1][j]=='o')
			{
				
				maze[i-1][j]='v';
				i=i-1;
			}}
			catch(ArrayIndexOutOfBoundsException a)
			{System.out.println("i am here up");
					break;
			}
			try{
				if(maze[i+1][j]=='o')
				{
					
					maze[i+1][j]='v';
					i=i+1;

				}
			}
			catch(ArrayIndexOutOfBoundsException a)
			{System.out.println("i am here down");
				break;
			}
			try{
				if(maze[i][j+1]=='o')
				{
					
					maze[i][j+1]='v';
					j=j+1;
				}
			}
			catch(ArrayIndexOutOfBoundsException a)
			{	System.out.println("i am here left");
				break;
			}
			try{
				if(maze[i][j-1]=='o')
				{
					
					maze[i][j-1]='v';
					j=j-1;
				}
			}
			catch(ArrayIndexOutOfBoundsException a)
			{	System.out.println("i am here right");
				break;
			}

		}
	}
	else
		System.out.println("no solution");
	}
	public static void main(String args[])
	{
		
		
		Solution s = new Solution(4,4);
	s.initialize();
		s.findStart();
		s.findEnd();
		s.findPath();
		s.display();

	}
}