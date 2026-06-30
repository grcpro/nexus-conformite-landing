import streamlit as st
import os
import glob
import textwrap
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

* {
    box-sizing: border-box;
}

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

[data-testid="stImage"] {
    max-width: 150px !important;
}

[data-testid="stImage"] img {
    max-width: 150px !important;
    width: 150px !important;
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
    box-sizing: border-box;
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
    box-sizing: border-box;
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

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 18px;
    width: 100%;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
    width: 100%;
}

.card {
    background: rgba(255,255,255,0.98);
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 26px;
    box-shadow: 0 16px 42px rgba(15,23,42,0.06);
    margin-bottom: 18px;
    box-sizing: border-box;
    max-width: 100%;
    overflow: hidden;
}

.card h3 {
    font-size: 23px;
    margin: 0 0 8px 0;
    color: var(--navy);
}

.card p {
    font-size: 17px;
    line-height: 1.5;
}

.card ul {
    margin: 12px 0 18px 0;
    padding-left: 19px;
}

.card li {
    font-size: 16px;
    line-height: 1.42;
    margin-bottom: 7px;
    overflow-wrap: break-word;
    word-break: normal;
}

.price {
    color: var(--green);
    font-size: 29px;
    font-weight: 900;
    margin: 8px 0;
}

.badge {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 12px;
    background: #EEF8F5;
    color: var(--green);
    border: 1px solid #CDEBE4;
}

.badge-gold {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 12px;
    background: #FFF8E8;
    color: #7A5C13;
    border: 1px solid #F0DB9B;
}

.gold-line {
    width: 78px;
    height: 4px;
    border-radius: 999px;
    background: var(--gold);
    margin: 12px 0 18px 0;
}

.problem-strip {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 14px 38px rgba(15,23,42,0.05);
    box-sizing: border-box;
    overflow: hidden;
}

.problem-strip h2 {
    font-size: clamp(31px, 4vw, 40px);
    line-height: 1.18;
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
    padding: 14px 14px;
    box-sizing: border-box;
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

.service-card-slider {
    background: rgba(255,255,255,0.98);
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 26px;
    box-shadow: 0 16px 42px rgba(15,23,42,0.06);
    margin-bottom: 18px;
    box-sizing: border-box;
    max-width: 100%;
    overflow: hidden;
    min-height: 690px;
}

.service-card-slider h3 {
    font-size: 23px;
    margin: 0 0 8px 0;
    color: var(--navy);
    line-height: 1.15;
}

.service-card-slider p {
    font-size: 16px;
    line-height: 1.5;
    color: var(--text);
}

.service-card-slider ul {
    margin: 12px 0 18px 0;
    padding-left: 19px;
}

.service-card-slider li {
    font-size: 15px;
    line-height: 1.4;
    margin-bottom: 7px;
}

.service-radio {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}

.service-slide {
    display: none;
    min-height: 520px;
}

#review-overview:checked ~ .service-slides .review-overview,
#review-details:checked ~ .service-slides .review-details,
#review-sample:checked ~ .service-slides .review-sample,
#cleanup-overview:checked ~ .service-slides .cleanup-overview,
#cleanup-details:checked ~ .service-slides .cleanup-details,
#cleanup-sample:checked ~ .service-slides .cleanup-sample,
#retainer-overview:checked ~ .service-slides .retainer-overview,
#retainer-details:checked ~ .service-slides .retainer-details,
#retainer-sample:checked ~ .service-slides .retainer-sample {
    display: block;
}

.slide-indicators {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-top: 16px;
}

.slide-indicators label {
    display: block;
    text-align: center;
    padding: 9px 8px;
    border-radius: 999px;
    border: 1px solid var(--line);
    color: var(--navy);
    background: #FFFFFF;
    font-size: 12px;
    font-weight: 800;
    cursor: pointer;
}

#review-overview:checked ~ .slide-indicators label[for="review-overview"],
#review-details:checked ~ .slide-indicators label[for="review-details"],
#review-sample:checked ~ .slide-indicators label[for="review-sample"],
#cleanup-overview:checked ~ .slide-indicators label[for="cleanup-overview"],
#cleanup-details:checked ~ .slide-indicators label[for="cleanup-details"],
#cleanup-sample:checked ~ .slide-indicators label[for="cleanup-sample"],
#retainer-overview:checked ~ .slide-indicators label[for="retainer-overview"],
#retainer-details:checked ~ .slide-indicators label[for="retainer-details"],
#retainer-sample:checked ~ .slide-indicators label[for="retainer-sample"] {
    background: var(--gold);
    color: var(--navy);
    border-color: var(--gold);
}

.result-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
    margin-top: 14px;
}

.result-box {
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 13px;
    background: #FBFCFE;
}

.result-box strong {
    display: block;
    color: var(--navy);
    font-size: 14px;
    margin-bottom: 4px;
}

.result-box span {
    display: block;
    color: #4B5563;
    font-size: 13px;
    line-height: 1.35;
}

.sample-collage {
    display: grid;
    grid-template-columns: 1fr;
    gap: 10px;
    margin-top: 12px;
}

.sample-frame {
    border: 1px solid #D7DEE8;
    border-radius: 16px;
    background: #FFFFFF;
    box-shadow: 0 10px 24px rgba(15,23,42,0.08);
    overflow: hidden;
}

.sample-top {
    background: linear-gradient(135deg, #061A35 0%, #0B2545 100%);
    color: white;
    padding: 9px 12px;
    display: flex;
    justify-content: space-between;
    gap: 8px;
    align-items: center;
}

.sample-top strong {
    font-size: 12px;
}

.sample-top span {
    font-size: 10px;
    color: #DDE6F2;
}

.sample-table {
    padding: 8px 10px 10px 10px;
}

.sample-row {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 8px;
    border-bottom: 1px solid #EEF1F5;
    padding: 6px 0;
    font-size: 11px;
    color: #374151;
}

.sample-row:last-child {
    border-bottom: none;
}

.sample-status {
    border-radius: 999px;
    padding: 3px 7px;
    font-size: 10px;
    font-weight: 800;
    background: #FFF8E8;
    color: #7A5C13;
    white-space: nowrap;
}

.sample-status.green {
    background: #EAF7F4;
    color: #0F766E;
}

.sample-status.red {
    background: #FEECEC;
    color: #991B1B;
}

.sample-note {
    border-left: 4px solid var(--gold);
    padding: 10px 12px;
    background: #FFFDF7;
    color: #374151;
    font-size: 12px;
    line-height: 1.4;
    margin-top: 10px;
    border-radius: 12px;
}

.notice {
    background: #FFF8E8;
    border: 1px solid #F0DB9B;
    border-left: 6px solid var(--gold);
    padding: 22px;
    border-radius: 22px;
    margin: 18px 0;
    box-sizing: border-box;
}

.green-notice {
    background: #EAF7F4;
    border: 1px solid #BFE4DC;
    border-left: 6px solid var(--green);
    padding: 22px;
    border-radius: 22px;
    margin: 18px 0;
    box-sizing: border-box;
}

.step {
    background: white;
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 24px;
    box-sizing: border-box;
    overflow: hidden;
}

.step-number {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: var(--navy);
    color: white;
    display: grid;
    place-items: center;
    font-weight: 900;
    margin-bottom: 12px;
}

.footer {
    background:
        radial-gradient(circle at top right, rgba(200,169,106,0.20), transparent 30%),
        linear-gradient(135deg, #061A35 0%, #0B2545 58%, #0F766E 100%);
    color: white;
    border-radius: 28px;
    padding: 38px 34px;
    margin-top: 34px;
    box-sizing: border-box;
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
    .grid-3 {
        grid-template-columns: 1fr;
    }

    .grid-2 {
        grid-template-columns: 1fr;
    }

    .review-cover-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .service-card-slider {
        min-height: auto;
    }

    .service-slide {
        min-height: auto;
    }
}

@media (max-width: 900px) {
    .block-container {
        padding-left: 0.9rem !important;
        padding-right: 0.9rem !important;
        max-width: 100vw !important;
        width: 100% !important;
    }

    [data-testid="stImage"] {
        max-width: 118px !important;
    }

    [data-testid="stImage"] img {
        max-width: 118px !important;
        width: 118px !important;
        height: auto !important;
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
        overflow-wrap: normal;
        word-break: normal;
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

    .card,
    .service-card-slider {
        padding: 22px;
        border-radius: 24px;
    }

    .problem-strip {
        padding: 24px;
    }

    .review-cover-grid {
        grid-template-columns: 1fr;
        gap: 10px;
    }

    .review-cover-item {
        padding: 13px 14px;
        min-height: auto;
    }

    .review-cover-item p {
        font-size: 16px;
    }

    p, li {
        font-size: 17px;
    }

    .btn-primary,
    .btn-secondary,
    .btn-light,
    .btn-dark {
        width: 100%;
        text-align: center;
        display: block;
    }

    .slide-indicators {
        grid-template-columns: 1fr;
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

    .footer-icon-row {
        justify-content: flex-start;
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
# REVIEW COVERAGE SECTION
# =========================================================
html("""
<div class="section">
    <h2>What the £149 review covers.</h2>
    <p class="section-intro">
    A practical review of the core evidence areas care providers are expected to keep organised, current, and ready to explain.
    </p>
</div>

<div class="review-cover-grid">
    <div class="review-cover-item">
        <div class="review-cover-icon">□</div>
        <p>Policies and procedures</p>
    </div>
    <div class="review-cover-item">
        <div class="review-cover-icon">✓</div>
        <p>Risk assessments</p>
    </div>
    <div class="review-cover-item">
        <div class="review-cover-icon">▤</div>
        <p>Training matrix</p>
    </div>
    <div class="review-cover-item">
        <div class="review-cover-icon">!</div>
        <p>Incidents and complaints logs</p>
    </div>
    <div class="review-cover-item">
        <div class="review-cover-icon">○</div>
        <p>Safeguarding records</p>
    </div>
    <div class="review-cover-item">
        <div class="review-cover-icon">☑</div>
        <p>Audit tracker</p>
    </div>
    <div class="review-cover-item">
        <div class="review-cover-icon">◉</div>
        <p>Governance minutes</p>
    </div>
    <div class="review-cover-item">
        <div class="review-cover-icon">⌂</div>
        <p>GDPR and data handling</p>
    </div>
</div>

<div class="review-cover-note">
    The review identifies whether these records are structured, traceable, current, and suitable for management review.
</div>
""")

# =========================================================
# SERVICES WITH INTEGRATED SLIDES
# =========================================================
html('<div id="services"></div>')

html("""
<div class="section">
    <h2>Select the level of support that matches your evidence position.</h2>
    <p class="section-intro">
    Each service card includes a quick overview, detail of what Nexus does, and a sample-style preview of the type of output the client may receive.
    </p>
</div>
""")

html(f"""
<div class="grid-3">

    <div class="service-card-slider">
        <input class="service-radio" type="radio" name="review-service" id="review-overview" checked>
        <input class="service-radio" type="radio" name="review-service" id="review-details">
        <input class="service-radio" type="radio" name="review-service" id="review-sample">

        <div class="service-slides">
            <div class="service-slide review-overview">
                <span class="badge-gold">Fixed first step</span>
                <h3>£149 CQC Evidence File Review</h3>
                <div class="price">£149</div>
                <p>A focused review for providers that need a clear evidence assessment before deciding whether deeper support is required.</p>
                <ul>
                    <li>Evidence structure review</li>
                    <li>Gap notes on weak or unclear records</li>
                    <li>Priority action direction</li>
                    <li>Written summary of next steps</li>
                </ul>
                <a class="btn-dark" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Buy Now</a>
            </div>

            <div class="service-slide review-details">
                <span class="badge-gold">What Nexus checks</span>
                <h3>What the review gives you.</h3>
                <p>The review is designed to help a manager understand the evidence position before committing to a larger package.</p>
                <div class="result-grid">
                    <div class="result-box"><strong>Evidence structure check</strong><span>How policies, trackers, audits, risk records, complaints, and governance evidence are arranged.</span></div>
                    <div class="result-box"><strong>Gap notes</strong><span>Weak, unclear, missing, outdated, or hard-to-explain records are identified.</span></div>
                    <div class="result-box"><strong>Priority direction</strong><span>The output shows what should be addressed first.</span></div>
                    <div class="result-box"><strong>Decision point</strong><span>The provider can decide whether a cleanup sprint or monthly support is justified.</span></div>
                </div>
            </div>

            <div class="service-slide review-sample">
                <span class="badge-gold">Sample-style output</span>
                <h3>Evidence review preview.</h3>
                <p>Sample visual only. Final output depends on the documents received.</p>
                <div class="sample-collage">
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Evidence Gap Summary.pdf</strong><span>Review extract</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Risk assessments</span><span class="sample-status">Check</span></div>
                            <div class="sample-row"><span>Training matrix</span><span class="sample-status red">Weak</span></div>
                            <div class="sample-row"><span>Audit tracker</span><span class="sample-status">Update</span></div>
                            <div class="sample-row"><span>Governance minutes</span><span class="sample-status green">Present</span></div>
                        </div>
                    </div>
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Priority Action Direction.xlsx</strong><span>Tracker view</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Update audit tracker</span><span class="sample-status">Priority</span></div>
                            <div class="sample-row"><span>Review complaints log</span><span class="sample-status">Check</span></div>
                            <div class="sample-row"><span>Confirm GDPR evidence</span><span class="sample-status red">Gap</span></div>
                        </div>
                    </div>
                    <div class="sample-note">The client receives a clear evidence position with practical next steps, not a generic document pack.</div>
                </div>
            </div>
        </div>

        <div class="slide-indicators">
            <label for="review-overview">1 Overview</label>
            <label for="review-details">2 Details</label>
            <label for="review-sample">3 Sample</label>
        </div>
    </div>

    <div class="service-card-slider">
        <input class="service-radio" type="radio" name="cleanup-service" id="cleanup-overview" checked>
        <input class="service-radio" type="radio" name="cleanup-service" id="cleanup-details">
        <input class="service-radio" type="radio" name="cleanup-service" id="cleanup-sample">

        <div class="service-slides">
            <div class="service-slide cleanup-overview">
                <span class="badge">Scoped private Payhip link</span>
                <h3>30-Day CQC Evidence Cleanup Sprint</h3>
                <div class="price">From £750</div>
                <p>For providers that need structured cleanup of evidence folders, trackers, policies, and management review records.</p>
                <ul>
                    <li>Scoped after intake review</li>
                    <li>Evidence folder organisation</li>
                    <li>Tracker and document-control cleanup</li>
                    <li>Preview before final balance</li>
                </ul>
                <a class="btn-dark" href="#request">Request Scope Review</a>
            </div>

            <div class="service-slide cleanup-details">
                <span class="badge">What Nexus does</span>
                <h3>What the cleanup sprint includes.</h3>
                <p>This service turns scattered evidence into a clearer working evidence pack.</p>
                <div class="result-grid">
                    <div class="result-box"><strong>Audit tracker update</strong><span>Actions, dates, owners, status, and follow-up points are made clearer.</span></div>
                    <div class="result-box"><strong>Incident and complaints logs</strong><span>Structure, missing fields, action links, trend visibility, and closure status are reviewed.</span></div>
                    <div class="result-box"><strong>Evidence index</strong><span>Records are grouped so the manager can locate what exists and what remains outstanding.</span></div>
                    <div class="result-box"><strong>Handover summary</strong><span>The client receives a clear summary of completed work, key gaps, and recommended next actions.</span></div>
                </div>
            </div>

            <div class="service-slide cleanup-sample">
                <span class="badge">Sample-style output</span>
                <h3>Cleanup package preview.</h3>
                <p>Sample visual only. Final files depend on the agreed scope.</p>
                <div class="sample-collage">
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Audit Tracker.xlsx</strong><span>Updated tracker</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Medication audit</span><span class="sample-status green">Closed</span></div>
                            <div class="sample-row"><span>Care plan audit</span><span class="sample-status">Open</span></div>
                            <div class="sample-row"><span>Staff file audit</span><span class="sample-status red">Overdue</span></div>
                        </div>
                    </div>
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Incident Log.xlsx</strong><span>Cleaned log</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Incident type</span><span class="sample-status green">Added</span></div>
                            <div class="sample-row"><span>Follow-up action</span><span class="sample-status">Review</span></div>
                            <div class="sample-row"><span>Manager sign-off</span><span class="sample-status red">Missing</span></div>
                        </div>
                    </div>
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Complaints Log.xlsx</strong><span>Review status</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Outcome recorded</span><span class="sample-status">Partial</span></div>
                            <div class="sample-row"><span>Learning captured</span><span class="sample-status red">Gap</span></div>
                            <div class="sample-row"><span>Closed status</span><span class="sample-status">Check</span></div>
                        </div>
                    </div>
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Evidence Index.xlsx</strong><span>Folder map</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Policies</span><span class="sample-status green">Indexed</span></div>
                            <div class="sample-row"><span>Risk records</span><span class="sample-status">Check</span></div>
                            <div class="sample-row"><span>Governance minutes</span><span class="sample-status green">Mapped</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="slide-indicators">
            <label for="cleanup-overview">1 Overview</label>
            <label for="cleanup-details">2 Details</label>
            <label for="cleanup-sample">3 Sample</label>
        </div>
    </div>

    <div class="service-card-slider">
        <input class="service-radio" type="radio" name="retainer-service" id="retainer-overview" checked>
        <input class="service-radio" type="radio" name="retainer-service" id="retainer-details">
        <input class="service-radio" type="radio" name="retainer-service" id="retainer-sample">

        <div class="service-slides">
            <div class="service-slide retainer-overview">
                <span class="badge">Scoped private Payhip link</span>
                <h3>Monthly Compliance Retainer</h3>
                <div class="price">Scoped</div>
                <p>For providers that need continued support with evidence tracking, action follow-up, document control, and monthly review records.</p>
                <ul>
                    <li>Monthly support after scope review</li>
                    <li>Evidence and action tracker updates</li>
                    <li>Policy and documentation support</li>
                    <li>Monthly management summary</li>
                </ul>
                <a class="btn-dark" href="#request">Request Retainer Scope</a>
            </div>

            <div class="service-slide retainer-details">
                <span class="badge">What Nexus does</span>
                <h3>What monthly support maintains.</h3>
                <p>This service supports evidence discipline so records do not fall behind after the first review or cleanup.</p>
                <div class="result-grid">
                    <div class="result-box"><strong>Monthly evidence check</strong><span>Selected evidence areas are reviewed and flagged for action.</span></div>
                    <div class="result-box"><strong>Action tracker follow-up</strong><span>Owners, due dates, open items, and status updates are maintained.</span></div>
                    <div class="result-box"><strong>Document-control support</strong><span>Policy lists, review dates, version control, and evidence indexing are supported.</span></div>
                    <div class="result-box"><strong>Management summary</strong><span>A concise monthly summary helps internal governance and follow-up.</span></div>
                </div>
            </div>

            <div class="service-slide retainer-sample">
                <span class="badge">Sample-style output</span>
                <h3>Monthly support preview.</h3>
                <p>Sample visual only. Monthly outputs are agreed after scope review.</p>
                <div class="sample-collage">
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Monthly Evidence Dashboard.xlsx</strong><span>Status view</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Policies reviewed</span><span class="sample-status green">4</span></div>
                            <div class="sample-row"><span>Trackers updated</span><span class="sample-status green">3</span></div>
                            <div class="sample-row"><span>High priority items</span><span class="sample-status red">2</span></div>
                        </div>
                    </div>
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Action Tracker Update.xlsx</strong><span>Month-end</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Owner assigned</span><span class="sample-status green">Yes</span></div>
                            <div class="sample-row"><span>Due dates added</span><span class="sample-status green">Yes</span></div>
                            <div class="sample-row"><span>Overdue items</span><span class="sample-status red">Review</span></div>
                        </div>
                    </div>
                    <div class="sample-frame">
                        <div class="sample-top"><strong>Governance Summary.docx</strong><span>Monthly note</span></div>
                        <div class="sample-table">
                            <div class="sample-row"><span>Management review</span><span class="sample-status">Prepared</span></div>
                            <div class="sample-row"><span>Risk points</span><span class="sample-status red">2</span></div>
                            <div class="sample-row"><span>Next actions</span><span class="sample-status green">Listed</span></div>
                        </div>
                    </div>
                    <div class="sample-note">The monthly retainer keeps the evidence position visible, current, and easier to review.</div>
                </div>
            </div>
        </div>

        <div class="slide-indicators">
            <label for="retainer-overview">1 Overview</label>
            <label for="retainer-details">2 Details</label>
            <label for="retainer-sample">3 Sample</label>
        </div>
    </div>

</div>
""")

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
""")

html("""
<div class="grid-2">
    <div class="card">
        <h3>Evidence-led review</h3>
        <p>The review considers whether records support management control, monitoring, review, and improvement.</p>
    </div>
    <div class="card">
        <h3>Decision-ready output</h3>
        <p>The summary helps managers understand the evidence position and decide whether further cleanup is required.</p>
    </div>
    <div class="card">
        <h3>Practical action points</h3>
        <p>The focus is on clear next steps, not generic templates or broad commentary.</p>
    </div>
    <div class="card">
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

html("""
<div class="grid-3">
    <div class="step">
        <div class="step-number">1</div>
        <h3>Choose the route</h3>
        <p>Buy the £149 review directly, or submit the intake form for scoped support such as the 30-Day Sprint or Monthly Retainer.</p>
    </div>
    <div class="step">
        <div class="step-number">2</div>
        <h3>Submit evidence</h3>
        <p>Upload redacted documents such as folder indexes, trackers, policies, audit summaries, risk registers, or training matrices.</p>
    </div>
    <div class="step">
        <div class="step-number">3</div>
        <h3>Receive the outcome</h3>
        <p>Fixed reviews are delivered after payment and intake. Custom work uses a 40% Payhip deposit, preview or summary, then final Payhip balance before file release.</p>
    </div>
</div>
""")

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
# REQUEST FORM WITH UPLOAD
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