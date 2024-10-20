
#This function is used to remove the duplicate items and keep only one of them in the tutorial group name list
#Tutorial group name list=[G1,G1,G1,G1...G100,G100,G100...,G99,G99], By using this function the turtorial group name list=[G1,G100,G99]
def remove_dup(x): 
  return list(dict.fromkeys(x)) #remove duplicate items in the list

#This function is used to sort the students in to the sequece of their CGPA from small to big
def sorted_cgpa(lst1):
    cgpa_sorted=[]
    cgpa=[]
    for item in lst1:
        cgpa.append(item['CGPA'])
    cgpa.sort()
    for item in cgpa:
        for std in lst1:
            if std['CGPA']==item:
                cgpa_sorted.append(std)
                lst1.remove(std)
    return cgpa_sorted

#This function is used to supplement the male group by the female group if the number of it is lower than 20, vice versa.
#The student that used to supplement will be the middle part of the group.
def supplement():
    global cgpa_male_sorted
    global cgpa_female_sorted
    if len(cgpa_male_sorted)<20:
        for num in range(len(cgpa_female_sorted)-30):
            cgpa_male_sorted.append(cgpa_female_sorted.pop(10))
        cgpa_male_sorted=sorted_cgpa(cgpa_male_sorted)
    elif len(cgpa_male_sorted)>30:
        for num in range(len(cgpa_male_sorted)-30):
            cgpa_female_sorted.append(cgpa_male_sorted.pop(10))
        cgpa_female_sorted=sorted_cgpa(cgpa_female_sorted)

#This function is used to select the student into the buffer group
#The number of student in buffer group will be 10
#The number of male in buffer group will be the total number of male minus 20, same for the female group, as we want to keep the male and female group in the number of 20.
#The student are selected from the middle part for both group ie. select from tenth last
def buffer():
    global buffer_list
    num_buffer_male=len(cgpa_male_sorted)-20
    buffer_male_list=[]
    num_buffer_female=len(cgpa_female_sorted)-20
    buffer_female_list=[]
    for num in range(10,10+num_buffer_male):
        buffer_male_list.append(cgpa_male_sorted.pop(10))
    for num in range(10,10+num_buffer_female):
        buffer_female_list.append(cgpa_female_sorted.pop(10))
    buffer_list=buffer_male_list+buffer_female_list
#This function will paired the student based on their cgpa
#The student who have the highest cgpa will pair the student have the lowest cgpa and the second last will pair the second one etc. (For both male and female group)
def pair_cgpa ():
    global male_paired_list
    global female_paired_list
    global copied_femaled_list
    male_paired_list=[]
    for num in range(0,10):
        paired_list=[]
        paired_list.append(cgpa_male_sorted[num])
        paired_list.append(cgpa_male_sorted[19-num])
        male_paired_list.append(paired_list)
    female_paired_list=[]
    for num in range(0,10):
        paired_list=[]
        paired_list.append(cgpa_female_sorted[num])
        paired_list.append(cgpa_female_sorted[19-num])
        female_paired_list.append(paired_list)
    

#This function is used to form a group of 4 by combining the pair from male group and female group
#The number of same school in the group of 4 must not exceed 3.
def group_4 ():
    
    copied_femaled_list=female_paired_list[:]
   
    global group_4_student
    group_4_student=[]
    pair=True
    #print(male_paired_list)
    for male_std in male_paired_list:
        #print(male_std)
        for female_std in female_paired_list:
            temp_pair=male_std+female_std
            temp_school=[]
            for items in temp_pair:
                temp_school.append(items["School"])
            for item in temp_school:
                if temp_school.count(item)>=3:
                    pair=False
                    break
                else:
                    pair=True
            if pair==True:
                group_4_student.append(temp_pair)
                #print(group_4_student)
                female_paired_list.remove(female_std)
                break
        if pair==False:
            pair2=True
            x=1
            while True:
                #print(x)
                pre_female_std=copied_femaled_list[copied_femaled_list.index(female_paired_list[0])-x]
                #print(pre_female_std)
                temp_pair=male_std+pre_female_std
                #print(temp_pair)
                temp_school=[]
                for items in temp_pair:
                    temp_school.append(items["School"])
                for item in temp_school:
                    if temp_school.count(item)>=3:
                        pair2=False
                        break
                    else:
                        pair2=True
                if pair2==True:
                    for items in group_4_student:
                        for item in pre_female_std:
                            if item in items:
                                male_regroup=[]
                                for i in range(0,2):
                                    male_regroup.append(items[i])
                                #print(male_regroup)
                                #print(1)
                                temp=male_paired_list[:]
                                temp.reverse()
                                index=len(temp)-temp.index(male_std)-1
                                male_paired_list.insert(index+1,male_regroup)
                                #print(male_paired_list)
                                remove_items=items
                                break
                    group_4_student.remove(remove_items)
                    group_4_student.append(temp_pair)
                    
                    print(remove_items)
                    print("\n")
                    print(male_std)
                    print(temp_pair)
                    print("2")
                    #print(male_paired_list)
                    copied_femaled_list.remove(pre_female_std)
                    break
                if pair2==False:
                    #print(temp_pair)
                    #print(1)
                    x=x+1
                    #print(x)
                    #print(male_std)
                    #print(pre_female_std)
                    continue
                #print(copied_femaled_list.index(female_paired_list[0])-x)
                #print(x)
            
    
#This function is used to insert the buffer into each group to form the group of 5
#The number of same school in the group of 4 must not exceed 3.
def group_5 ():
    temp_group_4_student=group_4_student[:]
    global group_5_student
    pair1=True
    group_5_student=[]
    for std_buffer in buffer_list:
        for items in group_4_student:
            temp_group_5=[std_buffer]+items
            print(temp_group_5)
            temp_school=[]
            for std in temp_group_5:
                temp_school.append(std["School"])
            for stds in temp_school:
                if temp_school.count(stds)>=3:
                    pair1=False
                    break
                else:
                    pair1=True
            if pair1==True:
                group_5_student.append(temp_group_5)
                group_4_student.remove(items)
                break
        if pair1==False:
            pair2=True
            x=1
            while True:
                #print(x)
                pre_group4_std=temp_group_4_student[temp_group_4_student.index(group_4_student[0])-x]
                ##print(item)
                #print(pre_group4_std)
                #print(pre_female_std)
                temp_pair=[std_buffer]+pre_group4_std
                #print(temp_pair)
                temp_school=[]
                for items in temp_pair:
                    temp_school.append(items["School"])
                for item in temp_school:
                    if temp_school.count(item)>=3:
                        pair2=False
                        break
                    else:
                        pair2=True
                if pair2==True:
                    for items in group_5_student:
                        for item in pre_group4_std:
                            if item in items:
                                buffer_regroup=[]
                                for i in range(0,1):
                                    buffer_regroup.append(items[i])
                                #print(male_regroup)
                                #print(1)
                                temp=buffer_list[:]
                                temp.reverse()
                                index=len(temp)-temp.index(std_buffer)-1
                                buffer_list.insert(index+1,buffer_regroup[0])
                                #print(male_paired_list)
                                remove_items=items
                                break
                    group_5_student.remove(remove_items)
                    group_5_student.append(temp_pair)
                    
                    #print(male_paired_list)
                    temp_group_4_student.remove(pre_group4_std)
                    break
                if pair2==False:
                    #print(temp_pair)
                    #print(1)
                    x=x+1
                    #print(x)
                    #print(male_std)
                    #print(pre_female_std)
                    continue
                #print(copied_femaled_list.index(female_paired_list[0])-x)
                #print(x)
    for item in group_5_student:
        for std in item:
            std["Team Assigned"]="T"+str(group_5_student.index(item)+1)+"\n"


final_sorted_list=[]
column_name=["Tutorial Group","Student ID","School","Name","Gender","CGPA","Team Assigned"]



def remove_n(lst1):
    for item in lst1:
        if "\n" in item:
            lst1[lst1.index(item)]=item.replace("\n","")
    return lst1
f = open("records.csv", "r")
header=remove_n(f.readline().split(","))
for i in range(120):
    g1_list_dict=[]#get the data for current tutorial group
    for x in range(50):
        std_info_dict={}
        std_info=remove_n((f.readline().split(",")))
        for item in header:
            std_info_dict[item]=std_info[header.index(item)]
        g1_list_dict.append(std_info_dict)
    #print(len(g1_list_dict))
    g1_male_dict=[student for student in g1_list_dict if student["Gender"]=="Male"]#get the group of male
    g1_female_dict=[student for student in g1_list_dict if student["Gender"]=="Female"]#get the group of female
    cgpa_male_sorted=sorted_cgpa(g1_male_dict)#sort the group of male based on their CGPA
    cgpa_female_sorted=sorted_cgpa(g1_female_dict)#sort the group of female based on their CGPA
    supplement()# supplment the male group or the female group if the number of it is lower than 20
    buffer()# select the buffer group, therefore both male group and female group have exact 20 students
    pair_cgpa()#pair the student in each group based on their CGPA(Hghest pair the lowest, second highest pair the second last)
    group_4()#form group of 4 by combining the pair in the male group and female group.
    group_5()#form the group of 5 by inserting the buffer to the group of 4
    #print(len(group_5_student))
    final_sorted_list=final_sorted_list+group_5_student# add the team allocation of current tutorial group into the final_sorted_list
#print(final_sorted_list)
#print(len(final_sorted_list))
#save the team allocation into a new csv file 
sorted_f = open("sorted_v7.csv", "w")
written_column=["Tutorial Group,","Student ID,","School,","Name,","Gender,","CGPA,","Team Assigned\n"]
sorted_f.writelines(written_column)
for tut_group in final_sorted_list:
    for std in tut_group:
        write_row=[]
        for items in column_name:
            if "\n" in std[items]:
                write_row.append(std[items])
            else:
                write_row.append(std[items]+",")
        sorted_f.writelines(write_row)
sorted_f.close()
    
    



