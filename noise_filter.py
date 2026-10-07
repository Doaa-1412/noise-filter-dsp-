import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

# قراءة ملف الصوت
data, fs = sf.read("ad.mp3")

# لو stereo خليه mono
if len(data.shape) > 1:
    data = data[:, 0]

# تحويل لـ float
data = data.astype(np.float32)

# إضافة ضوضاء
noise = np.random.normal(0, 0.5 * np.max(data), data.shape)
noisy_signal = data + noise

# تصميم فلتر Low-pass
b, a = signal.butter(4, 0.1, btype='low')
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# رسم النتائج
t = np.arange(len(data)) / fs

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, data)
plt.title('الإشارة الأصلية')

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal, color='red')
plt.title('الإشارة مع الضوضاء')

plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal, color='green')
plt.title('الإشارة بعد الفلتر')

plt.tight_layout()
plt.show()
