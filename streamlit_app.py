import streamlit as st
import os
import glob
import textwrap
import base64
import mimetypes
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Nexus Conformité | CQC Evidence & Compliance Support",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# BUSINESS DETAILS
# =========================================================
BUSINESS_NAME = "Nexus Conformité"
EMAIL = "nexusconformite@proton.me"
FACEBOOK_URL = "https://www.facebook.com/nexusconformite"
PAYHIP_URL = "https://payhip.com/NexusConformite"
LINKEDIN_URL = "https://www.linkedin.com/company/nexus-conformit%C3%A9/"
LINKEDIN_NAME = "Nexus Conformité"

# Payhip product code: 9OUm6 with capital O, not zero.
CQC_REVIEW_CHECKOUT_URL = "https://payhip.com/buy?link=9OUm6"

# =========================================================
# META PIXEL
# =========================================================
META_PIXEL_CODE = """
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){
if(f.fbq)return;
n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;
n.push=n;
n.loaded=!0;
n.version='2.0';
n.queue=[];
t=b.createElement(e);
t.async=!0;
t.src=v;
s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)
}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');

fbq('init', '1010121488430688');
fbq('track', 'PageView');
</script>
<noscript>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1010121488430688&ev=PageView&noscript=1"/>
</noscript>
<!-- End Meta Pixel Code -->
"""
components.html(META_PIXEL_CODE, height=1, scrolling=False)

# =========================================================
# SAFE HTML RENDERER
# =========================================================
def html(source: str):
    clean_source = textwrap.dedent(source).strip()
    st.markdown(clean_source, unsafe_allow_html=True)

# =========================================================
# LOGO FINDER
# =========================================================
def find_logo():
    preferred_names = [
        ".Nexus_Conformite_logo_transparent.png",
        "Nexus_Conformite_logo_transparent.png",
        "Nexus Conformite logo transparent.png",
        "Nexus_Conformité_logo_transparent.png",
        "logo.png",
        "Logo.png",
    ]

    for name in preferred_names:
        if os.path.exists(name):
            return name

    for pattern in ["*.png", "*.jpg", "*.jpeg", "*.webp", ".*.png", ".*.jpg", ".*.jpeg", ".*.webp"]:
        for file in glob.glob(pattern):
            clean = file.lower().replace(" ", "").replace("_", "").replace("-", "").replace(".", "")
            if "nexus" in clean or "conformite" in clean or "logo" in clean:
                return file

    return None

LOGO_PATH = find_logo()

def image_to_data_uri(path):
    if not path or not os.path.exists(path):
        return ""

    mime_type, _ = mimetypes.guess_type(path)
    if not mime_type:
        mime_type = "image/png"

    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"

LOGO_DATA_URI = image_to_data_uri(LOGO_PATH)

# =========================================================
# CSS
# =========================================================
html("""
<style>
:root {
    --navy: #061A35;
    --navy2: #0B2545;
    --gold: #C8A96A;
    --green: #0F766E;
    --soft: #F6F7FA;
    --cream: #FAF7F0;
    --white: #FFFFFF;
    --text: #172033;
    --muted: #6B7280;
    --line: #E5E7EB;
}

* { box-sizing: border-box; }

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}

html, body, .stApp {
    overflow-x: hidden !important;
    max-width: 100vw !important;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(200,169,106,0.10), transparent 26%),
        linear-gradient(180deg, #FFFFFF 0%, #F6F7FA 54%, #FAF7F0 100%);
    color: var(--text);
}

.block-container {
    max-width: 1160px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
    overflow-x: hidden !important;
}

[data-testid="stImage"] img {
    max-width: 118px !important;
    width: 118px !important;
    height: auto !important;
}

h1, h2, h3 {
    color: var(--navy);
    letter-spacing: -0.04em;
}

p, li {
    font-size: 18px;
    line-height: 1.65;
    color: var(--text);
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 24px;
    padding: 10px 0 24px 0;
    max-width: 100%;
    overflow: hidden;
}

.brand-title {
    font-size: 26px;
    font-weight: 800;
    color: var(--navy);
    margin: 0;
    line-height: 1.15;
    overflow-wrap: break-word;
}

.brand-subtitle {
    color: var(--muted);
    font-size: 15px;
    margin-top: 4px;
    line-height: 1.45;
    max-width: 620px;
}

.nav-pills {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: flex-end;
    max-width: 100%;
}

.nav-pills a {
    padding: 10px 14px;
    border-radius: 999px;
    background: white;
    border: 1px solid var(--line);
    color: var(--navy) !important;
    text-decoration: none;
    font-size: 14px;
    font-weight: 700;
    white-space: nowrap;
}

.hero {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle at 85% 12%, rgba(200,169,106,0.28), transparent 28%),
        linear-gradient(135deg, #061A35 0%, #0B2545 50%, #0F766E 100%);
    border-radius: 34px;
    padding: 68px 56px;
    margin: 8px 0 26px 0;
    box-shadow: 0 26px 70px rgba(6,26,53,0.22);
    max-width: 100%;
}

.hero h1 {
    color: white;
    font-size: clamp(36px, 5vw, 60px);
    line-height: 1.02;
    max-width: 900px;
    margin: 0 0 18px 0;
}

.hero p {
    color: #EAF0F7;
    font-size: clamp(18px, 2.2vw, 22px);
    max-width: 860px;
}

.eyebrow {
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 14px;
}

.cta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 26px;
}

.btn-primary,
.btn-secondary,
.btn-light,
.btn-dark {
    display: inline-block;
    padding: 14px 20px;
    border-radius: 999px;
    text-decoration: none !important;
    font-weight: 800;
    font-size: 15px;
    cursor: pointer;
    text-align: center;
}

.btn-primary {
    background: var(--gold);
    color: var(--navy) !important;
}

.btn-secondary {
    background: white;
    color: var(--navy) !important;
}

.btn-light {
    background: rgba(255,255,255,0.12);
    color: white !important;
    border: 1px solid rgba(255,255,255,0.25);
}

.btn-dark {
    background: var(--navy);
    color: white !important;
    width: 100%;
}

.section {
    margin: 34px 0;
}

.section h2 {
    font-size: clamp(31px, 4vw, 40px);
    margin-bottom: 8px;
}

.section-intro {
    max-width: 850px;
    color: var(--muted);
    font-size: 19px;
}

.problem-strip {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 14px 38px rgba(15,23,42,0.05);
    overflow: hidden;
}

.problem-strip h2 {
    font-size: clamp(31px, 4vw, 40px);
    line-height: 1.18;
}

.gold-line {
    width: 78px;
    height: 4px;
    border-radius: 999px;
    background: var(--gold);
    margin: 12px 0 18px 0;
}

.review-cover-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 12px;
    margin-top: 18px;
}

.review-cover-item {
    display: flex;
    gap: 12px;
    align-items: center;
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 14px;
    min-height: 78px;
    box-shadow: 0 10px 28px rgba(15,23,42,0.04);
}

.review-cover-icon {
    width: 38px;
    height: 38px;
    border-radius: 13px;
    border: 1px solid rgba(200,169,106,0.55);
    color: var(--gold);
    display: grid;
    place-items: center;
    font-size: 19px;
    font-weight: 900;
    flex: 0 0 38px;
}

.review-cover-item p {
    margin: 0;
    color: var(--navy);
    font-size: 16px;
    font-weight: 760;
    line-height: 1.22;
}

.review-cover-note {
    background: #FFFFFF;
    border-left: 5px solid var(--gold);
    padding: 16px 20px;
    margin-top: 16px;
    border-radius: 18px;
    color: var(--navy);
    font-size: 18px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 26px !important;
    box-shadow: 0 16px 42px rgba(15,23,42,0.06);
    background: rgba(255,255,255,0.98);
}

div[data-testid="stRadio"] label {
    color: var(--navy) !important;
    font-weight: 800 !important;
}

.stRadio [role="radiogroup"] {
    gap: 8px;
}

.stRadio [role="radio"] {
    border: 1px solid var(--line);
    border-radius: 999px;
    padding: 7px 10px;
    background: #FFFFFF;
}

[data-testid="stMarkdownContainer"] table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}

[data-testid="stMarkdownContainer"] th {
    background: #061A35;
    color: white;
    font-size: 12px;
    padding: 8px;
}

[data-testid="stMarkdownContainer"] td {
    border: 1px solid #E5E7EB;
    padding: 8px;
    font-size: 12px;
}

.notice {
    background: #FFF8E8;
    border: 1px solid #F0DB9B;
    border-left: 6px solid var(--gold);
    padding: 22px;
    border-radius: 22px;
    margin: 18px 0;
}

.green-notice {
    background: #EAF7F4;
    border: 1px solid #BFE4DC;
    border-left: 6px solid var(--green);
    padding: 22px;
    border-radius: 22px;
    margin: 18px 0;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
}

.step {
    background: white;
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 24px;
    overflow: hidden;
}

.footer {
    background:
        radial-gradient(circle at top right, rgba(200,169,106,0.20), transparent 30%),
        linear-gradient(135deg, #061A35 0%, #0B2545 58%, #0F766E 100%);
    color: white;
    border-radius: 28px;
    padding: 38px 34px;
    margin-top: 34px;
    box-shadow: 0 22px 60px rgba(6,26,53,0.20);
    overflow: hidden;
}

.footer h3 {
    color: white;
    font-size: 30px;
    margin-bottom: 8px;
}

.footer p {
    color: #DDE6F2;
    font-size: 16px;
}

.footer-cta {
    font-size: 20px;
    color: #FFFFFF !important;
    max-width: 760px;
    margin-bottom: 22px;
}

.footer-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin: 24px 0 20px 0;
}

.footer-icon-row {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 20px;
    align-items: center;
}

.icon-link {
    width: 54px;
    height: 54px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    background: rgba(255,255,255,0.10);
    color: white !important;
    border: 1px solid rgba(255,255,255,0.24);
    text-decoration: none !important;
    font-weight: 900;
    font-size: 17px;
    transition: 0.2s ease;
    line-height: 1;
}

.icon-link:hover {
    background: var(--gold);
    color: var(--navy) !important;
    border-color: var(--gold);
}

.footer-small {
    color: #C9D4E5 !important;
    font-size: 14px !important;
    margin-top: 22px;
}

@media (max-width: 1100px) {
    .review-cover-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .grid-2 {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 900px) {
    .block-container {
        padding-left: 0.9rem !important;
        padding-right: 0.9rem !important;
        max-width: 100vw !important;
        width: 100% !important;
    }

    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
    }

    [data-testid="stHorizontalBlock"] > div {
        min-width: 100% !important;
        flex: 1 1 100% !important;
    }

    .topbar {
        display: block;
        width: 100%;
        padding-bottom: 22px;
    }

    .brand-title {
        font-size: clamp(28px, 8vw, 36px);
        line-height: 1.08;
        max-width: 100%;
    }

    .brand-subtitle {
        font-size: 15px;
        line-height: 1.45;
        max-width: 100%;
    }

    .nav-pills {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 10px;
        width: 100%;
        margin-top: 16px;
        overflow: hidden;
    }

    .nav-pills a {
        display: block;
        width: 100%;
        text-align: center;
        white-space: normal;
        min-width: 0;
        padding: 10px 8px;
        font-size: 14px;
        line-height: 1.15;
    }

    .nav-pills a:nth-child(3) {
        grid-column: span 2;
    }

    .hero {
        padding: 38px 22px;
        border-radius: 28px;
        width: 100%;
    }

    .hero h1 {
        font-size: clamp(32px, 8vw, 40px);
        line-height: 1.08;
    }

    .hero p {
        font-size: 17px;
        line-height: 1.55;
    }

    .review-cover-grid {
        grid-template-columns: 1fr;
        gap: 10px;
    }

    .btn-primary,
    .btn-secondary,
    .btn-light,
    .btn-dark {
        width: 100%;
        text-align: center;
        display: block;
    }

    .footer {
        padding: 32px 24px;
    }

    .footer-actions {
        display: block;
    }

    .footer-actions a {
        margin-bottom: 12px;
    }
}

@media (max-width: 420px) {
    .brand-title {
        font-size: 31px;
    }

    .brand-subtitle {
        font-size: 14px;
    }

    .hero h1 {
        font-size: 32px;
    }

    .hero {
        padding: 34px 20px;
    }

    .nav-pills a {
        font-size: 13px;
        padding: 10px 6px;
    }
}
</style>
""")

# =========================================================
# HEADER
# =========================================================
if LOGO_PATH:
    st.image(LOGO_PATH, width=118)

html(f"""
<div class="topbar" id="top">
    <div>
        <p class="brand-title">Nexus Conformité</p>
        <p class="brand-subtitle">CQC evidence support, compliance organisation, governance documentation, and operational readiness.</p>
    </div>
    <div class="nav-pills">
        <a href="#services">Services</a>
        <a href="#process">Process</a>
        <a href="#request">Request Support</a>
        <a href="#faq">FAQs</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""")

# =========================================================
# HERO
# =========================================================
html(f"""
<div class="hero">
    <div class="eyebrow">UK care compliance support</div>
    <h1>Get a clear view of your CQC evidence position before issues escalate.</h1>
    <p>
    Nexus Conformité supports UK care managers and small providers with structured evidence reviews,
    documentation organisation, and compliance readiness support. The £149 Evidence File Review gives
    you a practical first assessment before committing to deeper cleanup or ongoing support.
    </p>
    <div class="cta-row">
        <a class="btn-primary" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Buy £149 Review</a>
        <a class="btn-secondary" href="#request">Request Custom Support</a>
        <a class="btn-light" href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer">View Digital Products</a>
    </div>
</div>
""")

# =========================================================
# PROBLEM SECTION
# =========================================================
html("""
<div class="problem-strip">
    <h2>Documents alone do not prove control. Evidence does.</h2>
    <div class="gold-line"></div>
    <p>
    Policies, trackers, audits, training records, incidents, complaints, and risk documents only support compliance when they are current,
    organised, and easy to explain.
    </p>
    <p>
    Nexus reviews the structure of your evidence and identifies the areas that need attention before they become a larger operational risk.
    </p>
</div>
""")

# =========================================================
# REVIEW COVERAGE
# =========================================================
html("""
<div class="section">
    <h2>What the £149 review covers.</h2>
    <p class="section-intro">
    A practical review of the core evidence areas care providers are expected to keep organised, current, and ready to explain.
    </p>
</div>

<div class="review-cover-grid">
    <div class="review-cover-item"><div class="review-cover-icon">□</div><p>Policies and procedures</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">✓</div><p>Risk assessments</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">▤</div><p>Training matrix</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">!</div><p>Incidents and complaints logs</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">○</div><p>Safeguarding records</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">☑</div><p>Audit tracker</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◉</div><p>Governance minutes</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">⌂</div><p>GDPR and data handling</p></div>
</div>

<div class="review-cover-note">
    The review identifies whether these records are structured, traceable, current, and suitable for management review.
</div>
""")

# =========================================================
# SERVICE CARDS WITH NATIVE SLIDES
# =========================================================
html('<div id="services"></div>')

html("""
<div class="section">
    <h2>Select the level of support that matches your evidence position.</h2>
    <p class="section-intro">
    Each service card includes an overview, detail of what Nexus does, and a sample-style preview of the type of output the client may receive.
    </p>
</div>
""")

def logo_block_html():
    if LOGO_DATA_URI:
        return f'<img src="{LOGO_DATA_URI}" alt="Nexus Conformité logo" class="report-logo">'
    return '<div class="fallback-logo">NC<span>NEXUS CONFORMITÉ</span></div>'

def report_preview_component():
    logo_block = logo_block_html()

    preview_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    background: transparent;
    font-family: Arial, sans-serif;
}
.frame {
    width: 100%;
    height: 500px;
    border-radius: 18px;
    overflow: hidden;
    background: #071C35;
    padding: 10px;
    box-shadow: 0 12px 28px rgba(15,23,42,0.18);
}
.stage {
    width: 100%;
    height: 100%;
    background: #071C35;
    border-radius: 14px;
    overflow: hidden;
    position: relative;
}
.sheet {
    width: 760px;
    height: 980px;
    background: white;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%) scale(0.48);
    transform-origin: center center;
    border-left: 9px solid #C8A96A;
    color: #172033;
}
.header {
    height: 78px;
    background: #F6F9FC;
    padding: 18px 58px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.header-left strong {
    display: block;
    color: #0B4778;
    font-size: 14px;
}
.header-left span {
    display: block;
    color: #7B8796;
    font-size: 11px;
    margin-top: 4px;
}
.logo-wrap {
    width: 170px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
}
.report-logo {
    max-width: 165px;
    max-height: 54px;
    object-fit: contain;
    display: block;
}
.fallback-logo {
    text-align: right;
    color: #C8A96A;
    font-weight: 900;
    font-size: 26px;
}
.fallback-logo span {
    display: block;
    color: #061A35;
    font-size: 10px;
    letter-spacing: 0.08em;
}
.content {
    padding: 34px 60px;
}
.kicker {
    color: #B18420;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
h1 {
    margin: 8px 0 12px 0;
    color: #172033;
    font-size: 40px;
    line-height: 1.05;
}
.lead {
    color: #6B7280;
    font-size: 20px;
    line-height: 1.25;
    margin-bottom: 22px;
}
.box-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 18px;
}
.box {
    border: 1px solid #E5E7EB;
    border-left: 5px solid #C8A96A;
    background: #FFFDF7;
    padding: 14px;
}
.box.teal {
    border-left-color: #0F766E;
    background: #EAF7F4;
}
.box strong {
    display: block;
    font-size: 18px;
    color: #172033;
    margin-bottom: 8px;
}
.box span {
    font-size: 15px;
    color: #64748B;
    line-height: 1.25;
}
.metrics {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border: 1px solid #E5E7EB;
    margin: 18px 0;
}
.metric {
    padding: 10px;
    text-align: center;
    border-right: 1px solid #E5E7EB;
    background: #EEF7FC;
}
.metric:nth-child(2) { background: #EAF7F4; }
.metric:nth-child(3) { background: #FFF8E8; }
.metric:nth-child(4) { background: #FEECEC; border-right: none; }
.metric strong {
    display: block;
    font-size: 34px;
    color: #0B4778;
}
.metric:nth-child(2) strong { color: #0F766E; }
.metric:nth-child(3) strong { color: #B18420; }
.metric:nth-child(4) strong { color: #B94343; }
.metric span {
    color: #64748B;
    font-size: 11px;
    font-weight: 700;
}
.conclusion {
    border: 1px solid #E5E7EB;
    border-left: 5px solid #061A35;
    padding: 14px 16px;
    margin-top: 18px;
}
.conclusion strong {
    display: block;
    font-size: 18px;
    color: #172033;
    margin-bottom: 8px;
}
.conclusion p {
    color: #64748B;
    font-size: 16px;
    line-height: 1.28;
    margin: 0 0 10px 0;
}
.mini-pages {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 18px;
}
.mini {
    border: 1px solid #E5E7EB;
    background: #FFFFFF;
    padding: 10px;
    min-height: 126px;
}
.mini h3 {
    margin: 0 0 8px 0;
    font-size: 15px;
    color: #172033;
}
.mini-row {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 6px;
    border-top: 1px solid #EEF1F5;
    padding: 5px 0;
    font-size: 11px;
    color: #4B5563;
}
.badge {
    font-size: 10px;
    font-weight: 900;
    border-radius: 999px;
    padding: 2px 6px;
    background: #FFF8E8;
    color: #8A6519;
}
.badge.green { background: #EAF7F4; color: #0F766E; }
.badge.red { background: #FEECEC; color: #991B1B; }
.footer {
    position: absolute;
    bottom: 26px;
    left: 60px;
    right: 60px;
    display: flex;
    justify-content: space-between;
    color: #9AA4B2;
    font-size: 10px;
    border-top: 1px solid #E5E7EB;
    padding-top: 8px;
}
@media (max-width: 430px) {
    .frame { height: 470px; }
    .sheet { transform: translate(-50%, -50%) scale(0.43); }
}
</style>
</head>
<body>
<div class="frame">
    <div class="stage">
        <div class="sheet">
            <div class="header">
                <div class="header-left">
                    <strong>Nexus Conformité | CQC Evidence Review</strong>
                    <span>Redacted UK care provider · client report</span>
                </div>
                <div class="logo-wrap">
                    __LOGO_BLOCK__
                </div>
            </div>

            <div class="content">
                <div class="kicker">Executive brief</div>
                <h1>Executive Summary</h1>
                <div class="lead">
                    This report gives the provider a clear evidence position before relying on its documentation for CQC readiness, commissioner assurance or internal governance reporting.
                </div>

                <div class="box-row">
                    <div class="box">
                        <strong>Overall readiness</strong>
                        <span><b>Amber - controlled cleanup required.</b><br>The evidence pack is usable, but not yet inspection-ready. The main weakness is inconsistent ownership, dating, version control and closure notes.</span>
                    </div>
                    <div class="box teal">
                        <strong>Client outcome</strong>
                        <span>The provider can now see what is strong, what is incomplete, and what must be corrected first. The action plan should be assigned to named owners and reviewed weekly.</span>
                    </div>
                </div>

                <div class="metrics">
                    <div class="metric"><strong>149</strong><span>Evidence points applied</span></div>
                    <div class="metric"><strong>87</strong><span>Acceptable / near-ready</span></div>
                    <div class="metric"><strong>42</strong><span>Partial / weak</span></div>
                    <div class="metric"><strong>20</strong><span>Missing / not supplied</span></div>
                </div>

                <div class="conclusion">
                    <strong>Executive conclusion</strong>
                    <p>The provider should not present the current file as a complete inspection evidence pack. The safer position is to use it as a working evidence base, complete the missing links, and create a short governance narrative showing how risks are identified, acted on, checked and closed.</p>
                    <p>The first corrections should focus on governance minutes, risk review records, training assurance, complaints and improvement logs, and care plan audit closure evidence.</p>
                </div>

                <div class="mini-pages">
                    <div class="mini">
                        <h3>Priorities</h3>
                        <div class="mini-row"><span>Governance oversight</span><span class="badge red">1</span></div>
                        <div class="mini-row"><span>Risk review records</span><span class="badge">2</span></div>
                        <div class="mini-row"><span>Training assurance</span><span class="badge">3</span></div>
                    </div>
                    <div class="mini">
                        <h3>CQC lens</h3>
                        <div class="mini-row"><span>Safe</span><span class="badge green">Used</span></div>
                        <div class="mini-row"><span>Effective</span><span class="badge green">Used</span></div>
                        <div class="mini-row"><span>Well-led</span><span class="badge red">Key</span></div>
                    </div>
                    <div class="mini">
                        <h3>14-day plan</h3>
                        <div class="mini-row"><span>Set control</span><span class="badge">D1-2</span></div>
                        <div class="mini-row"><span>Fix governance</span><span class="badge">D3-5</span></div>
                        <div class="mini-row"><span>Sign-off pack</span><span class="badge green">D12-14</span></div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <span>Confidential · redacted client report</span>
                <span>Sample preview</span>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""
    preview_html = preview_html.replace("__LOGO_BLOCK__", logo_block)
    components.html(preview_html, height=515, scrolling=False)

def incident_complaints_preview_component():
    logo_block = logo_block_html()

    preview_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    background: transparent;
    font-family: Arial, sans-serif;
}
.frame {
    width: 100%;
    height: 500px;
    border-radius: 18px;
    overflow: hidden;
    background: #071C35;
    padding: 10px;
    box-shadow: 0 12px 28px rgba(15,23,42,0.18);
}
.stage {
    width: 100%;
    height: 100%;
    background: #071C35;
    border-radius: 14px;
    overflow: hidden;
    position: relative;
}
.sheet {
    width: 760px;
    height: 980px;
    background: white;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%) scale(0.48);
    transform-origin: center center;
    border-left: 9px solid #C8A96A;
    color: #172033;
}
.header {
    height: 78px;
    background: #F6F9FC;
    padding: 18px 58px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.header-left strong {
    display: block;
    color: #0B4778;
    font-size: 14px;
}
.header-left span {
    display: block;
    color: #7B8796;
    font-size: 11px;
    margin-top: 4px;
}
.logo-wrap {
    width: 170px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
}
.report-logo {
    max-width: 165px;
    max-height: 54px;
    object-fit: contain;
    display: block;
}
.fallback-logo {
    text-align: right;
    color: #C8A96A;
    font-weight: 900;
    font-size: 26px;
}
.fallback-logo span {
    display: block;
    color: #061A35;
    font-size: 10px;
    letter-spacing: 0.08em;
}
.content {
    padding: 34px 58px;
}
.kicker {
    color: #B18420;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
h1 {
    margin: 8px 0 12px 0;
    color: #172033;
    font-size: 38px;
    line-height: 1.05;
}
.lead {
    color: #6B7280;
    font-size: 19px;
    line-height: 1.28;
    margin-bottom: 20px;
}
.chart-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 18px;
}
.chart-card {
    border: 1px solid #E5E7EB;
    border-left: 6px solid #0F766E;
    background: #FFFFFF;
    padding: 13px;
    height: 150px;
}
.chart-card.gold {
    border-left-color: #C8A96A;
}
.chart-title {
    font-size: 14px;
    font-weight: 900;
    color: #172033;
    margin-bottom: 8px;
}
.bars {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 7px;
    align-items: end;
    height: 82px;
}
.bar-wrap {
    display: grid;
    grid-template-rows: 1fr auto;
    gap: 4px;
    text-align: center;
    font-size: 9px;
    color: #64748B;
}
.bar-track {
    height: 70px;
    border-radius: 8px;
    background: #EEF2F7;
    display: flex;
    align-items: end;
    overflow: hidden;
}
.bar {
    width: 100%;
    border-radius: 8px 8px 0 0;
    background: #0F766E;
    color: white;
    font-size: 10px;
    font-weight: 900;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding-top: 4px;
}
.gold .bar {
    background: #C8A96A;
    color: #172033;
}
.main-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}
.main-table th {
    background: #061A35;
    color: white;
    font-size: 12px;
    text-align: left;
    padding: 10px;
}
.main-table td {
    border: 1px solid #E5E7EB;
    color: #4B5563;
    font-size: 12px;
    padding: 10px;
    vertical-align: top;
}
.main-table td:first-child {
    color: #172033;
    font-weight: 900;
}
.conclusion {
    border: 1px solid #CDEBE4;
    border-left: 6px solid #0F766E;
    background: #EAF7F4;
    padding: 15px 18px;
    margin-top: 18px;
}
.conclusion strong {
    display: block;
    color: #172033;
    font-size: 18px;
    margin-bottom: 8px;
}
.conclusion p {
    color: #64748B;
    font-size: 17px;
    line-height: 1.28;
    margin: 0;
}
.footer {
    position: absolute;
    bottom: 26px;
    left: 60px;
    right: 60px;
    display: flex;
    justify-content: space-between;
    color: #9AA4B2;
    font-size: 10px;
    border-top: 1px solid #E5E7EB;
    padding-top: 8px;
}
@media (max-width: 430px) {
    .frame { height: 470px; }
    .sheet { transform: translate(-50%, -50%) scale(0.43); }
}
</style>
</head>
<body>
<div class="frame">
    <div class="stage">
        <div class="sheet">
            <div class="header">
                <div class="header-left">
                    <strong>Nexus Conformité | Incident & Complaints Log Review</strong>
                    <span>Redacted UK care provider · client report</span>
                </div>
                <div class="logo-wrap">
                    __LOGO_BLOCK__
                </div>
            </div>

            <div class="content">
                <div class="kicker">Trend visibility</div>
                <h1>Trend Review - January to June 2026</h1>
                <div class="lead">
                    The entries show enough activity to create a trend view, but the supplied logs do not present trends clearly. The provider should add a monthly trend dashboard and discuss it at governance review.
                </div>

                <div class="chart-grid">
                    <div class="chart-card">
                        <div class="chart-title">Incident entries by month</div>
                        <div class="bars">
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:38%;">2</div></div><span>Jan</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:38%;">2</div></div><span>Feb</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:56%;">3</div></div><span>Mar</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:74%;">4</div></div><span>Apr</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:56%;">3</div></div><span>May</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:74%;">4</div></div><span>Jun</span></div>
                        </div>
                    </div>

                    <div class="chart-card gold">
                        <div class="chart-title">Complaint entries by month</div>
                        <div class="bars">
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:34%;">1</div></div><span>Jan</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:8%;">0</div></div><span>Feb</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:62%;">2</div></div><span>Mar</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:34%;">1</div></div><span>Apr</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:34%;">1</div></div><span>May</span></div>
                            <div class="bar-wrap"><div class="bar-track"><div class="bar" style="height:62%;">2</div></div><span>Jun</span></div>
                        </div>
                    </div>
                </div>

                <table class="main-table">
                    <thead>
                        <tr>
                            <th>Theme</th>
                            <th>Count</th>
                            <th>Trend interpretation</th>
                            <th>Governance action required</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Medication and MAR-related incidents</td>
                            <td>5</td>
                            <td>Largest incident theme across the review period.</td>
                            <td>Link to medication audit, staff competency checks and re-audit date.</td>
                        </tr>
                        <tr>
                            <td>Late / missed calls</td>
                            <td>7 combined</td>
                            <td>Appears in both incident and complaint records, mainly Apr-Jun.</td>
                            <td>Review rostering, call monitoring and communication with relatives.</td>
                        </tr>
                        <tr>
                            <td>Falls / manual handling / near misses</td>
                            <td>4</td>
                            <td>Recorded as isolated entries, but no monthly learning note found.</td>
                            <td>Add risk review and care plan update evidence where relevant.</td>
                        </tr>
                        <tr>
                            <td>Communication complaints</td>
                            <td>2</td>
                            <td>Relatives raised concerns about response and updates.</td>
                            <td>Add response standard, escalation route and close-out call record.</td>
                        </tr>
                    </tbody>
                </table>

                <div class="conclusion">
                    <strong>Trend conclusion</strong>
                    <p>The data suggests the provider should focus first on medication governance, late or missed calls, communication with relatives and closure discipline. These themes should be visible in the next management meeting minutes and in the master action tracker.</p>
                </div>
            </div>

            <div class="footer">
                <span>Confidential · redacted client report</span>
                <span>Sample preview</span>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""
    preview_html = preview_html.replace("__LOGO_BLOCK__", logo_block)
    components.html(preview_html, height=515, scrolling=False)

def sample_frame(title, subtitle, rows):
    with st.container(border=True):
        st.markdown(f"**{title}**  \n*{subtitle}*")
        table_rows = "\n".join([f"| {item} | {status} |" for item, status in rows])
        st.markdown(f"""
| Item | Status |
|---|---|
{table_rows}
""")

def review_card():
    with st.container(border=True):
        view = st.radio(
            "£149 review card view",
            ["Overview", "Details", "Sample"],
            horizontal=True,
            key="review_card_view",
            label_visibility="collapsed"
        )

        if view == "Overview":
            st.markdown("**Fixed first step**")
            st.subheader("£149 CQC Evidence File Review")
            st.markdown("## £149")
            st.write("A focused review for providers that need a clear evidence assessment before deciding whether deeper support is required.")
            st.markdown("""
- Evidence structure review
- Gap notes on weak or unclear records
- Priority action direction
- Written summary of next steps
""")
            st.markdown(f'<a class="btn-dark" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Buy Now</a>', unsafe_allow_html=True)

        elif view == "Details":
            st.markdown("**What Nexus checks**")
            st.subheader("What the review gives you")
            st.write("The review helps a manager understand the evidence position before committing to a larger package.")
            with st.container(border=True):
                st.markdown("**Evidence structure check**  \nHow policies, trackers, audits, risk records, complaints, and governance evidence are arranged.")
            with st.container(border=True):
                st.markdown("**Gap notes**  \nWeak, unclear, missing, outdated, or hard-to-explain records are identified.")
            with st.container(border=True):
                st.markdown("**Priority direction**  \nThe output shows what should be addressed first.")
            with st.container(border=True):
                st.markdown("**Decision point**  \nThe provider can decide whether a cleanup sprint or monthly support is justified.")

        else:
            st.markdown("**Sample-style output**")
            st.subheader("Redacted report preview")
            st.caption("Sample visual only. Final output depends on the evidence received.")
            report_preview_component()

def cleanup_card():
    with st.container(border=True):
        view = st.radio(
            "Cleanup card view",
            ["Overview", "Details", "Sample"],
            horizontal=True,
            key="cleanup_card_view",
            label_visibility="collapsed"
        )

        if view == "Overview":
            st.markdown("**Scoped private Payhip link**")
            st.subheader("30-Day CQC Evidence Cleanup Sprint")
            st.markdown("## From £750")
            st.write("For providers that need structured cleanup of evidence folders, trackers, policies, and management review records.")
            st.markdown("""
- Scoped after intake review
- Evidence folder organisation
- Tracker and document-control cleanup
- Preview before final balance
""")
            st.markdown('<a class="btn-dark" href="#request">Request Scope Review</a>', unsafe_allow_html=True)

        elif view == "Details":
            st.markdown("**What Nexus does**")
            st.subheader("What the cleanup sprint includes")
            st.write("This service turns scattered evidence into a clearer working evidence pack.")
            with st.container(border=True):
                st.markdown("**Audit tracker update**  \nActions, dates, owners, status, and follow-up points are made clearer.")
            with st.container(border=True):
                st.markdown("**Incident and complaints logs**  \nStructure, missing fields, action links, trend visibility, and closure status are reviewed.")
            with st.container(border=True):
                st.markdown("**Evidence index**  \nRecords are grouped so the manager can locate what exists and what remains outstanding.")
            with st.container(border=True):
                st.markdown("**Handover summary**  \nThe client receives a clear summary of completed work, key gaps, and recommended next actions.")

        else:
            st.markdown("**Sample-style output**")
            st.subheader("Incident & complaints log review preview")
            st.caption("Sample visual only. Final files depend on the agreed scope.")
            incident_complaints_preview_component()

def retainer_card():
    with st.container(border=True):
        view = st.radio(
            "Retainer card view",
            ["Overview", "Details", "Sample"],
            horizontal=True,
            key="retainer_card_view",
            label_visibility="collapsed"
        )

        if view == "Overview":
            st.markdown("**Scoped private Payhip link**")
            st.subheader("Monthly Compliance Retainer")
            st.markdown("## Scoped")
            st.write("For providers that need continued support with evidence tracking, action follow-up, document control, and monthly review records.")
            st.markdown("""
- Monthly support after scope review
- Evidence and action tracker updates
- Policy and documentation support
- Monthly management summary
""")
            st.markdown('<a class="btn-dark" href="#request">Request Retainer Scope</a>', unsafe_allow_html=True)

        elif view == "Details":
            st.markdown("**What Nexus does**")
            st.subheader("What monthly support maintains")
            st.write("This service supports evidence discipline so records do not fall behind after the first review or cleanup.")
            with st.container(border=True):
                st.markdown("**Monthly evidence check**  \nSelected evidence areas are reviewed and flagged for action.")
            with st.container(border=True):
                st.markdown("**Action tracker follow-up**  \nOwners, due dates, open items, and status updates are maintained.")
            with st.container(border=True):
                st.markdown("**Document-control support**  \nPolicy lists, review dates, version control, and evidence indexing are supported.")
            with st.container(border=True):
                st.markdown("**Management summary**  \nA concise monthly summary helps internal governance and follow-up.")

        else:
            st.markdown("**Sample-style output**")
            st.subheader("Monthly support preview")
            st.caption("Sample visual only. Monthly outputs are agreed after scope review.")
            sample_frame("Monthly Evidence Dashboard.xlsx", "Status view", [("Policies reviewed", "4"), ("Trackers updated", "3"), ("High priority items", "2")])
            sample_frame("Action Tracker Update.xlsx", "Month-end", [("Owner assigned", "Yes"), ("Due dates added", "Yes"), ("Overdue items", "Review")])
            sample_frame("Governance Summary.docx", "Monthly note", [("Management review", "Prepared"), ("Risk points", "2"), ("Next actions", "Listed")])
            st.info("The monthly retainer keeps the evidence position visible, current, and easier to review.")

service_cols = st.columns(3)
with service_cols[0]:
    review_card()
with service_cols[1]:
    cleanup_card()
with service_cols[2]:
    retainer_card()

html("""
<div class="notice">
    <h3>Payment and delivery</h3>
    <p>
    The £149 CQC Evidence File Review is the fixed public checkout service. After payment, the client completes the intake form and uploads
    redacted supporting documents.
    </p>
    <p>
    The 30-Day Cleanup Sprint and Monthly Compliance Retainer are custom services. After scope review, Nexus creates a private Payhip deposit
    link for that client. Work begins after the 40% deposit is paid.
    </p>
    <p>
    When the package is ready, the client receives a preview or summary. The final 60% is then paid through a private Payhip delivery link.
    Completed files are released only after final payment through Payhip.
    </p>
</div>
""")

# =========================================================
# WHY NEXUS
# =========================================================
html("""
<div class="section">
    <h2>Why care managers use Nexus.</h2>
    <p class="section-intro">
    Nexus focuses on evidence quality, document control, management accountability, and practical next steps.
    </p>
</div>

<div class="grid-2">
    <div class="step">
        <h3>Evidence-led review</h3>
        <p>The review considers whether records support management control, monitoring, review, and improvement.</p>
    </div>
    <div class="step">
        <h3>Decision-ready output</h3>
        <p>The summary helps managers understand the evidence position and decide whether further cleanup is required.</p>
    </div>
    <div class="step">
        <h3>Practical action points</h3>
        <p>The focus is on clear next steps, not generic templates or broad commentary.</p>
    </div>
    <div class="step">
        <h3>Controlled delivery</h3>
        <p>Custom packages are handled through intake, private Payhip deposit links, preview or summary review, and final Payhip delivery links before file release.</p>
    </div>
</div>
""")

# =========================================================
# PROCESS
# =========================================================
html('<div id="process"></div>')

html("""
<div class="section">
    <h2>How the process works.</h2>
</div>
""")

process_cols = st.columns(3)
with process_cols[0]:
    with st.container(border=True):
        st.markdown("### 1. Choose the route")
        st.write("Buy the £149 review directly, or submit the intake form for scoped support such as the 30-Day Sprint or Monthly Retainer.")
with process_cols[1]:
    with st.container(border=True):
        st.markdown("### 2. Submit evidence")
        st.write("Upload redacted documents such as folder indexes, trackers, policies, audit summaries, risk registers, or training matrices.")
with process_cols[2]:
    with st.container(border=True):
        st.markdown("### 3. Receive the outcome")
        st.write("Fixed reviews are delivered after payment and intake. Custom work uses a 40% Payhip deposit, preview or summary, then final Payhip balance before file release.")

html("""
<div class="green-notice">
    <h3>What Nexus needs before support begins</h3>
    <ul>
        <li>Full name and business/provider name</li>
        <li>Your role: registered manager, care manager, provider, owner, operations lead, or compliance lead</li>
        <li>Provider type: domiciliary care, home care, supported living, residential care, new provider, or small business</li>
        <li>The support you want: £149 review, 30-Day Sprint, monthly support, or not sure yet</li>
        <li>Main concern: evidence gaps, outdated policies, weak trackers, inspection pressure, or missing management review records</li>
        <li>Document condition and available evidence areas</li>
        <li>Redacted supporting documents where possible</li>
        <li>For paid orders, include the Payhip order email or reference if available</li>
    </ul>
</div>
""")

# =========================================================
# REQUEST FORM
# =========================================================
html('<div id="request"></div>')

html("""
<div class="section">
    <h2>Request service support.</h2>
    <p class="section-intro">
    Complete the intake form below so Nexus Conformité can assess your support need, evidence position, urgency, and available documents.
    For the £149 review, complete this after payment. For custom services, Nexus reviews your request and issues a private Payhip deposit link where suitable.
    </p>
</div>
""")

components.html(f"""
<div style="background:#ffffff; border:1px solid #E5E7EB; border-radius:26px; padding:28px; box-shadow:0 16px 42px rgba(15,23,42,0.06); font-family:Arial, sans-serif; color:#172033;">

    <form action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">

        <input type="hidden" name="_subject" value="New Nexus Conformité Service Request">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none">

        <h2 style="color:#061A35; margin-top:0;">Service Request Intake</h2>
        <p style="color:#6B7280; font-size:15px; line-height:1.6;">
            Provide enough detail for Nexus to assess the correct support route.
            Upload redacted documents only. Do not upload identifiable service-user records unless Nexus later requests them through a suitable secure method.
        </p>

        <hr style="border:none; border-top:1px solid #E5E7EB; margin:24px 0;">

        <h3 style="color:#061A35;">1. Contact details</h3>

        <label style="font-weight:700; color:#061A35;">Full name *</label><br>
        <input type="text" name="Full Name" required style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Business / provider name *</label><br>
        <input type="text" name="Business or Provider Name" required style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Email address *</label><br>
        <input type="email" name="email" required style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Phone / WhatsApp</label><br>
        <input type="text" name="Phone or WhatsApp" style="width:100%; padding:14px; margin:8px 0 22px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Payhip order email or reference, if already paid</label><br>
        <input type="text" name="Payhip Order Email or Reference" placeholder="Use this for the £149 review if you have already paid." style="width:100%; padding:14px; margin:8px 0 22px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">

        <h3 style="color:#061A35;">2. Organisation profile</h3>

        <label style="font-weight:700; color:#061A35;">Your role *</label><br>
        <select name="Role" required style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">
            <option value="">Select one</option>
            <option>Registered Manager</option>
            <option>Care Manager</option>
            <option>Provider / Owner</option>
            <option>Operations Manager</option>
            <option>Compliance Lead</option>
            <option>Small Business Owner</option>
            <option>Other</option>
        </select>

        <label style="font-weight:700; color:#061A35;">Organisation type *</label><br>
        <select name="Organisation Type" required style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">
            <option value="">Select one</option>
            <option>Domiciliary care provider</option>
            <option>Home care provider</option>
            <option>Supported living provider</option>
            <option>Residential care provider</option>
            <option>New care provider</option>
            <option>Small business</option>
            <option>Other</option>
        </select>

        <label style="font-weight:700; color:#061A35;">Approximate size</label><br>
        <select name="Approximate Size" style="width:100%; padding:14px; margin:8px 0 22px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">
            <option>Not sure / prefer to discuss</option>
            <option>New provider / pre-registration</option>
            <option>1–10 staff</option>
            <option>11–25 staff</option>
            <option>26–50 staff</option>
            <option>51+ staff</option>
        </select>

        <h3 style="color:#061A35;">3. Support needed</h3>

        <label style="font-weight:700; color:#061A35;">Support needed *</label><br>
        <select name="Support Needed" required style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">
            <option value="">Select one</option>
            <option>£149 CQC Evidence File Review - already paid or ready to start</option>
            <option>30-Day CQC Evidence Cleanup Sprint - scope review needed</option>
            <option>Monthly Compliance Retainer - scope review needed</option>
            <option>Small Business Compliance Readiness - scope review needed</option>
            <option>Not sure yet</option>
        </select>

        <label style="font-weight:700; color:#061A35;">Urgency *</label><br>
        <select name="Urgency" required style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">
            <option value="">Select one</option>
            <option>Not urgent</option>
            <option>Need support this month</option>
            <option>Inspection pressure / urgent</option>
            <option>Preparing before registration or review</option>
            <option>Ongoing monthly support needed</option>
        </select>

        <label style="font-weight:700; color:#061A35;">Current document condition *</label><br>
        <select name="Current Document Condition" required style="width:100%; padding:14px; margin:8px 0 22px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">
            <option value="">Select one</option>
            <option>Mostly organised</option>
            <option>Some documents are scattered</option>
            <option>Very scattered and unclear</option>
            <option>Starting from scratch</option>
            <option>Not sure</option>
        </select>

        <h3 style="color:#061A35;">4. Evidence areas available</h3>
        <p style="color:#6B7280; font-size:15px; line-height:1.6;">
            Tick the areas you can provide now. You do not need to upload everything at first contact.
        </p>

        <label><input type="checkbox" name="Available Evidence Areas" value="Policies and procedures"> Policies and procedures</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Risk assessments"> Risk assessments</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Training matrix or training records"> Training matrix or training records</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Incidents and complaints logs"> Incidents and complaints logs</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Safeguarding records"> Safeguarding records</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Audit tracker or audit records"> Audit tracker or audit records</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Governance minutes or management review notes"> Governance minutes or management review notes</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="GDPR and data handling records"> GDPR and data handling records</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Evidence folder index or screenshots"> Evidence folder index or screenshots</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Action tracker"> Action tracker</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="CQC correspondence or report"> CQC correspondence or report, if relevant</label><br>

        <br>

        <h3 style="color:#061A35;">5. Upload supporting documents</h3>
        <p style="color:#6B7280; font-size:15px; line-height:1.6;">
            Useful examples include a folder index, policy list, evidence tracker, action tracker, audit summary,
            risk register, training matrix, or screenshots showing the document structure.
        </p>

        <label style="font-weight:700; color:#061A35;">Upload files *</label><br>
        <input type="file" name="attachment" multiple required accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.png,.jpg,.jpeg" style="width:100%; padding:14px; margin:8px 0 12px 0; border:1px dashed #C8A96A; border-radius:14px; font-size:16px; background:#FFF8E8; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Additional files, if needed</label><br>
        <input type="file" name="attachment2" multiple accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.png,.jpg,.jpeg" style="width:100%; padding:14px; margin:8px 0 12px 0; border:1px dashed #D1D5DB; border-radius:14px; font-size:16px; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Additional files, if needed</label><br>
        <input type="file" name="attachment3" multiple accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.png,.jpg,.jpeg" style="width:100%; padding:14px; margin:8px 0 22px 0; border:1px dashed #D1D5DB; border-radius:14px; font-size:16px; box-sizing:border-box;">

        <h3 style="color:#061A35;">6. Main concern</h3>

        <label style="font-weight:700; color:#061A35;">Describe the issue *</label><br>
        <textarea name="Main Concern" required rows="7" placeholder="Example: Our evidence folders need review before inspection. We need help checking policies, risk assessments, training records, audit trackers, safeguarding records, complaints logs, governance minutes, and GDPR evidence." style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;"></textarea>

        <label style="font-weight:700; color:#061A35;">Preferred next step</label><br>
        <select name="Preferred Next Step" style="width:100%; padding:14px; margin:8px 0 22px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;">
            <option>Please review and advise the best support level</option>
            <option>I have paid for the £149 review and want to start</option>
            <option>I want a private Payhip deposit link for the 30-Day Sprint after scope review</option>
            <option>I want a private Payhip deposit link for monthly support after scope review</option>
        </select>

        <label style="display:block; font-size:14px; line-height:1.5; color:#374151; margin-bottom:18px;">
            <input type="checkbox" name="Client Confirmation" required value="Confirmed authority and redaction notice accepted">
            I confirm that I have authority to submit this request and that uploaded documents have been redacted where necessary.
        </label>

        <button type="submit" style="width:100%; background:#C8A96A; color:#061A35; padding:16px 22px; border:none; border-radius:999px; font-weight:800; font-size:17px; cursor:pointer;">
            Submit Request to Nexus
        </button>

        <p style="font-size:14px; color:#6B7280; margin-top:16px; line-height:1.6;">
            Nexus Conformité will review the request and advise the suitable next step. For scoped services,
            a private Payhip deposit link may be issued before work begins. When the package is ready,
            the customer receives a preview or summary, then pays the final 60% through a private Payhip
            delivery link before files are released.
        </p>

    </form>
</div>
""", height=3500, scrolling=True)

# =========================================================
# FAQS
# =========================================================
html('<div id="faq"></div>')

html("""
<div class="section">
    <h2>FAQs</h2>
    <p class="section-intro">Clear answers before a care manager decides to contact Nexus.</p>
</div>
""")

with st.expander("Is the £149 review a full compliance audit?"):
    st.write("No. It is a focused evidence structure review. It identifies obvious gaps, weak organisation, and practical next steps.")

with st.expander("Does Nexus replace the provider’s CQC responsibility?"):
    st.write("No. Nexus supports evidence organisation, documentation structure, action trackers, and management review preparation. The provider remains responsible for meeting regulatory requirements.")

with st.expander("Can Nexus support domiciliary care providers?"):
    st.write("Yes. The services are suitable for domiciliary care, home care, supported living, new providers, and small care providers that need clearer evidence structures.")

with st.expander("How does the £149 checkout work?"):
    st.write("The £149 CQC Evidence File Review is purchased through the public Payhip checkout link. After payment, the customer completes the intake form and uploads redacted documents. Delivery is within 3–5 business days after payment and receipt of the required intake documents.")

with st.expander("How does payment work for the 30-Day Sprint or Monthly Retainer?"):
    st.write("Custom services are scoped first. Once scope is agreed, Nexus issues a private Payhip link for the 40% deposit. Work begins after the deposit is paid. The final 60% is paid through a private Payhip delivery link before completed files are released.")

with st.expander("How are final files released for custom services?"):
    st.write("Nexus may provide a preview or summary of the completed package. Final files are released only after the client pays the remaining balance through the private Payhip delivery link. The private link is hidden from general customers and may be closed or archived after successful purchase.")

with st.expander("How are private Payhip delivery links used?"):
    st.write("For custom work, Nexus creates a private Payhip product or checkout link for that specific customer. The link is not displayed publicly. The customer pays through that private link, and completed files are released through Payhip after successful purchase.")

with st.expander("Can I move from the £149 review to the 30-Day Sprint?"):
    st.write("Yes. The £149 review can be used as the first step. If deeper cleanup is needed, the provider can move into the 30-Day Cleanup Sprint or monthly support.")

with st.expander("Should I upload confidential service-user records?"):
    st.write("No. Upload redacted documents only. Nexus will advise the next suitable secure step if more sensitive records are required.")

with st.expander("Does Nexus provide legal advice?"):
    st.write("No. Nexus Conformité provides compliance organisation, evidence readiness, governance documentation, and operational support. It does not replace legal advice.")

# =========================================================
# CONTACT / FOOTER
# =========================================================
html('<div id="contact"></div>')

html(f"""
<div class="footer">
    <h3>Nexus Conformité</h3>
    <p class="footer-cta">
        Need a clearer evidence position before your next review, inspection, or internal check?
        Start with the £149 Evidence File Review, request scoped support, or contact Nexus directly.
    </p>

    <div class="footer-actions">
        <a class="btn-primary" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Buy £149 Review</a>
        <a class="btn-secondary" href="#request">Contact / Request Support</a>
        <a class="btn-light" href="#top">Back to Top</a>
    </div>

    <div class="footer-icon-row" aria-label="Nexus Conformité contact links">
        <a class="icon-link" href="{FACEBOOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook" title="Facebook">f</a>
        <a class="icon-link" href="mailto:{EMAIL}" aria-label="Email" title="Email">@</a>
        <a class="icon-link" href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer" aria-label="Payhip" title="Payhip">P</a>
        <a class="icon-link" href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" title="LinkedIn">in</a>
    </div>

    <p class="footer-small">
        Nexus Conformité provides compliance organisation, evidence readiness, policy structure,
        and governance documentation support. Services do not replace legal advice or the provider’s own regulatory responsibilities.
    </p>
</div>
""")