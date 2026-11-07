from agent_state import AgentState
import fitz
from llm import structured_llm

def identify_fields(state: AgentState):

    prompt = f"""
    You are an invoice extraction assistant.

    Extract the following fields from the invoice:

    1. Invoice Number
    2. Bill To
    3. Ship To
    4. Order ID
    5. Total Amount

    Rules:
    - Extract only information present in the document.
    - Do not invent values.
    - Return None for missing fields.
    - Total Amount means the final invoice total,
      not subtotal or balance due.

    Invoice Text:
    {state['pdf_text']}
    """

    result = structured_llm.invoke(prompt)

    return {
        "invoice_fields": result.model_dump(),
        "error": None
    }


def highlight_fields(state: AgentState):

    highlights = {}

    fields = state["invoice_fields"]

    for field, value in fields.items():

        if not value:
            continue

        matches = []

        for block in state["blocks"]:

            if str(value).lower() in block["text"].lower():

                matches.append({
                    "page": block["page"],
                    "bbox": block["bbox"]
                })

        highlights[field] = matches

    return {
        "highlights": highlights
    }



def extract_pdf(state: AgentState):

    doc = fitz.open(
        stream=state["pdf_bytes"],
        filetype="pdf"
    )

    pdf_text = ""
    blocks_data = []

    for page_num, page in enumerate(doc):

        blocks = page.get_text("blocks")

        for b in blocks:

            text = b[4].strip()

            if text:
                pdf_text += text + "\n"

                blocks_data.append({
                    "page": page_num,
                    "text": text,
                    "bbox": [b[0], b[1], b[2], b[3]]
                })

    doc.close()

    return {
        "pdf_text": pdf_text,
        "blocks": blocks_data
    }