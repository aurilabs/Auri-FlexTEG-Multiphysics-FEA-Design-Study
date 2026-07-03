# Auri Labs: Advanced 3D FEA Thermoelectric Optimization
## Finned & Segmented Semiconductor Architecture (V2)

## English

### 1. Abstract
This folder contains the Version 2 (V2) 3D Finite Element Analysis (FEA) multiphysics simulations for the Auri-FlexTEG project developed in COMSOL Multiphysics. Moving beyond the monolithic baseline established in V1, this study introduces a geometrically optimized, segmented semiconductor architecture (n-type and p-type pairs) combined with longitudinal cooling fins. The objective is to maximize the radial thermal gradient ($\Delta T$) via passive atmospheric convection and validate the Seebeck voltage scaling principles under rigorous, non-uniform industrial boundary conditions.

### 2. Semiconductor Integration & Physics
To establish a functional thermoelectric circuit, the monolithic structure was partitioned into a discrete p-n junction pair, showcasing advanced control over transport properties in computational materials science:
* **P-Type Domain (Sol):** Configured with a positive Seebeck coefficient ($S_p = +120 \ \mu\text{V/K}$) to simulate hole-dominated carrier transport.
* **N-Type Domain (Sağ):** Configured with a negative Seebeck coefficient ($S_n = -120 \ \mu\text{V/K}$) to simulate electron-dominated carrier transport.
* **Electrical Insulation:** A strict electrical insulation boundary condition was applied at the continuous vertical interface between the p and n domains. This crucial boundary condition prevents internal charge recombination (short-circuiting), forcing carrier migration toward the terminal interconnects.

### 3. Realistic Aerodynamic & Material Parameters
The model incorporates precise isotropic material properties derived from analytical percolation thresholds of $\text{Ag}_2\text{Se}/\text{PEDOT:PSS}$ flexible composites, alongside highly realistic convective heat transfer profiles:
* **Core Heat Source (Industrial Pipe):** $r = 50 \text{ mm}$, internal boundary maintained at a constant $250^\circ\text{C}$ ($523.15\text{ K}$).
* **Active TE Layer Thickness:** $3 \text{ mm}$ base layer extending into $7 \text{ mm}$ longitudinal cooling fins (Total radius $r = 60 \text{ mm}$, Length $Z = 100 \text{ mm}$).
* **Electrical Conductivity ($\sigma$):** $8810 \text{ S/m}$
* **Thermal Conductivity ($k$):** $0.4 \text{ W/(m·K)}$
* **Density ($\rho$):** $1200 \text{ kg/m}^3$ | **Heat Capacity ($C_p$):** $1500 \text{ J/(kg·K)}$
* **Aerodynamic Heat Flux Split (Convective Cooling at $25^\circ\text{C}$):**
  * *Fin Tips & Flanks ($礼_1$):* Assigned $h = 50 \text{ W/(m}^2\text{·K)}$ to simulate direct exposure to high-velocity industrial drafts.
  * *Basal Valleys ($h_2$):* Assigned a reduced $h = 15 \text{ W/(m}^2\text{·K)}$ to model fluid stagnation zones and thermal boundary layer buildup between fins.

### 4. Engineering Assumptions & Abstractions
To optimize computational resources without compromising mathematical rigor, two key engineering abstractions were utilized in this V2 model:
* **Electrical Interconnect Abstraction:** The top electrical bridging between the p and n legs is modeled using a `Floating Potential` boundary condition. This serves as a mathematically perfect, zero-resistance abstraction for the metallic (copper) traces. Physical metallization layers and contact resistance parameters will be explicitly introduced in subsequent iterations.
* **Monolithic vs. Hybrid Manufacturing Note:** While this simulation treats the cooling fins as a monolithic extension of the thermoelectric composite to evaluate pure geometric coupling, the commercialized production model will deploy a **hybrid multi-layer system**. The active, expensive semiconductor composite will remain a thin, flexible flat band wrapped directly around the pipe, while the external fins will be manufactured from a highly conductive, low-cost passive thermal polymer or flexible aluminum mesh. This decouples electrical generation from mechanical stress and significantly reduces raw material costs.

### 5. Results & Validation
* **Thermal Gradient:** The segmented geometry successfully managed to maintain a robust temperature delta despite the low thermal conductivity of the polymer matrix. The fin tips dropped to approximately $350\text{ K}$ ($77^\circ\text{C}$), expanding the active operational $\Delta T$.
* **Voltage Generation:** The coupled multiphysics solver demonstrated a total potential difference of **$\sim 43 \text{ mV}$** ($\pm 21.5 \text{ mV}$ across opposing domains). This represents a **~6-fold increase** in power density compared to the flat monolithic V1 baseline ($7.5 \text{ mV}$), mathematically proving the viability of geometric surface area engineering in passive industrial environments.

***

## Türkçe

### 1. Özet
Bu klasör, Auri-Labs çatısı altında Auri-FlexTEG projesi için COMSOL Multiphysics ortamında geliştirilen Versiyon 2 (V2) 3 Boyutlu Sonlu Elemanlar Analizi (FEA) çoklu-fizik simülasyonlarını içermektedir. V1'de kurulan monolitik taban modelinin ötesine geçen bu çalışma; boylamsal soğutma kanatçıkları (fins) ile birleştirilmiş, segmentli bir yarı iletken mimarisini (n-tipi ve p-tipi çiftler) tanıtmaktadır. Amaç, pasif atmosferik konveksiyon yoluyla radyal sıcaklık gradyanını ($\Delta T$) maksimize etmek ve zorlu endüstriyel sınır koşulları altında Seebeck voltaj ölçekleme ilkelerini doğrulamaktır.

### 2. Yarı İletken Entegrasyonu ve Fizik
İşlevsel bir termoelektrik devre kurmak amacıyla, monolitik yapı iki bağımsız p-n etki alanına bölünmüştür. Bu durum, hesaplamalı malzeme bilimi açısından taşıyıcı iletim süreçleri üzerindeki yapısal hakimiyeti göstermektedir:
* **P-Tipi Bölge (Sol):** Boşluk (hole) baskın taşıyıcı iletimini simüle etmek için pozitif bir Seebeck katsayısı ($S_p = +120 \ \mu\text{V/K}$) ile yapılandırılmıştır.
* **N-Tipi Bölge (Sağ):** Elektron baskın taşıyıcı iletimini simüle etmek için negatif bir Seebeck katsayısı ($S_n = -120 \ \mu\text{V/K}$) ile yapılandırılmıştır.
* **Elektriksel Yalıtım:** P ve N bölgeleri arasındaki dikey ara yüzeye kesin bir `Electric Insulation` (Elektriksel Yalıtım) sınır koşulu uygulanmıştır. Bu kritik adım, iç yük rekombinasyonunu (kısa devre) önleyerek yük taşıyıcılarını terminal bağlantılarına doğru göçe zorlar.

### 3. Gerçekçi Aerodinamik ve Malzeme Parametreleri
Model, $\text{Ag}_2\text{Se}/\text{PEDOT:PSS}$ esnek kompozitlerinin analitik sızma eşiği (percolation) verilerinden türetilen izotropik malzeme özelliklerini ve gerçekçi ısı taşınım katsayılarını içerir:
* **Merkez Isı Kaynağı (Endüstriyel Boru):** $r = 50 \text{ mm}$, iç duvar sıcaklığı sabit $250^\circ\text{C}$ ($523.15\text{ K}$).
* **Aktif TE Katman Kalınlığı:** $3 \text{ mm}$ taban katmanı ve havaya uzanan $7 \text{ mm}$ boylamsal kanatçıklar (Toplam yarıçap $r = 60 \text{ mm}$, Uzunluk $Z = 100 \text{ mm}$).
* **Elektriksel İletkenlik ($\sigma$):** $8810 \text{ S/m}$
* **Termal İletkenlik ($k$):** $0.4 \text{ W/(m·K)}$
* **Yoğunluk ($\rho$):** $1200 \text{ kg/m}^3$ | **Isı Sığası ($C_p$):** $1500 \text{ J/(kg·K)}$
* **Aerodinamik Isı Akısı Dağılımı ($25^\circ\text{C}$ Ortam Sıcaklığında):**
  * *Kanatçık Uçları ve Yan Duvarlar ($h_1$):* Endüstriyel hava akımlarına doğrudan maruz kalmayı simüle etmek için $h = 50 \text{ W/(m}^2\text{·K)}$ atanmıştır.
  * *Taban Boşlukları ($h_2$):* Kanatçıklar arasında oluşan akış durgunluk bölgelerini ve termal sınır tabakası birikimini modellemek için düşürülmüş bir değer olan $h = 15 \text{ W/(m}^2\text{·K)}$ atanmıştır.

### 4. Mühendislik Kabulleri ve Soyutlamalar
Matematiksel titizlikten ödün vermeden hesaplama kaynaklarını optimize etmek için bu V2 modelinde iki temel mühendislik soyutlaması kullanılmıştır:
* **Elektriksel Bağlantı Soyutlaması:** P ve N kolları arasındaki üst elektriksel köprüleme, bir `Floating Potential` (Yüzer Potansiyel) sınır koşulu kullanılarak modellenmiştir. Bu, metalik (bakır) yollar için matematiksel olarak mükemmel, sıfır dirençli bir soyutlama görevi görür. Fiziksel metalizasyon katmanları ve temas direnci parametreleri sonraki versiyonlarda modele eklenecektir.
* **Monolitik - Hibrit Üretim Notu:** Bu simülasyon, saf geometrik eşleşmeyi değerlendirmek için soğutma kanatçıklarını termoelektrik kompozitin monolitik bir uzantısı olarak ele alsa da, ticari üretim modeli **hibrit çok katmanlı bir sistem** olarak hayata geçirilecektir. Aktif ve yüksek maliyetli yarı iletken kompozit, borunun etrafına doğrudan sarılan ince, esnek ve düz bir bant olarak kalacak; dış kanatçıklar ise yüksek iletkenlikli, düşük maliyetli pasif bir termal polimerden veya esnek alüminyum ağdan üretilecektir. Bu yaklaşım, elektriksel üretimi mekanik gerilimlerden ayırır ve hammadde maliyetlerini ciddi oranda düşürür.

### 5. Sonuçlar ve Doğrulama
* **Termal Gradyan:** Segmentli geometri, polimer matrisin düşük termal iletkenliğine rağmen güçlü bir sıcaklık deltasını korumayı başarmıştır. Kanatçık uçları yaklaşık $350\text{ K}$ ($77^\circ\text{C}$) seviyesine düşerek aktif operasyonel $\Delta T$'yi genişletmiştir.
* **Voltaj Üretimi:** Çoklu-fizik çözücü, toplamda **$\sim 43 \text{ mV}$** değerinde bir potansiyel farkı (zıt kutuplarda $\pm 21.5 \text{ mV}$) başarıyla hesaplamıştır. Bu sonuç, düz monolitik V1 taban modeline ($7.5 \text{ mV}$) kıyasla **~6 katlık bir artışı** temsil etmekte ve pasif endüstriyel ortamlarda geometrik yüzey alanı mühendisliğinin uygulanabilirliğini matematiksel olarak kanıtlamaktadır.

***
*(Görseller `images/` klasörünün altındadır / Images are stored under `images/` folder)*
![Mesh Structure](V2/mesh_structure.png)
![Thermal Gradient](V2/thermal_gradient.png)
![Voltage Output](V2/voltage_output.png)
