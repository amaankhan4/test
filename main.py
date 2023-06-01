import streamlit as st
import recordAudio as ra
def main():
    st.title("Speech to Text")
    st.write("Using Python")
    if 'recording' not in st.session_state:
        st.session_state['recording'] = False

    if st.button("Record"):
        if not st.session_state['recording']:
            st.session_state['recording'] = True
            st.info("Recording started...")
            text=ra.record_audio()
            st.write(text)
        else:
            st.session_state['recording'] = False       
if __name__ == "__main__":
    main()                   
