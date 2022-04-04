import streamlit as st
y = 50
st.header("Mark Checking Demo")


readme = st.checkbox("readme")

if readme:

    st.write("""
        This is a trial for mark checking. You may get the codes via [github](https://github.com/mohafis/DSA/blob/main/markcheck.py)
        """)

    st.write ("For more info, please contact:")

    st.write("[Mohd Hafizzudin Ismail](https://www.linkedin.com/in/mohd-hafizzudin-ismail-92b15274/)")
    

st.write("Key in your mark. Enter x to stop the algorithm.\n\n")
         
mark = st.text_input('Enter the mark here (0 to 100', 'xx')
         
         
try:
    val = float(mark)
            
    if (val > 100 or val < 0):
        st.write("\nThis mark is not valid, please re-enter a valid mark.\n")
                
    elif val >= y:
        st.write("\nYou passed your exam. Keep it up!\n")
       
    else:
        st.write("\nUnfortunately, you did not pass your exam. Work harder. You can make it.\n")

            
except ValueError:
    st.write("\nThis is not a number, kindly enter a number.\n")
