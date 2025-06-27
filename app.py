(Flask - Python) =================
# app.py
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    bab = data.get("bab")
    inputs = data.get("inputs")

    prompt = build_prompt(bab, inputs)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Anda ialah pembantu penulisan laporan teknikal dalam Bahasa Melayu."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response['choices'][0]['message']['content']
    return jsonify({"output": output})

def build_prompt(bab, inputs):
    if bab == "bab1":
        return f"""
Saya ingin anda hasilkan Bab 1: Pengenalan berdasarkan maklumat berikut:
Tajuk: {inputs['tajuk']}
Masalah: {inputs['masalah']}
Kepentingan: {inputs['kepentingan']}
Pihak terkesan: {inputs['pihak']}
Objektif: {inputs['objektif']}
Skop: {inputs['skop']}
Limitasi: {inputs['limitasi']}
Sumbangan: {inputs['sumbangan']}

Tulis dalam bahasa Melayu akademik, formal dan berstruktur. Panjang: 1–2 muka surat.
"""
    elif bab == "bab2":
        return f"""
Hasilkan Bab 2: Kajian Literatur berdasarkan:
Topik: {inputs['topik']}
Kajian/teknologi: {inputs['kajian']}
Kekurangan: {inputs['kekurangan']}
Justifikasi projek: {inputs['justifikasi']}

Tulis dengan ulasan perbandingan dan rumusan.
"""
    elif bab == "bab3":
        return f"""
Hasilkan Bab 3: Metodologi berdasarkan:
Jenis projek: {inputs['jenis']}
Komponen: {inputs['komponen']}
Prosedur pembangunan: {inputs['prosedur']}
Alat & bahan: {inputs['alat_bahan']}
Perisian/sistem: {inputs['perisian']}
Carta alir: {inputs['carta']}

Tulis dalam format berstruktur dan kronologi.
"""
    elif bab == "bab4":
        return f"""
Hasilkan Bab 4: Hasil dan Perbincangan berdasarkan:
Hasil akhir: {inputs['hasil']}
Ujian/penilaian: {inputs['ujian']}
Dapatan utama: {inputs['dapatan']}
Pencapaian objektif: {inputs['objektif_capai']}
Perbandingan: {inputs['perbandingan']}
Kelemahan & penambahbaikan: {inputs['kelemahan']}
"""
    elif bab == "bab5":
        return f"""
Hasilkan Bab 5: Rumusan dan Cadangan berdasarkan:
Rumusan: {inputs['rumusan']}
Pencapaian: {inputs['pencapaian']}
Cabaran: {inputs['cabaran']}
Cadangan kajian lanjut: {inputs['cadangan']}
Aplikasi sebenar: {inputs['aplikasi']}
"""
    else:
        return "Maklumat bab tidak dikenalpasti."

if __name__ == '__main__':
    app.run(debug=True)