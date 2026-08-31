def get_promo_cell(promo_code):
    promo_map = {
        'BHXTPDPFF5E': '50% OFF', '2RAK1VRJNVG': '50% OFF', '40MGG1W103D': '50% OFF', 'VE6PR5N8I4P': '50% OFF', 'OCUZRENUN5Z': '50% OFF',
        'F9SXMECOSFO': '50% OFF', 'JRSNVNQ65QD': '50% OFF', 'FYGWWQC38HY': '50% OFF', 'HBRPOIG8F1C': '50% OFF', 'VB9OOAEDOEC': '50% OFF',
        'T7A9TGIQHG9': '100% OFF (Full Waiver)', 'T6MJXK87AU5': '100% OFF (Full Waiver)', 'MTZX272HPOE': '100% OFF (Full Waiver)',
        'GYR3XKXWNRE': '100% OFF (Full Waiver)', 'OI65FDHJK1E': '100% OFF (Full Waiver)', 'YAYQ3S195JM': '100% OFF (Full Waiver)',
        'GDZVGPMM82I': '100% OFF (Full Waiver)', 'YY37Q9AH8RV': '100% OFF (Full Waiver)', 'K8PK3YR9OUD': '100% OFF (Full Waiver)',
        'IT3UEA3GE8N': '100% OFF (Full Waiver)',
        'SND8DUDD467': '50% OFF (Shared Code)', '6QIWEPXSK28': '50% OFF (Shared Code)', 'AFPK054NZDK': '50% OFF (Shared Code)',
        '8II49KQ71N8': '50% OFF (Shared Code)', '3JQIP98Q1ZX': '50% OFF (Shared Code)', 'HS1K3AQ6L6G': '50% OFF (Shared Code)',
        'CF07UQNUPQZ': '50% OFF (Shared Code)', 'KD6FLEEPZHP': '50% OFF (Shared Code)', 'BFNO6B9M80O': '50% OFF (Shared Code)',
        '1LR3PE29GD8': '50% OFF (Shared Code)'
    }
    code = (promo_code or "").strip().upper()
    return f"{code} [{promo_map.get(code, 'Discount Applied')}]" if code else ""

print("Empty:", repr(get_promo_cell("")))
print("Whitespace:", repr(get_promo_cell("   ")))
print("None:", repr(get_promo_cell(None)))
print("50% code:", repr(get_promo_cell("BHXTPDPFF5E")))
print("100% code:", repr(get_promo_cell("t7a9tgiqhg9")))
print("Shared code:", repr(get_promo_cell("SND8DUDD467")))
