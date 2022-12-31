from stack import Stack


precedence = {
  ')' : 0,
  '(' : 0,
  '+' : 1,
  '-' : 1,
  '/' : 2,
  '*' : 2,
  '%' : 2,
  '^': 3
}


def inf_to_pre(inf_exp):
  result =[]
  stack = Stack()
  
  for char in inf_exp[::-1]:
    
    if char == ')':
      stack.push(char)
      
    elif char == '(' :
      
      while(stack.list()[-1] != ')'):
        item = stack.pop()
        result.append(item)
        
      stack.pop() # deleting the ')'
    
    elif char in ['*','/','%','+','-']:
      if stack.size() > 0 :
        while precedence[stack.list()[-1]] > precedence[char]:
          item = stack.pop()
          result.append(item)
            
          if stack.size() == 0 :
            break
      stack.push(char)
      
    elif char == '^':
      if stack.size() > 0 :
        while precedence[stack.list()[-1]] >= precedence[char]:
          item = stack.pop()
          result.append(item)
            
          if stack.size() == 0 :
            break
          
      stack.push(char)
    
    else:
      result.append(char)
      
  if stack.size() > 0 :
    while stack.size() != 0:
      item = stack.pop()
      result.append(item)

  print(f"Prefix Expression = ",end='')
  for char in result[::-1]:
    print(char,end='')
  print()
  
def inf_to_post(inf_exp):
  result =[]
  stack = Stack()
  
  for char in inf_exp:
    
    if char == '(':
      stack.push(char)
    
    elif char == ')' :
      while(stack.list()[-1] != '('):
        item = stack.pop()
        result.append(item)
        
      stack.pop() # deleting the '('
      
    elif char in ['*','/','%','+','-']:
      if stack.size() > 0 :
        while precedence[stack.list()[-1]] >= precedence[char]:
          item = stack.pop()
          result.append(item)
              
          if stack.size() == 0 :
            break
      stack.push(char)
        
    elif char == '^':
      if stack.size() > 0 :
        while precedence[stack.list()[-1]] > precedence[char]:
          item = stack.pop()
          result.append(item)
              
          if stack.size() == 0 :
            break
      stack.push(char)
      
    else:
      result.append(char)
  
  

  while stack.size() != 0:
    item = stack.pop()
    result.append(item)
    
  print(f"Postfix Expression = ",end='')
  for char in result:
    print(char,end='')
  print()
  
  return ''.join(result)
  
 


def post_to_inf(post_exp):
  result =[]
  stack = Stack()
  for char in post_exp:
    
    if char not in precedence:
      stack.push(char)
    
    else:
      if stack.size() > 0:
        first_top_item = stack.pop()
        second_top_item = stack.pop()
      
        new_item = f"({second_top_item}{char}{first_top_item})"


        stack.push(new_item)
      
      

  item = stack.pop()
  result.append(item)
    
  print(f"Infix Expression = {result[0]}")

    
      
def post_to_pre(post_exp):
  result =[]
  stack = Stack()
  
  for char in post_exp:
    
    if char not in precedence:
      stack.push(char)
    
    else:
      if stack.size() > 0:
        first_top_item = stack.pop()
        second_top_item = stack.pop()
        
        new_item = f"{char}{second_top_item}{first_top_item}"

        stack.push(new_item)
      
      

  item = stack.pop()
  result.append(item)
    
  print(f"Prefix Expression = {result[0]}")
  

def pre_to_inf(pre_exp):
  result =[]
  stack = Stack()
  for char in pre_exp[::-1]:
    
    if char not in precedence:
      stack.push(char)
    
    else:
      if stack.size() > 0:
        first_top_item = stack.pop()
        second_top_item = stack.pop()
      
        new_item = f"({first_top_item}{char}{second_top_item})"


        stack.push(new_item)
      
      

  item = stack.pop()
  result.append(item)
    
  print(f"Infix Expression = {result[0]}")

def pre_to_post(pre_exp):
  result =[]
  stack = Stack()
  for char in pre_exp[::-1]:
    
    if char not in precedence:
      stack.push(char)
    
    else:
      if stack.size() > 0:
        first_top_item = stack.pop()
        second_top_item = stack.pop()
        
        new_item = f"{first_top_item}{second_top_item}{char}"

        stack.push(new_item)
      
      

  item = stack.pop()
  result.append(item)
    
  print(f"Postfix Expression = {result[0]}")
  return result[0]