import random
import time

print("="*60)
print("SERIAL BLOOD PRESSURE ANALYSIS SYSTEM")
print("="*60)

SAMPLE_SIZE = 1000000

signal = [
    random.randint(70,160)
    for _ in range(SAMPLE_SIZE)
]

start_time = time.time()

filtered = []

for i in range(1, len(signal)-1):

    avg = (
        signal[i-1]
        + signal[i]
        + signal[i+1]
    ) / 3

    filtered.append(avg)

peaks = []

for i in range(1, len(filtered)-1):

    if (
        filtered[i] > filtered[i-1]
        and filtered[i] > filtered[i+1]
        and filtered[i] > 130
    ):
        peaks.append(filtered[i])

end_time = time.time()

avg_pressure = sum(filtered)/len(filtered)

bpm = int(len(peaks)/1200)

print()
print("=== ANALISIS SINYAL ===")
print(f"Rata-rata Tekanan  : {avg_pressure:.2f} mmHg")
print(f"Peak Terdeteksi    : {len(peaks)}")
print(f"Estimasi BPM       : {bpm}")
print()
print("=== PERFORMA ===")
print(f"Waktu Eksekusi     : {end_time-start_time:.4f} detik")
print("="*60)
