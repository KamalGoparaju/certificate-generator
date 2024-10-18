
from fastapi import FastAPI, Form
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()

# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def get_html():
    # Read and return the HTML file as a response
    with open("Certificate.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.post("/generate_certificate/")
async def generate_certificate(
    name: str = Form(...),
    internship_duration: str = Form(...),
    role: str = Form(...),
    completion_date: str = Form(...)
):
    # Create a PDF
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Set certificate title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2.0, height - 100, "Internship Completion Certificate")

    # Add intern details
    c.setFont("Helvetica", 18)
    c.drawCentredString(width / 2.0, height - 200, f"This is to certify that {name}")
    c.drawCentredString(width / 2.0, height - 240, f"has successfully completed an internship as a {role}")
    c.drawCentredString(width / 2.0, height - 280, f"for the duration of {internship_duration}.")
    c.drawCentredString(width / 2.0, height - 320, f"Completed on: {completion_date}")

    # Add signature placeholder
    c.drawString(100, 150, "___________________")
    c.drawString(100, 130, "Signature")

    c.showPage()
    c.save()

    # Save the PDF in buffer and return it
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="application/pdf")
