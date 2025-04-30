import streamlit as st
from agents import AgentManager
from utils.logger import logger
import os
from dotenv import load_dotenv


load_dotenv()

def main():
    st.set_page_config(
        page_title="AI Agent", layout = "wide"
    )
    st.title("AI Agent with Collabration and Validator")

    st.sidebar.title("Select Task")

    task = st.sidebar.selectbox(
        "Select Task",
        ["Summarize", "Write Article", "Sanitize Data"]
    )

    agent_manager = AgentManager(max_retries=2, verbose=True)

    if task == "Summarize":
        summarize_section(agent_manager)

    elif task == "Write Article":
        write_article_section(agent_manager)

    elif task == "Sanitize Data":
        sanitize_data_section(agent_manager)



    
def summarize_section(agent_manager):
    st.header("Summarize Text")
    text = st.text_area("Enter text to summarize", height=200)
    if st.button("Summarize"):
        if text:
            summary = agent_manager.get_agent("summarize")
            validator_agent = agent_manager.get_agent("summary_validator")
            with st.spinner("Generating summary..."):
                try:
                    summary = summary.execute(text)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error generating summary: {str(e)}")
                    logger.error(f"Error generating summary: {str(e)}")
                    return

            with st.spinner("Validating summary..."):
                try:
                    validation = validator_agent.execute(text, summary)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Error validating summary: {str(e)}")
                    logger.error(f"Error validating summary: {str(e)}")
        else:
            st.warning("Please enter text to summarize")

def write_article_section(agent_manager):
    st.header("Write and Refine Article")
    topic = st.text_input("Enter topic")
    outline = st.text_area("Enter outline", height=150)
    if st.button("Write Article"):
        if topic:
            article = agent_manager.get_agent("write_article")
            refiner_agent = agent_manager.get_agent("refiner")
            validator_agent = agent_manager.get_agent("write_article_validator")
            with st.spinner("Generating article..."):
                try:
                    article = article.execute(topic, outline)
                    st.subheader("Article:")
                    st.write(article)
                except Exception as e:
                    st.error(f"Error generating article: {str(e)}")
                    logger.error(f"Error generating article: {str(e)}")
                    return

            with st.spinner("Refining article..."):
                try:
                    article = refiner_agent.execute(article)
                    st.subheader("Refined Article:")
                    st.write(article)
                except Exception as e:
                    st.error(f"Error refining article: {str(e)}")
                    logger.error(f"Error refining article: {str(e)}")
                    return

            with st.spinner("Validating article..."):
                try:
                    validation = validator_agent.execute(topic, outline, article)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Error validating article: {str(e)}")
                    logger.error(f"Error validating article: {str(e)}")
        else:
            st.warning("Please enter topic")


def sanitize_data_section(agent_manager):
    st.header("Sanitize Data")
    data = st.text_area("Enter data", height=200)
    if st.button("Sanitize Data"):
        if data:
            sanitize_data = agent_manager.get_agent("sanitize_data")
            validator_agent = agent_manager.get_agent("sanitize_data_validator")
            with st.spinner("Sanitizing data..."):
                try:
                    sanitized_data = sanitize_data.execute(data)
                    st.subheader("Sanitized Data:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error sanitizing data: {str(e)}")
                    logger.error(f"Error sanitizing data: {str(e)}")
                    return

            with st.spinner("Validating data..."):
                try:
                    validation = validator_agent.execute(data, sanitized_data)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Error validating data: {str(e)}")
                    logger.error(f"Error validating data: {str(e)}")
        else:
            st.warning("Please enter data")



if __name__ == "__main__":
    main()
    

                
    



