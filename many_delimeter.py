import re
some_str= "hey: how, are you; doing"

output_list =re.split(r"[:,;\s]\s*", some_str)
print(output_list) 
#OUTPUT:
# ['hey', 'how', 'are', 'you', 'doing']


#EXPLANATION:
#in the code above, charaters in the square bracket
# are the possible charaters sthat could be matched followed
# by zero or more white space (charater : followed by 0 or many white space or 
# character , followed by a white space(\s) or more).... whenever the pattern
# is matched the entire match will be come the delimeter between what
# lies behind the match and ehat lies ahead of the match e.g: using ,
# behind,ahead => ["behind","ahead"]