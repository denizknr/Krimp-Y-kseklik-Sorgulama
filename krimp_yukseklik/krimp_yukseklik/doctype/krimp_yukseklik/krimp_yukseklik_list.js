// Copyright (c) 2024, denizknr and contributors
// For license information, please see license.txt

frappe.listview_settings["KrimpYukseklik"] = {
    // Listede gösterilecek ek alanlar
    add_fields: ["durum", "oncelik", "referans_tipi", "vade_tarihi", "atanan"],

    // Durum alanına göre renkli gösterge (indicator badge)
    get_indicator: function (doc) {
        const durum_renk = {
            "Açık":      "red",
            "Kapalı":    "green",
            "Beklemede": "orange",
            "İptal":     "darkgrey"
        };
        const renk = durum_renk[doc.durum] || "blue";
        return [__(doc.durum || "—"), renk, "durum,=," + (doc.durum || "")];
    },

    // Sayfa yüklendiğinde varsayılan filtre: Açık kayıtlar
    onload: function (listview) {
        listview.filter_area.add([
            ["KrimpYukseklik", "durum", "=", "Açık", true]
        ]);

        // Öncelik sütununa renkli badge ekle
        listview.columns.forEach(function (col) {
            if (col.df && col.df.fieldname === "oncelik") {
                col.format = function (value) {
                    if (!value) return "";
                    const renk_map = {
                        "Düşük":  "var(--blue-500,   #3b82f6)",
                        "Orta":   "var(--yellow-500, #eab308)",
                        "Yüksek": "var(--orange-500, #f97316)",
                        "Acil":   "var(--red-500,    #ef4444)"
                    };
                    const bg = renk_map[value] || "#888";
                    return `<span style="
                        background:${bg};
                        color:#fff;
                        padding:2px 8px;
                        border-radius:12px;
                        font-size:0.75rem;
                        font-weight:600;
                        letter-spacing:0.03em;
                    ">${__(value)}</span>`;
                };
            }
        });
    },

    // Satır rengini vade durumuna göre değiştir
    get_form_link: function (doc) {
        return frappe.utils.get_form_link("KrimpYukseklik", doc.name);
    },

    // Ek buton: Seçili kayıtları "Kapalı" yap
    button: {
        show: function (doc) {
            return doc.durum === "Açık" || doc.durum === "Beklemede";
        },
        get_label: function () {
            return __("Kapat");
        },
        get_description: function (doc) {
            return __("Seçili kayıtları kapalı durumuna geçir");
        },
        action: function (doc) {
            frappe.call({
                method: "frappe.client.set_value",
                args: {
                    doctype: "KrimpYukseklik",
                    name: doc.name,
                    fieldname: "durum",
                    value: "Kapalı"
                },
                callback: function () {
                    cur_list.refresh();
                }
            });
        }
    }
};
