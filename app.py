import streamlit as st
import fitz
from main import graph

st.title("Invoice Information Extraction")

uploaded_file = st.file_uploader(
    "Upload Invoice PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_bytes = uploaded_file.getvalue()

    with st.spinner("Extracting invoice fields..."):

        result = graph.invoke({
            "pdf_bytes": pdf_bytes,
            "pdf_text": "",
            "blocks": [],
            "invoice_fields": None,
            "highlights": None,
            "error": None
        })

    st.subheader("Extracted Invoice Fields")

    for field, value in result["invoice_fields"].items():

        st.write(f"**{field.replace('_', ' ').title()}**: {value}")

    st.divider()

    st.subheader("Highlighted Invoice")

    doc = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    highlights = result["highlights"]

    for field, matches in highlights.items():

        for match in matches:

            page = doc[match["page"]]

            rect = fitz.Rect(match["bbox"])

            annot = page.add_highlight_annot(rect)

            annot.update()

    for page in doc:

        pix = page.get_pixmap(
            matrix=fitz.Matrix(1.5, 1.5),
            alpha=False
        )

        st.image(
            pix.tobytes("png"),
            use_container_width=True
        )

    doc.close()