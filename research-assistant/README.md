# 🔬 AI Research Assistant

A powerful, AI-driven research tool that provides comprehensive, multi-perspective analysis on any topic with professional citations and fact-checking capabilities.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

### 🔍 **Multi-Perspective Research**
- Generates 4 different search queries from various angles
- Comprehensive coverage of any research topic
- Eliminates blind spots in traditional single-query searches

### 🎯 **Source Credibility Analysis**
- **🟢 High Credibility**: Academic institutions, news outlets, government sources
- **🟡 Medium Credibility**: Industry publications, review sites
- **🔴 Low Credibility**: Commercial/sales-focused content
- Color-coded reliability indicators for instant assessment

### ✅ **Advanced Fact-Checking**
- Cross-references information across multiple sources
- Identifies contradictions and inconsistencies
- Provides confidence levels for key claims

### 📚 **Professional Citations**
- **APA Style**: Academic standard formatting
- **MLA Style**: Literary and humanities formatting  
- **Simple Format**: Clean, accessible citations
- Automatic inline citations with source mapping

### 📄 **PDF Report Generation**
- Professional, formatted research reports
- Executive summaries with key findings
- Complete source bibliography
- One-click download functionality

### 🎨 **Clean, Professional Interface**
- Intuitive, centered layout design
- Smart example queries with override functionality
- Real-time research progress indicators
- Mobile-responsive design

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- [Groq API Key](https://console.groq.com/) (for AI language processing)
- [Tavily API Key](https://tavily.com/) (for web search capabilities)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant
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

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:8501` to access the application.

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

## 📖 Usage

### Basic Research
1. Enter your research topic in the search bar
2. Click "🚀 Start Research" 
3. Watch as the AI generates multiple search perspectives
4. Review the comprehensive results with credibility indicators
5. Download your research as a PDF report

### Example Queries
- **Technology**: "Tesla vs competitors", "artificial intelligence ethics"
- **Environment**: "climate change solutions", "renewable energy trends"
- **Business**: "startup funding strategies", "remote work productivity"
- **Health**: "nutrition and mental health", "exercise and longevity"

### Smart Features
- **Auto-complete**: Type to see intelligent suggestions
- **Example Override**: Click example buttons to override your current query
- **Progress Tracking**: Real-time updates during research process
- **Source Filtering**: Focus on high-credibility sources when needed

## 🏗️ Project Structure

```
ai-research-assistant/
│
├── app.py                 # Streamlit frontend application
├── main.py               # Core research logic and AI integration
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create this)
├── README.md            # Project documentation
│
├── venv/                # Virtual environment (auto-generated)
└── __pycache__/         # Python cache (auto-generated)
```

## 🧠 How It Works

### Research Process
1. **Query Analysis**: AI analyzes your research topic
2. **Multi-Perspective Generation**: Creates 4 distinct search angles
3. **Web Search**: Executes searches using Tavily API
4. **Source Evaluation**: Analyzes credibility of each source
5. **Content Synthesis**: AI combines information from all sources
6. **Fact Verification**: Cross-references claims across sources
7. **Report Generation**: Creates comprehensive, cited research report

### AI Models Used
- **Groq LLaMA 3.1 8B**: Fast, efficient language processing
- **Tavily Search**: Advanced web search with source ranking
- **Custom Algorithms**: Credibility scoring and fact-checking

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
streamlit run app.py --server.port 8502
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

### Version 1.0.0 (Current)
- ✅ Multi-perspective research engine
- ✅ Source credibility analysis
- ✅ Professional citation formatting
- ✅ PDF report generation
- ✅ Clean, responsive UI
- ✅ Smart example button behavior

### Upcoming Features (Roadmap)
- 🔮 Research history and favorites
- 🔮 Advanced filtering options
- 🔮 Team collaboration features
- 🔮 API endpoint for integrations
- 🔮 Mobile app companion

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

**Made with ❤️ for researchers, students, and curious minds everywhere.**

*Happy Researching! 🔬✨*