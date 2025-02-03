#   2025-01-11 09:13:33

name ="Eric"
name1="wang"
Name=f"{name} {name1}"
message= f"Hello,{Name.title()},would you like learn some python?"
print(message)
print(name1.title())

# 1.f是转换格式的一种方式如果在第三行不加f输出将会变为Hello,{Name}{Name1},would you like learn some python?
# 2..title()要在所要求的变量格式下用花括号括起来。 
#3.print 后可加变量并显示变量的值，也可添加.title ()
print(name.upper())
print(name.lower())

# Name.upper() Name.lower() 是大小写的意思

message1='Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(message1)


Finally_name="\n\tada"
print(Finally_name)
print(Finally_name.rstrip())
print(Finally_name.lstrip())
print(Finally_name.strip())

#打印不能随便加语法 可以加.rstrip() .lstrip() .strip()
