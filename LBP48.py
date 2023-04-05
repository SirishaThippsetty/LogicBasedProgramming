'''
Accept video length in minutes the format is mm:ss in String format, 
create a function that takes video length and return it in seconds.
input --------> video length in mm:ss
constraint----> no
output -------> length in seconds
01234
01:00 ===> 60
02:05 ===> 125
22:01 ===> 1321



'''
video_length = input("Enter the length in mm:ss :")
v_list = video_length.split(":")
minutes = int(v_list[0])
seconds = int(v_list[1])
length_in_seconds = (minutes*60)+seconds
print(length_in_seconds)