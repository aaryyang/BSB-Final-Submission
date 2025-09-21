# app.py
import streamlit as st
from main import research
import time
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io

# Page configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional website CSS
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main layout */
    .main-header {
        font-size: 3.5rem;
        color: #1f77b4;
        text-align: center;
        margin: 2rem 0;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 3rem;
    }
    
    /* Content sections */
    .search-section {
        max-width: 800px;
        margin: 0 auto 2rem auto;
        text-align: center;
    }
    
    .examples-section {
        max-width: 600px;
        margin: 2rem auto;
        text-align: center;
    }
    
    .how-it-works {
        padding: 2rem;
        margin: 0;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        font-size: 1.1rem;
        padding: 1rem;
        text-align: center;
        border-radius: 25px;
        border: 2px solid #e0e0e0 !important;
        transition: all 0.3s ease;
        outline: none !important;
        box-shadow: none !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #1f77b4 !important;
        box-shadow: 0 0 10px rgba(31, 119, 180, 0.2) !important;
        outline: none !important;
    }
    
    /* Remove any error styling */
    .stTextInput > div {
        border: none !important;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 25px;
        font-weight: 600;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
    }
    
    /* Sidebar */
    .sidebar-info {
        margin-top: 0;
        padding-top: 0;
    }
    
    /* Metrics */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #1f77b4;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Add dynamic CSS based on user state - this needs to be after query is defined
def add_dynamic_css():
    user_typed = query and not st.session_state.get('from_example', False) and query != st.session_state.get('last_example_query', '')
    
    if user_typed:
        st.markdown("""
        <style>
        .examples-section button {
            visibility: hidden;
            height: 0;
            margin: 0;
            padding: 0;
        }
        .examples-section h3 {
            display: none;
        }
        </style>
        """, unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-header">  AI Research Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by Advanced AI with Multi-Perspective Analysis & Fact-Checking</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    
    # Citation style selection
    citation_style = st.selectbox(
        "Citation Style",
        ["APA", "MLA", "Simple"],
        help="Choose your preferred academic citation format"
    )
    
    st.markdown('<div class="sidebar-info">', unsafe_allow_html=True)
    st.markdown("## 🚀 Features")
    st.markdown("- **Multi-Perspective Search** - 4 different angles")
    st.markdown("- **Source Credibility Analysis** - Color-coded reliability")
    st.markdown("- **Fact-Checking** - Cross-reference verification")
    st.markdown("- **Professional Citations** - Academic formatting")
    st.markdown("- **Comprehensive Reports** - Executive summaries")
    
    st.markdown("---")
    st.markdown("## 📊 Credibility Legend")
    st.markdown("🟢 **High** - Academic, News, Gov")
    st.markdown("🟡 **Medium** - Industry, Reviews")
    st.markdown("🔴 **Low** - Commercial, Sales")

# Main Content - Centered Layout
st.markdown('<div class="search-section">', unsafe_allow_html=True)
st.markdown("## Enter Your Research Query")

# Search input
query = st.text_input(
    "Research Topic:",
    value=st.session_state.get('query', ''),
    placeholder="e.g., Tesla electric vehicles, artificial intelligence ethics, climate change solutions...",
    help="Enter any topic you'd like to research comprehensively",
    label_visibility="collapsed",
    key="query_input"
)

# Detect if user manually changed the input (not from example)
if query != st.session_state.get('query', ''):
    st.session_state.from_example = False
    st.session_state.query = query

# Apply dynamic CSS now that query is available
add_dynamic_css()

# Search button immediately below input
start_research = st.button("🚀 Start Research", type="primary", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Example queries section
if not start_research:
    # Check if user manually typed (not from example button)
    user_typed = query and not st.session_state.get('from_example', False) and query != st.session_state.get('last_example_query', '')
    
    # Always show the container but conditionally show the title
    st.markdown('<div class="examples-section">', unsafe_allow_html=True)
    
    if not user_typed:
        st.markdown("### 💡 Example Queries")
    
    # Always show buttons so they can be clicked
    example_cols = st.columns(3)
    with example_cols[0]:
        if st.button("🚗 Tesla vs competitors", use_container_width=True):
            st.session_state.query = "Tesla vs competitors"
            st.session_state.from_example = True
            st.session_state.last_example_query = "Tesla vs competitors"
            st.rerun()

    with example_cols[1]:
        if st.button("🤖 AI ethics concerns", use_container_width=True):
            st.session_state.query = "artificial intelligence ethics concerns"
            st.session_state.from_example = True
            st.session_state.last_example_query = "artificial intelligence ethics concerns"
            st.rerun()

    with example_cols[2]:
        if st.button("🌱 Climate solutions", use_container_width=True):
            st.session_state.query = "climate change solutions"
            st.session_state.from_example = True
            st.session_state.last_example_query = "climate change solutions"
            st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)# Research execution
if start_research:
    if query:
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Research phases
        phases = [
            "🔍 Generating search queries...",
            "🌐 Searching multiple perspectives...", 
            "🔍 Analyzing source credibility...",
            "✅ Cross-referencing facts...",
            "📝 Generating comprehensive report..."
        ]
        
        for i, phase in enumerate(phases):
            status_text.text(phase)
            progress_bar.progress((i + 1) / len(phases))
            time.sleep(0.5)  # Simulate progress
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        # Run research
        with st.spinner("🔬 Finalizing research..."):
            try:
                report = research(query, citation_style)
                
                # Success metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("📊 Search Queries", "4", help="Multiple perspectives analyzed")
                
                with col2:
                    st.metric("🔍 Sources Found", "~12", help="Unique sources analyzed")
                
                with col3:
                    st.metric("📚 Citation Style", citation_style, help="Academic formatting applied")
                
                with col4:
                    st.metric("✅ Fact-Checked", "Yes", help="Cross-referenced for accuracy")
                
                st.markdown("---")
                
                # Display report
                st.markdown("## 📋 Research Report")
                st.markdown(report)
                
                # Create PDF
                def create_pdf(content, title):
                    buffer = io.BytesIO()
                    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
                    
                    styles = getSampleStyleSheet()
                    story = []
                    
                    # Title
                    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=16, spaceAfter=30)
                    story.append(Paragraph(title, title_style))
                    story.append(Spacer(1, 12))
                    
                    # Content
                    lines = content.split('\n')
                    for line in lines:
                        if line.strip():
                            if line.startswith('#'):
                                # Headers
                                clean_line = line.replace('#', '').strip()
                                story.append(Paragraph(clean_line, styles['Heading2']))
                            else:
                                # Handle bold text within lines
                                processed_line = line
                                while '**' in processed_line:
                                    start = processed_line.find('**')
                                    if start != -1:
                                        end = processed_line.find('**', start + 2)
                                        if end != -1:
                                            bold_text = processed_line[start+2:end]
                                            processed_line = processed_line[:start] + f'<b>{bold_text}</b>' + processed_line[end+2:]
                                        else:
                                            break
                                    else:
                                        break
                                story.append(Paragraph(processed_line, styles['Normal']))
                            story.append(Spacer(1, 6))
                    
                    doc.build(story)
                    buffer.seek(0)
                    return buffer.getvalue()
                
                pdf_data = create_pdf(report, f"Research Report: {query}")
                
                # Download button
                st.download_button(
                    label="📥 Download PDF Report",
                    data=pdf_data,
                    file_name=f"research_report_{query.replace(' ', '_')}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"❌ Research failed: {str(e)}")
                st.info("💡 Try a different query or check your API keys in the .env file")
    else:
        st.warning("⚠️ Please enter a research topic to begin!")
        
# Reset example flag after research is complete
if start_research and query:
    st.session_state.from_example = False

# Footer
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px; font-size: 0.9rem;'>
    Made with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)

