# Auri Labs: Percolation Theory & Composite Mixing Models

## English

### Overview
This directory contains the foundational Python models used by Auri Labs to mathematically predict and formulate the volumetric and mass fractions of flexible thermoelectric composites. Before physical prototyping, these scripts ensure that we achieve maximum electrical conductivity through optimal nanowire percolation, without compromising the mechanical flexibility of the polymer matrix.

### Files Included
1. **`Percolation_Threshold.py` (Power-Law Conductivity Model):** Calculates the theoretical electrical conductivity of the composite based on the percolation threshold ($\phi_c$). It visualizes the non-linear phase transition where the insulating polymer matrix becomes highly conductive upon the formation of a continuous nanowire network.
2. **`volume-to-mass_lab_recipe.py` (Mass-to-Volume Precision Converter):** A crucial lab assistant script for empirical synthesis. Because mechanical flexibility is governed by Volume Fraction ($\phi$), but laboratory scales measure Mass Fraction ($w$), this script accounts for the extreme density differences between heavy metallic nanowires (e.g., $Bi_2Te_3$ at $\sim 7.7 \text{ g/cm}^3$) and the lightweight PEDOT:PSS matrix ($\sim 1.0 \text{ g/cm}^3$). It outputs precise mass values (in grams) for empirical batch mixing.

### Significance for V3/V4 Physical Prototypes
These baseline models dictate our manufacturing recipes. By targeting a "safe zone" slightly above the percolation threshold (e.g., 6% volume), we ensure the composite retains >90% of its native polymer flexibility while exhibiting metallic-like charge transport. Future iterations will integrate machine learning algorithms to map viscosity changes during the roll-to-roll printing process.

--------------------------------------------------------------------------------------------------------------

## Türkçe

### Genel Bakış
Bu klasör, Auri Labs tarafından esnek termoelektrik kompozitlerin hacimsel ve kütlesel karışım oranlarını matematiksel olarak tahmin etmek ve formüle etmek için kullanılan temel Python modellerini içerir. Fiziksel prototiplemeden önce bu komut dosyaları, polimer matrisinin mekanik esnekliğinden ödün vermeden optimum nanotel sızması (percolation) yoluyla maksimum elektriksel iletkenliğe ulaşmamızı garanti altına alır.

### İçerilen Dosyalar
1. **`Percolation_Threshold.py` (Power-Law İletkenlik Modeli):** Kompozitin teorik elektriksel iletkenliğini sızma eşiğine ($\phi_c$) dayalı olarak hesaplar. Yalıtkan polimer matrisin, sürekli bir nanotel ağının oluşumuyla yüksek oranda iletken hale geldiği doğrusal olmayan faz geçişini görselleştirir.
2. **`volume-to-mass_lab_recipe.py` (Kütle-Hacim Hassasiyet Dönüştürücüsü):** Deneysel sentez için kritik bir laboratuvar asistanı kodudur. Mekanik esneklik Hacim Oranı ($\phi$) tarafından belirlenirken laboratuvar terazileri Kütle Oranı ($w$) ölçtüğünden; bu komut dosyası, ağır metalik nanoteller (örn. $Bi_2Te_3$ $\sim 7.7 \text{ g/cm}^3$) ile hafif PEDOT:PSS matrisi ($\sim 1.0 \text{ g/cm}^3$) arasındaki aşırı yoğunluk farklarını hesaba katar. Laboratuvardaki fiziksel üretimler için terazide tartılacak kesin gramaj değerlerini verir.

### V3/V4 Fiziksel Prototipleri İçin Önemi
Bu temel modeller, üretim reçetelerimizi belirler. Sızma eşiğinin biraz üzerindeki (örneğin hacimce %6) bir "güvenli bölgeyi" hedefleyerek, kompozitin %90'dan fazla saf polimer esnekliğini korumasını ve aynı zamanda metalik şarj iletimi sergilemesini sağlıyoruz. Gelecekteki versiyonlar, rulo basım (roll-to-roll) süreci sırasındaki viskozite değişimlerini haritalamak için makine öğrenimi algoritmalarını da içerecektir.
