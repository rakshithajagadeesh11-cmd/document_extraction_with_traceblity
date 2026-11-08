# Invoice PDF Extraction using LangGraph and Ollama

## Overview

This project implements an AI-powered invoice information extraction pipeline using **LangGraph, Ollama, PyMuPDF, Pydantic, and Streamlit**.

Users can upload an invoice PDF, extract important invoice fields, and view the extracted information alongside the original document with relevant text highlighted using bounding boxes.

## Key Features

- Upload invoice PDFs through a Streamlit interface.
- Extract text and layout information from PDF documents using PyMuPDF (`fitz`).
- Identify key invoice fields using an LLM.
- Use Pydantic structured output for consistent extraction.
- Orchestrate the extraction workflow using LangGraph.
- Locate extracted values in the original PDF using bounding-box coordinates.
- Highlight extracted fields in the PDF.

## Information Extracted

The application is designed to extract:

- Invoice Number
- Bill To
- Ship To
- Order ID
- Total Amount

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| PyMuPDF | PDF text and bounding-box extraction |
| LangGraph | Workflow orchestration |
| Ollama | Local LLM inference |
| Llama 3.2 | Information extraction |
| Pydantic | Structured output validation |
| Streamlit | User interface |

## Architecture

The application follows a three-stage LangGraph workflow:

1. **PDF Extraction**
   - Accepts PDF bytes.
   - Extracts text and bounding-box coordinates using PyMuPDF.
   - Stores extracted content in the graph state.

2. **Field Identification**
   - Sends invoice text to the LLM.
   - Identifies the required invoice fields.
   - Returns structured output using Pydantic.

3. **Field Highlighting**
   - Matches extracted values against PDF text blocks.
   - Retrieves corresponding bounding-box coordinates.
   - Highlights the extracted information in the original PDF.

## Workflow

```text
       PDF Upload
           |
           v
    Streamlit Interface
           |
           v
      LangGraph
           |
           v
    Extract PDF Content
      (PyMuPDF)
           |
           v
    Identify Invoice Fields
       (Ollama LLM)
           |
           v
     Structured Output
        (Pydantic)
           |
           v
     Match Bounding Boxes
           |
           v
      Highlight PDF
           |
           v
    Display Results
      (Streamlit)
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/invoice-pdf-extraction-langgraph.git

cd invoice-pdf-extraction-langgraph
```

### 2. Create a virtual environment

```bash
python -m venv doc_ex
```

Activate it:

**macOS / Linux**

```bash
source doc_ex/bin/activate
```

**Windows**

```bash
doc_ex\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/

Pull the required model:

```bash
ollama pull llama3.2
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the local Streamlit URL displayed in your terminal.

## Project Structure

```text
invoice-pdf-extraction/
│
├── app.py              # Streamlit application
├── state.py            # LangGraph state definition
├── nodes.py            # PDF extraction and field identification nodes
├── graph.py            # LangGraph workflow definition
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore
└── data/               # Local invoice PDF files
```

*Adjust the filenames above to match your actual project.*

## Future Enhancements

- Support scanned PDFs using OCR.
- Improve extraction accuracy for complex invoice layouts.
- Add confidence scores for extracted fields.
- Support multiple invoice formats.
- Add field-level validation.
- Improve bounding-box matching for multi-page invoices.
- Introduce an evaluation dataset to measure extraction accuracy.

## Author

Developed as a hands-on project exploring document intelligence, LLM-based information extraction, and agentic workflow orchestration using LangGraph.


graph:
   +-----------+    
    | __start__ |    
    +-----------+    
          *          
          *          
          *          
  +-------------+    
  | extract_pdf |    
  +-------------+    
          *          
          *          
          *          
+-----------------+  
| identify_fields |  
+-----------------+  
          *          
          *          
          *          
+------------------+ 
| highlight_fields | 
+------------------+ 
          *          
          *          
          *          
    +---------+      
    | __end__ |      
    +---------+      
