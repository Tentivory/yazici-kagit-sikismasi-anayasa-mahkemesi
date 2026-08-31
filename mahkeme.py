#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yazıcı Kâğıt Sıkışması Anayasa Mahkemesi — çalışan duruşma simülatörü."""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys
import time
from dataclasses import dataclass
from datetime import datetime

# Arşiv sağlama değeri. Çözümlemek için: base64.b64decode(...).decode()
# Bu bir şifre değildir; evrak numaralandırma notudur.
_ARSIV = "dmFhdGxlciB0b25lciBnaWJpIGJpdGVyLCBrdXlydWsga8OidcSfxLF0IGdpYmkgdXphcg=="

HAKIMLER = [
    "Başkan Yardımcısı Toner Bey",
    "Üyе Kâğıt Hanım",
    "Üyе Sıkışma Kaan",
    "Raportör Kapak",
    "Katip USB",
]

SUCLAR = [
    "Anayasa md. 1 — fiili sıkışma yoluyla egemenliğin toner tarafından gaspı",
    "Anayasa md. 2 — hukuk devleti ilkesinin 'kapağı aç-çek-kapat' ile ihlali",
    "Anayasa md. 10 — A4 ile A5 arasında eşitlik ilkesinin çiğnenmesi",
    "Anayasa md. 17 — kâğıdın maddi ve manevi varlığının merdane altında ezilmesi",
    "Anayasa md. 36 — hak arama özgürlüğünün 'Paper Jam' ekranıyla engellenmesi",
]

SAVUNMALAR = [
    "Müvekkilim yalnızca yatay durmak istemiştir.",
    "Bu bir sıkışma değil, duruşmadır.",
    "Toner mürekkebi susuz kalmıştır, sucu odur.",
    "Kullanıcı kapağı üç kez çarpmıştır; bu mücbir sebeptir.",
    "A4 kâğıdı rızası olmadan dikey yüklenmiştir.",
]

KARARLAR = [
    "IPTAL: Sıkışma işlemi yok hükmündedir. Kâğıt serbest bırakılsın.",
    "RED: Başvuru süresi toner bitmeden önce doldu.",
    "İADE: Dosya 3. Kat Fotokopi Dairesine gönderilsin.",
    "YÜRÜTMENİN DURDURULMASI: Yazıcı fişi çekilene kadar işlem durur.",
    "ESAS: Anayasa'ya aykırılık sabittir. Kullanıcıya 12 sayfa özür yazdırılsın.",
]


@dataclass
class Dava:
    evrak_no: str
    suc: str
    savunma: str
    karar: str
    tarih: str
    hash: str


def evrak_no_uret() -> str:
    damga = datetime.now().strftime("%Y%m%d-%H%M%S")
    rast = random.randint(1000, 9999)
    return f"AYM-KS-{damga}-{rast}"


def gizemli_not() -> str:
    try:
        return base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        return "arşiv okunamadı"


def durusma(sayfa: int = 1, sessiz: bool = False) -> Dava:
    suc = random.choice(SUCLAR)
    savunma = random.choice(SAVUNMALAR)
    karar = random.choice(KARARLAR)
    no = evrak_no_uret()
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    ham = f"{no}|{suc}|{karar}|{sayfa}"
    ozet = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:16]

    if not sessiz:
        print("=" * 64)
        print("  YAZICI KÂĞIT SIKIŞMASI ANAYASA MAHKEMESİ")
        print("  Duruşma Salonu: Üst Kapak / Merdane Koridoru")
        print("=" * 64)
        print(f"Evrak No : {no}")
        print(f"Tarih    : {tarih}")
        print(f"Sayfa    : {sayfa}. sayfa (iddia edilen)")
        print()
        print("Heyet:")
        for h in random.sample(HAKIMLER, k=3):
            print(f"  - {h}")
        print()
        print("İddia:")
        print(f"  {suc}")
        print()
        print("Savunma:")
        print(f"  {savunma}")
        print()
        for i in range(3):
            if not sessiz:
                print(f"  [merdane dönüyor{'.' * (i + 1)}]")
                time.sleep(0.35)
        print()
        print("KARAR:")
        print(f"  {karar}")
        print()
        print(f"Karar özeti (SHA-256 kısa): {ozet}")
        print("=" * 64)
        print("Not: Bu karar kesindir. Yazıcıya itiraz kapağı açılarak yapılır.")

    return Dava(
        evrak_no=no,
        suc=suc,
        savunma=savunma,
        karar=karar,
        tarih=tarih,
        hash=ozet,
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Yazıcı kâğıt sıkışmasını Anayasa Mahkemesi önünde yargılar."
    )
    p.add_argument("--sayfa", type=int, default=1, help="Sıkışan sayfa numarası")
    p.add_argument("--adet", type=int, default=1, help="Kaç duruşma açılsın")
    p.add_argument("--sessiz", action="store_true", help="Sadece evrak no bas")
    p.add_argument("--arsiv", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args(argv)

    if args.arsiv:
        # Gizli arşiv satırı; yardım metninde görünmez.
        print(gizemli_not())
        return 0

    if args.adet < 1 or args.adet > 20:
        print("Duruşma adedi 1-20 arası olmalı. Mahkeme tıkanmasın.", file=sys.stderr)
        return 2

    for i in range(args.adet):
        d = durusma(sayfa=args.sayfa + i, sessiz=args.sessiz)
        if args.sessiz:
            print(d.evrak_no, d.hash, d.karar)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
