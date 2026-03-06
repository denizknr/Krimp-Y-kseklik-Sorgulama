<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Krimp Yüksekliği Sorgulama</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

  :root {
    --bg: #1a1a1a;
    --surface: #242424;
    --surface2: #2e2e2e;
    --surface3: #363636;
    --border: #3a3a3a;
    --accent-orange: #f0a500;
    --accent-blue: #4a9eff;
    --accent-green: #22c55e;
    --accent-red: #ef4444;
    --text: #e2e2e2;
    --text-dim: #888;
    --text-bright: #fff;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1.5rem;
  }

  .card {
    width: 100%;
    max-width: 580px;
    background: var(--surface);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 24px 60px rgba(0,0,0,0.5);
  }

  /* ── HEADER ── */
  .card-header {
    background: var(--surface2);
    padding: 1.25rem 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--border);
  }
  .card-header-left {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }
  .header-icon {
    width: 36px;
    height: 36px;
    background: rgba(240,165,0,0.15);
    border: 1px solid rgba(240,165,0,0.3);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
  }
  .header-title {
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text-bright);
  }
  .header-sub {
    font-size: 0.7rem;
    color: var(--text-dim);
    margin-top: 1px;
  }
  .doc-badge {
    font-size: 0.65rem;
    color: var(--text-dim);
    background: var(--surface3);
    border: 1px solid var(--border);
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 500;
    letter-spacing: 0.04em;
  }

  /* ── BODY ── */
  .card-body {
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  /* ── INPUT ROWS ── */
  .input-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.875rem;
  }

  .field {
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
  }
  .field label {
    font-size: 0.68rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-dim);
  }

  .select-wrap {
    position: relative;
  }
  .select-wrap::after {
    content: '▾';
    position: absolute;
    right: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-dim);
    pointer-events: none;
    font-size: 0.8rem;
  }

  select, input[type="text"] {
    width: 100%;
    background: var(--surface3);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    color: var(--text-bright);
    padding: 10px 36px 10px 12px;
    font-family: 'Inter', sans-serif;
    font-size: 0.875rem;
    font-weight: 500;
    outline: none;
    appearance: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    cursor: pointer;
  }
  select:focus, input[type="text"]:focus {
    border-color: var(--accent-orange);
    box-shadow: 0 0 0 3px rgba(240,165,0,0.12);
  }
  select:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }
  select option { background: #2e2e2e; }

  /* Kontak search input */
  .kontak-input-wrap {
    position: relative;
  }
  .kontak-input-wrap input {
    padding: 10px 12px;
    padding-right: 36px;
  }
  .kontak-input-wrap .clear-btn {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: var(--text-dim);
    cursor: pointer;
    font-size: 1rem;
    line-height: 1;
    padding: 2px 4px;
    display: none;
  }
  .kontak-input-wrap .clear-btn:hover { color: var(--text); }

  /* Dropdown listesi */
  .dropdown-list {
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    right: 0;
    background: var(--surface2);
    border: 1.5px solid var(--border);
    border-radius: 8px;
    max-height: 220px;
    overflow-y: auto;
    z-index: 100;
    display: none;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  }
  .dropdown-list.open { display: block; }
  .dropdown-item {
    padding: 9px 12px;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: background 0.1s;
  }
  .dropdown-item:hover, .dropdown-item.active {
    background: var(--surface3);
    color: var(--text-bright);
  }
  .dropdown-item .count-badge {
    margin-left: auto;
    font-size: 0.65rem;
    background: rgba(240,165,0,0.15);
    color: var(--accent-orange);
    padding: 2px 6px;
    border-radius: 10px;
    font-weight: 600;
  }
  .dropdown-no-result {
    padding: 12px;
    text-align: center;
    font-size: 0.8rem;
    color: var(--text-dim);
  }
  .dropdown-list::-webkit-scrollbar { width: 6px; }
  .dropdown-list::-webkit-scrollbar-track { background: transparent; }
  .dropdown-list::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

  /* ── DIVIDER ── */
  .divider {
    height: 1px;
    background: var(--border);
    margin: 0 -1.5rem;
  }

  /* ── RESULT PANEL ── */
  #resultPanel {
    display: none;
  }

  .result-label {
    font-size: 0.68rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-dim);
    margin-bottom: 0.75rem;
  }

  /* Single result */
  .result-single {
    background: var(--surface2);
    border: 1.5px solid rgba(240,165,0,0.25);
    border-radius: 12px;
    overflow: hidden;
  }
  .result-main {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0;
  }
  .result-cell {
    padding: 0.9rem 1.1rem;
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
  }
  .result-cell:nth-child(3n) { border-right: none; }
  .result-cell:nth-child(5),
  .result-cell:nth-child(6),
  .result-cell:nth-child(7) { border-bottom: none; }
  .result-cell-label {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-dim);
    font-weight: 600;
    margin-bottom: 4px;
  }
  .result-cell-value {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-bright);
    letter-spacing: 0.02em;
  }
  .result-cell-value.krimp {
    color: var(--accent-orange);
    font-size: 1.4rem;
  }
  .result-cell-value.kalip {
    color: var(--accent-blue);
  }
  .result-cell-value.izokrimp {
    color: #bc8cff;
  }
  .result-cell-value.cekme {
    color: var(--accent-green);
  }
  .tolerance-hint {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.6rem 1.25rem;
    background: rgba(240,165,0,0.06);
    font-size: 0.72rem;
    color: rgba(240,165,0,0.8);
    border-top: 1px solid rgba(240,165,0,0.15);
  }

  /* Note */
  .result-note {
    margin-top: 0.5rem;
    padding: 0.75rem 1rem;
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.2);
    border-radius: 8px;
    font-size: 0.8rem;
    color: #fca5a5;
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
  }

  /* Multiple results table */
  .result-multi {
    background: var(--surface2);
    border: 1.5px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }
  .result-multi-header {
    display: grid;
    grid-template-columns: 1fr 1.2fr 1fr 1fr 1fr;
    padding: 0.6rem 1rem;
    background: var(--surface3);
    border-bottom: 1px solid var(--border);
  }
  .result-multi-header span {
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-dim);
    font-weight: 600;
  }
  .result-multi-row {
    display: grid;
    grid-template-columns: 1fr 1.2fr 1fr 1fr 1fr;
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border);
    align-items: center;
    transition: background 0.15s;
  }
  .result-multi-row:last-child { border-bottom: none; }
  .result-multi-row:hover { background: var(--surface3); }
  .result-multi-row span { font-size: 0.85rem; }
  .val-kesit { color: var(--text-dim); font-size: 0.8rem !important; }
  .val-kalip { color: var(--accent-blue); font-weight: 600; }
  .val-krimp { color: var(--accent-orange); font-weight: 700; }
  .val-izok  { color: #bc8cff; }
  .val-cekme { color: var(--accent-green); }
  .val-empty { color: var(--border); }

  /* ── EMPTY / HINT STATE ── */
  .hint-state {
    text-align: center;
    padding: 2rem 1rem;
    color: var(--text-dim);
  }
  .hint-state .hint-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
    opacity: 0.4;
  }
  .hint-state p {
    font-size: 0.8rem;
    line-height: 1.5;
  }
  .hint-state p span {
    color: var(--accent-orange);
    font-weight: 600;
  }

  .no-result-state {
    text-align: center;
    padding: 2rem 1rem;
    color: var(--text-dim);
  }
  .no-result-state .no-icon { font-size: 2rem; margin-bottom: 0.5rem; opacity: 0.3; }
  .no-result-state p { font-size: 0.82rem; }

  /* ── RESET ── */
  .reset-btn {
    width: 100%;
    padding: 10px;
    background: transparent;
    border: 1.5px solid var(--border);
    border-radius: 8px;
    color: var(--text-dim);
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
  }
  .reset-btn:hover { border-color: var(--accent-orange); color: var(--accent-orange); }

  /* ── FOOTER ── */
  .card-footer {
    padding: 0.75rem 1.5rem;
    background: var(--surface2);
    border-top: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .footer-left { font-size: 0.7rem; color: var(--text-dim); }
  .footer-left strong { color: var(--text); }
  .footer-badge {
    font-size: 0.65rem;
    color: var(--text-dim);
    background: var(--surface3);
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid var(--border);
  }
</style>
</head>
<body>

<div class="card">
  <!-- HEADER -->
  <div class="card-header">
    <div class="card-header-left">
      <div class="header-icon">⚙️</div>
      <div>
        <div class="header-title">Krimp Yüksekliği Sorgulama</div>
        <div class="header-sub">Kontak ve kesit seçerek değerleri görüntüleyin</div>
      </div>
    </div>
    <div class="doc-badge">PTR-KT-006-28</div>
  </div>

  <!-- BODY -->
  <div class="card-body">

    <!-- INPUTS -->
    <div class="input-row">
      <!-- Kontak arama -->
      <div class="field">
        <label>Kontak No</label>
        <div class="kontak-input-wrap" style="position:relative">
          <input type="text" id="kontakInput" placeholder="Kontak ara..." autocomplete="off" oninput="onKontakInput()" onfocus="onKontakFocus()" />
          <button class="clear-btn" id="clearKontak" onclick="clearKontak()">✕</button>
          <div class="dropdown-list" id="kontakDropdown"></div>
        </div>
      </div>

      <!-- Kesit seç -->
      <div class="field">
        <label>Kesit</label>
        <div class="select-wrap">
          <select id="kesitSelect" disabled onchange="onKesitChange()">
            <option value="">Kesit seçin...</option>
          </select>
        </div>
      </div>
    </div>

    <div class="divider"></div>

    <!-- RESULT -->
    <div id="hintState" class="hint-state">
      <div class="hint-icon">🔍</div>
      <p>Önce <span>Kontak No</span> girin,<br>ardından uygun <span>kesiti</span> seçin.</p>
    </div>

    <div id="resultPanel">
      <div class="result-label" id="resultLabel">Sonuç</div>
      <div id="resultContent"></div>
    </div>

    <button class="reset-btn" onclick="resetAll()">↺ Temizle</button>
  </div>

  <!-- FOOTER -->
  <div class="card-footer">
    <div class="footer-left">
      Tolerans: <strong>± 0,05 mm</strong> &nbsp;·&nbsp; Toplam <strong id="totalFooter">—</strong> kayıt
    </div>
    <div class="footer-badge">KTA Endüstri</div>
  </div>
</div>

<script>
const DATA = [
  // 0,14 mm²
  {kesit:"0,14 mm²", kontak:"10024441", kalip:"89", krimp:"0,75", cekme:"18", krimp_gen:"", izok:"", not:""},
  {kesit:"0,14 mm²", kontak:"10025356", kalip:"106", krimp:"1,20", cekme:"18", krimp_gen:"2,10", izok:"", not:""},
  // 0,25 mm²
  {kesit:"0,25 mm²", kontak:"10025030", kalip:"113-141", krimp:"0,80", cekme:"32", krimp_gen:"", izok:"1,50", not:""},
  // 0,34 mm²
  {kesit:"0,34 mm²", kontak:"10000512", kalip:"Ş Onay 114", krimp:"1,25", cekme:"43", krimp_gen:"", izok:"", not:""},
  {kesit:"0,34 mm²", kontak:"10011685", kalip:"86", krimp:"1,10", cekme:"43", krimp_gen:"1,60", izok:"", not:""},
  {kesit:"0,34 mm²", kontak:"10023342", kalip:"Ş Onay 131", krimp:"0,90", cekme:"43", krimp_gen:"", izok:"", not:""},
  {kesit:"0,34 mm²", kontak:"10023577", kalip:"110", krimp:"0,83", cekme:"43", krimp_gen:"", izok:"", not:""},
  {kesit:"0,34 mm²", kontak:"10024309", kalip:"Ş Onay 131", krimp:"0,85", cekme:"43", krimp_gen:"", izok:"", not:""},
  {kesit:"0,34 mm²", kontak:"10025503", kalip:"278", krimp:"0,70", cekme:"43", krimp_gen:"", izok:"", not:""},
  {kesit:"0,34 mm²", kontak:"10034454", kalip:"176", krimp:"0,90", cekme:"43", krimp_gen:"", izok:"", not:""},
  // 0,35 mm²
  {kesit:"0,35 mm²", kontak:"10003731", kalip:"Ş Onay 82", krimp:"1,00", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10008845", kalip:"176-276-277-316-317", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10017874", kalip:"266", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10017953", kalip:"202-264", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10017954", kalip:"265", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10019009", kalip:"176-276-277-316-317", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10020599", kalip:"101", krimp:"0,80", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10023046", kalip:"14-50", krimp:"1,20", cekme:"45", krimp_gen:"", izok:"2,50", not:""},
  {kesit:"0,35 mm²", kontak:"10023159", kalip:"169", krimp:"1,25", cekme:"45", krimp_gen:"", izok:"2,50", not:""},
  {kesit:"0,35 mm²", kontak:"10023342", kalip:"131 Teflon", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10023574", kalip:"103", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10023577", kalip:"110-279", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10023590", kalip:"237", krimp:"0,95", cekme:"45", krimp_gen:"1,75", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024274", kalip:"42-43-192", krimp:"1,50", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024276", kalip:"115", krimp:"1,10", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024277", kalip:"216", krimp:"1,35", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024278", kalip:"115-191", krimp:"1,10", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024278", kalip:"261", krimp:"1,15", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024280", kalip:"10-190", krimp:"1,20", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024281", kalip:"91-187-271", krimp:"0,95", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024282", kalip:"87", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024283", kalip:"129- Ş.Onay", krimp:"1,40", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024284", kalip:"98-180", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024285", kalip:"49", krimp:"1,20", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024286", kalip:"31", krimp:"1,50", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024287", kalip:"241", krimp:"1,65", cekme:"45", krimp_gen:"3,30", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024288", kalip:"91-187-271", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024289", kalip:"101", krimp:"0,80", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024302", kalip:"Ş.Onay 185-304", krimp:"1,45", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024304", kalip:"244-342", krimp:"1,10", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024305", kalip:"113-141", krimp:"0,80", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024307", kalip:"49", krimp:"1,50", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024315", kalip:"214", krimp:"1,05", cekme:"45", krimp_gen:"", izok:"1,70", not:""},
  {kesit:"0,35 mm²", kontak:"10024316", kalip:"300", krimp:"1,00", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024316", kalip:"24", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"1,60", not:""},
  {kesit:"0,35 mm²", kontak:"10024318", kalip:"253-254", krimp:"1,30", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024319", kalip:"208", krimp:"1.20", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024320", kalip:"46 Ş.Onay", krimp:"1,25", cekme:"45", krimp_gen:"2,55", izok:"2,30", not:""},
  {kesit:"0,35 mm²", kontak:"10024320", kalip:"275 Ş.Onay", krimp:"1,30", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024320", kalip:"212", krimp:"1,40", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024321", kalip:"68", krimp:"1,10", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024326", kalip:"Ş.Onay 162-320", krimp:"1,50", cekme:"45", krimp_gen:"", izok:"2,78", not:""},
  {kesit:"0,35 mm²", kontak:"10024345", kalip:"170-328", krimp:"1,30", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024349", kalip:"96", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024350", kalip:"188", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024351", kalip:"1", krimp:"1,55", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024352", kalip:"170-328", krimp:"1,30", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024353", kalip:"96", krimp:"0,85", cekme:"45", krimp_gen:"1,70", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024355", kalip:"88-218", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024355", kalip:"330", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024356", kalip:"208", krimp:"1,10", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024358", kalip:"321", krimp:"1,30", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024359", kalip:"170-328", krimp:"1,55", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024360", kalip:"14-50", krimp:"1,20", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024362", kalip:"14-50-133", krimp:"1,30", cekme:"45", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024362", kalip:"327", krimp:"1,40", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024365", kalip:"50-245", krimp:"1,20", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024367", kalip:"245", krimp:"1,25", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024370", kalip:"10", krimp:"1,40", cekme:"45", krimp_gen:"", izok:"2,77", not:""},
  {kesit:"0,35 mm²", kontak:"10024361", kalip:"153", krimp:"1,00", cekme:"", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025206", kalip:"327", krimp:"1,25", cekme:"", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024373", kalip:"191", krimp:"1,05", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024376", kalip:"96", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024388", kalip:"22", krimp:"0,75", cekme:"45", krimp_gen:"", izok:"1,50", not:""},
  {kesit:"0,35 mm²", kontak:"10024450", kalip:"31", krimp:"1,45", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10024458", kalip:"33", krimp:"0,95", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025030", kalip:"113-141", krimp:"0,80", cekme:"45", krimp_gen:"", izok:"1,50", not:""},
  {kesit:"0,35 mm²", kontak:"10025036", kalip:"30-51-175", krimp:"1,60", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025155", kalip:"29-338", krimp:"1,60", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025156", kalip:"115-191", krimp:"0,95", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025157", kalip:"304", krimp:"1,45", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025157", kalip:"185", krimp:"1,45", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025159", kalip:"338", krimp:"1,65", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025206", kalip:"14-50", krimp:"1,35", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025254", kalip:"10", krimp:"1,35", cekme:"45", krimp_gen:"", izok:"2,60", not:""},
  {kesit:"0,35 mm²", kontak:"10025350", kalip:"191", krimp:"1,05", cekme:"45", krimp_gen:"2,00", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025355", kalip:"147", krimp:"0,95", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025503", kalip:"278", krimp:"0,85", cekme:"45", krimp_gen:"2,10", izok:"1,75", not:""},
  {kesit:"0,35 mm²", kontak:"10025524", kalip:"271", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10025524", kalip:"187", krimp:"0,95", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10026758", kalip:"257", krimp:"1,45", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10026828", kalip:"273", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10030031", kalip:"266-180", krimp:"0,80", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10030845", kalip:"291", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10031388", kalip:"287", krimp:"1,15", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10031553", kalip:"294", krimp:"0,90", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10031554", kalip:"289", krimp:"0,85", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10031642", kalip:"285", krimp:"1,20", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10033277", kalip:"115", krimp:"1,10", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"0,35 mm²", kontak:"10035865", kalip:"132", krimp:"1,05", cekme:"", krimp_gen:"", izok:"", not:""},
  // 0,38 mm²
  {kesit:"0,38 mm²", kontak:"10020436", kalip:"178-181-238-255", krimp:"0,80", cekme:"40", krimp_gen:"E 28010 DİRENÇ BASILACAK", izok:"", not:""},
  {kesit:"0,38 mm²", kontak:"10023360", kalip:"102", krimp:"0,80", cekme:"40", krimp_gen:"10023522 DİRENÇ BASILACAK", izok:"", not:""},
  {kesit:"0,38 mm²", kontak:"10023046", kalip:"50", krimp:"1,20", cekme:"50", krimp_gen:"", izok:"", not:""},
  {kesit:"0,38 mm²", kontak:"10024305", kalip:"113-141", krimp:"1,00", cekme:"50", krimp_gen:"", izok:"1,67", not:""},
  // 0,50 mm²
  {kesit:"0,50 mm²", kontak:"10000512", kalip:"114-230", krimp:"1,25", cekme:"60", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10000512", kalip:"114", krimp:"1,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10001498", kalip:"108-205", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10001582", kalip:"2", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10003566", kalip:"117", krimp:"1,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10003566", kalip:"224", krimp:"1,05", cekme:"60", krimp_gen:"2,00", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10003730", kalip:"179", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"2,50", not:""},
  {kesit:"0,50 mm²", kontak:"10003812", kalip:"117", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10006876", kalip:"226", krimp:"1,05", cekme:"60", krimp_gen:"2,03", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10006876", kalip:"117", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10006877", kalip:"226", krimp:"1,05", cekme:"60", krimp_gen:"2,03", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10006877", kalip:"117", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10008845", kalip:"119-176-276-277-316-317", krimp:"0,85", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10018584", kalip:"Ş Onay 115", krimp:"1,05", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10018960", kalip:"142", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10019009", kalip:"176-276-277-316-317", krimp:"1,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10019009", kalip:"+Direnç 176", krimp:"1,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10020436", kalip:"178-181-238-255", krimp:"0,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023342", kalip:"131-213", krimp:"0,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023344", kalip:"129", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023345", kalip:"184-185", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023348", kalip:"203", krimp:"1,10", cekme:"60", krimp_gen:"Max 2,10", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023348", kalip:"191", krimp:"1,30", cekme:"60", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023362", kalip:"205", krimp:"1,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023571", kalip:"210", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023572", kalip:"102", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023574", kalip:"103", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023584", kalip:"102", krimp:"0,85", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023584", kalip:"101", krimp:"1,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023586", kalip:"153", krimp:"1,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023590", kalip:"142", krimp:"0,95", cekme:"60", krimp_gen:"1,85", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023784", kalip:"117", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023788", kalip:"117", krimp:"1,25", cekme:"60", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023789", kalip:"224", krimp:"1,35", cekme:"60", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023791", kalip:"117", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023792", kalip:"230", krimp:"1,25", cekme:"60", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023806", kalip:"198", krimp:"1,25", cekme:"60", krimp_gen:"1,60", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10023808", kalip:"86", krimp:"1,00", cekme:"60", krimp_gen:"1,60", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024272", kalip:"338", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024272", kalip:"29", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024273", kalip:"10", krimp:"1,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024274", kalip:"42-43-192", krimp:"1,55", cekme:"60", krimp_gen:"2,65", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024276", kalip:"115", krimp:"1,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024278", kalip:"115--191", krimp:"1,20", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024280", kalip:"10", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024283", kalip:"129", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024285", kalip:"49", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024287", kalip:"241", krimp:"1,75", cekme:"60", krimp_gen:"3,30", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024295", kalip:"118-204", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024302", kalip:"185-304", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024306", kalip:"42-43", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024307", kalip:"49", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"3,23", not:""},
  {kesit:"0,50 mm²", kontak:"10024309", kalip:"131-213", krimp:"0,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024313", kalip:"207", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024313", kalip:"+Direnç 207", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024320", kalip:"Ş Onay 46-275", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024324", kalip:"10", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024325", kalip:"6", krimp:"1,20", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024326", kalip:"252-320", krimp:"1,50", cekme:"60", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024326", kalip:"162-196", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"3,15", not:""},
  {kesit:"0,50 mm²", kontak:"10024327", kalip:"63-155-215-250", krimp:"-", cekme:"60", krimp_gen:"", izok:"1,10", not:""},
  {kesit:"0,50 mm²", kontak:"10024335", kalip:"109", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024338", kalip:"16", krimp:"1,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024339", kalip:"118", krimp:"1,35", cekme:"60", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024345", kalip:"170-328", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024352", kalip:"170-328", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024358", kalip:"321", krimp:"1,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024359", kalip:"170-328", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"3,60", not:""},
  {kesit:"0,50 mm²", kontak:"10024360", kalip:"14-50", krimp:"1,25", cekme:"60", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024362", kalip:"14-50", krimp:"1,40", cekme:"60", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024370", kalip:"10", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024371", kalip:"53", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024372", kalip:"206", krimp:"1,05", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024378", kalip:"3-79", krimp:"1,50", cekme:"60", krimp_gen:"2,65", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024388", kalip:"22", krimp:"0,80", cekme:"60", krimp_gen:"1,90", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024390", kalip:"5", krimp:"1,20", cekme:"60", krimp_gen:"2,00", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024391", kalip:"114-205", krimp:"1,10", cekme:"60", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024392", kalip:"48-279", krimp:"1,10", cekme:"60", krimp_gen:"2,00", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024398", kalip:"78", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024420", kalip:"198", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024421", kalip:"155-215-250", krimp:"-", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024424", kalip:"Teflon 42-43", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024436", kalip:"318", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024439", kalip:"118", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024440", kalip:"230", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024441", kalip:"89", krimp:"0,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024445", kalip:"108-205", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024453", kalip:"201", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024454", kalip:"114", krimp:"1,05", cekme:"60", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10024454", kalip:"115", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025033", kalip:"174", krimp:"1,05", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025034", kalip:"15-21-128-232", krimp:"-", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025036", kalip:"Ş Onay 30-51-175", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025154", kalip:"203-261", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025181", kalip:"4", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025206", kalip:"14-50", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025216", kalip:"319", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025217", kalip:"256", krimp:"1,60", cekme:"60", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025247", kalip:"10", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025250", kalip:"52", krimp:"1,50", cekme:"60", krimp_gen:"2,30", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025308", kalip:"50", krimp:"1,30", cekme:"60", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025350", kalip:"115", krimp:"1,05", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025363", kalip:"195", krimp:"1,80", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025476", kalip:"99", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025476", kalip:"Ş.Onay 206-207", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025510", kalip:"260", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025724", kalip:"42-43", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025771", kalip:"136", krimp:"0,85", cekme:"60", krimp_gen:"1,50", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10025844", kalip:"28", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10026440", kalip:"50", krimp:"1,40", cekme:"60", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10027077", kalip:"251", krimp:"1,50", cekme:"60", krimp_gen:"2,70", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10027442", kalip:"117", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10031642", kalip:"285", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10034068", kalip:"326", krimp:"1,65", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,50 mm²", kontak:"10034070", kalip:"324", krimp:"1,85", cekme:"60", krimp_gen:"", izok:"", not:""},
  // 0,56 mm²
  {kesit:"0,56 mm²", kontak:"10001498", kalip:"108", krimp:"1,40", cekme:"60", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10003566", kalip:"224", krimp:"1,10", cekme:"72", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10025216", kalip:"319", krimp:"1,25", cekme:"72", krimp_gen:"", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10025355", kalip:"147", krimp:"0,95", cekme:"72", krimp_gen:"3,00", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10025355", kalip:"335", krimp:"1,10", cekme:"72", krimp_gen:"3,00", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10025400", kalip:"147-191-297", krimp:"1,20", cekme:"72", krimp_gen:"", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10027442", kalip:"117", krimp:"1,35", cekme:"72", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10031642", kalip:"285", krimp:"1,25", cekme:"72", krimp_gen:"", izok:"", not:""},
  {kesit:"0,56 mm²", kontak:"10000512", kalip:"114-230", krimp:"1,35", cekme:"72", krimp_gen:"", izok:"", not:""},
  // 0,75 mm²
  {kesit:"0,75 mm²", kontak:"10000512", kalip:"114-230", krimp:"1,35", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10001498", kalip:"108-205", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10003965", kalip:"204", krimp:"1,40", cekme:"85", krimp_gen:"2,35", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10008845", kalip:"176-276-277-316-317", krimp:"1,05", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10018584", kalip:"115", krimp:"1,10", cekme:"85", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10019009", kalip:"176-276-277-316-317", krimp:"1,05", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10022065", kalip:"28-134", krimp:"1,70", cekme:"85", krimp_gen:"2,65", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023046", kalip:"50", krimp:"1,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023314", kalip:"138", krimp:"1,25", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023322", kalip:"134", krimp:"2,20", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,40", cekme:"85", krimp_gen:"2,20", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023344", kalip:"129", krimp:"1,60", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023345", kalip:"184", krimp:"1,45", cekme:"85", krimp_gen:"2,35", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023348", kalip:"203", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023359", kalip:"-", krimp:"85", cekme:"0,75", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023570", kalip:"214", krimp:"1,20", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023571", kalip:"210", krimp:"1,05", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023572", kalip:"Ş.Onay 102", krimp:"1,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023573", kalip:"290", krimp:"0,95", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023573", kalip:"142-176", krimp:"1,00", cekme:"85", krimp_gen:"1,75", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023580", kalip:"179", krimp:"1,00", cekme:"85", krimp_gen:"1,65", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023584", kalip:"Ş.Onay 102", krimp:"0,85", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023586", kalip:"153-176", krimp:"1,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023590", kalip:"237", krimp:"0,95", cekme:"85", krimp_gen:"1,75", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023590", kalip:"176", krimp:"1,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023591", kalip:"142-153", krimp:"1,05", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10023592", kalip:"Ş.Onay 142", krimp:"0,90", cekme:"85", krimp_gen:"1,75", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024274", kalip:"42-43-192", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"2,60", not:""},
  {kesit:"0,75 mm²", kontak:"10024278", kalip:"115-191", krimp:"1,25", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024287", kalip:"241", krimp:"1,80", cekme:"85", krimp_gen:"3,30", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024293", kalip:"42-43-192", krimp:"1,70", cekme:"85", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024294", kalip:"167-168-173", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024295", kalip:"204", krimp:"1,50", cekme:"85", krimp_gen:"2,35", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024297", kalip:"31", krimp:"1,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024302", kalip:"304", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024302", kalip:"185", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024306", kalip:"42-43", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024307", kalip:"49", krimp:"1,55", cekme:"85", krimp_gen:"", izok:"3,35", not:""},
  {kesit:"0,75 mm²", kontak:"10024313", kalip:"M5-M6-207", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024318", kalip:"253-254", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024319", kalip:"46", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024320", kalip:"46-275", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024326", kalip:"162-196-320", krimp:"1,60", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024327", kalip:"63-155-215-250", krimp:"-", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024334", kalip:"301", krimp:"1,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024334", kalip:"253", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024339", kalip:"118", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024343", kalip:"53", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024344", kalip:"52", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024347", kalip:"114", krimp:"1,60", cekme:"85", krimp_gen:"2,15", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024348", kalip:"52", krimp:"1,40", cekme:"85", krimp_gen:"2,20", izok:"2,60", not:""},
  {kesit:"0,75 mm²", kontak:"10024356", kalip:"208", krimp:"1,10", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024358", kalip:"321", krimp:"1,55", cekme:"85", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024360", kalip:"14-50", krimp:"1,25", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024362", kalip:"245", krimp:"1,35", cekme:"85", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024362", kalip:"14-50-133", krimp:"1,40", cekme:"85", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024362  Silikon Kablo", kalip:"327", krimp:"1,55", cekme:"85", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024365", kalip:"14-50", krimp:"1,35", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024366", kalip:"151", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024367", kalip:"245", krimp:"1,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024367", kalip:"14-50", krimp:"1,35", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024375", kalip:"28", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024378", kalip:"3-79", krimp:"1,60", cekme:"85", krimp_gen:"2,95", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024378", kalip:"177", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024381", kalip:"248-199", krimp:"2,10", cekme:"85", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024384", kalip:"60", krimp:"1,85", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024398", kalip:"78", krimp:"1,35", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024401", kalip:"99-207", krimp:"1,60", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024404", kalip:"85", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024406", kalip:"49", krimp:"1,60", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024420", kalip:"198", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024421", kalip:"63-155-215-250", krimp:"-", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024422", kalip:"73", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024424", kalip:"333-42-43", krimp:"1,55", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024434", kalip:"77", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024436", kalip:"245", krimp:"1,20", cekme:"85", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024437", kalip:"178", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024439", kalip:"118", krimp:"1,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024440", kalip:"114-230", krimp:"1,25", cekme:"85", krimp_gen:"2,15", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024442", kalip:"10", krimp:"1,55", cekme:"85", krimp_gen:"1,55", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024445", kalip:"108-205", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024449", kalip:"108-205", krimp:"1,25", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024451", kalip:"65", krimp:"1,25", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024454", kalip:"115", krimp:"1,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10024460", kalip:"55", krimp:"2,35", cekme:"85", krimp_gen:"KUMPAS İLE ÖLÇÜLECEK", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025031", kalip:"186", krimp:"1,10", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025036", kalip:"30-51-175", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025041", kalip:"30-51-175", krimp:"1,95", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025087", kalip:"(SOL) 72-94", krimp:"1,20", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025087", kalip:"(SAĞ) 72-94", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025157", kalip:"185 -304", krimp:"1,45", cekme:"85", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025206", kalip:"14-50", krimp:"1,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025307", kalip:"49", krimp:"1,70", cekme:"85", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025350", kalip:"115", krimp:"1,10", cekme:"85", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025363", kalip:"195", krimp:"1,95", cekme:"85", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025510", kalip:"260", krimp:"1,30", cekme:"85", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025512", kalip:"195", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025823", kalip:"78", krimp:"0,95", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10025844", kalip:"47", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10026440", kalip:"190", krimp:"1,55", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10029971", kalip:"147", krimp:"1,20", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10030881", kalip:"286", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10034068", kalip:"326", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10034070", kalip:"324", krimp:"1,85", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10034415", kalip:"184", krimp:"1,45", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"0,75 mm²", kontak:"10034454", kalip:"176", krimp:"1,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  // 1,00 mm²
  {kesit:"1,00 mm²", kontak:"10000512", kalip:"114-230", krimp:"1,40", cekme:"108", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10001498", kalip:"108-205", krimp:"1,60", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10034068", kalip:"326", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10003566", kalip:"224", krimp:"1,10", cekme:"108", krimp_gen:"2,06", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10003566", kalip:"117", krimp:"1,20", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10003812", kalip:"117", krimp:"1,35", cekme:"108", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10003813", kalip:"117", krimp:"1,70", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10003965", kalip:"204", krimp:"1,45", cekme:"108", krimp_gen:"2,35", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10006876", kalip:"226", krimp:"1,20", cekme:"108", krimp_gen:"2,06", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10006876", kalip:"117", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10006877", kalip:"226", krimp:"1,20", cekme:"108", krimp_gen:"2,06", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10006877", kalip:"117", krimp:"1,40", cekme:"108", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10023345", kalip:"184", krimp:"1,55", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10023784", kalip:"117", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10023788", kalip:"117", krimp:"1,50", cekme:"108", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10023791", kalip:"117", krimp:"1,55", cekme:"108", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10023792", kalip:"114-230", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10023806", kalip:"198", krimp:"1,40", cekme:"108", krimp_gen:"2,15", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024274", kalip:"42-43-192", krimp:"1,75", cekme:"108", krimp_gen:"2,80", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024287", kalip:"241", krimp:"1,85", cekme:"108", krimp_gen:"3,30", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024291", kalip:"107", krimp:"1,60", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024293", kalip:"42-43", krimp:"1,50", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024297", kalip:"31", krimp:"1,30", cekme:"108", krimp_gen:"3,00", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024306", kalip:"42-43", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024307", kalip:"49", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"3,23", not:""},
  {kesit:"1,00 mm²", kontak:"10024313", kalip:"07", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024318", kalip:"253-254", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"2,80", not:""},
  {kesit:"1,00 mm²", kontak:"10024320", kalip:"46-211", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"2,50", not:""},
  {kesit:"1,00 mm²", kontak:"10024326", kalip:"162-320", krimp:"1,65", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024327", kalip:"63-155-215-250", krimp:"-", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024327", kalip:"152", krimp:"1,65", cekme:"108", krimp_gen:"2,30", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024339", kalip:"118", krimp:"1,50", cekme:"108", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024362", kalip:"14-50-104-133", krimp:"1,55", cekme:"108", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024365", kalip:"245", krimp:"1,30", cekme:"108", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024365", kalip:"14-50-104", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024366", kalip:"151", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024367", kalip:"14-50-104", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024368", kalip:"21-35-128", krimp:"-", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024398", kalip:"78", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024399", kalip:"77", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024401", kalip:"99-207", krimp:"1,60", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024402", kalip:"85", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024404", kalip:"85", krimp:"1,55", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024406", kalip:"49", krimp:"1,70", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024407", kalip:"73", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024420", kalip:"69", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024420", kalip:"198", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024421", kalip:"63-155-215-250", krimp:"1,50", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024422", kalip:"73-194", krimp:"1,70", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024424", kalip:"42-43", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024433", kalip:"137", krimp:"1,60", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024434", kalip:"27-77", krimp:"1,50", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024438", kalip:"53", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024439", kalip:"23-118", krimp:"1,60", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024440", kalip:"114-230", krimp:"1,30", cekme:"108", krimp_gen:"2,20", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024442", kalip:"10", krimp:"1,55", cekme:"108", krimp_gen:"2,40", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024445", kalip:"75-108-205", krimp:"1,60", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024449", kalip:"108-205", krimp:"1,50", cekme:"108", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10024453", kalip:"201", krimp:"1,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10025036", kalip:"30-51-175", krimp:"1,90", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10025041", kalip:"30-51-175", krimp:"2,05", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10025047", kalip:"249", krimp:"1,50", cekme:"108", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10025047", kalip:"85", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10025048", kalip:"70", krimp:"2,20", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10025206", kalip:"14-50", krimp:"1,45", cekme:"108", krimp_gen:"", izok:"2,80", not:""},
  {kesit:"1,00 mm²", kontak:"10025247", kalip:"10", krimp:"1,50", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10025833", kalip:"14-50", krimp:"1,50", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10027442", kalip:"117", krimp:"1,55", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"1,00 mm²", kontak:"10034070", kalip:"324", krimp:"1,95", cekme:"108", krimp_gen:"", izok:"", not:""},
  // 1,50 mm²
  {kesit:"1,50 mm²", kontak:"10001498", kalip:"75-108-205", krimp:"1,75", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10003813", kalip:"229", krimp:"1,70", cekme:"150", krimp_gen:"2,60", izok:"4,25", not:""},
  {kesit:"1,50 mm²", kontak:"10003965", kalip:"204", krimp:"1,55", cekme:"150", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023317", kalip:"83", krimp:"1,80", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,60", cekme:"150", krimp_gen:"1,90", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023327", kalip:"121-144-303", krimp:"1,60", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023345", kalip:"185-304", krimp:"1,80", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023346", kalip:"73-194", krimp:"1,80", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023575", kalip:"25-178-182", krimp:"1,70", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023578", kalip:"112", krimp:"1,80", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023588", kalip:"39", krimp:"2,35", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023783", kalip:"229", krimp:"1,65", cekme:"150", krimp_gen:"2,55", izok:"4,25", not:""},
  {kesit:"1,50 mm²", kontak:"10023786", kalip:"224", krimp:"1,50", cekme:"150", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023799", kalip:"228", krimp:"3,40", cekme:"150", krimp_gen:"4,80", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023806", kalip:"198", krimp:"1,55", cekme:"150", krimp_gen:"2,25", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10023807", kalip:"69-198", krimp:"1,75", cekme:"150", krimp_gen:"2,25", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024274", kalip:"42-43", krimp:"1,75", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024295", kalip:"204", krimp:"1,50", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024295", kalip:"118", krimp:"1,55", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024297", kalip:"31", krimp:"1,60", cekme:"150", krimp_gen:"3,0", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024302", kalip:"185-304", krimp:"1,40", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024326", kalip:"162-320", krimp:"1,75", cekme:"150", krimp_gen:"3,40", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024339", kalip:"118", krimp:"1,55", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024399", kalip:"77", krimp:"1,85", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024402", kalip:"85-207", krimp:"1,80", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024407", kalip:"73", krimp:"1,90", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024419", kalip:"76", krimp:"1,70", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024422", kalip:"73-194", krimp:"1,75", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024429", kalip:"83", krimp:"2,25", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024433", kalip:"137", krimp:"1,65", cekme:"150", krimp_gen:"3,20", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024437", kalip:"178-182", krimp:"1,60", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024439", kalip:"118", krimp:"1,75", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024445", kalip:"75-108-205", krimp:"1,75", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024448", kalip:"75", krimp:"1,55", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024449", kalip:"108-205", krimp:"1,60", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10024451", kalip:"65", krimp:"1,40", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025035", kalip:"246", krimp:"2,20", cekme:"150", krimp_gen:"4,10", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025035", kalip:"70", krimp:"2,25", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025036", kalip:"30-51-175", krimp:"2,00", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025037", kalip:"135", krimp:"2,40", cekme:"150", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025041", kalip:"30-51-175", krimp:"2,25", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025045", kalip:"Sağ Kalıp 95-240", krimp:"2,10", cekme:"150", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025045", kalip:"Sol Kalıp 159-239", krimp:"2,10", cekme:"150", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025047", kalip:"207", krimp:"1,75", cekme:"150", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025048", kalip:"70", krimp:"2,20", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025157", kalip:"185-304", krimp:"1,85", cekme:"150", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025423", kalip:"229", krimp:"1,70", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025478", kalip:"199", krimp:"1,80", cekme:"150", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025499", kalip:"304", krimp:"1,90", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025502", kalip:"158", krimp:"1,65", cekme:"150", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025512", kalip:"195", krimp:"1,70", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025525", kalip:"229", krimp:"1,70", cekme:"150", krimp_gen:"2,60", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025530", kalip:"71", krimp:"2,25", cekme:"150", krimp_gen:"5,00", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10025917", kalip:"109", krimp:"1,90", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10027083", kalip:"Ş.Onay 111", krimp:"1,60", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10027083", kalip:"198", krimp:"1,85", cekme:"150", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10029208", kalip:"241", krimp:"2,00", cekme:"150", krimp_gen:"3,25", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10029693", kalip:"284", krimp:"1,45", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10029694", kalip:"283-284", krimp:"1,45", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10029697", kalip:"284", krimp:"1,45", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10029699", kalip:"284", krimp:"1,45", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10034068", kalip:"326", krimp:"1,80", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10034070", kalip:"324", krimp:"2,00", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"1,50 mm²", kontak:"10040081", kalip:"199", krimp:"2,00", cekme:"150", krimp_gen:"", izok:"", not:""},
  // 2,50 mm²
  {kesit:"2,50 mm²", kontak:"10003813", kalip:"229", krimp:"2,10", cekme:"230", krimp_gen:"2,60", izok:"4,25", not:""},
  {kesit:"2,50 mm²", kontak:"10023318", kalip:"135", krimp:"2,55", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"2,00", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023327", kalip:"121-144-303", krimp:"1,80", cekme:"230", krimp_gen:"Max 2,90", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023328", kalip:"126-197", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023346", kalip:"73-194", krimp:"2,05", cekme:"230", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023347", kalip:"44", krimp:"2,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023364", kalip:"74", krimp:"2,60", cekme:"230", krimp_gen:"5,65", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023575", kalip:"182", krimp:"1,85", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023575", kalip:"25-178", krimp:"1,90", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023578", kalip:"112", krimp:"2,45", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023581", kalip:"70", krimp:"2,35", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023583", kalip:"70", krimp:"2,50", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023809", kalip:"125", krimp:"2,50", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10023877", kalip:"70", krimp:"3,25", cekme:"230", krimp_gen:"4,25", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024286", kalip:"31", krimp:"1,95", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024291", kalip:"107", krimp:"1,95", cekme:"230", krimp_gen:"3,00", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024295", kalip:"118-204", krimp:"1,85", cekme:"108 Ş. Onay", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024299", kalip:"137", krimp:"1,90", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024328", kalip:"77", krimp:"2,10", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024332", kalip:"120-144", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024333", kalip:"126", krimp:"1,90", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024339", kalip:"118", krimp:"2,10", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024399", kalip:"77", krimp:"2,00", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024402", kalip:"85-207", krimp:"2,05", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024403", kalip:"11", krimp:"2,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024405", kalip:"85", krimp:"2,05", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024422", kalip:"73-194", krimp:"2,00", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024423", kalip:"44", krimp:"2,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024429", kalip:"83", krimp:"2,55", cekme:"230", krimp_gen:"3,75", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024433", kalip:"137", krimp:"2,05", cekme:"230", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024437", kalip:"178-182", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024439", kalip:"118", krimp:"2,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024446", kalip:"75", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024450", kalip:"31", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024456", kalip:"73", krimp:"2,65", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025035", kalip:"70", krimp:"2,40", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025035", kalip:"246", krimp:"2,30", cekme:"230", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025037", kalip:"135", krimp:"2,60", cekme:"230", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024445", kalip:"205", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024447", kalip:"75-182", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10024448", kalip:"182", krimp:"1,70", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025038", kalip:"71", krimp:"2,55", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025041", kalip:"30-175", krimp:"2,35", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025043", kalip:"140-233", krimp:"3,65", cekme:"230", krimp_gen:"7,15", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025047", kalip:"207", krimp:"1,95", cekme:"230", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025048", kalip:"70", krimp:"2,40", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025049", kalip:"71-193", krimp:"2,65", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025340", kalip:"77", krimp:"2,15", cekme:"230", krimp_gen:"4,00", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10025467", kalip:"70", krimp:"3,25", cekme:"230", krimp_gen:"4,25", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10029693", kalip:"284", krimp:"1,65", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10029697", kalip:"284", krimp:"1,70", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10029703", kalip:"7", krimp:"1,90", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10029704", kalip:"195", krimp:"2,50", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10030851", kalip:"71", krimp:"2,10", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10031059", kalip:"280", krimp:"2,15", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10031059", kalip:"44-280", krimp:"2,10", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10031061", kalip:"262-282", krimp:"2,05", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10031139", kalip:"125", krimp:"2,15", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10031599", kalip:"44", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10031599", kalip:"280", krimp:"1,85", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10031999", kalip:"283", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10032265", kalip:"178", krimp:"1,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2,50 mm²", kontak:"10034070", kalip:"324", krimp:"2,15", cekme:"230", krimp_gen:"", izok:"", not:""},
  // 4,00 mm²
  {kesit:"4,00 mm²", kontak:"10023328", kalip:"126-197", krimp:"2,20", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10023347", kalip:"44", krimp:"2,50", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10023579", kalip:"7", krimp:"1,80", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10023579", kalip:"293", krimp:"1,90", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10023583", kalip:"7", krimp:"1,80", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10023583", kalip:"70", krimp:"2,90", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10025035", kalip:"70", krimp:"2,80", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10025038", kalip:"71", krimp:"2,65", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10025049", kalip:"71-193", krimp:"2,95", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10025348", kalip:"125", krimp:"3,60", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10025539", kalip:"125", krimp:"3,40", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"4,00 mm²", kontak:"10031038", kalip:"125", krimp:"3,20", cekme:"310", krimp_gen:"", izok:"", not:""},
  // 6,00 mm²
  {kesit:"6,00 mm²", kontak:"10023324", kalip:"125", krimp:"3,90", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023347", kalip:"259", krimp:"2,60", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023347", kalip:"135", krimp:"2,60", cekme:"360", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023355", kalip:"122", krimp:"2,90", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023793", kalip:"140-233", krimp:"5,10", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023798", kalip:"140-233", krimp:"4,60", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023803", kalip:"140", krimp:"4,25", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023805", kalip:"140", krimp:"4,20", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10023810", kalip:"222", krimp:"3,10", cekme:"360", krimp_gen:"5,65", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10024423", kalip:"135", krimp:"2,70", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025035", kalip:"70", krimp:"3,05", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025038", kalip:"71", krimp:"2,85", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025043", kalip:"140-233", krimp:"4,00", cekme:"360", krimp_gen:"7,20", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025049", kalip:"71", krimp:"3,20", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025049", kalip:"193", krimp:"3,35", cekme:"360", krimp_gen:"4,80", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025050", kalip:"74", krimp:"3,00", cekme:"360", krimp_gen:"5,70", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025050", kalip:"247", krimp:"3,10", cekme:"360", krimp_gen:"5,60", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025195", kalip:"140", krimp:"3,25", cekme:"360", krimp_gen:"7,00", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025196", kalip:"140", krimp:"4,00", cekme:"360", krimp_gen:"7,20", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10025274", kalip:"71", krimp:"3,10", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"6,00 mm²", kontak:"10027091", kalip:"140-233", krimp:"4,10", cekme:"360", krimp_gen:"", izok:"", not:""},
  // 10,00 mm²
  {kesit:"10,00 mm²", kontak:"10023794", kalip:"140-233", krimp:"4,80", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10023795", kalip:"140-233", krimp:"5,00", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10023796", kalip:"140-233", krimp:"4,90", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10023797", kalip:"140-233", krimp:"4,85", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10023801", kalip:"140", krimp:"4,80", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10023802", kalip:"140", krimp:"5,00", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10023804", kalip:"140", krimp:"4,90", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10023810", kalip:"222", krimp:"3,95", cekme:"380", krimp_gen:"5,75", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10025040", kalip:"124", krimp:"6,60", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10025043", kalip:"140-233", krimp:"4,80", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10025050", kalip:"74", krimp:"3,70", cekme:"380", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10025039", kalip:"140-233", krimp:"5,35", cekme:"500", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10025040", kalip:"124", krimp:"7,10", cekme:"500", krimp_gen:"", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10025054", kalip:"172", krimp:"5,80", cekme:"500", krimp_gen:"7,80", izok:"", not:""},
  {kesit:"10,00 mm²", kontak:"10025040", kalip:"124", krimp:"7,35", cekme:"600 min", krimp_gen:"", izok:"", not:""},
  // 2 x 0,34 mm²
  {kesit:"2 x 0,34 mm²", kontak:"10000512", kalip:"114", krimp:"1,35", cekme:"43", krimp_gen:"", izok:"", not:""},
  // 2 x 0,35 mm²
  {kesit:"2 x 0,35 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,35", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,35 mm²", kontak:"10024326", kalip:"162", krimp:"1,60", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,35 mm²", kontak:"10024362", kalip:"14-50", krimp:"1,45", cekme:"45", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"2 x 0,35 mm²", kontak:"10025206", kalip:"14-50", krimp:"1,50", cekme:"45", krimp_gen:"", izok:"", not:""},
  // 2 x 0,50 mm²
  {kesit:"2 x 0,50 mm²", kontak:"10000512", kalip:"114-230", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10001498", kalip:"108-205", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10023046", kalip:"50", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024276", kalip:"115", krimp:"1,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024322", kalip:"4", krimp:"-", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024324", kalip:"10", krimp:"1,85", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024326", kalip:"162", krimp:"1,65", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024327", kalip:"4-63-155-215", krimp:"-", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024345", kalip:"170-328", krimp:"1,45", cekme:"60", krimp_gen:"2,25", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024358", kalip:"332", krimp:"1,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024358", kalip:"321", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024371", kalip:"53", krimp:"1,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024391", kalip:"114-205", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024420", kalip:"69-198", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024424", kalip:"333", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024440", kalip:"114", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024447", kalip:"75", krimp:"1,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10027120", kalip:"161", krimp:"1,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10029009", kalip:"114", krimp:"1,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10029009", kalip:"329", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10023328", kalip:"126-197", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10023345", kalip:"184", krimp:"1,75", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10023346", kalip:"73-194", krimp:"1,80", cekme:"85", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10023580", kalip:"Ş.Onay 146", krimp:"1,25", cekme:"85", krimp_gen:"1,95", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024271", kalip:"160", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024307", kalip:"49", krimp:"1,75", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024326", kalip:"61", krimp:"1,80", cekme:"85", krimp_gen:"2,35", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024362", kalip:"245", krimp:"1,55", cekme:"85", krimp_gen:"2,65", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024362", kalip:"14-50", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024363", kalip:"14", krimp:"1,75", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024367", kalip:"14-50", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024374", kalip:"177", krimp:"1,80", cekme:"85", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024386", kalip:"47", krimp:"2,00", cekme:"85", krimp_gen:"3,20", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024386", kalip:"28", krimp:"2,20", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024399", kalip:"77", krimp:"1,85", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024400", kalip:"77", krimp:"2,35", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024402", kalip:"85-207", krimp:"1,85", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024405", kalip:"85", krimp:"1,85", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024407", kalip:"73", krimp:"1,90", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024414", kalip:"105", krimp:"1,60", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024419", kalip:"76", krimp:"1,60", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024422", kalip:"73-194", krimp:"1,80", cekme:"85", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024435", kalip:"77", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024445", kalip:"108-205", krimp:"1,55", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024446", kalip:"75", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024447", kalip:"75", krimp:"1,60", cekme:"85", krimp_gen:"2,65", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024450", kalip:"31", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10024451", kalip:"65", krimp:"1,35", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10025157", kalip:"185-304", krimp:"1,85", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 0,50 mm²", kontak:"10029971", kalip:"147", krimp:"1,50", cekme:"85", krimp_gen:"", izok:"", not:""},
  // 2 x 1,00 mm²
  {kesit:"2 x 1,00 mm²", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10023588", kalip:"39", krimp:"2,40", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024286", kalip:"31", krimp:"2,00", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024287", kalip:"241", krimp:"2,10", cekme:"108", krimp_gen:"3,30", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024299", kalip:"137", krimp:"1,90", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024293", kalip:"Ş. Onay 42-43", krimp:"1,70", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024399", kalip:"77", krimp:"1,95", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024407", kalip:"73", krimp:"1,95", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024415", kalip:"80", krimp:"-", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024419", kalip:"76", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024422", kalip:"73-194", krimp:"1,90", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024423", kalip:"44", krimp:"2,05", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024433", kalip:"137", krimp:"2,00", cekme:"108", krimp_gen:"3,20", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024445", kalip:"108", krimp:"1,65", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,00 mm²", kontak:"10024446", kalip:"75", krimp:"1,70", cekme:"108", krimp_gen:"", izok:"", not:""},
  // 2 x 1,50 mm²
  {kesit:"2 x 1,50 mm²", kontak:"10023328", kalip:"126-197", krimp:"2,00", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10023347", kalip:"259", krimp:"2,30", cekme:"150", krimp_gen:"4,45", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10023347", kalip:"135", krimp:"2,25", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024329", kalip:"44", krimp:"2,50", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024333", kalip:"126", krimp:"1,80", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024397", kalip:"84", krimp:"3,00", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024400", kalip:"77", krimp:"2,35", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024402", kalip:"85-207", krimp:"2,20", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024419", kalip:"76", krimp:"1,90", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024422", kalip:"73-194", krimp:"2,05", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024423", kalip:"44", krimp:"2,35", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10024429", kalip:"83", krimp:"2,60", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10025515", kalip:"44", krimp:"2,30", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10025539", kalip:"125", krimp:"3,25", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 1,50 mm²", kontak:"10026743", kalip:"304", krimp:"2,50", cekme:"150", krimp_gen:"", izok:"", not:""},
  // 2 x 2,50 mm²
  {kesit:"2 x 2,50 mm²", kontak:"10000512", kalip:"230", krimp:"1,45", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10023328", kalip:"Ş. Onay 126-197", krimp:"2,60", cekme:"230", krimp_gen:"3,45", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10023347", kalip:"44", krimp:"2,60", cekme:"230", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10023355", kalip:"122", krimp:"2,90", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10024333", kalip:"126", krimp:"2,25", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10024397", kalip:"84", krimp:"3,10", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10024417", kalip:"80", krimp:"-", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10024423", kalip:"44", krimp:"2,50", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10024423", kalip:"77", krimp:"2,65", cekme:"230", krimp_gen:"3,70", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10024440", kalip:"114", krimp:"1,35", cekme:"230", krimp_gen:"2,20", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10024440", kalip:"44", krimp:"2,95", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025035", kalip:"70", krimp:"3,10", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025038", kalip:"71", krimp:"3,10", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025043", kalip:"140-233", krimp:"4,00", cekme:"230", krimp_gen:"7,20", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025049", kalip:"71-193", krimp:"3,15", cekme:"230", krimp_gen:"4,75", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025050", kalip:"74-247", krimp:"2,90", cekme:"230", krimp_gen:"5,60", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025274", kalip:"71", krimp:"3,00", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025340", kalip:"77", krimp:"2,50", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025539", kalip:"125", krimp:"3,65", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10025845", kalip:"77", krimp:"2,50", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10029704", kalip:"195", krimp:"2,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10031059", kalip:"280", krimp:"2,75", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 2,50 mm²", kontak:"10031059", kalip:"280", krimp:"2,75", cekme:"230", krimp_gen:"", izok:"", not:""},
  // 2 x 4,00 mm²
  {kesit:"2 x 4,00 mm²", kontak:"10025038", kalip:"71", krimp:"3,20", cekme:"310", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 4,00 mm²", kontak:"10025043", kalip:"140-233", krimp:"4,40", cekme:"310", krimp_gen:"7,20", izok:"", not:""},
  {kesit:"2 x 4,00 mm²", kontak:"10025049", kalip:"Ş.Onay 71-193", krimp:"3,50", cekme:"310", krimp_gen:"4,80", izok:"", not:""},
  {kesit:"2 x 4,00 mm²", kontak:"10025035", kalip:"70", krimp:"3,10", cekme:"360", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 4,00 mm²", kontak:"10025039", kalip:"140-233", krimp:"5,10", cekme:"360", krimp_gen:"7,30", izok:"", not:""},
  {kesit:"2 x 4,00 mm²", kontak:"10025040", kalip:"Ş. Onay 124", krimp:"7,10", cekme:"360", krimp_gen:"7,30", izok:"", not:""},
  {kesit:"2 x 4,00 mm²", kontak:"10025043", kalip:"140-233", krimp:"5,10", cekme:"360", krimp_gen:"7,30", izok:"", not:""},
  // 2 x 10,00 mm²
  {kesit:"2 x 10,00 mm²", kontak:"10025040", kalip:"124", krimp:"7,25", cekme:"380", krimp_gen:"", izok:"", not:""},
  // 6 AWG 6 AWG
  {kesit:"6 AWG 6 AWG", kontak:"10023320", kalip:"295", krimp:"6,20", cekme:"410", krimp_gen:"", izok:"", not:""},
  {kesit:"6 AWG 6 AWG", kontak:"10025040", kalip:"124", krimp:"7,00", cekme:"410", krimp_gen:"", izok:"", not:""},
  // 8 AWG
  {kesit:"8 AWG", kontak:"10023319", kalip:"295", krimp:"4,15", cekme:"370", krimp_gen:"", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023319", kalip:"140-233", krimp:"4,25", cekme:"370", krimp_gen:"7,25", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023320", kalip:"140", krimp:"-", cekme:"370", krimp_gen:"2,53", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023323", kalip:"295", krimp:"4,35", cekme:"370", krimp_gen:"", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023323", kalip:"140-233", krimp:"4,50", cekme:"370", krimp_gen:"7,25", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"370", krimp_gen:"", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023357", kalip:"140", krimp:"5,00", cekme:"370", krimp_gen:"", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023357", kalip:"172", krimp:"6,55", cekme:"370", krimp_gen:"7,75", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10023365", kalip:"9", krimp:"4,40", cekme:"370", krimp_gen:"", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10025050", kalip:"247", krimp:"3,45", cekme:"370", krimp_gen:"5,75", izok:"", not:""},
  {kesit:"8 AWG", kontak:"10025050", kalip:"74", krimp:"3,60", cekme:"370", krimp_gen:"", izok:"", not:""},
  // 10 AWG
  {kesit:"10 AWG", kontak:"10023318", kalip:"135", krimp:"3,25", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10023319", kalip:"295", krimp:"3,95", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10023319", kalip:"140-233", krimp:"4,00", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10023324", kalip:"125", krimp:"3,90", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,70", cekme:"355", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10023355", kalip:"122", krimp:"3,00", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10023364", kalip:"74", krimp:"3,00", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10023797", kalip:"140-233", krimp:"5,00", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10025050", kalip:"74", krimp:"2,90", cekme:"355", krimp_gen:"", izok:"", not:""},
  {kesit:"10 AWG", kontak:"10025050", kalip:"247", krimp:"3,20", cekme:"355", krimp_gen:"5,60", izok:"", not:""},
  // 12 AWG
  {kesit:"12 AWG", kontak:"10023318", kalip:"135", krimp:"2,80", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023322", kalip:"134", krimp:"2,75", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023323", kalip:"140-233", krimp:"3,80", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023324", kalip:"125", krimp:"3,60", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,20", cekme:"275", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,45", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023364", kalip:"74", krimp:"2,85", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023327", kalip:"121-144", krimp:"2,20", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,15", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"12 AWG", kontak:"10025049", kalip:"71", krimp:"2,90", cekme:"275", krimp_gen:"", izok:"", not:""},
  // 14 AWG
  {kesit:"14 AWG", kontak:"10001498", kalip:"108-205", krimp:"1,90", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023316", kalip:"132-182", krimp:"1,70", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023316", kalip:"204", krimp:"1,95", cekme:"200", krimp_gen:"2,43", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023317", kalip:"83", krimp:"1,95", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023318", kalip:"135", krimp:"2,50", cekme:"200", krimp_gen:"", izok:"4,40", not:""},
  {kesit:"14 AWG", kontak:"10023322", kalip:"134-195", krimp:"2,50", cekme:"200", krimp_gen:"", izok:"4,05", not:""},
  {kesit:"14 AWG", kontak:"10023324", kalip:"125", krimp:"3,40", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023327", kalip:"121-144", krimp:"1,80", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023327 (10023326)  parçaları ile basıldı", kalip:"121-144", krimp:"2,20", cekme:"200", krimp_gen:"2,30", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023328", kalip:"121-126-197", krimp:"1,80", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,05", cekme:"200", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024272", kalip:"29", krimp:"1,70", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024299", kalip:"137", krimp:"2,10", cekme:"200", krimp_gen:"2,70", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024383", kalip:"77", krimp:"2,15", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024422", kalip:"73-194", krimp:"2,00", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024429", kalip:"83", krimp:"2,50", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024433", kalip:"137", krimp:"1,90", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024434", kalip:"77", krimp:"1,70", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024445", kalip:"108-205", krimp:"1,85", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024446", kalip:"75", krimp:"1,80", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024447", kalip:"75", krimp:"1,75", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024448", kalip:"75", krimp:"1,70", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024449", kalip:"108-205", krimp:"1,85", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024455", kalip:"70", krimp:"2,20", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10024456", kalip:"134", krimp:"2,55", cekme:"200", krimp_gen:"3,65", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10025047", kalip:"207", krimp:"1,90", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"14 AWG", kontak:"10025049", kalip:"71-193", krimp:"2,65", cekme:"230", krimp_gen:"", izok:"", not:""},
  // 15 AWG
  {kesit:"15 AWG", kontak:"10024272", kalip:"29", krimp:"1,80", cekme:"165", krimp_gen:"", izok:"", not:""},
  // 16 AWG
  {kesit:"16 AWG", kontak:"10001498", kalip:"108-205", krimp:"1,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10008837", kalip:"146", krimp:"1,30", cekme:"120", krimp_gen:"Terminal kablo ile uyumsuz", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023316", kalip:"132-182-204", krimp:"1,60", cekme:"135", krimp_gen:"2,40", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023322", kalip:"134-195", krimp:"2,40", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,65", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023327", kalip:"121-144", krimp:"1,60", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023327 Kare parça", kalip:"121-144", krimp:"2,10", cekme:"135", krimp_gen:"2,20", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023345", kalip:"184-185", krimp:"1,60", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,80", cekme:"135", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023375", kalip:"114", krimp:"1,45", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10023379", kalip:"137", krimp:"1,60", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024272", kalip:"338", krimp:"1,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024272", kalip:"29-268", krimp:"1,80", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024283", kalip:"29", krimp:"1,75", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024286", kalip:"31", krimp:"1,65", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024337", kalip:"46", krimp:"1,50", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024339", kalip:"118", krimp:"1,55", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024380", kalip:"54-200", krimp:"1,95", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024399", kalip:"77", krimp:"1,80", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024402", kalip:"85-207", krimp:"1,80", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024419", kalip:"76", krimp:"1,60", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024420", kalip:"198", krimp:"1,60", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024422", kalip:"73-194", krimp:"1,75", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024424", kalip:"42-43", krimp:"1,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024429", kalip:"83", krimp:"2,25", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024439", kalip:"118", krimp:"1,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024445", kalip:"108-205", krimp:"1,75", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024449", kalip:"108-205", krimp:"1,65", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024450", kalip:"31", krimp:"1,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024451", kalip:"65", krimp:"1,30", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10024456", kalip:"73", krimp:"2,30", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"16 AWG", kontak:"10029971", kalip:"147", krimp:"1,40", cekme:"135", krimp_gen:"", izok:"", not:""},
  // 18 AWG
  {kesit:"18 AWG", kontak:"10000512", kalip:"114-230", krimp:"1,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10001498", kalip:"108-205", krimp:"1,50", cekme:"90", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10003730", kalip:"179", krimp:"1,00", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10003731", kalip:"82", krimp:"1,05", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10008837", kalip:"146", krimp:"1,15", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10018584", kalip:"191", krimp:"1,10", cekme:"90", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10018584", kalip:"115", krimp:"1,20", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10022065", kalip:"28", krimp:"1,65", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023106", kalip:"118", krimp:"1,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023315", kalip:"138", krimp:"1,20", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023316", kalip:"132-182", krimp:"1,45", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023316", kalip:"204", krimp:"1,50", cekme:"90", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023317", kalip:"83", krimp:"1,80", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023322", kalip:"134-195", krimp:"2,20", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023325", kalip:"51-200", krimp:"1,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023326", kalip:"120-127-143-150-156-302", krimp:"1,45", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023327", kalip:"121-144", krimp:"1,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023342", kalip:"131", krimp:"1,10", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023344", kalip:"129", krimp:"1,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023345", kalip:"184", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"3,10", not:""},
  {kesit:"18 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,60", cekme:"90", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10023348", kalip:"191-203", krimp:"1,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024278", kalip:"115-191", krimp:"1,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024286", kalip:"31", krimp:"1,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024294", kalip:"167-168-173", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024297", kalip:"31", krimp:"1,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024299", kalip:"137", krimp:"1,45", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024306", kalip:"42-43", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024313", kalip:"Esbc 207", krimp:"1,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024313", kalip:"SUTEM 207", krimp:"1,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024324", kalip:"184", krimp:"1,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024326", kalip:"252", krimp:"1,60", cekme:"90", krimp_gen:"2,65", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024326", kalip:"162-196-320", krimp:"1,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024339", kalip:"118", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024358", kalip:"321", krimp:"1,50", cekme:"90", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024362", kalip:"14-50", krimp:"1,60", cekme:"90", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024367", kalip:"14-50", krimp:"1,40", cekme:"90", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024380", kalip:"200", krimp:"1,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024398", kalip:"78", krimp:"1,25", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024401", kalip:"99-207", krimp:"1,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024406", kalip:"49", krimp:"1,65", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024419", kalip:"76", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024420", kalip:"198", krimp:"1,45", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024421", kalip:"63-155-215-250", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024422", kalip:"73", krimp:"1,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024424", kalip:"42-43", krimp:"1,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024424", kalip:"333", krimp:"1,65", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024434", kalip:"77", krimp:"1,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024438", kalip:"179 Alternatif 53", krimp:"1,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024438", kalip:"186 Orijinal 53", krimp:"1,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024439", kalip:"118", krimp:"1,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024440", kalip:"53-114-230", krimp:"1,45", cekme:"90", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024442", kalip:"10", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024444", kalip:"214", krimp:"1,10", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024445", kalip:"108-205", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024449", kalip:"108-205", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024450", kalip:"31", krimp:"1,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024451", kalip:"65", krimp:"1,25", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024453", kalip:"136-201", krimp:"1,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024454", kalip:"166", krimp:"1,20", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024454", kalip:"115", krimp:"1,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10024583", kalip:"32", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10025047", kalip:"207", krimp:"1,60", cekme:"108", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10025206", kalip:"14-50", krimp:"1,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10028865", kalip:"115", krimp:"1,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10029971", kalip:"147", krimp:"1,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10034068", kalip:"326", krimp:"1,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"18 AWG", kontak:"10034070", kalip:"324", krimp:"1,95", cekme:"90", krimp_gen:"", izok:"", not:""},
  // 20 AWG
  {kesit:"20 AWG", kontak:"10001498 Dar parça kullanılacak", kalip:"108-205", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10003731", kalip:"82", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10020436", kalip:"178-181-238", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10020436", kalip:"131", krimp:"1,10", cekme:"60", krimp_gen:"1,55", izok:"2,05", not:""},
  {kesit:"20 AWG", kontak:"10020599", kalip:"90", krimp:"0,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10023315", kalip:"138", krimp:"1,20", cekme:"60", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10023317", kalip:"83", krimp:"1,70", cekme:"60", krimp_gen:"3,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10023342", kalip:"131-213", krimp:"0,95", cekme:"60", krimp_gen:"1,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10023345", kalip:"184", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10023348", kalip:"191-203", krimp:"1,20", cekme:"60", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10023367", kalip:"131", krimp:"0,85", cekme:"60", krimp_gen:"1,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024274", kalip:"42-43-192", krimp:"1,55", cekme:"60", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024275", kalip:"42-43-192", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024278", kalip:"191-115", krimp:"1,20", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024294", kalip:"168", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024308", kalip:"42-43", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024309", kalip:"318", krimp:"0,95", cekme:"60", krimp_gen:"1,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024339", kalip:"118", krimp:"1,35", cekme:"60", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024340", kalip:"343", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024359", kalip:"170-328", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024361", kalip:"142-153", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024367", kalip:"50-133", krimp:"1,25", cekme:"60", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024390", kalip:"5", krimp:"1,20", cekme:"60", krimp_gen:"2,00", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024391", kalip:"114", krimp:"1,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024392", kalip:"48-279", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024398", kalip:"78", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024401", kalip:"99", krimp:"1,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024439", kalip:"118", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024440", kalip:"114-230", krimp:"1,20", cekme:"60", krimp_gen:"2,20", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024445", kalip:"108-205", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024453", kalip:"136-201", krimp:"1,20", cekme:"60", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10024454", kalip:"114", krimp:"1,05", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10025317", kalip:"108", krimp:"1,20", cekme:"60", krimp_gen:"2,50", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10025355", kalip:"147", krimp:"1,05", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10025768", kalip:"Ş.Onay 204", krimp:"1,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10025768", kalip:"Ş.Onay 299", krimp:"1,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10028906", kalip:"297", krimp:"1,05", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10028907", kalip:"298", krimp:"1,25", cekme:"60", krimp_gen:"1,55", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10028908", kalip:"296", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10030552", kalip:"176-276-277", krimp:"0,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10031060", kalip:"281", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10034068", kalip:"326", krimp:"1,65", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10034070", kalip:"324", krimp:"1,85", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10035412", kalip:"200", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"20 AWG", kontak:"10040085", kalip:"300", krimp:"1,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  // 22 AWG
  {kesit:"22 AWG", kontak:"10000512", kalip:"Ş.Onay 114", krimp:"1,15", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10000512", kalip:"Ş.Onay 186", krimp:"1,25", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10001685", kalip:"86", krimp:"1,10", cekme:"40", krimp_gen:"1,60", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10003730", kalip:"179", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10008837", kalip:"Ş. Onay 146", krimp:"0,95", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10008845", kalip:"90-119-176-276-277", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10019009", kalip:"90-119-176-276-277", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10020436", kalip:"178-181-238-255", krimp:"0,85", cekme:"40", krimp_gen:"1,45", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023315", kalip:"138", krimp:"1,05", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023325", kalip:"200", krimp:"1,65", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,25", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024340", kalip:"343", krimp:"1,30", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023342", kalip:"131-213", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023345", kalip:"184", krimp:"1,40", cekme:"40", krimp_gen:"", izok:"3,05", not:""},
  {kesit:"22 AWG", kontak:"10023348", kalip:"Ş. Onay 203", krimp:"1,15", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023349", kalip:"191", krimp:"1,10", cekme:"40", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023349", kalip:"203", krimp:"1,15", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023354", kalip:"132", krimp:"1,00", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023360", kalip:"90", krimp:"0,75", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023361", kalip:"148", krimp:"0,70", cekme:"40", krimp_gen:"1,55", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023361", kalip:"153", krimp:"0,80", cekme:"40", krimp_gen:"1,50", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023367", kalip:"213", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023367", kalip:"131", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023370", kalip:"237", krimp:"0,85", cekme:"40", krimp_gen:"1,75", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023371", kalip:"101-119-237", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023372", kalip:"183", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023373", kalip:"154", krimp:"0,75", cekme:"40", krimp_gen:"1,35", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023374", kalip:"174", krimp:"0,80", cekme:"40", krimp_gen:"", izok:"1,80 max", not:""},
  {kesit:"22 AWG", kontak:"10023376", kalip:"234", krimp:"1,20", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023377", kalip:"Ş. Onay 234", krimp:"1,20", cekme:"40", krimp_gen:"Kablo terminal uyumsuz", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023380", kalip:"170", krimp:"1,45", cekme:"40", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023388", kalip:"Ş. Onay 234", krimp:"1,20", cekme:"40", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023572", kalip:"102", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023576", kalip:"38", krimp:"0,80", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023577", kalip:"110-279", krimp:"0,95", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023585", kalip:"157", krimp:"0,80", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023585", kalip:"142", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023586", kalip:"153", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023590", kalip:"142", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023592", kalip:"142", krimp:"0,80", cekme:"40", krimp_gen:"1,70", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10023593", kalip:"38", krimp:"0,80", cekme:"40", krimp_gen:"1,50", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024274", kalip:"42-43-192", krimp:"1,40", cekme:"40", krimp_gen:"2,55", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024275", kalip:"Ş. Onay 42-43-192", krimp:"1,40", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024284", kalip:"98-180", krimp:"0,95", cekme:"40", krimp_gen:"1,50", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024285", kalip:"49", krimp:"1,20", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024288", kalip:"187-271", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024308", kalip:"42-43", krimp:"1,25", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024308", kalip:"Ş.Onay 192", krimp:"1,50", cekme:"40", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024309", kalip:"318", krimp:"0,80", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024310", kalip:"137", krimp:"0,90", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024315", kalip:"214", krimp:"1,05", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024391", kalip:"279", krimp:"1,10", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024391", kalip:"201", krimp:"1,15", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024392", kalip:"48-279", krimp:"1,10", cekme:"40", krimp_gen:"1,05", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10024445", kalip:"108-205", krimp:"1,25", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10025030", kalip:"113-141", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10025338", kalip:"5", krimp:"1,30", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10025442", kalip:"141-202", krimp:"0,80", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10025503", kalip:"278", krimp:"0,85", cekme:"40", krimp_gen:"1,90 max", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10030551", kalip:"148", krimp:"0,75", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10030552", kalip:"176-276-277", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10030666", kalip:"281", krimp:"1,20", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10031060", kalip:"281", krimp:"1,20", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10031919", kalip:"281", krimp:"1,05", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10032332", kalip:"176", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"22 AWG", kontak:"10034454", kalip:"176", krimp:"0,85", cekme:"40", krimp_gen:"", izok:"", not:""},
  // 24 AWG
  {kesit:"24 AWG", kontak:"10003730", kalip:"179", krimp:"0,80", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10020436", kalip:"178-181-238-255", krimp:"0,85", cekme:"28", krimp_gen:"1,45", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10023342", kalip:"131-213", krimp:"0,80", cekme:"28", krimp_gen:"1,50", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10023361", kalip:"148", krimp:"0,65", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10023361", kalip:"153", krimp:"0,75", cekme:"28", krimp_gen:"1,50", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10023367", kalip:"131", krimp:"0,80", cekme:"28", krimp_gen:"1,50", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10023586", kalip:"Ş.Onay 142-176", krimp:"0,85", cekme:"28", krimp_gen:"1,55", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10023592", kalip:"Ş.Onay 142", krimp:"0,75", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10024309", kalip:"318", krimp:"0,80", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10025030", kalip:"113-141", krimp:"0,80", cekme:"28", krimp_gen:"", izok:"1,50", not:""},
  {kesit:"24 AWG", kontak:"10025338", kalip:"5", krimp:"1,15", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"24 AWG", kontak:"10025442", kalip:"202", krimp:"0,75", cekme:"28", krimp_gen:"1,75", izok:"", not:""},
  // 26 AWG
  {kesit:"26 AWG", kontak:"10008845", kalip:"90-119-276-277", krimp:"0,85", cekme:"15", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10020599", kalip:"102", krimp:"0,70", cekme:"15", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023572", kalip:"90-119", krimp:"0,75", cekme:"15", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023585", kalip:"157", krimp:"0,70", cekme:"15", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023590", kalip:"Ş. Onay 142", krimp:"0,80", cekme:"15", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10025030", kalip:"113-141", krimp:"0,70", cekme:"15", krimp_gen:"", izok:"1,50", not:""},
  {kesit:"26 AWG", kontak:"10014645", kalip:"189", krimp:"0,55", cekme:"11", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10025040", kalip:"124", krimp:"7,40", cekme:"410", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023319", kalip:"140-233", krimp:"4,05", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023323", kalip:"140-233", krimp:"4,15", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023347", kalip:"44", krimp:"3,05", cekme:"275", krimp_gen:"4,25", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023355", kalip:"122", krimp:"3,15", cekme:"275", krimp_gen:"4,80", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023324", kalip:"125", krimp:"3,85", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,40", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023341", kalip:"140-233", krimp:"4,20", cekme:"200", krimp_gen:"7,20", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10023347", kalip:"44", krimp:"2,55", cekme:"200", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10024397", kalip:"84", krimp:"3,20", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10024399", kalip:"77", krimp:"2,05", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10024417", kalip:"80", krimp:"-", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10024422", kalip:"73", krimp:"2,10", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"26 AWG", kontak:"10024423", kalip:"77", krimp:"2,35", cekme:"200", krimp_gen:"4,05", izok:"", not:""},
  // 2 x 14 AWG
  {kesit:"2 x 14 AWG", kontak:"10024423", kalip:"44", krimp:"2,50", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 14 AWG", kontak:"10025049", kalip:"71", krimp:"3,10", cekme:"200", krimp_gen:"5,30", izok:"", not:""},
  {kesit:"2 x 14 AWG", kontak:"10025050", kalip:"74-247", krimp:"2,90", cekme:"200", krimp_gen:"5,60", izok:"", not:""},
  {kesit:"2 x 14 AWG", kontak:"10025340", kalip:"77", krimp:"2,50", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 14 AWG", kontak:"10025515", kalip:"44", krimp:"2,15", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 14 AWG", kontak:"10025845", kalip:"77", krimp:"2,80", cekme:"200", krimp_gen:"", izok:"", not:""},
  // 2 x 16 AWG
  {kesit:"2 x 16 AWG", kontak:"10023328", kalip:"121-126-197", krimp:"2,05", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,30", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10023378", kalip:"ESCUBEDO 134", krimp:"1,90", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10023378", kalip:"134", krimp:"2,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024397", kalip:"84", krimp:"2,95", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024400", kalip:"77", krimp:"2,30", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024419", kalip:"76", krimp:"1,95", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024422", kalip:"73-194", krimp:"2,00", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024423", kalip:"Ş. Onay 77", krimp:"2,10", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024423", kalip:"44", krimp:"2,35", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024429", kalip:"83", krimp:"2,55", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024435", kalip:"77", krimp:"2,05", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10024455", kalip:"70", krimp:"2,35", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 16 AWG", kontak:"10025515", kalip:"44", krimp:"2,25", cekme:"135", krimp_gen:"", izok:"", not:""},
  // 2 x 18 AWG
  {kesit:"2 x 18 AWG", kontak:"10023314", kalip:"138", krimp:"1,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10023316", kalip:"182", krimp:"1,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10023317", kalip:"83", krimp:"1,85", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10023322", kalip:"134", krimp:"2,45", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,65", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10023327", kalip:"121-144", krimp:"1,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,85", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10023353", kalip:"178", krimp:"1,85", cekme:"90", krimp_gen:"2,40", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024286", kalip:"31", krimp:"2,10", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024287", kalip:"241", krimp:"2,15", cekme:"90", krimp_gen:"3,30", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024299", kalip:"137", krimp:"1,80", cekme:"90", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024339", kalip:"118", krimp:"1,90", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024363", kalip:"50", krimp:"2,00", cekme:"90", krimp_gen:"2,63", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024399", kalip:"77", krimp:"1,95", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024402", kalip:"85-207", krimp:"1,85", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024407", kalip:"73-105", krimp:"1,95", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024419", kalip:"76", krimp:"1,65", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024422", kalip:"73-105-194", krimp:"1,85", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024429", kalip:"83", krimp:"2,20", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024434", kalip:"77", krimp:"1,80", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 18 AWG", kontak:"10024450", kalip:"31", krimp:"1,80", cekme:"90", krimp_gen:"", izok:"", not:""},
  // 2 x 20 AWG
  {kesit:"2 x 20 AWG", kontak:"10001498", kalip:"108-205", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 20 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,60", cekme:"60", krimp_gen:"2,20", izok:"", not:""},
  {kesit:"2 x 20 AWG", kontak:"10023345", kalip:"184", krimp:"1,65", cekme:"60", krimp_gen:"2,35", izok:"", not:""},
  {kesit:"2 x 20 AWG", kontak:"10023346", kalip:"194", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 20 AWG", kontak:"10024274", kalip:"42-43", krimp:"1,55", cekme:"60", krimp_gen:"2,65", izok:"", not:""},
  {kesit:"2 x 20 AWG", kontak:"10024339", kalip:"118", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 20 AWG", kontak:"10024440", kalip:"114-230", krimp:"1,35", cekme:"60", krimp_gen:"2,15", izok:"", not:""},
  // 2 x 22 AWG
  {kesit:"2 x 22 AWG", kontak:"10000512", kalip:"114", krimp:"1,30", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,45", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,65", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023354", kalip:"132", krimp:"1,10", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023370", kalip:"142", krimp:"1,05", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023370", kalip:"150-176", krimp:"1,10", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023371", kalip:"176", krimp:"1,10", cekme:"40", krimp_gen:"", izok:"2,60", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023376", kalip:"234", krimp:"1,30", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10023388", kalip:"234", krimp:"1,30", cekme:"40", krimp_gen:"", izok:"2,55", not:""},
  {kesit:"2 x 22 AWG", kontak:"10024275", kalip:"42-43-192", krimp:"1,45", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10024312", kalip:"34", krimp:"1,75", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10024315", kalip:"214", krimp:"1,10", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10024392", kalip:"48-279", krimp:"1,20", cekme:"40", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10024424", kalip:"42-43", krimp:"1,45", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 22 AWG", kontak:"10024445", kalip:"108", krimp:"1,45", cekme:"40", krimp_gen:"2,50", izok:"", not:""},
  // 2 x 24 AWG
  {kesit:"2 x 24 AWG", kontak:"10000512", kalip:"114", krimp:"1,40", cekme:"40", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10000512", kalip:"114", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023316", kalip:"132-182", krimp:"2,00", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023317", kalip:"83", krimp:"1,90", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,65", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,80", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023318", kalip:"135", krimp:"2,60", cekme:"60", krimp_gen:"", izok:"4,10", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023319", kalip:"295", krimp:"3,65", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023319", kalip:"140-233", krimp:"3,90", cekme:"60", krimp_gen:"", izok:"3,90", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023320", kalip:"295", krimp:"5,65", cekme:"60", krimp_gen:"", izok:"7,70", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023323", kalip:"140-233", krimp:"4,20", cekme:"275", krimp_gen:"", izok:"7,20", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023323", kalip:"140-233", krimp:"4,30", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023323", kalip:"140-233", krimp:"-", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023323", kalip:"140-233", krimp:"-", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023324", kalip:"125", krimp:"3,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023324", kalip:"125", krimp:"3,95", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,50", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,40", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,45", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,65", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,65", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,65", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,80", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"1,75", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"1,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"1,85", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"1,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,05", cekme:"60", krimp_gen:"3,50", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,10", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,15", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,15", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,20", cekme:"60", krimp_gen:"2,90", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"Ş. Onay 126-197", krimp:"2,40", cekme:"60", krimp_gen:"3,50", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"Ş. Onay 126-197", krimp:"2,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,55", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,60", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,75", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023328", kalip:"Ş. Onay 126-197", krimp:"2,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023332", kalip:"123", krimp:"-", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023332", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023337", kalip:"123", krimp:"6,80", cekme:"370", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023338", kalip:"123", krimp:"-", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,85", cekme:"85", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,95", cekme:"85", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,20", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,05", cekme:"60", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,10", cekme:"60", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,10", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,20", cekme:"90", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,15", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,20", cekme:"60", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,05", cekme:"60", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,30", cekme:"85", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,05", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,15", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"108", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,30", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,25", cekme:"108", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,35", cekme:"135", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,20", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,35", cekme:"150", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"60", krimp_gen:"4,30", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"135", krimp:"2,35", cekme:"150", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,55", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,45", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-135-259", krimp:"2,80", cekme:"150", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,60", cekme:"90", krimp_gen:"4,25", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,75", cekme:"200", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,75", cekme:"90", krimp_gen:"4,25", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023353", kalip:"182-178", krimp:"1,90", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"2,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"2,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"2,60", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"2,80", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"2,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,05", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,00", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,00", cekme:"60", krimp_gen:"4,70", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,00", cekme:"150", krimp_gen:"5,00", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,05", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,10", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,15", cekme:"24", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,15", cekme:"60", krimp_gen:"4,70", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,20", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"230", krimp_gen:"5,00", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,80", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"3,95", cekme:"60", krimp_gen:"3,95", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,00", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,10", cekme:"60", krimp_gen:"4,85", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,10", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,10", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,15", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,15", cekme:"60", krimp_gen:"4,85", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,20", cekme:"60", krimp_gen:"4,90", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023355", kalip:"122", krimp:"4,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10023364", kalip:"74", krimp:"3,05", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024270", kalip:"Ek Terminal 242", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024270", kalip:"Ek Terminal 242", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024270", kalip:"Ek Terminal 242", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024274", kalip:"42-43", krimp:"1,65", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024299", kalip:"137", krimp:"1,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024299", kalip:"137", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024306", kalip:"42-43", krimp:"1,55", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024306", kalip:"42-43", krimp:"1,60", cekme:"45", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024326", kalip:"162-320", krimp:"1,65", cekme:"45", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024326", kalip:"162-320", krimp:"1,60", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024326", kalip:"162-320", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024363", kalip:"14", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024397", kalip:"84", krimp:"2,90", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024397", kalip:"84", krimp:"2,95", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024397", kalip:"84", krimp:"3,40", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024399", kalip:"77", krimp:"1,90", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024400", kalip:"77", krimp:"2,50", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024400", kalip:"77", krimp:"2,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024402", kalip:"85-207", krimp:"1,70", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024402", kalip:"85-207", krimp:"2,00", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024402", kalip:"85-207", krimp:"1,95", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024405", kalip:"85", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024405", kalip:"85", krimp:"2,05", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024407", kalip:"73-194", krimp:"2,05", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024419", kalip:"76", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024419", kalip:"76", krimp:"1,80", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024422", kalip:"73-194", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024422", kalip:"73-194", krimp:"1,75", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024422", kalip:"73-194", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024422", kalip:"73-194", krimp:"1,85", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024422", kalip:"194", krimp:"1,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024422", kalip:"73-194", krimp:"2,00", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,00", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,15", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,15", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,20", cekme:"150", krimp_gen:"4,10", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,20", cekme:"108", krimp_gen:"4,05", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,25", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,25", cekme:"90", krimp_gen:"4,05", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024423", kalip:"44", krimp:"2,40", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024424", kalip:"42-43", krimp:"1,80", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024429", kalip:"83", krimp:"2,55", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024429", kalip:"83", krimp:"2,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024433", kalip:"137", krimp:"1,85", cekme:"85", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024435", kalip:"77", krimp:"2,10", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024435", kalip:"77", krimp:"2,20", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024440", kalip:"114", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024445", kalip:"108", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10024455", kalip:"70", krimp:"2,35", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025038", kalip:"71", krimp:"2,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025038", kalip:"71", krimp:"2,90", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025157", kalip:"185", krimp:"1,65", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025157", kalip:"184 185-304", krimp:"1,80", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025340", kalip:"77", krimp:"2,20", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025340", kalip:"77", krimp:"2,25", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025340", kalip:"77", krimp:"2,30", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025340", kalip:"77", krimp:"2,35", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025340", kalip:"77", krimp:"2,40", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025512", kalip:"112", krimp:"2,00", cekme:"60", krimp_gen:"3,20", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025515", kalip:"44", krimp:"2,25", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025515", kalip:"44", krimp:"2,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"2 x 24 AWG", kontak:"10025845", kalip:"77", krimp:"2,30", cekme:"108", krimp_gen:"", izok:"", not:""},
  // ── DOPPEL (karma kesit) ──
  {kesit:"DOPPEL: 0,34mm+22 AWG", kontak:"10000512", kalip:"114", krimp:"1,40", cekme:"40", krimp_gen:"2,10", izok:"", not:""},
  {kesit:"DOPPEL: 20 AWG+0,50 mm", kontak:"10000512", kalip:"114", krimp:"1,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+18 AWG", kontak:"10023316", kalip:"132-182", krimp:"2,00", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+18 AWG", kontak:"10023317", kalip:"83", krimp:"1,90", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+18 AWG", kontak:"10023318", kalip:"135", krimp:"2,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+20 AWG", kontak:"10023318", kalip:"135", krimp:"2,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x20 AWG", kontak:"10023318", kalip:"135", krimp:"2,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 5x20 AWG", kontak:"10023318", kalip:"135", krimp:"2,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x18 AWG", kontak:"10023318", kalip:"135", krimp:"2,55", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14+18 AWG", kontak:"10023318", kalip:"135", krimp:"2,65", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+16 AWG", kontak:"10023318", kalip:"135", krimp:"2,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x18+16 AWG", kontak:"10023318", kalip:"135", krimp:"2,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 12+18 AWG", kontak:"10023318", kalip:"135", krimp:"2,80", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x18+16 AWG", kontak:"10023318", kalip:"135", krimp:"2,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x16+2x20 AWG", kontak:"10023318", kalip:"135", krimp:"2,60", cekme:"60", krimp_gen:"", izok:"4,10", not:""},
  {kesit:"DOPPEL: 2x14+2x20 AWG", kontak:"10023319", kalip:"295", krimp:"3,65", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x14+2x20 AWG", kontak:"10023319", kalip:"140-233", krimp:"3,90", cekme:"60", krimp_gen:"", izok:"3,90", not:""},
  {kesit:"DOPPEL: 3x20+2x12+14 AWG", kontak:"10023320", kalip:"295", krimp:"5,65", cekme:"60", krimp_gen:"", izok:"7,70", not:""},
  {kesit:"DOPPEL: 12+14 AWG", kontak:"10023323", kalip:"140-233", krimp:"4,20", cekme:"275", krimp_gen:"", izok:"7,20", not:""},
  {kesit:"DOPPEL: 10+12 AWG (6+4 MM)", kontak:"10023323", kalip:"140-233", krimp:"4,30", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 12+14 AWG", kontak:"10023323", kalip:"140-233", krimp:"-", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x12 AWG (4+4 MM)", kontak:"10023323", kalip:"140-233", krimp:"-", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14+16 AWG", kontak:"10023324", kalip:"125", krimp:"3,70", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 12+14 AWG", kontak:"10023324", kalip:"125", krimp:"3,95", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,50 +22 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,50", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+24 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,40", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x22 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,45", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,50+0,75 mm", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x22 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,65", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,50mm+16 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,65", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20 AWG", kontak:"10023326", kalip:"120-127-143-150-156", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+0,50 mm", kontak:"10023327", kalip:"121-144-303", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+20 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+24 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,65", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10023327", kalip:"121-144-303", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+16 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x0,50 mm", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10023327", kalip:"121-144-303", krimp:"1,75", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,50 mm", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+18 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 5x0,50 mm", kontak:"10023327", kalip:"121-144-303", krimp:"1,80", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x20 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 6x22 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14+20 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x18 AWG (8 MM)", kontak:"10023327", kalip:"121-144-303", krimp:"1,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+2,50 mm", kontak:"10023327", kalip:"121-144-303", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+20 AWG", kontak:"10023327", kalip:"121-144-303", krimp:"1,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 6x22 AWG", kontak:"10023328", kalip:"126-197", krimp:"1,75", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 6x0,50 mm", kontak:"10023328", kalip:"126-197", krimp:"2,00", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 5x20 AWG", kontak:"10023328", kalip:"126-197", krimp:"1,90", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10023328", kalip:"126-197", krimp:"1,85", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+14 AWG", kontak:"10023328", kalip:"126-197", krimp:"1,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+14 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,05", cekme:"60", krimp_gen:"3,50", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+2,50 mm", kontak:"10023328", kalip:"126-197", krimp:"2,10", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10023328", kalip:"126-197", krimp:"2,15", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+16 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,15", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+14+6 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,20", cekme:"60", krimp_gen:"2,90", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+2,50 mm", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+14 AWG (12 MM)", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x16+18 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+14 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+12 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,35", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x0,75+2,50 mm", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x1,50 mm", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x1,50+1,00+0,75 mm", kontak:"10023328", kalip:"126-197", krimp:"2,30", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x14+20 AWG", kontak:"10023328", kalip:"Ş. Onay 126-197", krimp:"2,40", cekme:"60", krimp_gen:"3,50", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+12 AWG", kontak:"10023328", kalip:"Ş. Onay 126-197", krimp:"2,45", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2,5+4,00 mm", kontak:"10023328", kalip:"126-197", krimp:"2,55", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 12+16 AWG", kontak:"10023328", kalip:"126-197", krimp:"2,60", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+4,00 mm", kontak:"10023328", kalip:"126-197", krimp:"2,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x1,50 mm", kontak:"10023328", kalip:"126-197", krimp:"2,75", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2,50+4,00 mm", kontak:"10023328", kalip:"126-197", krimp:"2,80", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x2,50+0,75 mm", kontak:"10023328", kalip:"Ş. Onay 126-197", krimp:"2,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 12+8 AWG", kontak:"10023332", kalip:"123", krimp:"-", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14+16+8 AWG", kontak:"10023332", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x14+2x16+2x12+10 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+2x16+10 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+2x16+10+18 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+2x16+12+18 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+2x16+12AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+3x16 (10+18AWG)", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+3x16+10+18 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+3x16+12+18 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+3x16+2x18+10 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+3x16+2x18+12 AWG", kontak:"10023334", kalip:"123", krimp:"-", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x8 AWG", kontak:"10023337", kalip:"123", krimp:"6,80", cekme:"370", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+20 AWG", kontak:"10023338", kalip:"123", krimp:"-", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10023346", kalip:"73-194", krimp:"1,85", cekme:"85", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+20 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"DOPPEL: 3x20 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,50 mm", kontak:"10023346", kalip:"73-194", krimp:"1,95", cekme:"85", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+18 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,20", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+18 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,05", cekme:"60", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"DOPPEL: 4x20 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,10", cekme:"60", krimp_gen:"3,15", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10023346", kalip:"73-194", krimp:"2,10", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18+14 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,20", cekme:"90", krimp_gen:"2,05", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+20 AWG", kontak:"10023346", kalip:"73-194", krimp:"1,90", cekme:"60", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"DOPPEL: 3x18 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,15", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+14 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,20", cekme:"60", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"DOPPEL: 4x20 AWG", kontak:"10023346", kalip:"73-194", krimp:"2,05", cekme:"60", krimp_gen:"3,05", izok:"", not:""},
  {kesit:"DOPPEL: 0,75 mm+14 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,30", cekme:"85", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 1,00 mm+2x18 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,05", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 18+16 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,15", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 1,00 mm+14 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"108", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 18+14 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,30", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 5x20 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,25", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10023347", kalip:"44-259", krimp:"2,25", cekme:"108", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 18+12 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+14 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,35", cekme:"135", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+16 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,20", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+2,50 mm", kontak:"10023347", kalip:"44-259", krimp:"2,35", cekme:"150", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+18+14 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+12 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"60", krimp_gen:"4,30", izok:"", not:""},
  {kesit:"DOPPEL: 4x18 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,35", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+2,50 mm", kontak:"10023347", kalip:"135", krimp:"2,35", cekme:"150", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+4,00 mm", kontak:"10023347", kalip:"44-259", krimp:"2,55", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x18+16 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,45", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18+14+16 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x18+16 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,40", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 12+18 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"90", krimp_gen:"4,15", izok:"", not:""},
  {kesit:"DOPPEL: 3x18+14 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,50", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+4,00 mm", kontak:"10023347", kalip:"44-135-259", krimp:"2,80", cekme:"150", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+12 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,60", cekme:"90", krimp_gen:"4,25", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+16+14 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14+12 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,75", cekme:"200", krimp_gen:"4,20", izok:"", not:""},
  {kesit:"DOPPEL: 6x18 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x18+12 AWG", kontak:"10023347", kalip:"44-259", krimp:"2,75", cekme:"90", krimp_gen:"4,25", izok:"", not:""},
  {kesit:"DOPPEL: 18+16 AWG", kontak:"10023353", kalip:"182-178", krimp:"1,90", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 5x20+14 AWG", kontak:"10023355", kalip:"122", krimp:"2,70", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x20+14 AWG", kontak:"10023355", kalip:"122", krimp:"2,60", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x1,50 mm", kontak:"10023355", kalip:"122", krimp:"2,60", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x20+24+14 AWG", kontak:"10023355", kalip:"122", krimp:"2,80", cekme:"28", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+12 AWG", kontak:"10023355", kalip:"122", krimp:"2,95", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+12 AWG", kontak:"10023355", kalip:"122", krimp:"3,05", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2,50+2x1,50 mm", kontak:"10023355", kalip:"122", krimp:"3,00", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x14+20 AWG", kontak:"10023355", kalip:"122", krimp:"3,00", cekme:"60", krimp_gen:"4,70", izok:"", not:""},
  {kesit:"DOPPEL: 4x1,50", kontak:"10023355", kalip:"122", krimp:"3,00", cekme:"150", krimp_gen:"5,00", izok:"", not:""},
  {kesit:"DOPPEL: 14+12 AWG", kontak:"10023355", kalip:"122", krimp:"3,05", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x1,50", kontak:"10023355", kalip:"122", krimp:"3,10", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x20+2x14 AWG", kontak:"10023355", kalip:"122", krimp:"3,10", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+10 AWG", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+12 AWG", kontak:"10023355", kalip:"122", krimp:"3,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+24+12 AWG", kontak:"10023355", kalip:"122", krimp:"3,15", cekme:"24", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+2x14 AWG", kontak:"10023355", kalip:"122", krimp:"3,15", cekme:"60", krimp_gen:"4,70", izok:"", not:""},
  {kesit:"DOPPEL: 2,50+4,00 mm", kontak:"10023355", kalip:"122", krimp:"3,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x2,50+1,00 mm", kontak:"10023355", kalip:"122", krimp:"3,20", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+4,00 mm", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2,50+6,00 mm", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"230", krimp_gen:"5,00", izok:"", not:""},
  {kesit:"DOPPEL: 20+ 10 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+ 11 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+24+14+12 AWG", kontak:"10023355", kalip:"122", krimp:"3,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x2,50+1,00+0,75 mm", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x20 + 2x14 AWG", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+10 AWG", kontak:"10023355", kalip:"122", krimp:"3,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 10+16 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+14+12 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x14+16 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x20+2x14AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 5x20+ 10 AWG", kontak:"10023355", kalip:"122", krimp:"3,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+2x12 AWG", kontak:"10023355", kalip:"122", krimp:"3,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 5x20+ 10 AWG", kontak:"10023355", kalip:"122", krimp:"3,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x14+16 AWG", kontak:"10023355", kalip:"122", krimp:"3,80", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 10+12 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"275", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+14+10 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+14+10 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x12+16 AWG", kontak:"10023355", kalip:"122", krimp:"3,90", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+8 AWG", kontak:"10023355", kalip:"122", krimp:"3,95", cekme:"60", krimp_gen:"3,95", izok:"", not:""},
  {kesit:"DOPPEL: 16+8 AWG", kontak:"10023355", kalip:"122", krimp:"4,00", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 20+8 AWG", kontak:"10023355", kalip:"122", krimp:"4,10", cekme:"60", krimp_gen:"4,85", izok:"", not:""},
  {kesit:"DOPPEL: 2x12+14+16 AWG", kontak:"10023355", kalip:"122", krimp:"4,10", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x14+16+12 AWG", kontak:"10023355", kalip:"122", krimp:"4,10", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x12+14+16 AWG", kontak:"10023355", kalip:"122", krimp:"4,15", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x20+8 AWG", kontak:"10023355", kalip:"122", krimp:"4,15", cekme:"60", krimp_gen:"4,85", izok:"", not:""},
  {kesit:"DOPPEL: 3x20+8 AWG", kontak:"10023355", kalip:"122", krimp:"4,20", cekme:"60", krimp_gen:"4,90", izok:"", not:""},
  {kesit:"DOPPEL: 4x2,50 mm", kontak:"10023355", kalip:"122", krimp:"4,20", cekme:"230", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 4x18+16 AWG", kontak:"10023364", kalip:"74", krimp:"3,05", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,45mm Direnç+0,50 mm Kablo", kontak:"10024270", kalip:"Ek Terminal 242", krimp:"1,15", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: Direnç+0,50 mm Kablo", kontak:"10024270", kalip:"Ek Terminal 242", krimp:"1,30", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x0,80 Direnç+0,50 mm Kablo", kontak:"10024270", kalip:"Ek Terminal 242", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x0,35", kontak:"10024274", kalip:"42-43", krimp:"1,65", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18+20 AWG", kontak:"10024299", kalip:"137", krimp:"1,55", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024299", kalip:"137", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 22+18 AWG", kontak:"10024306", kalip:"42-43", krimp:"1,55", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x0,35 mm", kontak:"10024306", kalip:"42-43", krimp:"1,60", cekme:"45", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"DOPPEL: 3x0,35 mm", kontak:"10024326", kalip:"162-320", krimp:"1,65", cekme:"45", krimp_gen:"2,45", izok:"", not:""},
  {kesit:"DOPPEL: 0,35+0,75 mm", kontak:"10024326", kalip:"162-320", krimp:"1,60", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,50+0,75 mm", kontak:"10024326", kalip:"162-320", krimp:"1,75", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024363", kalip:"14", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10024397", kalip:"84", krimp:"2,90", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10024397", kalip:"84", krimp:"2,95", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14+12 AWG", kontak:"10024397", kalip:"84", krimp:"3,40", cekme:"200", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024399", kalip:"77", krimp:"1,90", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10024400", kalip:"77", krimp:"2,50", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 +14 AWG", kontak:"10024400", kalip:"77", krimp:"2,60", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 22+18 AWG", kontak:"10024402", kalip:"85-207", krimp:"1,70", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10024402", kalip:"85-207", krimp:"2,00", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 +16 AWG", kontak:"10024402", kalip:"85-207", krimp:"1,95", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024405", kalip:"85", krimp:"2,00", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024405", kalip:"85", krimp:"2,05", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 +16 AWG", kontak:"10024407", kalip:"73-194", krimp:"2,05", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024419", kalip:"76", krimp:"1,65", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 +16 AWG", kontak:"10024419", kalip:"76", krimp:"1,80", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 AWG + 0.75mm", kontak:"10024422", kalip:"73-194", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024422", kalip:"73-194", krimp:"1,75", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16 AWG + 0.75mm", kontak:"10024422", kalip:"73-194", krimp:"1,80", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 +16 AWG", kontak:"10024422", kalip:"73-194", krimp:"1,85", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75mm+22AWG", kontak:"10024422", kalip:"194", krimp:"1,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10024422", kalip:"73-194", krimp:"2,00", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10024423", kalip:"44", krimp:"2,00", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14 AWG +0,75mm", kontak:"10024423", kalip:"44", krimp:"2,15", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18 AWG +1,00mm", kontak:"10024423", kalip:"44", krimp:"2,15", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+2,50 mm", kontak:"10024423", kalip:"44", krimp:"2,20", cekme:"150", krimp_gen:"4,10", izok:"", not:""},
  {kesit:"DOPPEL: 14 AWG +1,00mm", kontak:"10024423", kalip:"44", krimp:"2,20", cekme:"108", krimp_gen:"4,05", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10024423", kalip:"44", krimp:"2,25", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 +14 AWG", kontak:"10024423", kalip:"44", krimp:"2,25", cekme:"90", krimp_gen:"4,05", izok:"", not:""},
  {kesit:"DOPPEL: 16 +14 AWG", kontak:"10024423", kalip:"44", krimp:"2,40", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 22 +18 AWG", kontak:"10024424", kalip:"42-43", krimp:"1,80", cekme:"40", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+1,50 mm", kontak:"10024429", kalip:"83", krimp:"2,55", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 14+18 AWG", kontak:"10024429", kalip:"83", krimp:"2,70", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+1,00 mm", kontak:"10024433", kalip:"137", krimp:"1,85", cekme:"85", krimp_gen:"3,10", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10024435", kalip:"77", krimp:"2,10", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16 +14 AWG", kontak:"10024435", kalip:"77", krimp:"2,20", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,56+20 AWG", kontak:"10024440", kalip:"114", krimp:"1,40", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,50+20 AWG", kontak:"10024445", kalip:"108", krimp:"1,50", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+18 AWG", kontak:"10024455", kalip:"70", krimp:"2,35", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 2x18+12 AWG", kontak:"10025038", kalip:"71", krimp:"2,75", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 3x18+12 AWG", kontak:"10025038", kalip:"71", krimp:"2,90", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,35+0,50 mm", kontak:"10025157", kalip:"185", krimp:"1,65", cekme:"45", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,35+0,75 mm", kontak:"10025157", kalip:"184 185-304", krimp:"1,80", cekme:"60", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+14 AWG", kontak:"10025340", kalip:"77", krimp:"2,20", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10025340", kalip:"77", krimp:"2,25", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+14 AWG", kontak:"10025340", kalip:"77", krimp:"2,30", cekme:"108", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,50+2,50 mm", kontak:"10025340", kalip:"77", krimp:"2,35", cekme:"150", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 16+14 AWG", kontak:"10025340", kalip:"77", krimp:"2,40", cekme:"135", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 0,50+0,75 mm", kontak:"10025512", kalip:"112", krimp:"2,00", cekme:"60", krimp_gen:"3,20", izok:"", not:""},
  {kesit:"DOPPEL: 0,75+2,50 mm", kontak:"10025515", kalip:"44", krimp:"2,25", cekme:"85", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 18 +14 AWG", kontak:"10025515", kalip:"44", krimp:"2,30", cekme:"90", krimp_gen:"", izok:"", not:""},
  {kesit:"DOPPEL: 1,00+2,50 mm", kontak:"10025845", kalip:"77", krimp:"2,30", cekme:"108", krimp_gen:"", izok:"", not:""},
];

// Build unique kontak list
const allKontaklar = [...new Set(DATA.map(d => d.kontak))].sort();
let selectedKontak = null;
let dropdownOpen = false;

document.getElementById('totalFooter').textContent = DATA.length;

// ── KONTAK INPUT ──
function onKontakInput() {
  const val = document.getElementById('kontakInput').value.trim();
  document.getElementById('clearKontak').style.display = val ? 'block' : 'none';
  showDropdown(val);
  selectedKontak = null;
  resetKesit();
  showHint();
}

function onKontakFocus() {
  const val = document.getElementById('kontakInput').value.trim();
  showDropdown(val);
}

function showDropdown(query) {
  const dd = document.getElementById('kontakDropdown');
  const filtered = query
    ? allKontaklar.filter(k => k.includes(query))
    : allKontaklar.slice(0, 50);

  if (filtered.length === 0) {
    dd.innerHTML = '<div class="dropdown-no-result">Kontak bulunamadı</div>';
  } else {
    dd.innerHTML = filtered.map(k => {
      const count = DATA.filter(d => d.kontak === k).length;
      const kesitCount = [...new Set(DATA.filter(d => d.kontak === k).map(d => d.kesit))].length;
      const doppelCount = DATA.filter(d => d.kontak === k && d.kesit.startsWith('DOPPEL:')).length;
      const normalCount = kesitCount - doppelCount;
      const badge = doppelCount > 0
        ? `<span class="count-badge">${normalCount} kesit</span> <span class="count-badge" style="background:rgba(251,146,60,0.15);color:#fb923c">+${doppelCount} doppel</span>`
        : `<span class="count-badge">${kesitCount} kesit</span>`;
      return `<div class="dropdown-item" onclick="selectKontak('${k}')">${k} ${badge}</div>`;
    }).join('');
  }
  dd.classList.add('open');
  dropdownOpen = true;
}

function selectKontak(k) {
  selectedKontak = k;
  document.getElementById('kontakInput').value = k;
  document.getElementById('clearKontak').style.display = 'block';
  document.getElementById('kontakDropdown').classList.remove('open');
  dropdownOpen = false;
  populateKesit(k);
}

function clearKontak() {
  document.getElementById('kontakInput').value = '';
  document.getElementById('clearKontak').style.display = 'none';
  selectedKontak = null;
  resetKesit();
  showHint();
}

// Close dropdown on outside click
document.addEventListener('click', e => {
  if (!e.target.closest('.kontak-input-wrap')) {
    document.getElementById('kontakDropdown').classList.remove('open');
  }
});

// ── KESİT SEÇ ──
function populateKesit(kontak) {
  const rows = DATA.filter(d => d.kontak === kontak);
  const kesitler = [...new Set(rows.map(d => d.kesit))];
  const sel = document.getElementById('kesitSelect');
  sel.innerHTML = '<option value="">Kesit seçin...</option>';

  const normal = kesitler.filter(k => !k.startsWith('DOPPEL:'));
  const doppel = kesitler.filter(k => k.startsWith('DOPPEL:'));

  if (normal.length > 0) {
    const grp = document.createElement('optgroup');
    grp.label = '── Tek Kesit ──';
    normal.forEach(k => {
      const opt = document.createElement('option');
      opt.value = k;
      opt.textContent = k;
      grp.appendChild(opt);
    });
    sel.appendChild(grp);
  }

  if (doppel.length > 0) {
    const grp = document.createElement('optgroup');
    grp.label = '── DOPPEL (Karma) ──';
    doppel.forEach(k => {
      const opt = document.createElement('option');
      opt.value = k;
      opt.textContent = k.replace('DOPPEL: ', '');
      grp.appendChild(opt);
    });
    sel.appendChild(grp);
  }

  sel.disabled = false;

  // Auto-select if only 1 kesit
  if (kesitler.length === 1) {
    sel.value = kesitler[0];
    onKesitChange();
  } else {
    showHint();
  }
}

function resetKesit() {
  const sel = document.getElementById('kesitSelect');
  sel.innerHTML = '<option value="">Kesit seçin...</option>';
  sel.disabled = true;
}

function onKesitChange() {
  const kesit = document.getElementById('kesitSelect').value;
  if (!selectedKontak || !kesit) { showHint(); return; }
  const rows = DATA.filter(d => d.kontak === selectedKontak && d.kesit === kesit);
  showResult(rows, selectedKontak, kesit);
}

// ── RESULT RENDER ──
function showHint() {
  document.getElementById('hintState').style.display = 'block';
  document.getElementById('resultPanel').style.display = 'none';
}

function showResult(rows, kontak, kesit) {
  document.getElementById('hintState').style.display = 'none';
  const panel = document.getElementById('resultPanel');
  panel.style.display = 'block';

  const kesitLabel = kesit.startsWith('DOPPEL: ') ? '🔀 DOPPEL: ' + kesit.replace('DOPPEL: ','') : kesit;
  document.getElementById('resultLabel').textContent =
    `${kontak}  ·  ${kesitLabel}  —  ${rows.length} kayıt`;

  const content = document.getElementById('resultContent');

  if (rows.length === 0) {
    content.innerHTML = `<div class="no-result-state"><div class="no-icon">⚠️</div><p>Bu kombinasyon için kayıt bulunamadı.</p></div>`;
    return;
  }

  if (rows.length === 1) {
    const r = rows[0];
    content.innerHTML = `
      <div class="result-single">
        <div class="result-main">
          <div class="result-cell">
            <div class="result-cell-label">Krimp Yüksekliği</div>
            <div class="result-cell-value krimp">${r.krimp} mm</div>
          </div>
          <div class="result-cell">
            <div class="result-cell-label">Krimp Genişliği</div>
            <div class="result-cell-value" style="font-size:1.1rem;font-weight:700;color:#38bdf8">${r.krimp_gen ? r.krimp_gen + ' mm' : '—'}</div>
          </div>
          <div class="result-cell">
            <div class="result-cell-label">İzokrimp Yüksekliği</div>
            <div class="result-cell-value izokrimp">${r.izok ? r.izok + ' mm' : '—'}</div>
          </div>
          <div class="result-cell">
            <div class="result-cell-label">Kalıp No</div>
            <div class="result-cell-value kalip">${r.kalip}</div>
          </div>
          <div class="result-cell">
            <div class="result-cell-label">Çekme Kuvveti Min. (N)</div>
            <div class="result-cell-value cekme">${r.cekme ? r.cekme + ' N' : '—'}</div>
          </div>

          <div class="result-cell">
            <div class="result-cell-label">Not</div>
            <div class="result-cell-value" style="font-size:0.85rem;color:#fca5a5;font-weight:500">${r.not || '—'}</div>
          </div>
        </div>
        <div class="tolerance-hint">
          ${kesit.startsWith('DOPPEL: ') ? '🔀 DOPPEL / Karma Kesit &nbsp;·&nbsp; ' : ''}⚡ Tolerans: ± 0,05 mm &nbsp;·&nbsp; Çekme Kuvveti: DIN/EN 60352-2
        </div>
      </div>
      ${r.not ? `<div class="result-note">⚠️ <span>${r.not}</span></div>` : ''}
    `;
  } else {
    // Multiple rows (same kontak+kesit, different kalip)
    const rowsHtml = rows.map(r => `
      <div class="result-multi-row">
        <span class="val-kalip">${r.kalip}</span>
        <span class="val-krimp">${r.krimp} mm</span>
        <span class="val-izok">${r.izok ? r.izok + ' mm' : '<span class="val-empty">—</span>'}</span>
        <span class="val-cekme">${r.cekme ? r.cekme + ' N' : '<span class=\"val-empty\">—</span>'}</span>

        <span style="font-size:0.72rem;color:#fca5a5">${r.not || ''}</span>
      </div>
    `).join('');

    content.innerHTML = `
      <div class="result-multi">
        <div class="result-multi-header">
          <span>Kalıp No</span>
          <span>Krimp Yük.</span>
          <span>Krimp Gen.</span>
          <span>İzokrimp Yük.</span>
          <span>Çekme Min. (N)</span>

          <span>Not</span>
        </div>
        ${rowsHtml}
      </div>
    `;
  }
}

// ── RESET ──
function resetAll() {
  document.getElementById('kontakInput').value = '';
  document.getElementById('clearKontak').style.display = 'none';
  selectedKontak = null;
  resetKesit();
  showHint();
}
</script>
</body>
</html>
