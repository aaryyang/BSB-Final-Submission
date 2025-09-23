# 🤖 AI Research Agent

An intelligent conversational research assistant that provides comprehensive, multi-perspective analysis through natural chat interaction. Built with advanced AI capabilities and a modern, clean interface.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![Groq](https://img.shields.io/badge/AI-Groq%20LLaMA-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Key Features

### � **Conversational AI Interface**
- Natural chat-based interaction with your research agent
- Intelligent intent recognition (research vs. questions vs. greetings)
- Memory and conversation context for follow-up questions
- Smooth typing indicators and professional chat bubbles

### 🔍 **Intelligent Research Engine**
- Multi-perspective research with 4 different query angles
- Automatic topic extraction and query optimization
- Real-time research progress with clean UI (input area hidden during research)
- Professional research reports with comprehensive analysis

### 🎯 **Smart User Experience**
- One-click example buttons for instant interaction
- Research Mode toggle for forcing research on any query
- Dark theme with professional styling and animations
- Clean progress indicators positioned above input area

### 🧠 **Advanced AI Capabilities**
- Powered by Groq LLaMA for fast, intelligent responses
- Context-aware conversation memory
- Sophisticated intent analysis and response generation
- Seamless integration between chat and research functionality

### 📊 **Professional Research Output**
- Comprehensive analysis from multiple sources
- Fact-checking and credibility assessment
- Professional citations (APA, MLA, Simple formats)
- Expandable research results sections

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- [Groq API Key](https://console.groq.com/) (for AI conversation and analysis)
- [Tavily API Key](https://tavily.com/) (for comprehensive web research)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-research-agent.git
   cd ai-research-agent
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

5. **Run the AI Research Agent**
   ```bash
   streamlit run agent_app.py
   ```

6. **Start chatting with your agent**
   
   Navigate to `http://localhost:8501` and begin your research conversation!

## 🔧 Configuration

### API Keys Setup

#### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Generate a new API key
5. Add it to your `.env` file

#### Tavily API Key
1. Visit [Tavily](https://tavily.com/)
2. Create an account
3. Access your dashboard
4. Copy your API key
5. Add it to your `.env` file

### Citation Styles
The application supports three citation formats:
- **APA**: American Psychological Association format
- **MLA**: Modern Language Association format  
- **Simple**: Clean, accessible format

## � How to Use Your AI Research Agent

### Getting Started
1. **Launch the agent** and you'll see three example buttons:
   - 👋 "Hello, what can you do?" - Learn about agent capabilities
   - 🚗 "Research Tesla vs competitors" - Instant research demo
   - 🤖 "Tell me about AI ethics" - Explore AI topics

2. **Start a conversation** by clicking any button or typing in the chat input

### Conversation Types

#### 🤝 **Ask Questions**
- "What can you do?"
- "How do you work?"
- "What are your capabilities?"
- Agent responds with helpful information about its features

#### 🔬 **Request Research**
- "Research Tesla vs competitors"
- "Tell me about climate change"
- "Analyze startup funding trends"
- Agent performs comprehensive multi-source research

#### 💭 **Natural Chat**
- "Hello" or greetings
- Follow-up questions about previous research
- Clarifications and expansions on topics

### Advanced Features
- **Research Mode Toggle**: Force any input to trigger research
- **Clean Research Experience**: Input area disappears during research for focused viewing
- **Conversation Memory**: Agent remembers context for better follow-ups
- **Citation Styles**: Choose APA, MLA, or Simple format for research outputs

### Example Research Topics
- **Technology**: "AI ethics", "blockchain applications", "cybersecurity trends"
- **Business**: "Remote work productivity", "startup strategies", "market analysis"
- **Science**: "Climate solutions", "space exploration", "medical breakthroughs"
- **Society**: "Education trends", "social media impact", "urban planning"

## 🏗️ Project Structure

```
BSB-Final-Submission/
│
├── agent_app.py          # Main AI Research Agent application
├── main.py              # Core research engine and API integration
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore rules (API keys secured)
├── README.md           # Project documentation
│
└── venv/               # Virtual environment (auto-generated)
```

### Key Files
- **`agent_app.py`**: Complete conversational AI interface with chat, research, and UI
- **`main.py`**: Research engine with Tavily integration and multi-perspective analysis
- **`.env`**: Secure storage for Groq and Tavily API keys
- **`requirements.txt`**: All necessary Python packages

## 🧠 How It Works

### Conversation Flow
1. **Intent Analysis**: AI determines if you're asking questions, requesting research, or just chatting
2. **Context Memory**: Agent remembers previous conversation for relevant follow-ups
3. **Response Generation**: Creates appropriate responses based on your intent
4. **Research Triggers**: Automatically initiates research when topics are requested

### Research Process
1. **Topic Extraction**: Clean extraction of research topics from natural language
2. **Multi-Perspective Generation**: Creates 4 distinct search angles for comprehensive coverage
3. **Clean UI Experience**: Input area disappears, showing only research progress
4. **Web Search**: Executes searches using Tavily API with advanced ranking
5. **Source Analysis**: Evaluates credibility and relevance of sources
6. **Content Synthesis**: AI combines information from all sources into coherent analysis
7. **Professional Presentation**: Results displayed in expandable, well-formatted sections

### AI Technology Stack
- **Groq LLaMA 3.1 8B**: Lightning-fast conversational AI and analysis
- **Tavily Search API**: Advanced web search with source credibility ranking
- **Streamlit**: Modern, responsive web interface with real-time updates
- **Custom Algorithms**: Intent recognition, context management, and UI optimization

## 🔒 Privacy & Security

- **No Data Storage**: Queries and results are not permanently stored
- **Secure API Calls**: All external API communications are encrypted
- **Local Processing**: Research reports generated locally
- **Environment Variables**: Sensitive API keys stored securely

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run tests**: Ensure existing functionality works
5. **Commit changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add docstrings to new functions
- Test with different research topics
- Ensure mobile responsiveness for UI changes

## 📋 Requirements

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: 3.8 or higher
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Internet**: Stable connection for API calls

### Dependencies
```
streamlit>=1.28.0        # Web application framework
groq>=0.4.0             # AI language model API
tavily-python>=0.3.0    # Web search API
python-dotenv>=1.0.0    # Environment variable management
reportlab>=4.0.0        # PDF generation
```

## 🐛 Troubleshooting

### Common Issues

**"Module not found" errors**
```bash
pip install -r requirements.txt
```

**API Key errors**
- Verify your API keys in the `.env` file
- Check that your API keys have sufficient credits
- Ensure no extra spaces in the `.env` file

**Streamlit not starting**
```bash
# Check if port 8501 is available
streamlit run agent_app.py --server.port 8502
```

**PDF generation issues**
- Ensure `reportlab` is properly installed
- Check available disk space
- Verify write permissions in the project directory

## 📊 Performance

### Response Times
- **Simple queries**: 15-30 seconds
- **Complex research**: 45-90 seconds
- **PDF generation**: 2-5 seconds

### Rate Limits
- **Groq API**: 30 requests/minute (free tier)
- **Tavily API**: 1000 requests/month (free tier)

## 🔄 Updates & Changelog

### Version 2.0.0 (Current)
- ✅ Conversational AI interface with natural chat
- ✅ Intelligent intent recognition (questions vs. research vs. greetings)
- ✅ Multi-perspective research engine with 4-angle analysis
- ✅ Clean research experience (hidden input during research)
- ✅ Professional dark theme with smooth animations
- ✅ Context-aware conversation memory
- ✅ Smart example buttons with proper state management
- ✅ Progress indicators positioned above input area
- ✅ Expandable research results with professional formatting
- ✅ Multiple citation formats (APA, MLA, Simple)
- ✅ Research Mode toggle for forcing comprehensive analysis

### Upcoming Features (Roadmap)
- 🔮 Conversation history and bookmarking
- 🔮 Export research results to PDF/DOCX
- 🔮 Advanced source filtering and preferences
- 🔮 Multi-language support
- 🔮 Team collaboration and sharing features

## 📞 Support

### Getting Help
- **Issues**: Report bugs via GitHub Issues
- **Documentation**: Check this README first
- **Community**: Join discussions in GitHub Discussions

### Contact
- **Email**: [your-email@example.com]
- **GitHub**: [@yourusername]
- **Twitter**: [@yourhandle]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq**: For providing fast, efficient AI language processing
- **Tavily**: For comprehensive web search capabilities
- **Streamlit**: For the excellent web app framework
- **ReportLab**: For professional PDF generation
- **Community**: For feedback and contributions

---

## 🎯 Perfect For

- **Students**: Research papers, assignments, and academic projects
- **Professionals**: Market analysis, competitive research, and industry insights
- **Writers**: Background research, fact-checking, and source gathering
- **Curious Minds**: Learning about any topic with comprehensive, reliable information
- **Teams**: Collaborative research with consistent, professional outputs

## 🌟 What Makes This Special

Unlike traditional search tools, this AI Research Agent:
- **Thinks like a researcher**: Multiple perspectives, not just one search
- **Converses naturally**: Chat with your agent like a colleague
- **Maintains context**: Remembers what you've discussed for better follow-ups
- **Provides clean experience**: UI adapts to focus on what matters
- **Delivers professionally**: Properly cited, credible, comprehensive results

---

**Made with ❤️ for researchers, students, and curious minds everywhere.**

*Happy Researching with your AI Agent! 🤖✨*