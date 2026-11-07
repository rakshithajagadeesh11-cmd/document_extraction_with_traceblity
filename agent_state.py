from typing import TypedDict, Optional

class AgentState(TypedDict):

    pdf_bytes: bytes
    pdf_text: str
    blocks: list
    invoice_fields: Optional[dict]
    highlights: Optional[dict]
    error: Optional[str]