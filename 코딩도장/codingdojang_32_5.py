files = input().split()
#1 format
# x= '1.jpg'
# print(x.split('.')[0], x.split('.')[1]) # 1 jpg
# print('{0}.{1}'.format(int(x.split('.')[0]), x.split('.')[1])) #1.jpg

#2 map
#map(function, list)
# x = ['1', '2', '3', '4']
# print(list(map(int, x))) #[1,2,3,4]
# print(list(map(lambda x: 출력할 내용, 리스트)))

print(list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]), x.split('.')[1]), files)))