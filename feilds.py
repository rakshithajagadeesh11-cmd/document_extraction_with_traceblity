from pydantic import BaseModel, Field

class InvoiceFields(BaseModel):

    invoice_number: str | None = Field(
        description="Invoice number"
    )

    bill_to: str | None = Field(
        description="Customer name under Bill To"
    )

    ship_to: str | None = Field(
        description="Shipping address"
    )

    order_id: str | None = Field(
        description="Order ID"
    )

    total_amount: str | None = Field(
        description="Final invoice total amount "
    )