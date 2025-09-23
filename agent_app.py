# agent_app.py - AI Agent Version
import streamlit as st
from main import research
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
from groq import Groq
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for conversation
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_context" not in st.session_state:
    st.session_state.conversation_context = ""

# CSS for chat interface with better contrast
st.markdown("""
<style>
    /* Dark theme compatibility */
    .main-header {
        font-size: 3rem;
        color: #4fc3f7 !important;
        text-align: center;
        margin: 1rem 0;
        font-weight: 700;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #b0b0b0 !important;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1.2rem;
        margin: 0.8rem 0;
        border-radius: 15px;
        max-width: 75%;
        border: 1px solid #444;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        line-height: 1.5;
    }
    
    .message-header {
        font-weight: bold;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .message-content {
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .message-content strong {
        font-weight: 700;
        color: #fff !important;
    }
    
    .message-content code {
        background-color: rgba(0,0,0,0.3) !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
        font-family: 'Courier New', monospace !important;
        font-size: 0.9em !important;
        color: #ffeb3b !important;
    }
    
    .user-message {
        background-color: #2196f3 !important;
        color: white !important;
        margin-left: auto;
        text-align: right;
        border-color: #1976d2 !important;
    }
    
    .agent-message {
        background-color: #424242 !important;
        color: white !important;
        margin-right: auto;
        border-color: #616161 !important;
    }
    
    .research-section {
        border: 2px solid #1f77b4;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #333 !important;
        color: white !important;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #1976d2 !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #1565c0 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #2e2e2e !important;
    }
    
    /* Chat input styling */
    .stChatInput > div > div > div > div {
        background-color: #424242 !important;
        border: 2px solid #1976d2 !important;
        color: white !important;
    }
    
    /* Smooth animations */
    .chat-message {
        animation: slideIn 0.3s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Progress indicator styling */
    .research-progress {
        background-color: #333 !important;
        border-radius: 10px !important;
        margin: 0.5rem 0 !important;
        padding: 0.8rem !important;
        text-align: center !important;
        font-style: italic !important;
        opacity: 0.8 !important;
        border: 1px dashed #666 !important;
    }
</style>
""", unsafe_allow_html=True)

def analyze_user_intent(message):
    """Analyze user message to determine if research is needed"""
    message_lower = message.lower().strip()
    
    # More specific intent recognition
    greeting_words = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
    
    # Capability/question patterns - more comprehensive
    question_patterns = [
        'what can you do', 'what are your capabilities', 'how do you work', 
        'what is this', 'help me', 'what are you', 'who are you',
        'explain yourself', 'tell me about yourself', 'your features',
        'what else can you do', 'what other things can you do',
        'what are your skills', 'what functions do you have',
        'how can you help', 'what services do you provide'
    ]
    
    # Research trigger words - explicit research requests
    research_triggers = [
        'research', 'tell me about', 'find information about',
        'analyze', 'investigate', 'study', 'explore the topic of',
        'gather information', 'look up', 'search for'
    ]
    
    clarification_words = ['tell me more', 'explain further', 'clarify', 'expand on', 'more details']
    
    # Check for greetings
    if any(word in message_lower for word in greeting_words):
        return "GREETING"
    
    # Check for capability questions first (more specific)
    elif any(phrase in message_lower for phrase in question_patterns):
        return "QUESTION"
    
    # Check for clarification requests
    elif any(phrase in message_lower for phrase in clarification_words):
        return "CLARIFICATION"
    
    # Check for explicit research triggers
    elif any(trigger in message_lower for trigger in research_triggers):
        return "RESEARCH"
    
    # For ambiguous cases, default to QUESTION to be safe
    else:
        return "QUESTION"

def extract_research_topic(message):
    """Extract the actual research topic from user message"""
    message_lower = message.lower().strip()
    
    # Remove common research prefixes
    prefixes_to_remove = [
        'tell me about ', 'research ', 'find information about ',
        'analyze ', 'investigate ', 'study ', 'explore ',
        'gather information about ', 'look up ', 'search for ',
        'what is ', 'what are ', 'who is ', 'who are ',
        'how does ', 'how do ', 'why does ', 'why do '
    ]
    
    cleaned_message = message
    for prefix in prefixes_to_remove:
        if message_lower.startswith(prefix):
            cleaned_message = message[len(prefix):].strip()
            break
    
    # Capitalize first letter for better presentation
    if cleaned_message:
        cleaned_message = cleaned_message[0].upper() + cleaned_message[1:]
    
    return cleaned_message if cleaned_message else message

def generate_agent_response(message, intent, context=""):
    """Generate conversational response based on intent"""
    if intent == "GREETING":
        return "Hello there! 👋 I'm your AI Research Agent, ready to help you explore any topic in depth. I can provide comprehensive analysis with multiple perspectives, fact-checking, and professional citations. What would you like to research today?"
    
    elif intent == "QUESTION":
        return """I'm an intelligent research agent with several powerful capabilities:

**Multi-perspective research** - I analyze topics from 4 different angles
**Source credibility analysis** - Color-coded reliability scoring  
**Advanced fact-checking** - Cross-reference verification
**Professional citations** - APA, MLA, or simple format
**Memory & context** - I remember our conversation
**Natural conversation** - Chat with me like a colleague

**To research a topic**: Simply ask "research [topic]" or use the 🔬 Research Mode checkbox
**To chat**: Ask questions about my capabilities, say hello, or request clarifications

What would you like to know or research?"""
    
    elif intent == "CLARIFICATION":
        return f"I'd be happy to clarify or expand on our previous research. Based on our conversation: {context}. What specific aspect would you like me to explore further?"
    
    else:  # RESEARCH
        topic = extract_research_topic(message)
        return f"I'll research **'{topic}'** for you. Let me gather comprehensive information from multiple angles and provide you with well-sourced, fact-checked insights."

# Header
st.markdown('<h1 class="main-header">AI Research Agent</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your intelligent research companion with memory and conversation</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Agent Settings")
    
    citation_style = st.selectbox(
        "Citation Style",
        ["APA", "MLA", "Simple"],
        help="Choose your preferred academic citation format"
    )
    
    st.markdown("## 🧠 Agent Capabilities")
    st.markdown("- **Conversational Interface** - Natural chat interaction")
    st.markdown("- **Memory & Context** - Remembers our conversation")
    st.markdown("- **Intent Recognition** - Understands what you need")
    st.markdown("- **Multi-Perspective Research** - 4 different angles")
    st.markdown("- **Source Credibility Analysis** - Color-coded reliability")
    st.markdown("- **Fact-Checking** - Cross-reference verification")
    
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.session_state.conversation_context = ""
        st.rerun()

# Chat interface
st.markdown("## Chat with Your Research Agent")

# Display conversation history
for i, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.markdown(f'''
        <div class="chat-message user-message">
            <div class="message-header">👤 <strong>You:</strong></div>
            <div class="message-content">{message["content"]}</div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        # Format agent message content properly
        content = message["content"]
        
        # Handle bold text with regex
        import re
        content = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', content)
        # Handle code blocks
        content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
        # Handle line breaks
        content = content.replace('\n', '<br>')
        
        st.markdown(f'''
        <div class="chat-message agent-message">
            <div class="message-header">🤖 <strong>Agent:</strong></div>
            <div class="message-content">{content}</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Display research results if available
        if "research_report" in message:
            with st.expander("📊 Research Results", expanded=True):
                st.markdown(message["research_report"], unsafe_allow_html=True)

# Research mode toggle
st.markdown("---")
# Show research progress if research is in progress
if st.session_state.get('research_in_progress', False) and st.session_state.get('research_started', False):
    st.markdown(f'''
    <div class="research-progress">
        🔬 <em>Conducting comprehensive research on "{st.session_state.get('research_topic', 'topic')}"...</em>
    </div>
    ''', unsafe_allow_html=True)
    
    # Add visual progress bar
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        time.sleep(0.02)  # Fast smooth progress
    
    # The actual research will continue after this visual feedback
    user_input = None  # No input during research
else:
    # Show input area only when not researching
    col_input, col_button = st.columns([4, 1])
    
    with col_input:
        # Chat input
        user_input = st.chat_input("Ask me anything or request research on any topic...")
    
    with col_button:
        research_mode = st.checkbox("🔬 Research Mode", help="Check this box to force research on any input")

if user_input:
    # Add user message to conversation
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Update conversation context
    st.session_state.conversation_context += f" User asked: {user_input}."
    
    # Analyze intent - override if research mode is enabled
    with st.spinner("🤔 Understanding your request..."):
        if st.session_state.get('research_in_progress', False):
            intent = "RESEARCH"  # Force research if already in progress
        elif 'research_mode' in locals() and research_mode:
            intent = "RESEARCH"
        else:
            intent = analyze_user_intent(user_input)
    
    # Generate response based on intent
    if intent == "RESEARCH":
        # Extract clean topic
        research_topic = extract_research_topic(user_input)
        
        # Show typing indicator first
        with st.spinner("🤖 Agent is typing..."):
            time.sleep(0.8)  # Brief realistic typing delay
        
        # Add immediate response and rerun to show it
        agent_response = f"I'll research **'{research_topic}'** for you. Let me gather comprehensive information from multiple angles and provide you with well-sourced, fact-checked insights."
        st.session_state.messages.append({"role": "assistant", "content": agent_response})
        st.rerun()
        
    else:
        # For non-research responses, show typing indicator
        with st.spinner("🤖 Agent is typing..."):
            time.sleep(0.5)  # Brief realistic typing delay
            
        # Generate and show response
        agent_response = generate_agent_response(user_input, intent, st.session_state.conversation_context)
        st.session_state.messages.append({"role": "assistant", "content": agent_response})
        
        # Update context
        st.session_state.conversation_context += f" Agent responded to {intent.lower()} with guidance."
        
        st.rerun()
    
    st.rerun()

# Handle research execution separately after the immediate response is shown
if st.session_state.messages and len(st.session_state.messages) >= 2:
    last_message = st.session_state.messages[-1]
    if (last_message["role"] == "assistant" and 
        "I'll research" in last_message["content"] and 
        "research_report" not in last_message):
        
        # Extract the research topic from the message
        import re
        topic_match = re.search(r"I'll research \*\*'([^']+)'\*\*", last_message["content"])
        if topic_match:
            research_topic = topic_match.group(1)
            
            # Find the corresponding user message
            user_message = st.session_state.messages[-2]["content"] if len(st.session_state.messages) >= 2 else ""
            
            # Mark for research processing - this will trigger the progress bar
            if not st.session_state.get('research_started', False):
                st.session_state.research_in_progress = True
                st.session_state.research_topic = research_topic
                st.session_state.research_user_message = user_message
                st.session_state.research_started = True
                st.rerun()  # Rerun to show progress bar
            
            try:
                # Run research with the original user input (this happens after progress shows)
                report = research(user_message, citation_style)
                
                # Clear research state
                st.session_state.research_in_progress = False
                st.session_state.research_started = False
                
                # Add research results
                result_message = f"Research completed! Here are my findings on **'{research_topic}'**:"
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": result_message,
                    "research_report": report
                })
                
                # Update context
                st.session_state.conversation_context += f" Agent researched {research_topic} and provided comprehensive findings."
                
                st.rerun()
                
            except Exception as e:
                # Clear research state on error
                st.session_state.research_in_progress = False
                st.session_state.research_started = False
                
                error_response = f"I encountered an issue while researching **'{research_topic}'**. Please check your API keys and try again. Error: {str(e)}"
                st.session_state.messages.append({"role": "assistant", "content": error_response})
                st.rerun()
    


# Show example interactions ONLY at the very start
show_initial_buttons = (
    not hasattr(st.session_state, 'messages') or 
    len(st.session_state.messages) == 0
) and not st.session_state.get('research_in_progress', False)

if show_initial_buttons:
    st.markdown("### 💡 Try asking me:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👋 Hello, what can you do?", key="hello_start", use_container_width=True):
            if 'messages' not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": "Hello, what can you do?"})
            response = "Hello there! 👋 I'm your AI Research Agent, ready to help you explore any topic in depth. I can provide comprehensive analysis with multiple perspectives, fact-checking, and professional citations. What would you like to research today?"
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.conversation_context += " User greeted and asked about capabilities."
            st.rerun()
    
    with col2:
        if st.button("🚗 Research Tesla vs competitors", key="tesla_start", use_container_width=True):
            if 'messages' not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": "Research Tesla vs competitors"})
            response = "I'll research **'Tesla vs competitors'** for you. Let me gather comprehensive information from multiple angles and provide you with well-sourced, fact-checked insights."
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.conversation_context += " User requested Tesla vs competitors research."
            st.rerun()
    
    with col3:
        if st.button("🤖 Tell me about AI ethics", key="ai_start", use_container_width=True):
            if 'messages' not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": "Tell me about AI ethics"})
            response = "I'll research **'AI ethics'** for you. Let me gather comprehensive information from multiple angles and provide you with well-sourced, fact-checked insights."
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.conversation_context += " User asked about AI ethics topic."
            st.rerun()