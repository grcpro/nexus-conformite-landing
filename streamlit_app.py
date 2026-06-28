import streamlit as st
import os
import glob
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
LINKEDIN_NAME = "Nexus Conformité"

# Correct Payhip direct checkout link for £149 review
CQC_REVIEW_CHECKOUT_URL = "https://payhip.com/buy?link=9OUm6"

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
st.markdown("""
<style>
:root {
    --navy: #061A35;
    --gold: #C8A96A;
    --green: #0F766E;
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
}

.hero h1 {
    color: white;
    font-size: 60px;
    line-height: 1.02;
    max-width: 900px;
    margin: 0 0 18px 0;
}

.hero p {
    color: #EAF0F7;
    font-size: 22px;
    max-width: 850px;
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
    text-decoration: none;
    font-weight: 800;
    font-size: 15px;
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
    font-size: 40px;
    margin-bottom: 8px;
}

.section-intro {
    max-width: 820px;
    color: var(--muted);
    font-size: 19px;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 18px;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
}

.card {
    background: rgba(255,255,255,0.98);
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 30px;
    box-shadow: 0 16px 42px rgba(15,23,42,0.06);
    margin-bottom: 18px;
}

.card h3 {
    font-size: 24px;
    margin: 0 0 8px 0;
}

.price {
    color: var(--green);
    font-size: 30px;
    font-weight: 900;
    margin: 10px 0;
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

.step {
    background: white;
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 24px;
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
    background: var(--navy);
    color: white;
    border-radius: 28px;
    padding: 34px;
    margin-top: 34px;
}

.footer p {
    color: #DDE6F2;
    font-size: 16px;
}

.footer h3 {
    color: white;
}

@media (max-width: 900px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
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
        padding: 44px 26px;
        border-radius: 28px;
    }

    .hero h1 {
        font-size: 39px;
    }

    .hero p {
        font-size: 18px;
    }

    .section h2 {
        font-size: 31px;
    }

    .grid-3,
    .grid-2 {
        grid-template-columns: 1fr;
    }

    .card {
        padding: 24px;
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
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
if LOGO_PATH:
    st.image(LOGO_PATH, width=135)

st.markdown(f"""
<div class="topbar">
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
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================
st.markdown(f"""
<div class="hero">
    <div class="eyebrow">UK care compliance support</div>
    <h1>CQC evidence support for care managers who need clarity before pressure increases.</h1>
    <p>
    Nexus Conformité helps care managers and small providers organise evidence files,
    policies, SOPs, trackers, and governance records into a clearer review-ready structure.
    </p>
    <div class="cta-row">
        <a class="btn-primary" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Buy £149 Review</a>
        <a class="btn-secondary" href="#request">Request Custom Support</a>
        <a class="btn-light" href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer">View Digital Products</a>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# PROBLEM SECTION
# =========================================================
st.markdown("""
<div class="problem-strip">
    <h2>Most providers do not fail because they have no documents. They struggle because the evidence is scattered.</h2>
    <div class="gold-line"></div>
    <p>
    Policies may exist. Training may be done. Incidents may be recorded. But when evidence is spread across folders,
    chats, spreadsheets, old templates, and unclear trackers, it becomes difficult to prove what is happening in the service.
    </p>
    <p>
    Nexus turns that scattered information into a clearer structure managers can review, explain, and improve.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SERVICES
# =========================================================
st.markdown('<div id="services"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>Choose the support route that fits your current risk.</h2>
    <p class="section-intro">
    The £149 review is a fixed public checkout. Larger services are scoped privately because each client’s evidence, documents, and delivery package are different.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="grid-3">
    <div class="card">
        <span class="badge-gold">Fixed public checkout</span>
        <h3>£149 CQC Evidence File Review</h3>
        <div class="price">£149</div>
        <p>A focused review of your current evidence structure with gap notes, action points, and a practical next-step recommendation.</p>
        <ul>
            <li>Evidence folder structure review</li>
            <li>Gap notes</li>
            <li>Action tracker direction</li>
            <li>Summary of next steps</li>
            <li>Delivered within 3–5 business days after payment and receipt of required intake documents</li>
        </ul>
        <a class="btn-dark" href="{CQC_REVIEW_CHECKOUT_URL}" target="_blank" rel="noopener noreferrer">Buy Now</a>
    </div>

    <div class="card">
        <span class="badge">Scoped private Payhip link</span>
        <h3>30-Day CQC Evidence Cleanup Sprint</h3>
        <div class="price">From £750</div>
        <p>For providers with scattered or weak evidence files that need structured cleanup and clearer management records.</p>
        <ul>
            <li>Scoped after intake review</li>
            <li>40% deposit paid through a private Payhip link before work starts</li>
            <li>Preview or summary shown before final payment</li>
            <li>Final 60% paid through a private Payhip delivery link</li>
            <li>Completed files are released only after final payment</li>
        </ul>
        <a class="btn-dark" href="#request">Request Scope Review</a>
    </div>

    <div class="card">
        <span class="badge">Scoped private Payhip link</span>
        <h3>Monthly Compliance Retainer</h3>
        <div class="price">Scoped</div>
        <p>For providers that want regular evidence tracking, action tracker updates, document support, and monthly management summaries.</p>
        <ul>
            <li>Monthly support priced after scope review</li>
            <li>40% deposit paid through a private Payhip link before work starts</li>
            <li>Preview or summary shown before final payment where applicable</li>
            <li>Final 60% paid through a private Payhip delivery link</li>
            <li>Completed files are released only after final payment</li>
        </ul>
        <a class="btn-dark" href="#request">Request Retainer Scope</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="notice">
    <h3>Payment and delivery method</h3>
    <p>
    The £149 CQC Evidence File Review is the only fixed-price public checkout service.
    It can be purchased directly through Payhip checkout.
    </p>
    <p>
    Custom services, including the 30-Day Cleanup Sprint and Monthly Compliance Retainer,
    are handled through private Payhip links because each client’s evidence package is different.
    Once scope is agreed, Nexus creates a private hidden Payhip payment link for the 40% deposit.
    Work begins after the deposit is paid.
    </p>
    <p>
    When the work is ready, the customer receives a preview or summary of the package.
    The final 60% balance is then paid through a private Payhip delivery link.
    Files are released only after final payment through Payhip. The private delivery link is hidden
    from general customers and may be closed or archived after successful purchase.
    </p>
    <a class="btn-dark" href="{PAYHIP_URL}" target="_blank" rel="noopener noreferrer">View Digital Products on Payhip</a>
</div>
""", unsafe_allow_html=True)

# =========================================================
# WHY NEXUS
# =========================================================
st.markdown("""
<div class="section">
    <h2>Why this works for care managers.</h2>
    <p class="section-intro">
    Nexus does not sell random paperwork. The focus is evidence: what exists, what is weak, what is missing, and what needs action.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid-2">
    <div class="card">
        <h3>Evidence-first</h3>
        <p>The focus is on the records that show how the service is managed, monitored, reviewed, and improved.</p>
    </div>
    <div class="card">
        <h3>Manager-friendly</h3>
        <p>The output is designed to help managers understand the evidence position without drowning in paperwork.</p>
    </div>
    <div class="card">
        <h3>Action-focused</h3>
        <p>Every review should lead to clear next steps, not vague advice.</p>
    </div>
    <div class="card">
        <h3>Secure staged delivery</h3>
        <p>Custom packages are handled through scoped intake, Payhip deposit links, preview/summary review, and final Payhip delivery links before file release.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# PROCESS
# =========================================================
st.markdown('<div id="process"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>A simple process from first contact to clearer records.</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid-3">
    <div class="step">
        <div class="step-number">1</div>
        <h3>Choose the right route</h3>
        <p>Buy the £149 review directly, or submit the intake form for scoped support such as the 30-Day Sprint or Monthly Retainer.</p>
    </div>
    <div class="step">
        <div class="step-number">2</div>
        <h3>Submit intake and documents</h3>
        <p>Upload redacted documents such as folder indexes, trackers, policies, audit summaries, risk registers, or training matrices.</p>
    </div>
    <div class="step">
        <div class="step-number">3</div>
        <h3>Pay and receive securely</h3>
        <p>Fixed reviews are delivered after payment and intake. Custom work uses a 40% Payhip deposit, preview/summary, then final 60% Payhip delivery link before files are released.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# WHAT TO SEND
# =========================================================
st.markdown("""
<div class="green-notice">
    <h3>What Nexus needs before support begins</h3>
    <ul>
        <li>Full name and business/provider name</li>
        <li>Your role: registered manager, care manager, owner, operations lead, or compliance lead</li>
        <li>Provider type: domiciliary care, home care, supported living, residential care, new provider, or small business</li>
        <li>The support you want: £149 review, 30-Day Sprint, monthly support, or not sure yet</li>
        <li>Main concern: scattered evidence, outdated policies, weak trackers, inspection pressure, or missing management review records</li>
        <li>Document condition and available evidence areas</li>
        <li>Redacted supporting documents where possible</li>
        <li>For paid orders, include the Payhip order email or reference if available</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# =========================================================
# REQUEST FORM WITH UPLOAD
# =========================================================
st.markdown('<div id="request"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>Request service support.</h2>
    <p class="section-intro">
    Complete the intake form below so Nexus Conformité can understand your support need,
    evidence position, urgency, and the documents available for review. For the £149 review,
    please complete this after payment. For custom services, Nexus will review your request and
    issue a private Payhip deposit link where suitable.
    </p>
</div>
""", unsafe_allow_html=True)

components.html(f"""
<div style="background:#ffffff; border:1px solid #E5E7EB; border-radius:26px; padding:28px; box-shadow:0 16px 42px rgba(15,23,42,0.06); font-family:Arial, sans-serif; color:#172033;">

    <form action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">

        <input type="hidden" name="_subject" value="New Nexus Conformité Service Request">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none">

        <h2 style="color:#061A35; margin-top:0;">Service Request Intake</h2>
        <p style="color:#6B7280; font-size:15px; line-height:1.6;">
            Please provide enough detail for Nexus to recommend the right support level.
            Upload redacted documents only. Avoid sending identifiable service-user records unless Nexus later requests them through a secure method.
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

        <label><input type="checkbox" name="Available Evidence Areas" value="Policies and SOPs"> Policies and SOPs</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Evidence folder index or screenshots"> Evidence folder index or screenshots</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Risk register"> Risk register</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Training matrix or training records"> Training matrix or training records</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Audit records"> Audit records</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Incident records or incident tracker"> Incident records or incident tracker</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Complaints records or complaints tracker"> Complaints records or complaints tracker</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Action tracker"> Action tracker</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="Management review notes"> Management review notes</label><br>
        <label><input type="checkbox" name="Available Evidence Areas" value="CQC correspondence or report"> CQC correspondence or report, if relevant</label><br>

        <br>

        <h3 style="color:#061A35;">5. Upload supporting documents</h3>
        <p style="color:#6B7280; font-size:15px; line-height:1.6;">
            Upload redacted documents only. Useful examples include a folder index, policy list,
            evidence tracker, action tracker, audit summary, risk register, training matrix,
            or screenshots showing the document structure.
        </p>

        <label style="font-weight:700; color:#061A35;">Upload files *</label><br>
        <input type="file" name="attachment" multiple required accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.png,.jpg,.jpeg" style="width:100%; padding:14px; margin:8px 0 12px 0; border:1px dashed #C8A96A; border-radius:14px; font-size:16px; background:#FFF8E8; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Additional files, if needed</label><br>
        <input type="file" name="attachment2" multiple accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.png,.jpg,.jpeg" style="width:100%; padding:14px; margin:8px 0 12px 0; border:1px dashed #D1D5DB; border-radius:14px; font-size:16px; box-sizing:border-box;">

        <label style="font-weight:700; color:#061A35;">Additional files, if needed</label><br>
        <input type="file" name="attachment3" multiple accept=".pdf,.doc,.docx,.xls,.xlsx,.csv,.png,.jpg,.jpeg" style="width:100%; padding:14px; margin:8px 0 22px 0; border:1px dashed #D1D5DB; border-radius:14px; font-size:16px; box-sizing:border-box;">

        <h3 style="color:#061A35;">6. Main concern</h3>

        <label style="font-weight:700; color:#061A35;">Describe the issue *</label><br>
        <textarea name="Main Concern" required rows="7" placeholder="Example: Our policies exist but the evidence folders are scattered. We need help organising audits, incidents, complaints, training records, action trackers, and management review notes." style="width:100%; padding:14px; margin:8px 0 16px 0; border:1px solid #D1D5DB; border-radius:12px; font-size:16px; box-sizing:border-box;"></textarea>

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
""", height=2550, scrolling=True)

# =========================================================
# FAQS
# =========================================================
st.markdown('<div id="faq"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>FAQs</h2>
    <p class="section-intro">Clear answers before a care manager decides to contact Nexus.</p>
</div>
""", unsafe_allow_html=True)

with st.expander("Is the £149 review a full compliance audit?"):
    st.write("No. It is a focused evidence structure review. It helps identify obvious gaps, weak organisation, and practical next steps.")

with st.expander("Does Nexus replace the provider’s CQC responsibility?"):
    st.write("No. Nexus supports evidence organisation, documentation structure, action trackers, and management review preparation. The provider remains responsible for meeting regulatory requirements.")

with st.expander("Can Nexus support domiciliary care providers?"):
    st.write("Yes. The services are suitable for domiciliary care, home care, supported living, new providers, and small care providers that need clearer evidence structures.")

with st.expander("How does the £149 checkout work?"):
    st.write("The £149 CQC Evidence File Review is purchased through the public Payhip checkout link. After payment, the customer completes the intake form and uploads redacted documents. Delivery is within 3–5 business days after payment and receipt of the required intake documents.")

with st.expander("How does payment work for the 30-Day Sprint or Monthly Retainer?"):
    st.write("Custom services are scoped first. Once the scope is agreed, Nexus issues a private Payhip link for the 40% deposit. Work begins after the deposit is paid. The final 60% is paid through a private Payhip delivery link before completed files are released.")

with st.expander("How are final files released for custom services?"):
    st.write("Nexus may provide a preview or summary of the completed package. The final files are released only after the client pays the remaining balance through the private Payhip delivery link. The private link is hidden from general customers and may be closed or archived after successful purchase.")

with st.expander("How are private Payhip delivery links used?"):
    st.write("For custom work, Nexus creates a private Payhip product or checkout link for that specific customer. The link is not displayed publicly. The customer pays through that private link, and the completed files are released through Payhip after successful purchase.")

with st.expander("Can I move from the £149 review to the 30-Day Sprint?"):
    st.write("Yes. The £149 review is designed as the first step. If deeper cleanup is needed, the provider can move into the 30-Day Cleanup Sprint or monthly support.")

with st.expander("How are digital products delivered?"):
    st.write("Digital products and packages are delivered securely through Payhip where applicable. Custom support is scoped before delivery is confirmed.")

with st.expander("Should I upload confidential service-user records?"):
    st.write("No. Upload redacted documents only. Nexus will advise the next secure step if more sensitive records are required.")

with st.expander("Does Nexus provide legal advice?"):
    st.write("No. Nexus Conformité provides compliance organisation, evidence readiness, governance documentation, and operational support. It does not replace legal advice.")

# =========================================================
# CONTACT / FOOTER
# =========================================================
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="footer">
    <h3>Nexus Conformité</h3>
    <p>Connecting Law, Risk, and Compliance.</p>
    <p>
        Email: {EMAIL}<br>
        Facebook: @nexusconformite<br>
        Payhip: payhip.com/NexusConformite<br>
        LinkedIn: {LINKEDIN_NAME}
    </p>
    <p>
        Nexus Conformité provides compliance organisation, evidence readiness, policy structure,
        and governance documentation support. Services do not replace legal advice or the provider’s own regulatory responsibilities.
    </p>
</div>
""", unsafe_allow_html=True)