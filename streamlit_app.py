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
    if hasattr(st, "html"):
        st.html(clean_source)
    else:
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

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stToolbar"] {visibility: hidden;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}

html, body, .stApp {
    overflow-x: hidden;
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
}

.brand-title {
    font-size: 26px;
    font-weight: 800;
    color: var(--navy);
    margin: 0;
}

.brand-subtitle {
    color: var(--muted);
    font-size: 15px;
    margin-top: 4px;
}

.nav-pills {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: flex-end;
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
}

.hero h1 {
    color: white;
    font-size: clamp(38px, 5vw, 60px);
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
}

@media (max-width: 900px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
    }

    .topbar {
        display: block;
    }

    .nav-pills {
        justify-content: flex-start;
        margin-top: 16px;
    }

    .nav-pills a {
        font-size: 13px;
        padding: 9px 12px;
    }

    .hero {
        padding: 42px 24px;
        border-radius: 28px;
    }

    .hero h1 {
        line-height: 1.08;
    }

    .hero p {
        font-size: 18px;
    }

    .card {
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
</style>
""")

# =========================================================
# HEADER
# =========================================================
if LOGO_PATH:
    st.image(LOGO_PATH, width=135)

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
# SERVICES
# =========================================================
html('<div id="services"></div>')

html("""
<div class="section">
    <h2>Select the level of support that matches your evidence position.</h2>
    <p class="section-intro">
    The £149 CQC Evidence File Review is a fixed first step. Larger services are scoped privately because the level of work depends on document volume,
    urgency, evidence quality, and the final delivery package required.
    </p>
</div>
""")

html(f"""
<div class="grid-3">
    <div class="card">
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
    <div class="card">
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
    <div class="card">
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
</div>
""")

# =========================================================
# SERVICE DETAIL CAROUSEL
# =========================================================
components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
:root {
    --navy: #061A35;
    --navy2: #0B2545;
    --gold: #C8A96A;
    --green: #0F766E;
    --text: #172033;
    --muted: #6B7280;
    --line: #E5E7EB;
    --cream: #FAF7F0;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: transparent;
    color: var(--text);
}

.carousel-shell {
    background:
        radial-gradient(circle at top right, rgba(200,169,106,0.18), transparent 28%),
        linear-gradient(135deg, #FFFFFF 0%, #FAF7F0 100%);
    border: 1px solid var(--line);
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 16px 42px rgba(15,23,42,0.06);
    overflow: hidden;
}

.carousel-top {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    align-items: flex-start;
    margin-bottom: 20px;
}

.carousel-eyebrow {
    color: #8A6519;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 8px;
}

.carousel-top h2 {
    color: var(--navy);
    font-size: 34px;
    line-height: 1.1;
    margin: 0;
    letter-spacing: -0.04em;
}

.carousel-top p {
    color: var(--muted);
    font-size: 16px;
    line-height: 1.55;
    max-width: 560px;
    margin: 8px 0 0 0;
}

.carousel-controls {
    display: flex;
    gap: 10px;
    flex: 0 0 auto;
}

.carousel-btn {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: 1px solid rgba(6,26,53,0.16);
    background: #FFFFFF;
    color: var(--navy);
    font-size: 22px;
    font-weight: 900;
    cursor: pointer;
}

.carousel-btn:hover {
    background: var(--navy);
    color: white;
}

.slide-frame {
    position: relative;
    min-height: 500px;
}

.nc-slide {
    display: none;
    animation: fadeIn 0.35s ease;
}

.nc-slide.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

.slide-card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 24px;
    padding: 26px;
    min-height: 485px;
}

.service-tag {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 999px;
    background: #EEF8F5;
    border: 1px solid #CDEBE4;
    color: var(--green);
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 12px;
}

.service-tag.gold {
    background: #FFF8E8;
    border-color: #F0DB9B;
    color: #7A5C13;
}

.slide-card h3 {
    color: var(--navy);
    font-size: 28px;
    margin: 0 0 10px 0;
    letter-spacing: -0.03em;
}

.slide-card p {
    font-size: 16px;
    line-height: 1.55;
    color: #374151;
    margin-top: 0;
}

.detail-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
    margin-top: 18px;
}

.detail-box {
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 16px;
    background: #FBFCFE;
}

.detail-box strong {
    display: block;
    color: var(--navy);
    font-size: 15px;
    margin-bottom: 6px;
}

.detail-box span {
    color: #4B5563;
    font-size: 14px;
    line-height: 1.45;
}

.mini-collage {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 18px;
}

.mini-sheet {
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 14px;
    background: #FBFCFE;
    min-height: 210px;
}

.mini-sheet h4 {
    color: var(--navy);
    font-size: 15px;
    margin: 0 0 10px 0;
}

.mini-row {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 8px;
    border-top: 1px solid #EDF0F5;
    padding: 8px 0;
    font-size: 12px;
    color: #374151;
}

.status {
    border-radius: 999px;
    padding: 4px 7px;
    font-size: 11px;
    font-weight: 800;
    background: #FFF8E8;
    color: #7A5C13;
}

.status.green {
    background: #EAF7F4;
    color: #0F766E;
}

.status.red {
    background: #FEECEC;
    color: #991B1B;
}

.dots {
    display: flex;
    justify-content: center;
    gap: 7px;
    margin-top: 18px;
}

.dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #D1D5DB;
}

.dot.active {
    background: var(--gold);
}

@media (max-width: 760px) {
    .carousel-shell {
        padding: 22px;
        border-radius: 24px;
    }

    .carousel-top {
        display: block;
    }

    .carousel-controls {
        margin-top: 14px;
    }

    .carousel-top h2 {
        font-size: 28px;
    }

    .slide-frame {
        min-height: 610px;
    }

    .slide-card {
        min-height: 590px;
        padding: 20px;
    }

    .slide-card h3 {
        font-size: 24px;
    }

    .detail-grid,
    .mini-collage {
        grid-template-columns: 1fr;
    }

    .mini-sheet {
        min-height: auto;
    }
}
</style>
</head>
<body>
<div class="carousel-shell">
    <div class="carousel-top">
        <div>
            <div class="carousel-eyebrow">Service detail preview</div>
            <h2>See what each service is designed to produce.</h2>
            <p>Use the arrows to move through the service detail slides. The section also rotates automatically.</p>
        </div>
        <div class="carousel-controls">
            <button class="carousel-btn" onclick="prevSlide()" aria-label="Previous slide">‹</button>
            <button class="carousel-btn" onclick="nextSlide()" aria-label="Next slide">›</button>
        </div>
    </div>

    <div class="slide-frame">

        <div class="nc-slide active">
            <div class="slide-card">
                <span class="service-tag gold">£149 Evidence File Review · What you receive</span>
                <h3>A focused review of your evidence position.</h3>
                <p>The review gives the manager a clear first assessment before deciding whether deeper cleanup is needed.</p>
                <div class="detail-grid">
                    <div class="detail-box"><strong>Evidence structure check</strong><span>Review of how policies, trackers, audits, risk records, complaints, and governance evidence are arranged.</span></div>
                    <div class="detail-box"><strong>Gap notes</strong><span>Identification of weak, unclear, missing, outdated, or hard-to-explain records.</span></div>
                    <div class="detail-box"><strong>Priority actions</strong><span>A practical action direction so the manager can see what needs attention first.</span></div>
                    <div class="detail-box"><strong>Written summary</strong><span>A concise review outcome suitable for internal follow-up and service planning.</span></div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag gold">£149 Evidence File Review · Result</span>
                <h3>Clearer judgement before spending more.</h3>
                <p>The result is a practical evidence summary, not a generic template pack.</p>
                <div class="detail-grid">
                    <div class="detail-box"><strong>Manager clarity</strong><span>Know whether the evidence is organised, traceable, and ready to explain.</span></div>
                    <div class="detail-box"><strong>Risk visibility</strong><span>See where document gaps may create pressure during review, inspection, or internal checks.</span></div>
                    <div class="detail-box"><strong>Decision point</strong><span>Decide whether a 30-Day Cleanup Sprint or monthly support is justified.</span></div>
                    <div class="detail-box"><strong>Low-risk entry</strong><span>Start with a fixed £149 review before committing to a larger service.</span></div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag gold">£149 Evidence File Review · Sample preview</span>
                <h3>Example of the type of output reviewed.</h3>
                <p>Sample visual only. Final output depends on the documents received.</p>
                <div class="mini-collage">
                    <div class="mini-sheet">
                        <h4>Evidence Gap Summary</h4>
                        <div class="mini-row"><span>Risk assessments</span><span class="status">Check</span></div>
                        <div class="mini-row"><span>Training matrix</span><span class="status red">Weak</span></div>
                        <div class="mini-row"><span>Audit tracker</span><span class="status">Update</span></div>
                        <div class="mini-row"><span>Governance minutes</span><span class="status green">Present</span></div>
                    </div>
                    <div class="mini-sheet">
                        <h4>Action Direction</h4>
                        <div class="mini-row"><span>Update audit tracker</span><span class="status">Priority</span></div>
                        <div class="mini-row"><span>Index policies</span><span class="status green">Next</span></div>
                        <div class="mini-row"><span>Review complaints log</span><span class="status">Check</span></div>
                        <div class="mini-row"><span>Confirm GDPR evidence</span><span class="status red">Gap</span></div>
                    </div>
                    <div class="mini-sheet">
                        <h4>Manager Summary</h4>
                        <div class="mini-row"><span>Evidence structure</span><span class="status">Mixed</span></div>
                        <div class="mini-row"><span>Traceability</span><span class="status red">Weak</span></div>
                        <div class="mini-row"><span>Immediate action</span><span class="status">Yes</span></div>
                        <div class="mini-row"><span>Cleanup needed</span><span class="status green">Likely</span></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag">30-Day Cleanup Sprint · What Nexus does</span>
                <h3>Structured cleanup of the evidence file.</h3>
                <p>This service is for providers that already have records but need them organised, updated, and easier to manage.</p>
                <div class="detail-grid">
                    <div class="detail-box"><strong>Evidence folder structure</strong><span>Organise the evidence file around core review areas and management visibility.</span></div>
                    <div class="detail-box"><strong>Audit tracker cleanup</strong><span>Update or rebuild the tracker so actions, dates, owners, and status are clearer.</span></div>
                    <div class="detail-box"><strong>Incident and complaints logs</strong><span>Review structure, missing fields, action links, and follow-up visibility.</span></div>
                    <div class="detail-box"><strong>Governance summary</strong><span>Prepare a clearer management summary of what was cleaned, updated, and still needs attention.</span></div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag">30-Day Cleanup Sprint · Result</span>
                <h3>A clearer evidence pack managers can use.</h3>
                <p>The work is designed to make records easier to locate, explain, and maintain.</p>
                <div class="detail-grid">
                    <div class="detail-box"><strong>Updated tracker position</strong><span>Audit, action, incident, or complaints trackers become easier to read and follow up.</span></div>
                    <div class="detail-box"><strong>Cleaner evidence structure</strong><span>Folders and records are arranged so the manager can see what exists and what remains outstanding.</span></div>
                    <div class="detail-box"><strong>Stronger management review</strong><span>Evidence becomes more suitable for internal review, governance meetings, and action monitoring.</span></div>
                    <div class="detail-box"><strong>Final handover summary</strong><span>The client receives a summary of completed work, key gaps, and recommended next steps.</span></div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag">30-Day Cleanup Sprint · Sample preview</span>
                <h3>Example cleanup outputs.</h3>
                <p>Sample visual only. Final files depend on the scope agreed after intake.</p>
                <div class="mini-collage">
                    <div class="mini-sheet">
                        <h4>Audit Tracker</h4>
                        <div class="mini-row"><span>Medication audit</span><span class="status green">Closed</span></div>
                        <div class="mini-row"><span>Care plan audit</span><span class="status">Open</span></div>
                        <div class="mini-row"><span>Staff file audit</span><span class="status red">Overdue</span></div>
                        <div class="mini-row"><span>Action owner added</span><span class="status green">Yes</span></div>
                    </div>
                    <div class="mini-sheet">
                        <h4>Incident Log</h4>
                        <div class="mini-row"><span>Incident type</span><span class="status green">Added</span></div>
                        <div class="mini-row"><span>Follow-up action</span><span class="status">Review</span></div>
                        <div class="mini-row"><span>Trend field</span><span class="status">Added</span></div>
                        <div class="mini-row"><span>Manager sign-off</span><span class="status red">Missing</span></div>
                    </div>
                    <div class="mini-sheet">
                        <h4>Complaints Log</h4>
                        <div class="mini-row"><span>Date received</span><span class="status green">Clear</span></div>
                        <div class="mini-row"><span>Outcome recorded</span><span class="status">Partial</span></div>
                        <div class="mini-row"><span>Learning captured</span><span class="status red">Gap</span></div>
                        <div class="mini-row"><span>Closed status</span><span class="status">Check</span></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag">Monthly Retainer · What Nexus does</span>
                <h3>Ongoing support for evidence discipline.</h3>
                <p>This service is for providers that need monthly structure, follow-up, and documentation support after review or cleanup.</p>
                <div class="detail-grid">
                    <div class="detail-box"><strong>Monthly evidence check</strong><span>Review selected evidence areas and identify records needing attention.</span></div>
                    <div class="detail-box"><strong>Action tracker follow-up</strong><span>Update action status, owner fields, due dates, and outstanding items.</span></div>
                    <div class="detail-box"><strong>Document-control support</strong><span>Support policy lists, version control, review dates, and evidence indexing.</span></div>
                    <div class="detail-box"><strong>Management summary</strong><span>Prepare a short monthly summary for internal governance and follow-up.</span></div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag">Monthly Retainer · Result</span>
                <h3>Records stay current instead of falling behind.</h3>
                <p>The aim is to support consistent evidence maintenance, not last-minute document pressure.</p>
                <div class="detail-grid">
                    <div class="detail-box"><strong>Ongoing visibility</strong><span>Managers can see current actions, overdue items, and priority document gaps.</span></div>
                    <div class="detail-box"><strong>Better governance records</strong><span>Monthly updates help evidence show review, follow-up, and improvement activity.</span></div>
                    <div class="detail-box"><strong>Reduced drift</strong><span>Policies, trackers, and action logs are less likely to become outdated or inconsistent.</span></div>
                    <div class="detail-box"><strong>Clear month-end position</strong><span>The provider receives a concise update on what changed and what needs action next.</span></div>
                </div>
            </div>
        </div>

        <div class="nc-slide">
            <div class="slide-card">
                <span class="service-tag">Monthly Retainer · Sample preview</span>
                <h3>Example monthly management view.</h3>
                <p>Sample visual only. Monthly outputs are agreed after scope review.</p>
                <div class="mini-collage">
                    <div class="mini-sheet">
                        <h4>Monthly Evidence Status</h4>
                        <div class="mini-row"><span>Policies reviewed</span><span class="status green">4</span></div>
                        <div class="mini-row"><span>Trackers updated</span><span class="status green">3</span></div>
                        <div class="mini-row"><span>Open actions</span><span class="status">6</span></div>
                        <div class="mini-row"><span>High priority</span><span class="status red">2</span></div>
                    </div>
                    <div class="mini-sheet">
                        <h4>Action Tracker</h4>
                        <div class="mini-row"><span>Owner assigned</span><span class="status green">Yes</span></div>
                        <div class="mini-row"><span>Due dates added</span><span class="status green">Yes</span></div>
                        <div class="mini-row"><span>Overdue items</span><span class="status red">Review</span></div>
                        <div class="mini-row"><span>Closed this month</span><span class="status">3</span></div>
                    </div>
                    <div class="mini-sheet">
                        <h4>Governance Note</h4>
                        <div class="mini-row"><span>Management review</span><span class="status">Prepared</span></div>
                        <div class="mini-row"><span>Risk points</span><span class="status red">2</span></div>
                        <div class="mini-row"><span>Next actions</span><span class="status green">Listed</span></div>
                        <div class="mini-row"><span>Month-end summary</span><span class="status green">Ready</span></div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <div class="dots" id="dots"></div>
</div>

<script>
let currentSlide = 0;
const slides = document.querySelectorAll(".nc-slide");
const dotsContainer = document.getElementById("dots");

slides.forEach(function(_, i) {
    const dot = document.createElement("div");
    dot.className = "dot" + (i === 0 ? " active" : "");
    dot.onclick = function() { showSlide(i); };
    dotsContainer.appendChild(dot);
});

const dots = document.querySelectorAll(".dot");

function showSlide(index) {
    slides[currentSlide].classList.remove("active");
    dots[currentSlide].classList.remove("active");
    currentSlide = (index + slides.length) % slides.length;
    slides[currentSlide].classList.add("active");
    dots[currentSlide].classList.add("active");
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}

setInterval(nextSlide, 7000);
</script>
</body>
</html>
""", height=840, scrolling=False)

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