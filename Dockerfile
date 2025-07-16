# Gunakan Ubuntu versi terbaru sebagai base image
#FROM ubuntu:24.04 
#FROM ubuntu:22.04 
FROM ubuntu:20.04 

# Set environment variable untuk non-interaktif saat instalasi paket
ENV DEBIAN_FRONTEND=noninteractive

# Update paket dan instal tool yang diperlukan, termasuk tzdata
RUN apt-get update && \
    apt-get install -y tzdata sudo git wget vim curl nano && \
    rm -rf /var/lib/apt/lists/*

# Konfigurasi timezone ke Asia/Tokyo (Jepang)
# Untuk daftar timezone yang tersedia, Anda bisa cek di https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata


CMD ["bash"]