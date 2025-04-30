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
    st.header("Text Summarization")
    text = st.text_area("Enter text to summarize", height=200)
    if st.button("Generate Summary"):
        if text:
            summarizer = agent_manager.get_agent("TextSummarizer")
            validator = agent_manager.get_agent("SummaryValidator")
            with st.spinner("Generating summary..."):
                try:
                    summary = summarizer.process(text)
                    st.subheader("Generated Summary:")
                    st.write(summary)
                    
                    if validator:
                        with st.spinner("Validating summary..."):
                            validation = validator.process(text, summary)
                            st.subheader("Validation Report:")
                            st.write(validation)
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
    st.header("Article Generation")
    topic = st.text_input("Enter article topic")
    outline = st.text_area("Optional outline", height=100)
    if st.button("Generate Article"):
        if topic:
            generator = agent_manager.get_agent("ArticleGenerator")
            validator = agent_manager.get_agent("ArticleQualityValidator")
            with st.spinner("Generating article..."):
                try:
                    article = generator.process(topic, outline)
                    st.subheader("Generated Article:")
                    st.write(article)
                    
                    if validator:
                        with st.spinner("Validating article..."):
                            validation = validator.process(topic, article, outline)
                            st.subheader("Quality Report:")
                            st.write(validation)
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
    st.header("Data Sanitization")
    data = st.text_area("Enter data to sanitize", height=200)
    if st.button("Sanitize Data"):
        if data:
            sanitizer = agent_manager.get_agent("DataSanitizer")
            validator = agent_manager.get_agent("DataSanitizationValidator")
            with st.spinner("Sanitizing data..."):
                try:
                    sanitized_data = sanitizer.process(data)
                    st.subheader("Sanitized Data:")
                    st.write(sanitized_data)
                    
                    if validator:
                        with st.spinner("Validating sanitization..."):
                            validation = validator.process(data, sanitized_data)
                            st.subheader("Validation Report:")
                            st.write(validation)
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
    

                
    



