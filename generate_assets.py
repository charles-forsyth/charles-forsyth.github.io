import sqlite3
import os

DB_PATH = '/home/chuck/Projects/digital-me/digital_me.db'
OUTPUT_DIR = '/home/chuck/Projects/charles-forsyth.github.io/assets'

def get_icon_for_type(asset_type):
    mapping = {
        'Vehicle': 'fas fa-car',
        'Boat': 'fas fa-ship',
        'Property': 'fas fa-home',
        'Computer': 'fas fa-laptop',
        'Laptop': 'fas fa-laptop',
        'Server': 'fas fa-server',
        'Application Server': 'fas fa-server',
        'Network Gear': 'fas fa-network-wired',
        'Radio': 'fas fa-broadcast-tower',
        'Smart Home': 'fas fa-home',
        'Security': 'fas fa-shield-alt',
        'Smart Speaker': 'fas fa-speaker',
        'Kayak': 'fas fa-water',
        'Personal Device': 'fas fa-mobile-alt',
        'Workstation': 'fas fa-desktop'
    }
    return mapping.get(asset_type, 'fas fa-box')

def generate_pages():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM assets ORDER BY asset_type, asset_name")
    assets = [dict(row) for row in cursor.fetchall()]

    css_content = """
.asset-hero {
  background: linear-gradient(135deg, rgba(10, 25, 47, 0.9) 0%, rgba(2, 12, 27, 0.9) 100%);
  padding: 4rem 0;
}
.asset-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}
.asset-card {
  background: var(--bg-primary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 1.5rem;
  transition: transform 0.3s ease, border-color 0.3s ease;
  display: flex;
  flex-direction: column;
}
.asset-card:hover {
  transform: translateY(-5px);
  border-color: var(--accent-color);
}
.asset-card h4 {
  margin-top: 0;
  color: var(--text-primary);
  font-size: 1.25rem;
}
.asset-card p {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-bottom: 1rem;
  flex-grow: 1;
}
.spec-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}
.spec-item {
  background: var(--bg-primary);
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  font-size: 0.95rem;
  color: var(--text-secondary);
}
.spec-item strong {
  color: var(--text-primary);
  display: block;
  margin-bottom: 0.25rem;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.log-timeline {
  max-width: 800px;
  margin: 3rem auto 0;
  position: relative;
}
.log-timeline::before {
  content: '';
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  height: 100%;
  background-color: var(--accent-color);
  opacity: 0.3;
}
.log-entry {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  position: relative;
}
.log-entry::after {
  content: '';
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background-color: var(--accent-color);
  border: 4px solid var(--bg-secondary);
}
.log-date {
  width: 45%;
  text-align: right;
  padding-right: 2rem;
  font-family: var(--font-mono);
  color: var(--accent-color);
  font-weight: bold;
}
.log-content {
  width: 45%;
  padding-left: 2rem;
  background: var(--bg-primary);
  padding: 1.5rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
}
.log-entry:nth-child(even) {
  flex-direction: row-reverse;
}
.log-entry:nth-child(even) .log-date {
  text-align: left;
  padding-left: 2rem;
  padding-right: 0;
}
.log-entry:nth-child(even) .log-content {
  padding-right: 2rem;
  padding-left: 1.5rem;
}
.log-content h4 {
  margin: 0 0 0.5rem 0;
  color: var(--text-primary);
}
.log-content p {
  margin: 0;
  font-size: 0.9rem;
  color: var(--text-secondary);
}
@media (max-width: 768px) {
  .log-timeline::before { left: 20px; }
  .log-entry::after { left: 20px; }
  .log-entry, .log-entry:nth-child(even) { flex-direction: column; align-items: flex-start; padding-left: 45px; }
  .log-date, .log-entry:nth-child(even) .log-date { width: 100%; text-align: left; padding: 0 0 0.5rem 0; }
  .log-content, .log-entry:nth-child(even) .log-content { width: 100%; padding: 1rem; }
}
"""
    with open(os.path.join(OUTPUT_DIR, 'assets.css'), 'w') as f:
        f.write(css_content)

    index_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Asset Fleet | Charles Forsyth</title>
    <link rel="stylesheet" href="../style.css" />
    <link rel="stylesheet" href="assets.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
  </head>
  <body>
    <header class="hero asset-hero">
      <div class="container">
        <div class="hero-content">
          <h1>Asset Fleet Directory</h1>
          <p>Digital Twin telemetry and historical logging for my physical and digital assets.</p>
          <div class="cta-buttons">
            <a href="../index.html" class="btn btn-secondary"><i class="fas fa-arrow-left"></i> Back to Main Site</a>
          </div>
        </div>
      </div>
    </header>
    <main>
      <section class="section-light">
        <div class="container">
"""
    
    assets_by_type = {}
    for a in assets:
        t = a.get('asset_type', 'Other')
        if t not in assets_by_type:
            assets_by_type[t] = []
        assets_by_type[t].append(a)

    for atype, items in sorted(assets_by_type.items()):
        icon = get_icon_for_type(atype)
        index_html += f"<h3><i class='{icon}'></i> {atype}s</h3>\n<div class='asset-grid'>\n"
        for item in items:
            if item['asset_id'] == 1:
                link = "../truck/index.html"
            elif item['asset_id'] == 5:
                link = "../boat/index.html"
            else:
                link = f"asset_{item['asset_id']}.html"
            
            index_html += f"""
            <div class="asset-card">
              <h4>{item['asset_name']}</h4>
              <p><strong>Status:</strong> {item.get('status', 'Unknown')} <br>
                 <strong>Location:</strong> {item.get('primary_location', 'N/A')}</p>
              <a href="{link}" class="btn-link">View Telemetry <i class="fas fa-arrow-right"></i></a>
            </div>
            """
        index_html += "</div><br><br>\n"

    index_html += """
        </div>
      </section>
    </main>
    <footer class="section-dark text-center">
      <div class="container"><p class="footer-note">&copy; 2026 Charles Forsyth. Auto-generated via Digital-Me.</p></div>
    </footer>
  </body>
</html>
"""
    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as f:
        f.write(index_html)

    # SENSITIVE DATA FILTERING
    SENSITIVE_KEYS = [
        'serial_number_or_vin', 'vin', 'hin', 'registration_number', 'registration_expires',
        'insurance_provider', 'insurance_policy_#', 'primary_user', 'purchase_price', 
        'current_value', 'permit_valid', 'pa_launch_permit_tan', 'notes_path'
    ]

    def is_safe(key):
        return key.lower().replace(' ', '_') not in SENSITIVE_KEYS

    for asset in assets:
        if asset['asset_id'] in [1, 5]:
            continue
        
        asset_id = asset['asset_id']
        cursor.execute("SELECT attribute_name, attribute_value FROM asset_attributes WHERE asset_id = ?", (asset_id,))
        attrs = cursor.fetchall()
        
        safe_attrs = [attr for attr in attrs if is_safe(attr['attribute_name'])]
        
        cursor.execute("SELECT service_date, service_description FROM maintenance_logs WHERE asset_id = ? ORDER BY service_date DESC", (asset_id,))
        logs = cursor.fetchall()

        cursor.execute("SELECT description, priority FROM tasks WHERE asset_id = ? AND status != 'complete' ORDER BY priority", (asset_id,))
        tasks = cursor.fetchall()

        page_html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{asset['asset_name']} | Charles Forsyth</title>
    <link rel="stylesheet" href="../style.css" />
    <link rel="stylesheet" href="assets.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
  </head>
  <body>
    <header class="hero asset-hero">
      <div class="container">
        <div class="hero-content">
          <h1>{asset['asset_name']}</h1>
          <h2>{asset.get('asset_type', 'Asset')}</h2>
          <div class="cta-buttons">
            <a href="index.html" class="btn btn-secondary"><i class="fas fa-arrow-left"></i> Back to Fleet</a>
          </div>
        </div>
      </div>
    </header>

    <main>
      <section class="section-light">
        <div class="container">
          <div class="about-grid">
            <div class="about-text">
              <h3><i class="fas fa-info-circle"></i> Core Telemetry</h3>
              <div class="spec-grid">
                <div class="spec-item"><strong>Status:</strong> {asset.get('status', 'N/A')}</div>
                <div class="spec-item"><strong>Location:</strong> {asset.get('primary_location', 'N/A')}</div>
                <div class="spec-item"><strong>Manufacturer:</strong> {asset.get('manufacturer', 'N/A')}</div>
                <div class="spec-item"><strong>Model:</strong> {asset.get('model', 'N/A')}</div>
              </div>
            </div>"""

        if safe_attrs or tasks:
            page_html += "\n            <div class=\"about-text\">\n"
            if safe_attrs:
                page_html += "              <h3><i class=\"fas fa-cogs\"></i> Extended Attributes</h3>\n              <div class=\"spec-grid\">\n"
                for attr in safe_attrs:
                    page_html += f"                <div class=\"spec-item\"><strong>{attr['attribute_name']}:</strong> {attr['attribute_value']}</div>\n"
                page_html += "              </div><br>\n"
            
            if tasks:
                page_html += "              <h3><i class=\"fas fa-tools\"></i> Pending Actions</h3>\n              <div class=\"spec-grid\">\n"
                for t in tasks:
                    page_html += f"                <div class=\"spec-item\"><strong>Priority {t['priority']}:</strong> {t['description']}</div>\n"
                page_html += "              </div>\n"
            page_html += "            </div>\n"

        page_html += """          </div>
        </div>
      </section>"""

        if logs:
            page_html += """
      <section class="section-dark">
        <div class="container">
          <h3 class="text-center"><i class="fas fa-clipboard-list"></i> Activity Log</h3>
          <div class="log-timeline">"""
            for log in logs:
                page_html += f"""
            <div class="log-entry">
              <div class="log-date">{log['service_date']}</div>
              <div class="log-content">
                <p>{log['service_description']}</p>
              </div>
            </div>"""
            page_html += """
          </div>
        </div>
      </section>"""

        page_html += """
    </main>
    <footer class="section-dark text-center">
      <div class="container"><p class="footer-note">&copy; 2026 Charles Forsyth. Data dynamically sourced from Digital-Me.</p></div>
    </footer>
  </body>
</html>"""
        
        with open(os.path.join(OUTPUT_DIR, f"asset_{asset_id}.html"), 'w') as f:
            f.write(page_html)

    conn.close()
    print("Asset pages generated successfully!")

if __name__ == "__main__":
    generate_pages()
