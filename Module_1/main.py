import random
import streamlit as st

st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("I love AI VIET Nam")
st.divider()
st.markdown('# This is a')
st.markdown('# [AI VIETNAM](http://)')
st.markdown(r'$ \sqrt{2x} $')
st.divider()

st.latex('\sqrt{2x}')
st.divider()

st.write('AI VIETNAM')
st.write('$\sqrt{2x}$')

st.divider()
st.write('[google](https://www.google.com/)')

st.code("""
import streamlit
print("heello")
        """)
st.divider()


def get_year():
    return 1999


with st.echo():
    st.write('this is a test')

    def get_name():
        return 'AI VIETNAM'
    name = get_name()
    year = get_year()
    st.write(name, year)

st.divider()
st.image('D:\Github\AIO-exercise\Module_1\logo.png')

st.divider()
agree = st.checkbox('I agree')

if agree:
    st.write('You agree')

st.radio('List colorss:', ['Yellow', 'Red', 'Green'],
         captions=['Vàng', 'Đỏ', 'Xanh'])

st.selectbox('List colorssss:', ['Yellow', 'Red', 'Green'])
options = st.multiselect(
    'List colors:', ['Yellow', 'Red', 'Green'], ['Yellow'])

st.select_slider('List colors:', [0, 1, 2, 3, 4, 5])

if st.button("Say Hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

value = st.text_input('Your name', value="Hiep")
st.write(value)

st.divider()

st.file_uploader('Choose file to upload', accept_multiple_files=True)

with st.form('my form'):
    col1, col2 = st.columns(2)
    fname = col1.text_input("Name:")
    fyear = col1.text_input("Year:")
    submit = st.form_submit_button('Submit')
    if submit:
        st.write(fname, fyear)

st.divider()
value_random = random.randint(1, 10)

if 'key' not in st.session_state:
    st.session_state['key'] = value_random
st.write(st.session_state)
