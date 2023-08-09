import streamlit as st
import pandas as pd


if 'employee_data' not in st.session_state:
    st.session_state.employee_data = pd.DataFrame(
        columns=['Empno', 'Ename', 'Job', 'deptno'])

if 'department_data' not in st.session_state:
    st.session_state.department_data = pd.DataFrame(
        columns=['deptno', 'Dname', 'Loc'])

# session_state = st.SessionState.get(
#     employee_df=employee_data, department_df=department_data)

EMPLOYEE_PAGE = "Employee Page"
DEPARTMENT_PAGE = "Depatment Page"
VISUALISATION_PAGE = "Visualisation Page"


def render_employee():
    st.title("Employee Details")
    st.header("Enter employee details")
    empno = st.text_input("Enter employee number")
    ename = st.text_input("Enter employee name")
    job = st.text_input("Enter employee job ")
    deptno = st.text_input("Enter department number ")

    if st.button("Add Employee"):
        if empno and ename and job and deptno:
            st.session_state.employee_data.loc[
                len(st.session_state.employee_data)] = [empno, ename,
                                                        job, deptno]
            st.success("Employee added successfully!")
        else:
            st.error("All fields are required for adding an employee.")


def render_department():
    st.title("Department Details")
    st.header("Enter department details")
    deptno = st.text_input("Enter department number")
    dname = st.text_input("Enter department name")
    loc = st.text_input("Enter department location")

    if st.button("Add Departmenat"):
        if deptno and dname and loc:
            st.session_state.department_data.loc[
                len(st.session_state.department_data)] = [deptno, dname, loc]
            st.success("Department added successfully!")
        else:
            st.error("All fields are required for adding a department.")


def visualize_data():
    st.title("Visualize Data")
    joined_data = pd.merge(st.session_state.employee_data,
                           st.session_state.department_data,
                           on='deptno', how='inner')
    st.dataframe(joined_data)


def main():
    st.sidebar.title('Navigation')
    page_selection = st.sidebar.radio('Go to',
                                      ["Employee Data Entry",
                                       "Department Data Entry",
                                       "Visualize Data"]
                                      )

    if page_selection == "Employee Data Entry":
        render_employee()
    elif page_selection == "Department Data Entry":
        render_department()
    elif page_selection == "Visualize Data":
        visualize_data()


if __name__ == "__main__":
    main()