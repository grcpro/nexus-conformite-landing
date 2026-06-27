import streamlit as st
import os
import glob
from urllib.parse import quote

st.set_page_config(
    page_title="Nexus Conformité | CQC Evidence & Compliance Support",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BUSINESS_NAME = "Nexus Conformité"
EMAIL = "nexusconformite@proton.me"
FACEBOOK_URL = "https://www.facebook.com/nexusconformite"
PAYHIP_URL = "https://payhip.com/NexusConformite"
LINKEDIN_NAME = "Nexus Conformité"


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

st.markdown("""
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
.btn-light {
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
    .btn-light {
        width: 100%;
        text-align: center;
    }
}
</style>
""", unsafe_allow_html=True)


# Header
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
        <a href="#faq">FAQs</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)


# Hero
st.markdown(f"""
<div class="hero">
    <div class="eyebrow">UK care compliance support</div>
    <h1>CQC evidence support for care managers who need clarity before pressure increases.</h1>
    <p>
    Nexus Conformité helps care managers and small providers organise evidence files,
    policies, SOPs, trackers, and governance records into a clearer review-ready structure.
    </p>
    <div class="cta-row">
        <a class="btn-primary" href="{PAYHIP_URL}" target="_blank">Start with the £149 Review</a>
        <a class="btn-secondary" href="{FACEBOOK_URL}" target="_blank">Message on Facebook</a>
        <a class="btn-light" href="mailto:{EMAIL}">Email Nexus</a>
    </div>
</div>
""", unsafe_allow_html=True)


# Problem psychology section
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


# Services
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <h2>Choose the support level that fits your current risk.</h2>
    <p class="section-intro">
    The service ladder is simple: start small, understand the evidence gaps, clean up what matters, then maintain it monthly if needed.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid-3">
    <div class="card">
        <span class="badge-gold">Best first step</span>
        <h3>£149 CQC Evidence File Review</h3>
        <div class="price">£149</div>
        <p>A focused review of your current evidence structure with gap notes, action points, and a practical next step recommendation.</p>
        <ul>
            <li>Evidence folder structure review</li>
            <li>Gap notes</li>
            <li>Action tracker direction</li>
            <li>Summary of next steps</li>
        </ul>
    </div>
    <div class="card">
        <span class="badge">Structured cleanup</span>
        <h3>30-Day CQC Evidence Cleanup Sprint</h3>
        <div class="price">£750–£1,500</div>
        <p>For providers with scattered or weak evidence files that need structured cleanup and clearer management records.</p>
        <ul>
            <li>Evidence folder cleanup</li>
            <li>Policy and SOP organisation</li>
            <li>Risk, training, audit, incident, and complaints record structure</li>
            <li>Management review summary</li>
        </ul>
    </div>
    <div class="card">
        <span class="badge">Ongoing control</span>
        <h3>Monthly Compliance Retainer</h3>
        <div class="price">Scoped</div>
        <p>For providers that want regular evidence tracking, action tracker updates, document support, and monthly management summaries.</p>
        <ul>
            <li>Monthly evidence tracker update</li>
            <li>Action tracker review</li>
            <li>Policy update support</li>
            <li>Management summary notes</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)


# Why Nexus
st.markdown("""
<div class="section">
    <h2>Why this works for care managers.</h2>
    <p class="section-intro">
    The page is not selling random templates. The offer is built around the real management need: know what evidence exists, what is weak, what is missing, and what needs action.
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
        <h3>Scalable</h3>
        <p>Clients can start with the £149 review, move into cleanup, then continue with monthly support.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# Process
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
        <h3>Send the basics</h3>
        <p>Share your role, provider type, main concern, urgency, and current document condition.</p>
    </div>
    <div class="step">
        <div class="step-number">2</div>
        <h3>Start with the right offer</h3>
        <p>Most clients begin with the £149 review. Urgent or scattered files may move straight to scope review.</p>
    </div>
    <div class="step">
        <div class="step-number">3</div>
        <h3>Receive clear next steps</h3>
        <p>You receive practical direction on what is missing, weak, scattered, or ready for cleanup.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# What to email
st.markdown("""
<div class="green-notice">
    <h3>What to email Nexus before support begins</h3>
    <ul>
        <li>Full name and business/provider name</li>
        <li>Your role: registered manager, care manager, owner, operations lead, or compliance lead</li>
        <li>Provider type: domiciliary care, home care, supported living, residential care, new provider, or small business</li>
        <li>The service you want: £149 review, 30-Day Sprint, monthly support, or not sure yet</li>
        <li>Your main concern: scattered evidence, outdated policies, weak trackers, inspection pressure, or missing management review records</li>
        <li>Your urgency level and whether any deadline exists</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# Form
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <h2>Prepare your request.</h2>
    <p class="section-intro">
    This form prepares an email for you. It does not store sensitive information on the website.
    </p>
</div>
""", unsafe_allow_html=True)

with st.form("nexus_contact_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full name")
        business_name = st.text_input("Business / provider name")
        client_email = st.text_input("Your email address")
        phone = st.text_input("Phone / WhatsApp")

    with col2:
        role = st.selectbox(
            "Your role",
            ["Registered Manager", "Care Manager", "Provider / Owner", "Operations Manager", "Compliance Lead", "Small Business Owner", "Other"]
        )

        organisation_type = st.selectbox(
            "Organisation type",
            ["Domiciliary care provider", "Home care provider", "Supported living provider", "Residential care provider", "New care provider", "Small business", "Other"]
        )

        service_needed = st.selectbox(
            "Support needed",
            ["£149 CQC Evidence File Review", "30-Day CQC Evidence Cleanup Sprint", "Monthly Compliance Retainer", "Small Business Compliance Readiness", "Not sure yet"]
        )

        urgency = st.selectbox(
            "Urgency",
            ["Not urgent", "Need support this month", "Inspection pressure / urgent", "Preparing before registration or review", "Ongoing monthly support needed"]
        )

    document_state = st.radio(
        "Current document condition",
        ["Mostly organised", "Some documents are scattered", "Very scattered and unclear", "Starting from scratch", "Not sure"]
    )

    main_concern = st.text_area(
        "Main concern",
        placeholder="Example: Our policies exist but the evidence folders are scattered. We need help organising audits, incidents, complaints, training records, and action trackers."
    )

    submitted = st.form_submit_button("Prepare email")

if submitted:
    if not name or not client_email or not main_concern:
        st.error("Please include your name, email address, and main concern.")
    else:
        subject = f"Nexus Conformité Support Request - {service_needed}"
        body = f"""Hello Nexus Conformité,

I would like to request support.

Full name: {name}
Business / provider name: {business_name}
Email address: {client_email}
Phone / WhatsApp: {phone}

Role: {role}
Organisation type: {organisation_type}
Support needed: {service_needed}
Urgency: {urgency}
Current document condition: {document_state}

Main concern:
{main_concern}

Please advise the suitable next step.

Kind regards,
{name}
"""
        mailto = f"mailto:{EMAIL}?subject={quote(subject)}&body={quote(body)}"

        st.success("Your email is prepared. Tap below to open your email app.")
        st.markdown(f"""
        <div class="cta-row">
            <a class="btn-primary" href="{mailto}">Open prepared email</a>
        </div>
        """, unsafe_allow_html=True)

        st.text_area("Copy of prepared email", body, height=300)


# FAQs
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

with st.expander("Can I move from the £149 review to the 30-Day Sprint?"):
    st.write("Yes. The £149 review is designed as the first step. If deeper cleanup is needed, the provider can move into the 30-Day Cleanup Sprint or monthly support.")

with st.expander("How are digital products delivered?"):
    st.write("Digital products and packages are delivered securely through Payhip where applicable. Custom support is scoped before delivery is confirmed.")

with st.expander("Does Nexus provide legal advice?"):
    st.write("No. Nexus Conformité provides compliance organisation, evidence readiness, governance documentation, and operational support. It does not replace legal advice.")


# Footer
st.markdown(f"""
<div class="footer">
    <h3 style="color:white;">Nexus Conformité</h3>
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