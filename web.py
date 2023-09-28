import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is helpful to increase your productivity")

todos = functions.get_todos()

for i, todo in enumerate(todos):
    box = "checkbox" + str(i)
    checkbox = st.checkbox(todo, key=box)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[box]
        st.experimental_rerun()

st.text_input(label="Enter a todo item", placeholder="type here",
              on_change=add_todo, key="new_todo")

# pip freeze > requirements.txt
