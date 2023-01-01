# Expression-Converter
convert Infix, Postfix, Prefix expression to each other and print the Expression Tree.

## run (run.py) file, in the terminal :
- ``` Which Expression You wanna Enter? ``` example: [ postfix, prefix or infix ]
- ``` Enter your Infix Expression: ``` example: (A+B)*(C-B)
### result :
```
Infix Expression = (A+B)*(C-B)
Prefix Expression = *+AB-CB
Postfix Expression = AB+CB-*
------------------------------

       *
   /¯¯¯ ¯¯¯\
   +       -
 /¯ ¯\   /¯ ¯\
 A   B   C   B
 
 ```
