import expressions as ep
from tree import construct_tree

exp = input("Which Expression You wanna Enter? ").upper()
while True:
  if exp not in ['PREFIX', "POSTFIX", "INFIX"]:
    exp = input("Please Enter Valid Expression: ").upper()
  else:
    break
  

if exp == 'INFIX':
  inf_exp = input('Enter your Infix Expression: ' ).replace(' ','')
  print(f"Infix Expression = {inf_exp}")
  ep.inf_to_pre(inf_exp)
  postfix = ep.inf_to_post(inf_exp)

  print('------------------------------')
  construct_tree(postfix)

  
elif exp == 'POSTFIX':
  post_exp = input('Enter your Postfix Expression: ' ).replace(' ','')
  print(f"Postfix Expression = {post_exp}")
  ep.post_to_inf(post_exp)
  ep.post_to_pre(post_exp)

  print('------------------------------')
  construct_tree(post_exp)

  
else:
  pre_exp = input('Enter your Prefix Expression: ' ).replace(' ','')
  print(f"Prefix Expression = {pre_exp}")
  ep.pre_to_inf(pre_exp)
  postfix = ep.pre_to_post(pre_exp)

  print('------------------------------')
  construct_tree(postfix)