from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ContactForm(BaseModel):
    nama: str
    email: str
    pesan: str

@app.post("/api/contact")
async def submit_contact(form: ContactForm):
    # Simulasi memproses dan menerima pesan dari website CV
    return {
        "status": "sukses", 
        "pesan": f"Terima kasih {form.nama}, pesan Anda akan segera dibalas ke {form.email}."
    }