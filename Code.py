#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random 


# In[2]:


root=Tk()
root.geometry("430x450")
root.resizable(False,False)


# In[3]:


adjectives = ["Cool", "Happy", "Strong", "Fast", "Smart", "Tough", "Bright", "Bold"]
nouns = ["Tiger", "Dragon", "Lion", "Eagle", "Hawk", "Bull", "Wolf", "Bear"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_chars = ["!", "@", "#", "$", "&", "*"]


# In[4]:


def generate(include_num=False,include_spec_char=False,length=13):
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    username=adjective+noun
    
    if include_num:
        num_count=random.randint(1,3)
        username+=''.join(random.choice(numbers) for _ in range(num_count))
                 
    if include_spec_char:
        char_count=random.randint(1,2)
        username+=''.join(random.choice(special_chars) for _ in range(char_count))
    
    username=username[:length]
    return username


# In[5]:


num_var = BooleanVar()
num_checkbox = Checkbutton(root, text="Include numbers", variable=num_var).place(x='40', y='320')

spec_char_var=BooleanVar()
char_checkbox=Checkbutton(root,text="Include special char", variable=spec_char_var).place(x='200',y='320')


# In[6]:


username=" "


# In[7]:


def display_username():
    global username
    include_num = num_var.get()
    include_spec_char = spec_char_var.get()
    username=generate(include_num,include_spec_char)
    Label(root,text=f'Username is :- {username}',font='impack 18 bold',bg='purple',fg='white').place(x='10',y='50')


# In[8]:


def save_to_file():
    global username
    if username != "":
        
        with open("usernames.txt", 'a') as file:
            file.write(username + '\n')
        print(f"Username saved to usernames.txt")
    else:
        print("Please generate a username first.")


# In[9]:


Button(root, text='Generate', bg='Blue', fg='White', font='impack 16 bold', command=display_username).place(x='135', y='360')

Button(root, text='Save to file', bg='green', fg='white', font='impack 12 bold', command=save_to_file).place(x='140', y='410')

mainloop()


# In[ ]:




