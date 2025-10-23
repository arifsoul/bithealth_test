import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

# LangChain Imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Untuk memuat API key dari .env
from dotenv import load_dotenv

load_dotenv()

# Cek apakah API key ada
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY tidak ditemukan. Harap buat file .env dan tambahkan GOOGLE_API_KEY='AIza...'.")

LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "gemini-2.5-flash-preview-09-2025")

# --- Model Pydantic (Validasi Input & Output) ---

class PatientInfo(BaseModel):
    """Model untuk data input pasien."""
    gender: str = Field(..., description="Jenis kelamin pasien (misal: 'female', 'male')")
    age: int = Field(..., description="Usia pasien dalam tahun", gt=0)
    symptoms: List[str] = Field(..., description="Daftar gejala yang dilaporkan pasien", min_length=1)

    class Config:
        json_schema_extra = {
            "example": {
                "gender": "female",
                "age": 62,
                "symptoms": ["pusing", "mual", "sulit berjalan"]
            }
        }

class RecommendationResponse(BaseModel):
    """Model untuk data output rekomendasi."""
    recommended_department: str = Field(..., description="Departemen spesialis yang direkomendasikan")


# --- Inisialisasi FastAPI ---
app = FastAPI(
    title="BitHealth AI Triage API",
    description="API untuk merekomendasikan departemen rumah sakit berdasarkan gejala pasien menggunakan LLM.",
    version="1.0.0"
)


# --- Pengaturan LangChain (LLM Chain) ---

# 1. Definisikan Model LLM
# --- PERUBAHAN BARU ---
# Menggunakan variabel LLM_MODEL_NAME dari .env
model = ChatGoogleGenerativeAI(model=LLM_MODEL_NAME, temperature=0.2)
# --- AKHIR PERUBAHAN ---


# 2. Definisikan Prompt Template
system_prompt = """
Anda adalah asisten triase AI yang ahli di rumah sakit Indonesia. 
Tugas Anda adalah merekomendasikan SATU departemen spesialis yang paling relevan 
berdasarkan data pasien.

Daftar departemen yang valid adalah:
- Kardiology (Jantung dan pembuluh darah)
- Neurology (Otak, tulang belakang, dan sistem saraf)
- Ortopedi (Tulang, sendi, ligamen)
- Gastroenterology (Sistem pencernaan, lambung, usus)
- Pulmonology (Paru-paru dan pernapasan)
- THT (Telinga, Hidung, Tenggorokan)
- Mata
- Penyakit Dalam (Kondisi medis umum dan kronis)
- Ginekology (Kesehatan reproduksi wanita)
- Urology (Saluran kemih dan sistem reproduksi pria)
- Dermatology (Kulit)

Analisis data pasien dan berikan HANYA NAMA departemen yang paling sesuai. 
Jangan berikan penjelasan, hanya nama departemen.
"""

human_prompt = "Data Pasien:\n- Jenis Kelamin: {gender}\n- Usia: {age} tahun\n- Gejala: {symptoms_list}"

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", human_prompt)
])

# 3. Definisikan Output Parser
output_parser = StrOutputParser()

# 4. Rangkai (Chain) semua komponen
chain = prompt_template | model | output_parser


# --- Endpoint FastAPI ---

@app.post(
    "/recommend",
    response_model=RecommendationResponse,
    summary="Rekomendasikan Departemen Spesialis",
    tags=["Triage"]
)
async def recommend_department(patient_info: PatientInfo):
    """
    Menerima data pasien (usia, jenis kelamin, gejala) dan 
    mengembalikan rekomendasi departemen spesialis.
    """
    try:
        symptoms_string = ", ".join(patient_info.symptoms)
        
        input_data = {
            "gender": patient_info.gender,
            "age": patient_info.age,
            "symptoms_list": symptoms_string
        }
        
        # Panggil LangChain (chain.invoke)
        raw_recommendation = await chain.ainvoke(input_data)
        
        cleaned_recommendation = raw_recommendation.strip()
        
        return RecommendationResponse(recommended_department=cleaned_recommendation)

    except Exception as e:
        print(f"Error saat memanggil LLM: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Terjadi kesalahan pada server saat memproses rekomendasi: {str(e)}"
        )

# Perintah untuk menjalankan server (jika file ini dieksekusi langsung)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

