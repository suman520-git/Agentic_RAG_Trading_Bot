# Agentic_Trading_Bot

A Agentic Chatbot  gives response for given query about finacial details of companies,stock details,genral investment suggestions.
## 🎯 Project Overview

This project demonstrates Agentic RAG concepts with Tavily search tool and Polygon financial search tool, a practical implementation steps includes:
- Creation of Pinecone vector data base from the  documents ('.pdf' and '.docx', format) uploaded dynamically through front end by the user .
- Define the In-built Tools (Tavily search tool and Polygon Financial tool).
- Binding LLM with Retriver ,Tavily and Polygon tools
- Defining the Agentic Workflow
- Building API with FastAPI 
- creation of streamlit app file for front end ,integrated with API

## 🚀 Agentic Workflow


![image alt](https://github.com/suman520-git/Agentic_RAG_Trading_Bot/blob/main/images/Workflow_graph.png?raw=true)

## 📋 Project Structure

```
Agentic_RAG_Trading_Bot                  
├─ agent                                 
│  ├─ workflow.py                        
│  └─ __init__.py                        
├─ config                                
│  └─ config.yaml                        
├─ custom_logging                        
│  ├─ my_logger.py                       
│  └─ __init__.py                        
├─ data_ingestion                        
│  ├─ ingestion_pipeline.py              
│  └─ __init__.py                        
├─ data_model                            
│  ├─ models.py                          
│  └─ __init__.py                        
├─ exception                             
│  ├─ exceptions.py                      
│  └─ __init__.py                        
├─ Experimentation                       
│  └─ experi1.ipynb                      
├─ fallback_data                         
│  ├─ 1.docx                             
│  ├─ stock_market.pdf                   
│  ├─ stock_market_investing_guide.docx  
│  └─ trading_basics.pdf                 
├─ images                                
│  └─ Workflow_graph.png                 
├─ logs                                  
│  ├─ 08_23_2025_03_05_55.log            
│  ├─ 08_23_2025_03_27_02.log            
│  └─ 08_23_2025_03_28_20.log            
├─ toolkit                               
│  ├─ tools.py                           
│  └─ __init__.py                        
├─ utils                                 
│  ├─ config_loader.py                   
│  ├─ model_loaders.py                   
│  └─ __init__.py                        
├─ main.py                               
├─ README.md                             
├─ requirements.txt                      
├─ setup.py                              
└─ streamlit_ui.py                       
            

```

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone the repository
git clone <repository-url>
cd Agentic_RAG_Trading_Bot

# Create virtual environment
conda create -p venv python==3.10 -y
conda activate venv/ 

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Create environment template
.env

# Edit .env with your API keys
# Required:
# - TAVILY_API_KEY="xxx"
# - PINECONE_API_KEY="xxx"
# - POLYGON_API_KEY="xxxx"
# - GOOGLE_API_KEY="xxxx"
# - GROQ_API_KEY="xxxx"
```

### 3. Verify Setup

```bash
# Or start the FastAPI server (from project root in virtual environment)
step.1 uvicorn main:app --host 0.0.0.0 --port 8000
# Visit http://localhost:8000/docs
step.2 after step.1 ,start through streamlit: streamlit run Streamlit_ui.py
```

## 📚 Usage

### Interactive Development
Start with in order:
1. **ingestion_pipeline.py** - Data Transformation and Ingestion in to Vectore store(PineConeDB)
2. **tools.py** - Defining the tools
3. **workflow.py** - Defining the Agentic workflow
4. **main.py** - API testing
4. **streamlit_ui.py** - Creation of front end file , integrated with API


### API Usage
Start the FastAPI server and visit `/docs` for interactive API documentation:

```bash
# Or start the FastAPI server (from project root in virtual environment)
step.1 uvicorn main:app --host 0.0.0.0 --port 8000
# Visit http://localhost:8000/docs
step.2 after step.1 ,start through streamlit: streamlit run Streamlit_ui.py
``` start through streamlit 
streamlit run Streamlit_ui.py
```

### Model Settings
- **LLM**: "meta-llama/llama-4-maverick-17b-128e-instruct"
- **Embedding**: "models/text-embedding-004"
- **Top-K Retrieval**: 2 documents



## 🆘 Support

For issues and questions:
1. Review the configuration settings
2. Ensure all API keys are properly set
3. Verify network connectivity to external services

---


