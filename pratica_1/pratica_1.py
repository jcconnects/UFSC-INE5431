# Aula prática de áudio digital
import numpy as np
import matplotlib
matplotlib.use('Agg')  # sem display gráfico
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample
import os
import subprocess
import math


def process_audio_advanced(filename, target_rate=44100, bits=16):
    # Ler arquivo original:
    # - original_rate -> taxa de amostragem em Hz
    # - audio_data -> um array NumPy contendo as amostras do áudio.
    # - audio_data.shape (1 ou 2): número de canais: 1D para mono e 2D para estéreo
    original_rate, audio_data = wavfile.read(filename)

    # Se estéreo, pegar apenas um canal
    if len(audio_data.shape) > 1:
        audio_data = audio_data[:,0]
        # Seleciona todas as linhas (:) e apenas a primeira coluna (0), ou seja, o canal esquerdo.

    # Altera a taxa de amostragem do áudio (resampling),
    # len(audio_data) → número total de amostras no áudio original.
    # original_rate → taxa de amostragem do áudio original (em Hz).
    # target_rate → nova taxa de amostragem desejada (em Hz).
    # Ajusta o número de amostras do áudio para a nova taxa de amostragem.
    num_samples = int(len(audio_data) * target_rate / original_rate)

    # gera o novo áudio com a taxa de amostragem selecionada
    audio_resampled = resample(audio_data, num_samples)

    #determina o maior valor de amostra
    max_val = np.max(np.abs(audio_resampled))

    # Normaliza o áudio:
    # - Divide cada amostra pelo valor absoluto máximo (max_val) do áudio resampleado.
    # - Resultado: valores entre -1 e 1, independentemente da amplitude original.
    audio_normalized = audio_resampled / max_val

    max_val = np.max(np.abs(audio_resampled))
    if bits == 8:
        # Converte para byte entre [0,255], onde 127 é zero
        audio_processed = np.uint8(audio_normalized*127 + 128)
    elif bits == 16:
        # Converte para int16 entre [-32767, +32767]
        audio_processed = np.int16(audio_normalized * 32767)
    elif bits == 4:
        # audio_processed: valores inteiros de -7 até +7 (15 níveis)
        audio_processed = np.round(audio_normalized * 7)
        # Reescala para [0, 14]
        audio_processed = audio_processed + 7
        # Mapeia para [0, 255]
        audio_processed = np.uint8(audio_processed * (255 // 14))
    else:
        raise ValueError("Bits permitidos: 4, 8 ou 16")

    # Salvar arquivo
    base, ext = os.path.splitext(filename)
    output_filename = f"{base}_{target_rate}Hz_{bits}bit.wav"
    wavfile.write(output_filename, target_rate, audio_processed)

    if bits == 8 or bits == 4:
        # Antes de calcular a FFT, converta para float centrado em zero
        audio_processed = audio_processed.astype(np.float32)        # converte para float
        audio_processed = audio_processed - 128                     # remove offset DC
    fft_vals = np.fft.rfft(audio_processed)
    fft_freq = np.fft.rfftfreq(len(audio_processed), 1/target_rate)
    magnitude = np.abs(fft_vals)

    return audio_processed, fft_freq, magnitude, output_filename, num_samples


def get_disk_size(filepath):
    # stat retorna: tamanho_bytes blocos_512B tamanho_bloco_fs
    result = subprocess.run(['stat', '-f', '%z %b %k', filepath], capture_output=True, text=True)
    parts = result.stdout.split()
    blocks_512 = int(parts[1])
    fs_block = int(parts[2])
    # blocos de 512 bytes × 512 = bytes em disco
    disk_bytes = blocks_512 * 512
    return disk_bytes, fs_block


def maior_freq_acima_magnitude(fft_freq, magnitude, db_threshold=-30):
    # Usa threshold relativo em dB: frequências com magnitude acima de db_threshold
    # em relação ao pico máximo (ex: -30 dB = 1/1000 da magnitude máxima)
    mag_db = 20 * np.log10(magnitude / magnitude.max() + 1e-12)
    mask = mag_db > db_threshold
    if np.any(mask):
        return fft_freq[mask][-1]
    return 0.0


# ===========================================================================
# QUESTÃO A: 40 kHz, 16 bits
# ===========================================================================
filename = "audio.wav"
TARGET_A = 40000
BITS_A = 16

audio_a, freq_a, mag_a, out_a, nsamples_a = process_audio_advanced(filename, TARGET_A, BITS_A)

file_size_a = os.path.getsize(out_a)
disk_size_a, fs_block_a = get_disk_size(out_a)
data_size_a = nsamples_a * (BITS_A // 8)          # tamanho teórico dos dados
max_freq_a = maior_freq_acima_magnitude(freq_a, mag_a)
nyquist_a = TARGET_A // 2

BLOCK_SIZE = 2048
num_blocks_a = math.ceil(file_size_a / BLOCK_SIZE)
disk_size_block_a = num_blocks_a * BLOCK_SIZE

print("=" * 60)
print(f"QUESTÃO A — {TARGET_A} Hz, {BITS_A} bits por amostra")
print("=" * 60)
print(f"  i)  Maior frequência com conteúdo significativo (acima de -30 dB): {max_freq_a:.0f} Hz")
print(f"  ii) Maior frequência possível (Nyquist): {nyquist_a} Hz ({nyquist_a/1000:.0f} kHz)")
print(f"  iii) Tamanho teórico dos dados: {data_size_a} bytes ({data_size_a/1024:.0f} KB)")
print(f"  iv) Tamanho real do arquivo: {file_size_a} bytes")
print(f"       Diferença: {file_size_a - data_size_a} bytes de cabeçalho WAV (metadados do formato RIFF/WAV)")
print(f"  v)  Tamanho em disco: {disk_size_a} bytes (bloco do FS: {fs_block_a} B)")
fs_blocks_a = math.ceil(file_size_a / fs_block_a)
print(f"       O FS aloca em blocos de {fs_block_a} B: ceil({file_size_a}/{fs_block_a})={fs_blocks_a} blocos = {fs_blocks_a*fs_block_a} bytes.")
print(f"       Diferença de {disk_size_a - file_size_a:+d} bytes em relação ao tamanho do arquivo.")
print(f"  vi) Tamanho em disco com bloco de {BLOCK_SIZE} B:")
print(f"       ceil({file_size_a} / {BLOCK_SIZE}) = {num_blocks_a} blocos × {BLOCK_SIZE} B = {disk_size_block_a} bytes")

# ===========================================================================
# QUESTÃO B: 10 kHz, 16 bits
# ===========================================================================
TARGET_B = 10000
BITS_B = 16

audio_b, freq_b, mag_b, out_b, nsamples_b = process_audio_advanced(filename, TARGET_B, BITS_B)

data_size_b = nsamples_b * (BITS_B // 8)
nyquist_b = TARGET_B // 2

print()
print("=" * 60)
print(f"QUESTÃO B — {TARGET_B} Hz, {BITS_B} bits por amostra")
print("=" * 60)
print(f"  i)  Efeito: redução da taxa de amostragem elimina frequências acima de {nyquist_b} Hz,")
print(f"       tornando o áudio mais abafado (perda de agudos).")
print(f"       Maior frequência possível (Nyquist): {nyquist_b} Hz ({nyquist_b/1000:.0f} kHz)")
print(f"  ii) Tamanho dos dados: {data_size_b} bytes ({data_size_b/1024:.0f} KB)")

# ===========================================================================
# QUESTÃO C: 4 kHz, 4 bits
# ===========================================================================
TARGET_C = 4000
BITS_C = 4

audio_c, freq_c, mag_c, out_c, nsamples_c = process_audio_advanced(filename, TARGET_C, BITS_C)

file_size_c = os.path.getsize(out_c)
data_size_c_teorico = int(nsamples_c * BITS_C / 8)   # tamanho teórico com 4 bits reais
data_size_c_real = nsamples_c * 1                     # uint8 = 1 byte por amostra no arquivo
nyquist_c = TARGET_C // 2

print()
print("=" * 60)
print(f"QUESTÃO C — {TARGET_C} Hz, {BITS_C} bits por amostra")
print("=" * 60)
print(f"  i)  Efeito: taxa muito baixa causa perda severa de frequências e audível ruído de")
print(f"       quantização (apenas 15 níveis). O áudio fica abafado com artefatos.")
print(f"       Maior frequência possível (Nyquist): {nyquist_c} Hz ({nyquist_c/1000:.0f} kHz)")
print(f"  ii) Tamanho teórico (4 bits/amostra): {nsamples_c} amostras × 0,5 byte = {data_size_c_teorico} bytes ({data_size_c_teorico/1024:.0f} KB)")
print(f"  iii) O arquivo gerado NÃO mantém 4 bits por amostra.")
print(f"       O formato WAV não suporta 4 bits; o menor tipo disponível é uint8 (8 bits).")
print(f"       Por isso cada amostra ocupa 1 byte, e o arquivo de dados tem {data_size_c_real} bytes")
print(f"       (tamanho real do arquivo: {file_size_c} bytes).")
