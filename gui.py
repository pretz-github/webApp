import streamlit as st
import functions

def todo_call():
   todo_new=st.session_state['todo_new']+"\n"

   #Get the
   todo_list= functions.get_todo()
   todo_list.append(todo_new)
   functions.write_todo(todo_list)

   #Clear the input field
   st.session_state.todo_new=" "




st.title("Tod-do app")
st.subheader("It is a to do application")
st.write("This is todo <b>app</b>",unsafe_allow_html=True)

#creating check boxes
todos = functions.get_todo()
print("------------")
print( f"{len(todos)} length of the array")
print(f"print todos {todos}")
for todo in todos:
   todo_print= todo.strip("\n")
   print(f"{todo_print} in for loop")
   check_box=st.checkbox(todo, key=todo)
   print(f"check box is checked {check_box} ")
   if check_box:
      todos.remove(todo)
      functions.write_todo(todos)
      del st.session_state[todo]
      st.rerun()





print("Hi before call")
input_var = st.text_input(label="ADD New Todo",placeholder = "Enter the todo",on_change=todo_call,key='todo_new')

print("hello+3+4")
