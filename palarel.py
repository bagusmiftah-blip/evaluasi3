from multiprocessing import Pool
import random
import time


# ==========================
# SIGNAL PROCESSING
# ==========================

def process_chunk(chunk):

    # Moving Average Filter
    filtered = []

    for i in range(1, len(chunk)-1):
        avg = (
            chunk[i-1]
            + chunk[i]
            + chunk[i+1]
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

    return {
        "mean": sum(filtered)/len(filtered),
        "max": max(filtered),
        "min": min(filtered),
        "peak_count": len(peaks)
    }


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":

    print("="*60)
    print("PARALLEL BLOOD PRESSURE ANALYSIS SYSTEM")
    print("="*60)

    SAMPLE_SIZE = 1000000
    NUM_PROCESS = 4

    # Simulasi data sensor tekanan darah
    signal = [
        random.randint(70,160)
        for _ in range(SAMPLE_SIZE)
    ]

    chunk_size = len(signal)//NUM_PROCESS

    chunks = []

    for i in range(NUM_PROCESS):

        start = i*chunk_size

        if i == NUM_PROCESS-1:
            end = len(signal)
        else:
            end = (i+1)*chunk_size

        chunks.append(signal[start:end])

    start_time = time.time()

    with Pool(NUM_PROCESS) as pool:
        results = pool.map(process_chunk, chunks)

    end_time = time.time()

    avg_pressure = sum(
        r["mean"] for r in results
    ) / len(results)

    max_pressure = max(
        r["max"] for r in results
    )

    min_pressure = min(
        r["min"] for r in results
    )

    total_peaks = sum(
        r["peak_count"] for r in results
    )

    # Simulasi BPM
    bpm = int(total_peaks / 1200)

    print(f"Jumlah Sampel      : {SAMPLE_SIZE:,}")
    print(f"Jumlah Process     : {NUM_PROCESS}")
    print()
    print("=== ANALISIS SINYAL ===")
    print(f"Rata-rata Tekanan  : {avg_pressure:.2f} mmHg")
    print(f"Tekanan Maksimum   : {max_pressure:.2f} mmHg")
    print(f"Tekanan Minimum    : {min_pressure:.2f} mmHg")
    print(f"Peak Terdeteksi    : {total_peaks}")
    print(f"Estimasi BPM       : {bpm}")
    print()
    print("=== PERFORMA ===")
    print(f"Waktu Eksekusi     : {end_time-start_time:.4f} detik")
    print("="*60)
