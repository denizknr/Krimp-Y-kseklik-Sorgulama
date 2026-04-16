# Copyright (c) 2024, denizknr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class KrimpYukseklik(Document):
    def validate(self):
        """Kayıt doğrulama: vade tarihi geçmişte ise uyarı ver."""
        if self.vade_tarihi:
            from frappe.utils import nowdate, getdate
            if getdate(self.vade_tarihi) < getdate(nowdate()):
                if self.durum not in ("Kapalı", "İptal"):
                    frappe.msgprint(
                        frappe._("Vade tarihi geçmiş. Lütfen durumu güncelleyin."),
                        indicator="orange",
                        alert=True,
                    )

    def before_save(self):
        """Kaydeden kullanıcıyı 'Atamayı Yapan' alanına otomatik doldur."""
        if not self.atanayi_yapan:
            self.atanayi_yapan = frappe.session.user
