import streamlit as st
import os
import glob
import textwrap
import base64
import mimetypes
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIG (Clean, Professional institutional Layout)
# =========================================================
st.set_page_config(
    page_title="Nexus Conformité | CQC Evidence Architecture & Inspection Readiness",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# BUSINESS DETAILS & ASYMMETRIC ANCHORING
# =========================================================
BUSINESS_NAME = "Nexus Conformité"
EMAIL = "nexusconformite@proton.me"
FACEBOOK_URL = "https://www.facebook.com/nexusconformite"
PAYHIP_URL = "https://payhip.com/NexusConformite"
LINKEDIN_URL = "https://www.linkedin.com/company/nexus-conformit%C3%A9/"
LINKEDIN_NAME = "Nexus Conformité"

CQC_REVIEW_CHECKOUT_URL = "https://payhip.com/buy?link=9OUm6"

# =========================================================
# META PIXEL CONTROL
# =========================================================
META_PIXEL_CODE = """
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
<img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=1010121488430688&ev=PageView&noscript=1"/>
</noscript>
"""
components.html(META_PIXEL_CODE, height=1, scrolling=False)

def html(source: str):
    st.markdown(textwrap.dedent(source).strip(), unsafe_allow_html=True)

# =========================================================
# LOGO RETRIEVAL UTILITIES
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
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

LOGO_DATA_URI = image_to_data_uri(LOGO_PATH)

# =========================================================
# OPTIMIZED CSS (High Trust Typography & Focus Zones)
# =========================================================
html("""
<style>
:root {
    --navy: #05162E;
    --navy2: #0B2545;
    --gold: #C8A96A;
    --gold-hover: #B59353;
    --teal: #0D9488;
    --bg-gradient: linear-gradient(180deg, #FFFFFF 0%, #F4F6F9 40%, #FDFBF7 100%);
    --text: #1E293B;
    --muted: #64748B;
    --line: #E2E8F0;
}

* { box-sizing: border-box; }
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none; }

html, body, .stApp {
    overflow-x: hidden !important;
    max-width: 100vw !important;
}

.stApp {
    background: var(--bg-gradient);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 5rem;
}

h1, h2, h3 {
    color: var(--navy);
    font-weight: 800;
    letter-spacing: -0.03em;
}

p, li {
    font-size: 17px;
    line-height: 1.65;
    color: var(--text);
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0 24px 0;
}

.brand-title {
    font-size: 28px;
    font-weight: 900;
    color: var(--navy);
    margin: 0;
}

.brand-subtitle {
    color: var(--muted);
    font-size: 14px;
    margin-top: 2px;
}

.nav-pills {
    display: flex;
    gap: 8px;
}

.nav-pills a {
    padding: 8px 16px;
    border-radius: 999px;
    background: white;
    border: 1px solid var(--line);
    color: var(--navy) !important;
    text-decoration: none;
    font-size: 13px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.nav-pills a:hover {
    border-color: var(--gold);
    background: #FFFDF9;
}

/* Hero Section Optimized for Loss Aversion & Urgency */
.hero {
    background: linear-gradient(135deg, #05162E 0%, #0B2545 60%, #064E3B 100%);
    border-radius: 24px;
    padding: 60px 50px;
    margin-bottom: 30px;
    box-shadow: 0 20px 50px rgba(5,22,46,0.15);
}

.hero h1 {
    color: white;
    font-size: clamp(34px, 4.5vw, 54px);
    line-height: 1.1;
    margin-bottom: 20px;
}

.hero p {
    color: #E2E8F0;
    font-size: clamp(17px, 1.8vw, 20px);
    max-width: 820px;
    margin-bottom: 30px;
}

.eyebrow {
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 12px;
    display: inline-block;
    background: rgba(200,169,106,0.15);
    padding: 4px 12px;
    border-radius: 4px;
}

.badge-tag {
    background: #E11D48;
    color: white;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
    margin-bottom: 10px;
    display: inline-block;
}

.cta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.btn-primary {
    background: var(--gold);
    color: var(--navy) !important;
    font-weight: 800;
    padding: 14px 28px;
    border-radius: 999px;
    text-decoration: none;
    box-shadow: 0 4px 14px rgba(200,169,106,0.3);
    transition: transform 0.2s;
}

.btn-primary:hover {
    transform: translateY(-1px);
    background: var(--gold-hover);
}

.btn-secondary {
    background: white;
    color: var(--navy) !important;
    font-weight: 700;
    padding: 14px 28px;
    border-radius: 999px;
    text-decoration: none;
    border: 1px solid var(--line);
}

.btn-light {
    background: rgba(255,255,255,0.1);
    color: white !important;
    font-weight: 700;
    padding: 14px 28px;
    border-radius: 999px;
    text-decoration: none;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Psychological Pain Point Banner */
.pain-banner {
    background: #FFFFFF;
    border-left: 6px solid #E11D48;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    margin-bottom: 40px;
}

.pain-banner h2 {
    font-size: clamp(24px, 3vw, 32px);
    margin: 0 0 10px 0;
}

/* Psychological Badges for Choice Architecture */
.tier-tag {
    font-size: 11px;
    font-weight: 900;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 999px;
    display: inline-block;
    margin-bottom: 8px;
}
.tag-popular { background: #FEF3C7; color: #92400E; }
.tag-sprint { background: #E0F2FE; color: #0369A1; }
.tag-retainer { background: #E1F5FE; color: #0288D1; }

.review-cover-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 20px;
}

.review-cover-item {
    background: white;
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.review-cover-icon {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #FFFDF5;
    border: 1px solid var(--gold);
    color: var(--gold);
    display: grid;
    place-items: center;
    font-weight: 900;
    flex-shrink: 0;
}

.review-cover-item p {
    margin: 0;
    font-size: 15px;
    font-weight: 700;
    color: var(--navy);
}

.notice {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    border-left: 6px solid var(--gold);
    padding: 24px;
    border-radius: 16px;
    margin: 30px 0;
}

.green-notice {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-left: 6px solid var(--teal);
    padding: 24px;
    border-radius: 16px;
    margin: 30px 0;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.step-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 24px;
}

@media (max-width: 900px) {
    .review-cover-grid { grid-template-columns: repeat(2, 1fr); }
    .grid-2 { grid-template-columns: 1fr; }
    .topbar { flex-direction: column; align-items: flex-start; gap: 16px; }
    .nav-pills { width: 100%; display: grid; grid-template-columns: repeat(2, 1fr); }
    .nav-pills a { text-align: center; }
}
</style>
""")

# =========================================================
# TRUST-ANCHORED BRAND HEADER (Routing Tuned to #request)
# =========================================================
if LOGO_PATH:
    st.image(LOGO_PATH, width=118)

html(f"""
<div class="topbar" id="top">
    <div>
        <p class="brand-title">Nexus Conformité</p>
        <p class="brand-subtitle">CQC Evidence Architecture • Inspection Defense Systems • Governance Engineering</p>
    </div>
    <div class="nav-pills">
        <a href="#services">Inspection Frameworks</a>
        <a href="#process">Verification Process</a>
        <a href="#faq">Systemic FAQ</a>
        <a href="#request">Contact Advisory / Intake</a>
    </div>
</div>
""")

# =========================================================
# HIGH-CONVERSION HERO (Loss Aversion Engine)
# =========================================================
html(f"""
<div class="hero">
    <span class="badge-tag">🚨 Inspection Exposure Prevention</span><br>
    <div class="eyebrow">UK Adult Social Care Compliance Architecture</div>
    <h1>Stop Guessing Your Inspection Readiness.<br>Expose Your Evidence Gaps Before the CQC Does.</h1>
    <p>
    A template repository won't defend your registration. In a hard regulatory evaluation, undocumented execution equals failure. 
    The <b>£149 Evidence File Review</b> functions as an objective structural audit—giving you an explicit, risk-mapped 
    diagnostic of your gaps before they turn into a business-critical downgrade.
    </p>
    <div class="cta-row">
        <a class="btn-primary" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Isolate My Risk Now (£149)</a>
        <a class="btn-secondary" href="#request">Deploy Structural Intake</a>
        <a class="btn-light" href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer">Browse Core Framework Toolkits</a>
    </div>
</div>
""")

# =========================================================
# COGNITIVE RESET (The Execution Fallacy)
# =========================================================
html("""
<div class="pain-banner">
    <h2>The Template Trap: Having a policy is not evidence of operational control.</h2>
    <div style="width: 60px; height: 3px; background: #E11D48; margin: 12px 0 16px 0;"></div>
    <p style="margin: 0; font-size: 17px; color: #334155;">
    CQC Inspectors do not award ratings based on text files sitting in a cloud directory. They look for closed loop execution: 
    <b>Are your logs connected to your governance minutes? Are your tracking matrices updated weekly? Is your training data fully verified?</b> 
    Nexus cuts through passive administrative overhead to build bulletproof, review-ready evidence architecture.
    </p>
</div>
""")

# =========================================================
# THE £149 DIAGNOSTIC BREAKDOWN
# =========================================================
html("""
<div class="section">
    <h2>The Asymmetric Diagnostics: What the £149 Matrix Validates</h2>
    <p class="section-intro" style="color: var(--muted); margin-bottom: 24px;">
    An un-biased, cold-eyes assessment of the core records you will be commanded to justify under inspection stress.
    </p>
</div>

<div class="review-cover-grid">
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Policy Deployment Control</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Live Risk Registers</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Training Verification Matrix</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Closed-Loop Incident Logs</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Safeguarding Traceability</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Continuous Audit Trackers</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Active Governance Minutes</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Data Sovereignty & GDPR</p></div>
</div>
""")

# =========================================================
# SERVICE ARCHITECTURE (Choice Optimization & Previews)
# =========================================================
html('<div id="services" style="margin-top: 40px;"></div>')
html("""
<div class="section">
    <h2>Select Your Level of Evidence Intervention</h2>
    <p class="section-intro" style="color: var(--muted); margin-bottom: 30px;">
    From low-friction initial diagnostics to absolute end-to-end documentation overhaul and architectural preservation.
    </p>
</div>
""")

# Dynamic Iframe Injection Logic
def get_logo_html():
    if LOGO_DATA_URI:
        return f'<img src="{LOGO_DATA_URI}" alt="Logo" style="max-width:165px; max-height:54px; object-fit:contain;">'
    return '<div style="color:#C8A96A; font-weight:900; font-size:22px;">NEXUS CONFORMITÉ</div>'

def render_preview_1():
    logo = get_logo_html()
    src = f"""
    <!DOCTYPE html><html><head><style>
    body {{ margin:0; background:#071C35; font-family:sans-serif; padding:10px; }}
    .sheet {{ width:100%; background:white; height:460px; border-left:8px solid #C8A96A; padding:20px; box-sizing:border-box; overflow:hidden; }}
    .hdr {{ display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #EEE; padding-bottom:10px; }}
    .badge {{ background:#FEF3C7; color:#92400E; padding:4px 8px; font-size:11px; font-weight:bold; border-radius:4px; }}
    .metric-box {{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:20px 0; }}
    .m {{ background:#F8FAFC; padding:10px; border:1px solid #E2E8F0; text-align:center; }}
    .m text {{ display:block; font-size:24px; font-weight:800; color:#071C35; }}
    </style></head><body><div class="sheet">
    <div class="hdr"><div><b>CQC Diagnostic Evaluation Report</b><br><small style="color:#64748B;">Redacted Active Care Network Instance</small></div>{logo}</div>
    <div style="margin-top:15px;"><span class="badge">EVIDENCE STATUS: AMBER CORRECTION REQUIRED</span></div>
    <h3 style="color:#071C35; margin:15px 0 5px 0;">Structural Gap Matrix</h3>
    <p style="font-size:13px; color:#475569; margin:0;">Systemic disconnect detected between management meeting minutes and active incident resolution logs. Exposure vector identified under CQC 'Well-Led' domain criteria.</p>
    <div class="metric-box">
        <div class="m"><text>149</text><small>Checked Nodes</small></div>
        <div class="m" style="border-left:4px solid #10B981;"><text>87</text><small>Defensible</small></div>
        <div class="m" style="border-left:4px solid #F59E0B;"><text>42</text><small>Exposed</small></div>
        <div class="m" style="border-left:4px solid #EF4444;"><text>20</text><small>Critical Failure</small></div>
    </div>
    </div></body></html>
    """
    components.html(src, height=490, scrolling=False)

def render_preview_2():
    logo = get_logo_html()
    src = f"""
    <!DOCTYPE html><html><head><style>
    body {{ margin:0; background:#071C35; font-family:sans-serif; padding:10px; }}
    .sheet {{ width:100%; background:white; height:460px; border-left:8px solid #0D9488; padding:20px; box-sizing:border-box; overflow:hidden; }}
    .hdr {{ display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #EEE; padding-bottom:10px; }}
    table {{ width:100%; border-collapse:collapse; margin-top:15px; font-size:12px; }}
    th {{ background:#071C35; color:white; padding:8px; text-align:left; }}
    td {{ padding:8px; border:1px solid #E2E8F0; }}
    </style></head><body><div class="sheet">
    <div class="hdr"><div><b>Incident Trackers & Cross-Reference Mapping</b><br><small style="color:#64748B;">30-Day Forensic Cleanup Stream</small></div>{logo}</div>
    <table>
        <tr><th>Exposed Core Vulnerability Theme</th><th>Vector Count</th><th>Root Cause Determination</th><th>Execution Remediation Action Taken</th></tr>
        <tr><td><b>MAR-Chart Administration Deviations</b></td><td>5 In Instances</td><td>Weak competency confirmation loop</td><td>Engineered active weekly validation protocols</td></tr>
        <tr><td><b>Missed / Latent Operational Shifts</b></td><td>7 Records</td><td>Rostering engine mismatch</td><td>Injected mandatory variance reporting forms</td></tr>
        <tr><td><b>Manual Handling Near-Miss Disconnects</b></td><td>4 Records</td><td>Isolated silo tracking entries</td><td>Synthesized live feedback loop directly into risk registers</td></tr>
    </table>
    </div></body></html>
    """
    components.html(src, height=490, scrolling=False)

def render_preview_3():
    logo = get_logo_html()
    src = f"""
    <!DOCTYPE html><html><head><style>
    body {{ margin:0; background:#071C35; font-family:sans-serif; padding:10px; }}
    .sheet {{ width:100%; background:white; height:460px; border-left:8px solid #05162E; padding:20px; box-sizing:border-box; overflow:hidden; }}
    .hdr {{ display:flex; justify-content:space-between; align-items:center; background:#05162E; color:white; padding:15px; }}
    .kpi-row {{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin-top:15px; }}
    .kpi {{ background:#F0Fdf4; border-top:4px solid #0D9488; padding:10px; text-align:center; font-size:11px; }}
    </style></head><body><div class="sheet">
    <div class="hdr"><div><b>Continuous Governance Architecture Engine</b><br><small style="color:#94A3B8;">Real-Time Retainer Interface Control</small></div>{logo}</div>
    <div class="kpi-row">
        <div class="kpi"><b>Current Defensibility Score</b><br><span style="font-size:20px; font-weight:800; color:#0D9488;">96.4%</span></div>
        <div class="kpi" style="background:#FFF7ED; border-top-color:#F97316;"><b>Active Alerts Pending</b><br><span style="font-size:20px; font-weight:800; color:#F97316;">2</span></div>
        <div class="kpi" style="background:#FEF2F2; border-top-color:#EF4444;"><b>Critical Breaches Defended</b><br><span style="font-size:20px; font-weight:800; color:#EF4444;">0</span></div>
        <div class="kpi"><b>Next Scheduled Audit Matrix</b><br><span style="font-size:14px; font-weight:800; color:#05162E;">July 15, 2026</span></div>
    </div>
    <h4 style="margin:20px 0 5px 0; color:#05162E;">Defensive Perimeter Management Status</h4>
    <p style="font-size:12px; color:#475569; margin:0;">Active verification cycles running across all system nodes. Systematic validation proofs compiled automatically for direct inspector handover generation routines.</p>
    </div></body></html>
    """
    components.html(src, height=490, scrolling=False)

# Render Framework Tiers
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown('<span class="tier-tag tag-popular">★ RECOMMENDED ENTRY ROUTE</span>', unsafe_allow_html=True)
        st.subheader("£149 Forensic Evidence Review")
        st.markdown("## £149 <small style='font-size:14px; color:gray;'>Fixed Fee</small>", unsafe_allow_html=True)
        st.write("An analytical triage mapping out your core operational vulnerabilities before committing to intensive infrastructural rework.")
        
        v1 = st.radio("Toggle Architecture Perspective:", ["Structural Profile", "Deep Verification Spectrum", "Live Output Visual"], key="r_tier_1")
        if v1 == "Structural Profile":
            st.markdown("""
- Full data architecture triage across 8 core axes
- Isolation of unverified data entries
- Traceability scoring framework
- Actionable executive recovery protocol
""")
            st.link_button("Initiate Low-Friction Audit", CQC_REVIEW_CHECKOUT_URL, use_container_width=True)
        elif v1 == "Deep Verification Spectrum":
            st.caption("We trace exact chain-of-custody tracking across key frameworks to guarantee they hold up under interrogative review.")
        else:
            render_preview_1()

with col2:
    with st.container(border=True):
        st.markdown('<span class="tier-tag tag-sprint">⚡ AGGRESSIVE TURNAROUND</span>', unsafe_allow_html=True)
        st.subheader("30-Day Structural Evidence Sprint")
        st.markdown("## From £750 <small style='font-size:14px; color:gray;'>Custom Scoped</small>", unsafe_allow_html=True)
        st.write("Complete systemic overhaul to turn scattered documents into organized, legally defensible, inspection-ready frameworks.")
        
        v2 = st.radio("Toggle Architecture Perspective:", ["Structural Profile", "Deep Verification Spectrum", "Live Output Visual"], key="r_tier_2")
        if v2 == "Structural Profile":
            st.markdown("""
- Deep structural clean-up of messy, unlinked files
- Complete alignment of audit trackers to governance entries
- Incident & complaints validation overhaul
- Post-sprint operational handover asset map
""")
            st.link_button("Secure Priority Target Allocation", "#request", use_container_width=True)
        elif v2 == "Deep Verification Spectrum":
            st.caption("A comprehensive diagnostic deep-clean designed to clear severe backlogs and prepare systems for imminent inspections.")
        else:
            render_preview_2()

with col3:
    with st.container(border=True):
        st.markdown('<span class="tier-tag tag-retainer">🛡️ PERPETUAL PROTECTION</span>', unsafe_allow_html=True)
        st.subheader("Continuous Compliance Architecture")
        st.markdown("## Managed Retainer <small style='font-size:14px; color:gray;'>Bespoke Placement</small>", unsafe_allow_html=True)
        st.write("Ongoing external oversight to ensure data controls and evidence matrices remain robust and up to date month after month.")
        
        v3 = st.radio("Toggle Architecture Perspective:", ["Structural Profile", "Deep Verification Spectrum", "Live Output Visual"], key="r_tier_3")
        if v3 == "Structural Profile":
            st.markdown("""
- Programmatic recurring evidence validation checks
- Perpetual optimization of documentation controls
- Version control assurance routines
- Real-time management readiness dashboards
""")
            st.link_button("Apply for Retainer Advisory", "#request", use_container_width=True)
        elif v3 == "Deep Verification Spectrum":
            st.caption("Continuous system defenses for small providers who refuse to let their evidence drift between inspection periods.")
        else:
            render_preview_3()

# =========================================================
# SYSTEM SECURITY & ESCROW RATIONALE
# =========================================================
html("""
<div class="notice">
    <h3>Transaction Sovereignty & Phased Engineering Controls</h3>
    <p>
    The £149 Forensics Intake works via direct transactional capture. Upon checkout authorization, the portal opens access to your secure uploads environment for processing.
    </p>
    <p>
    Bespoke Engineering Engagements (Structural Sprints & Continuous Retainers) operate under strict verification logic: a structured 40% capitalization token activates the intake workflow. 
    The remaining 60% balance is executed inside a closed, private delivery envelope upon presentation of verified systems proofing matrices. 
    <b>Data Isolation Clause:</b> Your sensitive infrastructure files are never held in long-term exposure layers. Completed files are only released following final cryptographically verified transaction sign-off.
    </p>
</div>
""")

# =========================================================
# THE PROCESS (Reducing Friction via Chronological Logic)
# =========================================================
html('<div id="process"></div>')
html("""
<div class="section">
    <h2>The Onboarding Protocol: Three Phases to Total Defensibility</h2>
</div>
""")

p_col1, p_col2, p_col3 = st.columns(3)
with p_col1:
    with st.container(border=True):
        st.markdown("### Step 1: Isolation Allocation")
        st.write("Authorize the basic triage checkpoint (£149 review) or complete our structured telemetry intake to map your custom enterprise requirement scale.")
with p_col2:
    with st.container(border=True):
        st.markdown("### Step 2: Telemetry Ingestion")
        st.write("Drop your heavily redacted internal files—indexes, tracking arrays, historical audit shapes, maps—directly into our secure staging environment.")
with p_col3:
    with st.container(border=True):
        st.markdown("### Step 3: Deployment Handover")
        st.write("Receive your complete vulnerability report or fully re-engineered documentation set. Your private links remain archived immediately following system handoff.")

html("""
<div class="green-notice">
    <h3>Required Telemetry for Systems Validation Protocol Activation</h3>
    <p style="margin-bottom:10px; font-size:15px; color:#15803D;">Nexus requires the following parameters to execute a targeted defense analysis:</p>
    <ul style="grid-template-columns: repeat(2, 1fr); display: grid; font-size:14px; gap:6px; color:#166534;">
        <li>• Verified Corporate Registration Identity</li>
        <li>• Executive Scope Authorization Role</li>
        <li>• Specific Care Model Taxonomy</li>
        <li>• Targeted Deployment Tier Selection</li>
        <li>• Core Systemic Exposure Drivers</li>
        <li>• Current Evidence Integrity Level</li>
        <li>• Redacted Compliance Telemetry Maps</li>
        <li>• Verification Token (Payhip reference numbers)</li>
    </ul>
</div>
""")

# =========================================================
# INTERACTIVE DIAGNOSTIC INTAKE ENGINE
# =========================================================
html('<div id="request"></div>')
html("""
<div class="section">
    <h2>Secure Structural Diagnostic Telemetry Intake</h2>
    <p class="section-intro" style="color: var(--muted); margin-bottom: 24px;">
    Transmit your architectural profile through our secure layer below. For existing £149 authorizations, supply your validation reference to prioritize execution queues.
    </p>
</div>
""")

form_html = f"""
<div style="background:#ffffff; border:1px solid #E2E8F0; border-radius:16px; padding:30px; box-shadow:0 10px 35px rgba(0,0,0,0.02); font-family:sans-serif; color:#05162E;">
    <form action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="_subject" value="URGENT: Nexus Telemetry Intake Manifest Received">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none">

        <h3 style="margin-top:0; color:#05162E;">1. Executive Profile Mapping</h3>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-bottom:16px;">
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Authorized Personnel Name *</label>
                <input type="text" name="Legal Representative" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Provider Legal Entity Name *</label>
                <input type="text" name="Corporate Entity" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
        </div>
        
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-bottom:24px;">
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Secure Direct Communication Routing *</label>
                <input type="email" name="email" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Verification Token (Payhip Transaction ID if prepaid)</label>
                <input type="text" name="Validation Token Reference" placeholder="Alpha-Numeric Reference Key" style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
        </div>

        <h3 style="color:#05162E;">2. Structural Dimensions</h3>
        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:16px; margin-bottom:24px;">
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Your Operational Title *</label>
                <select name="Executive Taxonomy" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; background:white;">
                    <option value="">Select Domain Role</option>
                    <option>Registered Manager</option>
                    <option>Care Manager</option>
                    <option>Nominated Individual / Owner</option>
                    <option>Operations Director</option>
                    <option>Compliance Lead</option>
                    <option>Other</option>
                </select>
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Care Model Classification *</label>
                <select name="Care Delivery Taxonomy" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; background:white;">
                    <option value="">Select Framework Profile</option>
                    <option>Domiciliary Care Engine</option>
                    <option>Supported Living Environment</option>
                    <option>Residential Care Facility</option>
                    <option>Specialized Complex Care</option>
                    <option>Pre-Registration Startup</option>
                </select>
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Targeted Intervention Tier *</label>
                <select name="Requested Strategic Response" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; background:white;">
                    <option value="">Select Service Scope</option>
                    <option>£149 Diagnostic Forensic Review</option>
                    <option>30-Day Intensive Clean-up Sprint</option>
                    <option>Continuous Architectural Retainer</option>
                </select>
            </div>
        </div>

        <h3 style="color:#05162E;">3. Core Vulnerability Profile</h3>
        <div style="margin-bottom:24px;">
            <label style="font-weight:700; font-size:13px; color:#475569;">What keeps you awake at night? Describe the primary risk drivers or exposure vectors you need neutralized *</label>
            <textarea name="Vulnerability Narrative Focus" required rows="5" placeholder="Example: We have an upcoming inspection window. Our training matrix numbers lag behind active records, and incident closure notes are unlinked from our meeting minutes." style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; font-family:sans-serif;"></textarea>
        </div>

        <h3 style="color:#05162E;">4. Secure Telemetry Encapsulation (Upload Files)</h3>
        <p style="font-size:13px; color:#64748B; margin-top:-8px;">Upload redacted folder profiles, unlinked logging sheets, or framework screenshots. Max 20MB per node.</p>
        <div style="margin-bottom:24px;">
            <input type="file" name="Primary Telemetry Segment" required style="width:100%; padding:15px; border:2px dashed #C8A96A; background:#FFFDF7; border-radius:8px;">
            <input type="file" name="Secondary Telemetry Segment" style="width:100%; padding:15px; border:1px dashed #CBD5E1; margin-top:8px; border-radius:8px;">
        </div>

        <label style="display:block; font-size:13px; color:#334155; margin-bottom:24px; cursor:pointer;">
            <input type="checkbox" name="Sovereignty & Redaction Confirmation" required value="Authorized" style="margin-right:8px;">
            I hereby certify that all transmitted records have undergone mandatory identity redaction protocols and that I hold explicit executive clearance to authorize this technical assessment.
        </label>

        <button type="submit" style="width:100%; background:#C8A96A; color:#05162E; padding:16px; border:none; border-radius:999px; font-weight:800; font-size:16px; cursor:pointer; box-shadow:0 4px 12px rgba(200,169,106,0.25);">
            Transmit Diagnostic Payload to Nexus Control
        </button>
    </form>
</div>
"""
components.html(form_html, height=1050, scrolling=True)

# =========================================================
# FAQ SECTION (Anxiety Reduction & Objections Handling)
# =========================================================
html('<div id="faq" style="margin-top:40px;"></div>')
html("""
<div class="section">
    <h2>Anxiety Resolution & Systemic Guardrails</h2>
    <p class="section-intro" style="color: var(--muted); margin-bottom: 24px;">
    Clear answers to common operational friction points before initiating engagement.
    </p>
</div>
""")

with st.expander("Is the £149 Forensic Review an insurance policy against negative ratings?"):
    st.write("No. The review acts as a neutral diagnostic tool. It exposes exactly what an analytical inspector will flag, giving you a definitive list of gaps to fix before the CQC schedules your inspection.")

with st.expander("Does utilizing Nexus offload legal or regulatory accountability?"):
    st.write("No. Nexus engineers the structural frameworks, maps documentation pathways, and removes messy file drift. The provider retains ultimate regulatory execution responsibility.")

with st.expander("Can this layout handle complex multi-site domiciliary frameworks?"):
    st.write("Yes. Our clean-up and retainer tiers are built specifically to standardize evidence across decentralized healthcare structures.")

with st.expander("What is the exact processing timeline for the prepaid diagnostic?"):
    st.write("Once your transaction is verified and your file payload is submitted, the final diagnostic matrix is assembled and delivered within 3 to 5 business days.")

with st.expander("How do escrow and payment cycles function for custom projects?"):
    st.write("We maintain clear milestones: a 40% resource allocation fee starts the project. We then build out your systems and show you a preview or validation map. The final 60% completion token releases the source code and files directly via a private Payhip delivery link.")

# =========================================================
# HIGH-TRUST FOOTER ADVISORY MODULE
# =========================================================
footer_html = f"""
<div class="footer" style="width:100%; background:linear-gradient(135deg, #05162E 0%, #0B2545 70%, #0D9488 100%); color:white; border-radius:24px; padding:45px; box-shadow:0 20px 50px rgba(5,22,46,0.15);">
    <h3 style="color:white; font-size:32px; margin:0 0 10px 0;">Nexus Conformité</h3>
    <p style="color:#CBD5E1; font-size:18px; max-width:760px; line-height:1.5; margin-bottom:30px;">
    Do not enter an inspection window guessing where your vulnerabilities are. Safeguard your operational history, organize your documentation, and establish a bulletproof governance perimeter.
    </p>
    
    <div style="display:flex; flex-wrap:wrap; gap:12px; margin-bottom:30px;">
        <a class="btn-primary" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Authorize £149 Forensic Review</a>
        <a class="btn-secondary" href="#request" target="_parent">Open Strategic Advisory Request</a>
        <a class="btn-light" href="#top" target="_parent">Return to Telemetry Root</a>
    </div>

    <div style="display:flex; gap:12px; align-items:center; margin-bottom:24px;">
        <a href="{FACEBOOK_URL}" target="_blank" rel="noopener noreferrer" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">FB</a>
        <a href="mailto:{EMAIL}" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">@</a>
        <a href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">PH</a>
        <a href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">LN</a>
    </div>

    <p style="color:#94A3B8; font-size:13px; margin:0; line-height:1.5;">
    Nexus Conformité is an independent GRC advisory and data infrastructure architecture firm. Services focus purely on structural defense, evidence alignment, and technical documentation engineering. This output does not constitute representation under formal legal practice acts.
    </p>
</div>
"""
components.html(footer_html, height=440, scrolling=False)
