bicycle =["tee","tree","the one", "finally", "andraiod"]
print(bicycle[0].title())
print(bicycle[-1].title())
print(bicycle[-2].title())
#python 中可用-1，-2等表示最后一个和倒数第二个元素

print(bicycle)

bicycle.append('little')
print (bicycle)

bicycle.insert (3,'wed')
print(bicycle)

del bicycle[3]
print (bicycle)

poped_bicycle=bicycle.pop()
print(bicycle)
print(poped_bicycle.title())