#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 Exercises

# ## Algorithm Workbench No. 5

# We are asked to write a python statement that assigns the sum of 10 and 14 to the variable total

# In[3]:


Total = 10 + 14


# In the line above, I started with the variable "Total," and set it equal to the numbers 10 plus fourteen which adds the two together. Now the variable "Total" means 10 and 14 added together. When the print function is used it will give us the sum of the two numbers. 

# In[4]:


print(Total)


# When using the print function and inserting "Total," the output is 24, the sum of 10 and 14. This is because I set "Total" to be the variable for the sum of 10 and 14, now my computer knows that the word Total means the sum of 10 and 14, as shown in the line above.

# ## Programming Exercises No. 1

# We are asked to write a program that displays the personal information of a made up character in a list form

# print('Cameron Calero')
# 
# print('2045 Heliport Loop')
# 
# print(Riverfork, IN 43286')
# 
# print(812-555-1212)
# 
# print(Major: Business)

# In the lines above, I displayed how I beleive is the correct way to make my output the personal information in list form of Cameron Calero. In the next line, I'm going to displayt my prediction of the output from the program I have typed above this line.

# Cameron Calero
# 
# 2045 Heliport Loop
# 
# Riverfolk, IN 43286
# 
# 812-555-1212
# 
# Major: Business

# Now, I'm actually going to run the code to see if my prediction was correct

# In[6]:


print('Cameron Calero')

print('2045 Heliport Loop')

print(Riverfork, IN 43286')

print(812-555-1212)

print(Major: Business)


# I was presented with a syntax error because somehow I forgot to include quotation marks, heres my fixed program below

# In[8]:


print('Cameron Calero')

print('2045 Heliport Loop')

print('Riverfork, IN 43286')

print('812-555-1212')

print('Major: Business')


# As you can see above, now that all my errors were worked out, my output is correct and the personal information of Cameron Calero is presented in list form

# ## Programming Exercises No. 13

# We are asked to calculate the number of grape vines that will fit in a row

# In[54]:


#find the length of the row, in feet
length = int(input('Please enter the length of the row, in feet:'))


# I included int since it is a whole number

# In[74]:


print(length)


# In the lines above, I chose my own number for the length of the row in feet (60) since the textbook didn't give us any numbers to use. Now the number 60 is associated with the length in my computers memory, as shown with the print function

# In[75]:


#find the amount of space used in an end-post assemply, in feet
endpost_space_used = int(input("Please enter the amount of space used in an end-post assembly, in feet:"))


# In the cell above, I again chose my own number (4) for the amount of space used in an end-post assembly

# In[76]:


print(endpost_space_used)


# Now the number 4 is associated with the endpost space used in my computers memory by using variables, as shown in the cell above

# In[77]:


#find the space between vines, in feet
space_between_vines = int(input("Please enter the space between vines, in feet:"))


# In the cell above, I once again chose my own number (2) for the space between vines

# In[78]:


print(space_between_vines)


# Now the number 2 is associated with the space between vines in my computers memory

# In[79]:


#set each letter(R,E, and S) equal to the variables i just created (Length, space used, and space between)
R = length
E = endpost_space_used
S = space_between_vines


# In[80]:


#Test to make sure it works
print(R)
print(E)
print(S)


# In[81]:


#use the original equation given in problem 13 and set it equal to V to get answer
V = (R - 2 * E)/S


# In[82]:


print(V)


# In[ ]:




