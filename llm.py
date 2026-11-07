from langchain_ollama import ChatOllama
from feilds import InvoiceFields

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

structured_llm = llm.with_structured_output(
    InvoiceFields,
    method="json_schema"
)

