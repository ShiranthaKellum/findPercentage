
# A dictionary data structure (type) has a keys and a values. ex : {'key': value, 'key_1' : value_1, .....}

n = int (input ())                                                      # insert number of students

records = {}                                                            # creat a dectionary to store students' marks

for i in range (n):
    name, *line = input ().split ()                                     # *line removes the [] from front and behind
    marks = list (map (float, line))                                    # get rest of input strings as marks to the marks list
    records [name] = marks                                              # specify marks by names

#print(records)                                                         # {'k': [10.0, 15.0, 20.0], 'm': [10.0, 20.0, 30.0]}

qName = input ()                                                        # insert the name wants to persentage

print ('{0:.2f}'.format (sum (records [qName]) / len (records [qName])))