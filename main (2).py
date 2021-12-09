maze =[[".",".",".","."]
      ,[".","x","x","x"]
      ,[".",".",".","."]
      ,[".","x","x","."]
      ,[".",".",".","."]]

def printmaze(maze):
  for i in maze:
    line=""
    for j in i:
      line+=j+" "
    print(line)


def solvemaze(maze,sol,pr,pc):
  print(sol)
  num_row=len(maze)
  num_col=len(maze[0])
#basecase
  #robot is home
  if pr==num_row-1 and pc==num_col-1:
    return sol
  #encounter obstacle or out of bound 
  if pr>=num_row or pc>=num_col :
    return None
  if maze[pr][pc]=="x":
    return None
#recursivecase
 #tryright
  sol.append("r")
  solright=solvemaze(maze,sol,pr,pc+1)
  if solright is not None:
    return solright
 #if right nhucac then try down 
  sol.pop()
  sol.append("d")
  soldown=solvemaze(maze,sol,pr+1,pc)
  if soldown is not None:
    return soldown 
  sol.pop()
  return None
def client(maze,sol,pr,pc):
  if len(maze)>0 and len(maze[0])>0:
    printmaze(maze)
    print("this is how it works")
    return solvemaze(maze,sol,pr,pc)
