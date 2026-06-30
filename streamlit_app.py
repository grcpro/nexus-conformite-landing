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
    page_title="Nexus Conformité | CQC Evidence Review & Inspection Readiness",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# BUSINESS DETAILS & LINKS
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
# LOGO RETRIEVAL
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
# CSS DESIGN
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

/* Hero Section */
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

/* Pain Point Banner */
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

/* Badges for Choice Architecture */
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

@media (max-width: 900px) {
    .review-cover-grid { grid-template-columns: repeat(2, 1fr); }
    .topbar { flex-direction: column; align-items: flex-start; gap: 16px; }
    .nav-pills { width: 100%; display: grid; grid-template-columns: repeat(2, 1fr); }
    .nav-pills a { text-align: center; }
}
</style>
""")

# =========================================================
# BRAND HEADER
# =========================================================
if LOGO_PATH:
    st.image(LOGO_PATH, width=118)

html(f"""
<div class="topbar" id="top">
    <div>
        <p class="brand-title">Nexus Conformité</p>
        <p class="brand-subtitle">CQC Evidence Reviews • Document Cleanup • Ongoing Compliance</p>
    </div>
    <div class="nav-pills">
        <a href="#services">Our Services</a>
        <a href="#process">How It Works</a>
        <a href="#faq">FAQ</a>
        <a href="#request">Contact Us / Intake</a>
    </div>
</div>
""")

# =========================================================
# HERO SECTION
# =========================================================
html(f"""
<div class="hero">
    <span class="badge-tag">🚨 Inspection Readiness</span><br>
    <div class="eyebrow">UK Adult Social Care Compliance</div>
    <h1>Stop Guessing Your Inspection Readiness.<br>Find Your Missing Evidence Before the CQC Does.</h1>
    <p>
    Having a policy document is not enough to pass an inspection. If your logs, minutes, and training matrices aren't connected, you're at risk. 
    The <b>£149 Evidence Review</b> gives you a clear, objective report of your missing documents before they turn into a negative rating.
    </p>
    <div class="cta-row">
        <a class="btn-primary" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Start My Review Now (£149)</a>
        <a class="btn-secondary" href="#request">Contact the Team</a>
        <a class="btn-light" href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer">Browse Our Toolkits</a>
    </div>
</div>
""")

# =========================================================
# THE TEMPLATE TRAP
# =========================================================
html("""
<div class="pain-banner">
    <h2>The Template Trap: A blank policy won't protect you.</h2>
    <div style="width: 60px; height: 3px; background: #E11D48; margin: 12px 0 16px 0;"></div>
    <p style="margin: 0; font-size: 17px; color: #334155;">
    CQC Inspectors don't give "Good" ratings just because you have a folder full of downloaded templates. They look for action: 
    <b>Are your incidents mentioned in your staff meetings? Is your training matrix up to date?</b> 
    Nexus helps you organize your evidence so you can prove you are delivering safe, well-led care.
    </p>
</div>
""")

# =========================================================
# WHAT WE CHECK
# =========================================================
html("""
<div class="section">
    <h2>What the £149 Evidence Review Covers</h2>
    <p class="section-intro" style="color: var(--muted); margin-bottom: 24px;">
    An honest, unbiased review of the exact documents an inspector will ask you for.
    </p>
</div>

<div class="review-cover-grid">
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Policy Updates</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Risk Registers</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Staff Training Logs</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Incident Reports</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Safeguarding Records</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Internal Audits</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Meeting Minutes</p></div>
    <div class="review-cover-item"><div class="review-cover-icon">◆</div><p>Data Protection (GDPR)</p></div>
</div>
""")

# =========================================================
# SERVICE TIERS (With fixed 2x2 grid iframe visuals)
# =========================================================
html('<div id="services" style="margin-top: 40px;"></div>')
html("""
<div class="section">
    <h2>Choose Your Level of Support</h2>
    <p class="section-intro" style="color: var(--muted); margin-bottom: 30px;">
    From a quick health-check of your documents to a complete clean-up of your compliance system.
    </p>
</div>
""")

def get_logo_html():
    if LOGO_DATA_URI:
        return f'<img src="{LOGO_DATA_URI}" alt="Logo" style="max-width:165px; max-height:54px; object-fit:contain;">'
    return '<div style="color:#C8A96A; font-weight:900; font-size:22px;">NEXUS CONFORMITÉ</div>'

# FIXED MOBILE GRID CLIPPING: Changed metric-box from 4 columns to a 2x2 grid
def render_preview_1():
    logo = get_logo_html()
    src = f"""
    <!DOCTYPE html><html><head><style>
    body {{ margin:0; background:#071C35; font-family:sans-serif; padding:10px; }}
    .sheet {{ width:100%; background:white; height:460px; border-left:8px solid #C8A96A; padding:20px; box-sizing:border-box; overflow:hidden; }}
    .hdr {{ display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #EEE; padding-bottom:10px; }}
    .badge {{ background:#FEF3C7; color:#92400E; padding:4px 8px; font-size:11px; font-weight:bold; border-radius:4px; }}
    .metric-box {{ display:grid; grid-template-columns:repeat(2,1fr); gap:12px; margin:20px 0; }}
    .m {{ background:#F8FAFC; padding:12px; border:1px solid #E2E8F0; text-align:center; border-radius:6px; }}
    .m text {{ display:block; font-size:24px; font-weight:800; color:#071C35; }}
    </style></head><body><div class="sheet">
    <div class="hdr"><div><b>CQC Readiness Report</b><br><small style="color:#64748B;">Sample Care Home Profile</small></div>{logo}</div>
    <div style="margin-top:15px;"><span class="badge">STATUS: ACTION NEEDED</span></div>
    <h3 style="color:#071C35; margin:15px 0 5px 0;">Missing Evidence Summary</h3>
    <p style="font-size:13px; color:#475569; margin:0;">We found that your recent meeting minutes do not mention recent incidents. This is a common issue CQC inspectors flag under the 'Well-Led' category.</p>
    <div class="metric-box">
        <div class="m"><text>149</text><small>Files Checked</small></div>
        <div class="m" style="border-left:4px solid #10B981;"><text>87</text><small>Safe & Ready</small></div>
        <div class="m" style="border-left:4px solid #F59E0B;"><text>42</text><small>At Risk</small></div>
        <div class="m" style="border-left:4px solid #EF4444;"><text>20</text><small>Fix Now</small></div>
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
    <div class="hdr"><div><b>Incident Log Cleanup</b><br><small style="color:#64748B;">30-Day Action Plan</small></div>{logo}</div>
    <table>
        <tr><th>Risk Area Found</th><th>Total Issues</th><th>Why It Happened</th><th>How We Fixed It</th></tr>
        <tr><td><b>Missed Med Signatures</b></td><td>5 Records</td><td>Staff forgot to sign MAR charts</td><td>Created new weekly review sheet</td></tr>
        <tr><td><b>Missing Shift Logs</b></td><td>7 Records</td><td>Rota software didn't update</td><td>Added a manual shift-check form</td></tr>
        <tr><td><b>Unreported Incidents</b></td><td>4 Records</td><td>Staff didn't know how to report</td><td>Added quick-report steps to register</td></tr>
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
    .kpi-row {{ display:grid; grid-template-columns:repeat(2,1fr); gap:12px; margin-top:15px; }}
    .kpi {{ background:#F0Fdf4; border-top:4px solid #0D9488; padding:12px; text-align:center; font-size:12px; border-radius:4px; }}
    </style></head><body><div class="sheet">
    <div class="hdr"><div><b>Ongoing Compliance Dashboard</b><br><small style="color:#94A3B8;">Monthly Account Summary</small></div>{logo}</div>
    <div class="kpi-row">
        <div class="kpi"><b>Overall Safety Score</b><br><span style="font-size:22px; font-weight:800; color:#0D9488;">96.4%</span></div>
        <div class="kpi" style="background:#FFF7ED; border-top-color:#F97316;"><b>Updates Pending</b><br><span style="font-size:22px; font-weight:800; color:#F97316;">2</span></div>
        <div class="kpi" style="background:#FEF2F2; border-top-color:#EF4444;"><b>Issues Fixed</b><br><span style="font-size:22px; font-weight:800; color:#EF4444;">14</span></div>
        <div class="kpi" style="background:#F8FAFC; border-top-color:#64748B;"><b>Next Audit Date</b><br><span style="font-size:16px; font-weight:800; color:#05162E; display:block; margin-top:5px;">July 15, 2026</span></div>
    </div>
    <h4 style="margin:20px 0 5px 0; color:#05162E;">System Health Check</h4>
    <p style="font-size:12px; color:#475569; margin:0;">We are actively monitoring your records to ensure everything remains updated and ready for your next inspector visit.</p>
    </div></body></html>
    """
    components.html(src, height=490, scrolling=False)

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown('<span class="tier-tag tag-popular">★ MOST POPULAR</span>', unsafe_allow_html=True)
        st.subheader("£149 Evidence Review")
        st.markdown("## £149 <small style='font-size:14px; color:gray;'>One-Time Fee</small>", unsafe_allow_html=True)
        st.write("A quick, clear review highlighting exactly what documents you are missing before a CQC visit.")
        
        v1 = st.radio("Choose a view:", ["What You Get", "How We Check", "Live Output Visual"], key="r_tier_1")
        if v1 == "What You Get":
            st.markdown("""
- Full check of your 8 core document areas
- A clear list of missing files
- A simple risk score
- A step-by-step plan on what to fix first
""")
            st.link_button("Start Your £149 Review", CQC_REVIEW_CHECKOUT_URL, use_container_width=True)
        elif v1 == "How We Check":
            st.caption("We cross-reference your files exactly how an inspector would, ensuring everything matches up and makes sense.")
        else:
            render_preview_1()

with col2:
    with st.container(border=True):
        st.markdown('<span class="tier-tag tag-sprint">⚡ FAST TURNAROUND</span>', unsafe_allow_html=True)
        st.subheader("30-Day Document Cleanup")
        st.markdown("## From £750 <small style='font-size:14px; color:gray;'>Custom Quote</small>", unsafe_allow_html=True)
        st.write("A complete overhaul to organize your messy files into a clear, inspection-ready system.")
        
        v2 = st.radio("Choose a view:", ["What You Get", "How We Check", "Live Output Visual"], key="r_tier_2")
        if v2 == "What You Get":
            st.markdown("""
- Deep clean of all outdated or messy files
- Linking your meeting minutes to incidents
- Fixing your training and complaints logs
- Handing back a fully organized folder system
""")
            st.link_button("Request a Cleanup Quote", "#request", use_container_width=True)
        elif v2 == "How We Check":
            st.caption("Perfect for providers who have fallen behind on paperwork and need to get ready for an inspection fast.")
        else:
            render_preview_2()

with col3:
    with st.container(border=True):
        st.markdown('<span class="tier-tag tag-retainer">🛡️ ONGOING SUPPORT</span>', unsafe_allow_html=True)
        st.subheader("Monthly Compliance Support")
        st.markdown("## Monthly Retainer <small style='font-size:14px; color:gray;'>Custom Quote</small>", unsafe_allow_html=True)
        st.write("We act as your external compliance team, keeping your documents updated month after month.")
        
        v3 = st.radio("Choose a view:", ["What You Get", "How We Check", "Live Output Visual"], key="r_tier_3")
        if v3 == "What You Get":
            st.markdown("""
- Monthly checks of all your evidence files
- Fixing broken links and missing signatures
- Continuous updates to policies
- A monthly health-check report for owners
""")
            st.link_button("Apply for Ongoing Support", "#request", use_container_width=True)
        elif v3 == "How We Check":
            st.caption("For busy care managers who want peace of mind knowing their paperwork won't drift out of date again.")
        else:
            render_preview_3()

# =========================================================
# PAYMENT & SECURITY INFO
# =========================================================
html("""
<div class="notice">
    <h3>How Payments & Security Work</h3>
    <p>
    <b>The £149 Review:</b> You pay securely via checkout, which instantly opens a portal to upload your files.
    </p>
    <p>
    <b>Custom Cleanups & Monthly Support:</b> We start with a 40% deposit. We only ask for the final 60% when the work is complete and you have verified the new, organized system. 
    <b>Your Privacy:</b> We never hold onto your sensitive files longer than necessary. Once the project is complete and handed back to you, our copies are securely deleted.
    </p>
</div>
""")

# =========================================================
# HOW IT WORKS
# =========================================================
html('<div id="process"></div>')
html("""
<div class="section">
    <h2>How It Works: Three Simple Steps</h2>
</div>
""")

p_col1, p_col2, p_col3 = st.columns(3)
with p_col1:
    with st.container(border=True):
        st.markdown("### Step 1: Choose Your Service")
        st.write("Start with the simple £149 review, or fill out the intake form below if you need a bigger cleanup project.")
with p_col2:
    with st.container(border=True):
        st.markdown("### Step 2: Send Us Your Files")
        st.write("Securely upload your index sheets, tracking spreadsheets, and old audits for us to review.")
with p_col3:
    with st.container(border=True):
        st.markdown("### Step 3: Get Your Results")
        st.write("Receive your easy-to-read missing evidence report or your completely reorganized documentation folder.")

# =========================================================
# INTAKE FORM
# =========================================================
html('<div id="request"></div>')
html("""
<div class="section">
    <h2>Secure Compliance Intake Form</h2>
    <p class="section-intro" style="color: var(--muted); margin-bottom: 24px;">
    Use this form to request a custom quote or submit files for your prepaid £149 review.
    </p>
</div>
""")

form_html = f"""
<div style="background:#ffffff; border:1px solid #E2E8F0; border-radius:16px; padding:30px; box-shadow:0 10px 35px rgba(0,0,0,0.02); font-family:sans-serif; color:#05162E;">
    <form action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="_subject" value="New Client Intake Form Received">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none">

        <h3 style="margin-top:0; color:#05162E;">1. Your Details</h3>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-bottom:16px;">
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Your Full Name *</label>
                <input type="text" name="Name" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Company Name *</label>
                <input type="text" name="Company" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
        </div>
        
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; margin-bottom:24px;">
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Email Address *</label>
                <input type="email" name="email" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Order ID (If you already paid for the £149 Review)</label>
                <input type="text" name="Order ID" placeholder="Leave blank if requesting a quote" style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px;">
            </div>
        </div>

        <h3 style="color:#05162E;">2. Your Business Type</h3>
        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:16px; margin-bottom:24px;">
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Your Job Title *</label>
                <select name="Job Title" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; background:white;">
                    <option value="">Select Role</option>
                    <option>Registered Manager</option>
                    <option>Care Manager</option>
                    <option>Owner / Nominated Individual</option>
                    <option>Operations Director</option>
                    <option>Compliance Lead</option>
                    <option>Other</option>
                </select>
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Type of Care Service *</label>
                <select name="Service Type" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; background:white;">
                    <option value="">Select Service</option>
                    <option>Domiciliary Care (Home Care)</option>
                    <option>Supported Living</option>
                    <option>Residential Care Home</option>
                    <option>Nursing Home / Complex Care</option>
                    <option>New Startup (Pre-Registration)</option>
                </select>
            </div>
            <div>
                <label style="font-weight:700; font-size:13px; color:#475569;">Service Requested *</label>
                <select name="Requested Service" required style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; background:white;">
                    <option value="">Select Option</option>
                    <option>Submitting files for the £149 Review</option>
                    <option>Quote for 30-Day Cleanup Sprint</option>
                    <option>Quote for Monthly Ongoing Support</option>
                </select>
            </div>
        </div>

        <h3 style="color:#05162E;">3. What do you need help with?</h3>
        <div style="margin-bottom:24px;">
            <label style="font-weight:700; font-size:13px; color:#475569;">Tell us your main concerns or what you want us to focus on *</label>
            <textarea name="Main Concerns" required rows="4" placeholder="Example: We have a CQC inspection coming up soon. We know our staff training spreadsheet is out of date and our incident logs are messy." style="width:100%; padding:12px; margin-top:6px; border:1px solid #CBD5E1; border-radius:8px; font-family:sans-serif;"></textarea>
        </div>

        <h3 style="color:#05162E;">4. Secure File Upload</h3>
        <p style="font-size:13px; color:#64748B; margin-top:-8px;">Upload your tracker sheets, spreadsheets, or audit logs here. (Max 20MB per file).</p>
        <div style="margin-bottom:24px;">
            <input type="file" name="Document 1" required style="width:100%; padding:15px; border:2px dashed #C8A96A; background:#FFFDF7; border-radius:8px;">
            <input type="file" name="Document 2" style="width:100%; padding:15px; border:1px dashed #CBD5E1; margin-top:8px; border-radius:8px;">
        </div>

        <label style="display:block; font-size:13px; color:#334155; margin-bottom:24px; cursor:pointer;">
            <input type="checkbox" name="Consent & Privacy" required value="Agreed" style="margin-right:8px;">
            I confirm I have the authority to share these documents and have removed highly sensitive patient names where necessary.
        </label>

        <button type="submit" style="width:100%; background:#C8A96A; color:#05162E; padding:16px; border:none; border-radius:999px; font-weight:800; font-size:16px; cursor:pointer; box-shadow:0 4px 12px rgba(200,169,106,0.25);">
            Send Details to the Nexus Team
        </button>
    </form>
</div>
"""
components.html(form_html, height=1000, scrolling=True)

# =========================================================
# FAQ SECTION
# =========================================================
html('<div id="faq" style="margin-top:40px;"></div>')
html("""
<div class="section">
    <h2>Frequently Asked Questions</h2>
</div>
""")

with st.expander("Does the £149 Evidence Review guarantee a 'Good' CQC rating?"):
    st.write("No. The review is a health-check tool. It highlights exactly what documents an inspector will ask for that you are currently missing, giving you a list of things to fix *before* the CQC arrives.")

with st.expander("Are you replacing our Registered Manager?"):
    st.write("No. We do the heavy lifting of organizing spreadsheets, cleaning up folders, and linking documents together. The care provider still retains full responsibility for the actual care delivered.")

with st.expander("Can you handle multi-site care providers?"):
    st.write("Yes. Our 30-Day Cleanup and Monthly Support packages are designed to help larger providers standardize their paperwork across multiple different locations.")

with st.expander("How quickly will I get my £149 Review results back?"):
    st.write("Once you pay and upload your files, you will receive your full diagnostic report within 3 to 5 business days.")

# =========================================================
# FOOTER
# =========================================================
footer_html = f"""
<div class="footer" style="width:100%; background:linear-gradient(135deg, #05162E 0%, #0B2545 70%, #0D9488 100%); color:white; border-radius:24px; padding:45px; box-shadow:0 20px 50px rgba(5,22,46,0.15);">
    <h3 style="color:white; font-size:32px; margin:0 0 10px 0;">Nexus Conformité</h3>
    <p style="color:#CBD5E1; font-size:18px; max-width:760px; line-height:1.5; margin-bottom:30px;">
    Don't enter an inspection window guessing if your paperwork is ready. We organize your documents so you can focus on delivering care.
    </p>
    
    <div style="display:flex; flex-wrap:wrap; gap:12px; margin-bottom:30px;">
        <a class="btn-primary" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Start £149 Review</a>
        <a class="btn-secondary" href="#request" target="_parent">Request a Quote</a>
        <a class="btn-light" href="#top" target="_parent">Back to Top</a>
    </div>

    <div style="display:flex; gap:12px; align-items:center; margin-bottom:24px;">
        <a href="{FACEBOOK_URL}" target="_blank" rel="noopener noreferrer" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">FB</a>
        <a href="mailto:{EMAIL}" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">@</a>
        <a href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">PH</a>
        <a href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer" style="color:white; text-decoration:none; background:rgba(255,255,255,0.1); width:40px; height:40px; border-radius:50%; display:grid; place-items:center; font-weight:bold;">LN</a>
    </div>

    <p style="color:#94A3B8; font-size:13px; margin:0; line-height:1.5;">
    Nexus Conformité is an independent compliance support firm. We help providers organize their paperwork and evidence. This service does not constitute formal legal representation.
    </p>
</div>
"""
components.html(footer_html, height=440, scrolling=False)
