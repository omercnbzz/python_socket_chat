## Python Socket Chat App

Bu proje, Python kullanılarak geliştirilmiş basit bir TCP/IP tabanlı chat uygulamasıdır. Bir sunucu (`chat_server.py`) ve bir istemci (`chat_client.py`) dosyasından oluşur. Her istemci sunucuya bağlanarak anlık mesajlaşma gerçekleştirebilir.

## Özellikler

- Birden fazla istemciyle eş zamanlı iletişim
- Basit terminal tabanlı chat
- `threading` ile çoklu istemci desteği
- Kolay anlaşılır ve sade yapı

##  Dosyalar

- `chat_server.py` – Sunucu kodu, gelen istemci bağlantılarını dinler.
- `chat_client.py` – İstemci kodu, sunucuya bağlanıp mesaj gönderir/alır.

## Gereksinimler

- Python 3.x (tavsiye edilen: 3.8+)

## Kullanım

### 1. Sunucuyu başlat

```bash
python chat_server.py
