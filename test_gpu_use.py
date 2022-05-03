import tensorflow as tf
tf.__version__
print('Проверка настройки использования GPU')
print('По окончании теста должно быть такое сообщение:')
print(60*'_')
print("[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]")
print(60*'=')
print('Результат теста:')
print(tf.config.list_physical_devices())
print(60*'_')