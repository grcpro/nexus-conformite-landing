import streamlit as st
import os
import glob
from urllib.parse import quote

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Nexus Conformité | CQC Compliance Support for UK Care Providers",
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

# =========================================================
# LOGO FINDER
# =========================================================
def find_logo():
    preferred_names = [
        "Nexus_Conformite_logo_transparent.png",
        "Nexus Conformite logo transparent.png",
        "Nexus_Conformité_logo_transparent.png",
        ".Nexus_Conformite_logo_transparent.png",
        ". Nexus_Conformite_logo_transparent.png",
        "logo.png",
        "Logo.png",
    ]

    for name in preferred_names:
        if os.path.exists(name):
            return name

    image_files = []
    for pattern in ["*.png", "*.jpg", "*.jpeg", "*.webp", ".*.png", ".*.jpg", ".*.jpeg", ".*.webp"]:
        image_files.extend(glob.glob(pattern))

    for file in image_files:
        clean = file.lower().replace(" ", "").replace("_", "").replace("-", "")
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
    --navy: #071B3A;
    --navy2: #0B2545;
    --blue: #12375B;
    --gold: #C8A96A;
    --green: #0F766E;
    --cream: #FAF8F2;
    --light: #F5F7FA;
    --white: #FFFFFF;
    --text: #1F2937;
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
    background: linear-gradient(180deg, #FFFFFF 0%, #F5F7FA 50%, #FAF8F2 100%);
    color: var(--text);
}

.block-container {
    padding-top: 1.1rem;
    padding-bottom: 4rem;
    max-width: 1180px;
}

h1, h2, h3, h4 {
    color: var(--navy);
    letter-spacing: -0.03em;
}

p, li {
    font-size: 18px;
    line-height: 1.65;
    color: var(--text);
}

.brand-text h1 {
    font-size: 30px;
    margin: 0;
    color: var(--navy);
}

.brand-text p {
    margin: 4px 0 0 0;
    color: var(--muted);
    font-size: 15px;
}

.nav-label {
    font-size: 13px;
    text-transform: uppercase;
    color: var(--muted);
    letter-spacing: 0.12em;
    margin-top: 14px;
    margin-bottom: 4px;
}

.hero {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle at top right, rgba(200,169,106,0.24), transparent 28%),
        linear-gradient(135deg, #071B3A 0%, #0B2545 48%, #0F766E 100%);
    border-radius: 34px;
    padding: 64px 54px;
    margin: 24px 0 26px 0;
    box-shadow: 0 24px 60px rgba(7,27,58,0.22);
}

.hero::after {
    content: "";
    position: absolute;
    width: 340px;
    height: 340px;
    right: -130px;
    bottom: -150px;
    background: rgba(255,255,255,0.06);
    border-radius: 50%;
}

.eyebrow {
    color: var(--gold);
    font-size: 14px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 14px;
}

.hero h1 {
    color: white;
    font-size: 56px;
    line-height: 1.02;
    margin: 0 0 18px 0;
    max-width: 940px;
}

.hero p {
    color: #EAF0F7;
    font-size: 22px;
    max-width: 880px;
    margin-bottom: 0;
}

.cta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin: 22px 0 8px 0;
}

.btn-primary, .btn-secondary, .btn-light {
    display: inline-block;
    padding: 14px 20px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 16px;
    text-decoration: none;
}

.btn-primary {
    background: var(--gold);
    color: var(--navy) !important;
}

.btn-secondary {
    background: var(--navy);
    color: white !important;
}

.btn-light {
    background: white;
    color: var(--navy) !important;
    border: 1px solid var(--line);
}

.section-title {
    font-size: 38px;
    margin-bottom: 10px;
}

.section-intro {
    color: var(--muted);
    max-width: 860px;
    font-size: 19px;
}

.card {
    background: rgba(255,255,255,0.97);
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 30px;
    margin-bottom: 20px;
    box-shadow: 0 16px 40px rgba(15,23,42,0.06);
}

.card h2 {
    font-size: 31px;
    margin-top: 0;
}

.card h3 {
    font-size: 23px;
    margin-top: 0;
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

.service-card {
    background: white;
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 28px;
    box-shadow: 0 14px 34px rgba(7,27,58,0.07);
}

.service-card h3 {
    color: var(--navy);
    font-size: 24px;
    margin-bottom: 6px;
}

.price {
    font-size: 30px;
    color: var(--green);
    font-weight: 800;
    margin: 10px 0;
}

.gold-line {
    width: 78px;
    height: 4px;
    background: var(--gold);
    border-radius: 999px;
    margin: 12px 0 18px 0;
}

.badge {
    display: inline-block;
    background: #EEF8F5;
    color: var(--green);
    border: 1px solid #CDEBE4;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
}

.gold-badge {
    display: inline-block;
    background: #FFF8E8;
    color: #7A5C13;
    border: 1px solid #F0DB9B;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
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
    position: relative;
    background: white;
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 24px;
    margin-bottom: 14px;
}

.footer {
    margin-top: 36px;
    background: var(--navy);
    color: white;
    border-radius: 28px;
    padding: 34px;
}

.footer p {
    color: #DDE6F2;
    font-size: 16px;
}

.footer strong {
    color: white;
}

.form-note {
    font-size: 15px;
    color: var(--muted);
}

@media (max-width: 900px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        padding: 42px 26px;
        border-radius: 28px;
    }

    .hero h1 {
        font-size: 38px;
    }

    .hero p {
        font-size: 18px;
    }

    .section-title {
        font-size: 31px;
    }

    .grid-3, .grid-2 {
        grid-template-columns: 1fr;
    }

    .card, .service-card {
        padding: 24px;
        border-radius: 22px;
    }

    p, li {
        font-size: 17px;
    }

    .btn-primary, .btn-secondary, .btn-light {
        width: 100%;
        text-align: center;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# COMPONENTS
# =========================================================
def render_header():
    if LOGO_PATH:
        col_logo, col_text = st.columns([1, 5])
        with col_logo:
            st.image(LOGO_PATH, width=105)
        with col_text:
            st.markdown("""
            <div class="brand-text">
                <h1>Nexus Conformité</h1>
                <p>CQC compliance support, evidence organisation, governance documentation, and operational readiness.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="brand-text">
            <h1>Nexus Conformité</h1>
            <p>CQC compliance support, evidence organisation, governance documentation, and operational readiness.</p>
        </div>
        """, unsafe_allow_html=True)


def hero(eyebrow, title, body):
    st.markdown(f"""
    <div class="hero">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{title}</h1>
        <p>{body}</p>
    </div>
    """, unsafe_allow_html=True)


def cta_buttons(primary_text="Start with the £149 Review", primary_url=PAYHIP_URL):
    st.markdown(f"""
    <div class="cta-row">
        <a class="btn-primary" href="{primary_url}" target="_blank">{primary_text}</a>
        <a class="btn-secondary" href="{FACEBOOK_URL}" target="_blank">Message on Facebook</a>
        <a class="btn-light" href="mailto:{EMAIL}">Email Nexus</a>
    </div>
    """, unsafe_allow_html=True)


def footer():
    st.markdown(f"""
    <div class="footer">
        <strong>Nexus Conformité</strong>
        <p>Connecting Law, Risk, and Compliance.</p>
        <p>
            Email: {EMAIL}<br>
            Facebook: @nexusconformite<br>
            Payhip: payhip.com/NexusConformite<br>
            LinkedIn: {LINKEDIN_NAME}
        </p>
        <p>
            Nexus Conformité provides compliance organisation, evidence readiness,
            policy structure, and governance documentation support. Services do not replace
            legal advice or the provider’s own regulatory responsibilities.
        </p>
    </div>
    """, unsafe_allow_html=True)


def email_request_form(default_service="£149 CQC Evidence File Review", key="general"):
    st.markdown("""
    <div class="card">
        <h2>Request support</h2>
        <div class="gold-line"></div>
        <p>
        Complete the details below. The form will prepare an email for you to send to Nexus Conformité.
        This keeps the process simple, secure, and clear before any scope review begins.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form(f"contact_form_{key}"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full name")
            business_name = st.text_input("Business / provider name")
            email_address = st.text_input("Your email address")
            phone = st.text_input("Phone / WhatsApp number")

        with col2:
            role = st.selectbox(
                "Your role",
                [
                    "Registered Manager",
                    "Care Manager",
                    "Provider / Owner",
                    "Operations Manager",
                    "Compliance Lead",
                    "Small Business Owner",
                    "Other"
                ]
            )
            provider_type = st.selectbox(
                "Type of organisation",
                [
                    "Domiciliary care provider",
                    "Home care provider",
                    "Supported living provider",
                    "Residential care provider",
                    "New care provider",
                    "Small business",
                    "Other"
                ]
            )
            service_needed = st.selectbox(
                "Support needed",
                [
                    "£149 CQC Evidence File Review",
                    "30-Day CQC Evidence Cleanup Sprint",
                    "Monthly Compliance Retainer",
                    "Small Business Compliance Readiness",
                    "Not sure yet"
                ],
                index=[
                    "£149 CQC Evidence File Review",
                    "30-Day CQC Evidence Cleanup Sprint",
                    "Monthly Compliance Retainer",
                    "Small Business Compliance Readiness",
                    "Not sure yet"
                ].index(default_service) if default_service in [
                    "£149 CQC Evidence File Review",
                    "30-Day CQC Evidence Cleanup Sprint",
                    "Monthly Compliance Retainer",
                    "Small Business Compliance Readiness",
                    "Not sure yet"
                ] else 0
            )
            urgency = st.selectbox(
                "Urgency",
                [
                    "Not urgent",
                    "Need support this month",
                    "Inspection pressure / urgent",
                    "Preparing before registration or review",
                    "Ongoing monthly support needed"
                ]
            )

        document_state = st.radio(
            "Current document condition",
            [
                "Mostly organised",
                "Some documents are scattered",
                "Very scattered and unclear",
                "We are starting from scratch",
                "Not sure"
            ],
            horizontal=False
        )

        main_concern = st.text_area(
            "Main concern",
            placeholder="Example: Our policies exist but the evidence folders are scattered. We need help organising audits, incidents, complaints, training records, and action trackers."
        )

        submitted = st.form_submit_button("Prepare email request")

    if submitted:
        if not name or not email_address or not main_concern:
            st.error("Please include at least your name, email address, and main concern.")
        else:
            subject = f"Nexus Conformité Support Request - {service_needed}"
            body = f"""Hello Nexus Conformité,

I would like to request support.

Full name: {name}
Business / provider name: {business_name}
Email address: {email_address}
Phone / WhatsApp: {phone}

Role: {role}
Organisation type: {provider_type}
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

            st.success("Your email request is prepared. Tap the button below to open your email app.")
            st.markdown(f"""
            <div class="cta-row">
                <a class="btn-primary" href="{mailto}">Open prepared email</a>
            </div>
            """, unsafe_allow_html=True)

            st.text_area("Copy of prepared email", body, height=320)


def what_to_email_card():
    st.markdown("""
    <div class="card">
        <h2>What to include when contacting Nexus</h2>
        <div class="gold-line"></div>
        <ul>
            <li>Your full name and business or provider name</li>
            <li>Your role, such as registered manager, care manager, provider, owner, or operations lead</li>
            <li>The type of service, such as domiciliary care, home care, supported living, residential care, or small business</li>
            <li>The support you are interested in: £149 review, 30-Day Cleanup Sprint, monthly retainer, or small business readiness</li>
            <li>Your main concern, such as scattered evidence, outdated policies, weak trackers, inspection pressure, or missing management review records</li>
            <li>Your urgency level and whether any deadline or inspection pressure exists</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# HEADER + NAV
# =========================================================
render_header()

st.markdown('<div class="nav-label">Select a page</div>', unsafe_allow_html=True)

page = st.selectbox(
    "Select a page",
    [
        "Home",
        "£149 CQC Evidence File Review",
        "30-Day CQC Evidence Cleanup Sprint",
        "Monthly Compliance Retainer",
        "Small Business Compliance Readiness",
        "FAQs",
        "About Nexus",
        "Contact"
    ],
    label_visibility="collapsed"
)

# =========================================================
# HOME
# =========================================================
if page == "Home":
    hero(
        "UK Care Compliance Support",
        "CQC evidence support for UK care managers and small care providers.",
        "Nexus Conformité helps care managers organise evidence files, policies, SOPs, trackers, and governance records so compliance is clearer, easier to review, and better prepared for inspection pressure."
    )

    cta_buttons()

    st.markdown("""
    <div class="card">
        <h2>Built for managers who need proof, not just paperwork.</h2>
        <div class="gold-line"></div>
        <p>
        Many care providers are doing the work but struggle to show it clearly through
        organised records, evidence trails, management reviews, risk logs, incident files,
        complaints records, training records, and action trackers.
        </p>
        <p>
        Nexus Conformité helps turn scattered compliance documents into a clearer,
        review-ready evidence structure.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="grid-3">
        <div class="service-card">
            <span class="gold-badge">Best first step</span>
            <h3>£149 CQC Evidence File Review</h3>
            <div class="price">£149</div>
            <p>A focused review of your current evidence structure with practical gap notes, action points, and recommended next steps.</p>
        </div>
        <div class="service-card">
            <span class="badge">Structured cleanup</span>
            <h3>30-Day CQC Evidence Cleanup Sprint</h3>
            <div class="price">£750–£1,500</div>
            <p>A structured cleanup service for providers that need stronger evidence files, clearer trackers, organised policies, and management review records.</p>
        </div>
        <div class="service-card">
            <span class="badge">Ongoing support</span>
            <h3>Monthly Compliance Retainer</h3>
            <div class="price">Scoped</div>
            <p>Ongoing evidence tracking, policy support, action tracker updates, and monthly management summary support.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="green-notice">
        <strong>Recommended client journey:</strong><br>
        Start with the £149 CQC Evidence File Review. If deeper support is needed,
        move into the 30-Day Cleanup Sprint, then monthly compliance support.
    </div>
    """, unsafe_allow_html=True)

    what_to_email_card()
    email_request_form(default_service="£149 CQC Evidence File Review", key="home")
    footer()

# =========================================================
# £149 REVIEW
# =========================================================
elif page == "£149 CQC Evidence File Review":
    hero(
        "Entry Review Offer",
        "£149 CQC Evidence File Review.",
        "A focused review for UK care managers who need to understand what is missing, weak, scattered, duplicated, or unclear in their compliance evidence structure."
    )

    cta_buttons("Request the £149 Review", PAYHIP_URL)

    st.markdown("""
    <div class="grid-2">
        <div class="card">
            <h2>What this review is for</h2>
            <div class="gold-line"></div>
            <p>
            This review is designed for care managers and small providers who need a practical
            starting point before investing in a larger compliance cleanup package.
            </p>
            <p>
            It helps identify whether your records are easy to explain, easy to locate,
            and strong enough to support management review, internal monitoring, and inspection preparation.
            </p>
        </div>
        <div class="card">
            <h2>Price and outcome</h2>
            <div class="gold-line"></div>
            <div class="price">£149</div>
            <p>
            You receive a practical summary of your current evidence position,
            gap notes, and recommended next steps.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>What is included</h2>
        <ul>
            <li>Review of your current evidence folder structure</li>
            <li>Gap notes identifying missing, weak, duplicated, or unclear records</li>
            <li>CQC evidence checklist direction</li>
            <li>Basic action tracker</li>
            <li>Notes on policy and SOP organisation</li>
            <li>Short written summary of recommended next steps</li>
            <li>Recommendation on whether a full 30-Day Cleanup Sprint is needed</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    what_to_email_card()
    email_request_form(default_service="£149 CQC Evidence File Review", key="review")
    footer()

# =========================================================
# 30 DAY SPRINT
# =========================================================
elif page == "30-Day CQC Evidence Cleanup Sprint":
    hero(
        "Higher Support Package",
        "30-Day CQC Evidence Cleanup Sprint.",
        "A structured cleanup service for care providers that need stronger evidence files, clearer trackers, better documentation, and a more organised compliance system."
    )

    cta_buttons("Request Sprint Scope Review", f"mailto:{EMAIL}")

    st.markdown("""
    <div class="card">
        <h2>What the sprint solves</h2>
        <div class="gold-line"></div>
        <p>
        Care providers often have policies, training records, incidents, audits,
        complaints, risk documents, and management notes spread across different folders or formats.
        This creates stress when managers need to explain what is happening in the service.
        </p>
        <p>
        The sprint brings those records into a clearer structure so management can see what exists,
        what is missing, and what needs action.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="grid-2">
        <div class="card">
            <h2>What can be included</h2>
            <ul>
                <li>Evidence folder cleanup</li>
                <li>Policy and SOP organisation</li>
                <li>Risk, incident, complaints, training, and audit record structure</li>
                <li>Evidence gap identification</li>
                <li>Action tracker development</li>
                <li>Management review summary</li>
                <li>Final evidence pack structure</li>
            </ul>
        </div>
        <div class="card">
            <h2>Pricing</h2>
            <div class="price">£750–£1,500</div>
            <p>
            Final pricing depends on document volume, urgency, provider size,
            and the current condition of the records.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    email_request_form(default_service="30-Day CQC Evidence Cleanup Sprint", key="sprint")
    footer()

# =========================================================
# MONTHLY RETAINER
# =========================================================
elif page == "Monthly Compliance Retainer":
    hero(
        "Ongoing Support",
        "Monthly Compliance Retainer.",
        "Ongoing compliance organisation for care providers and small businesses that want their records, policies, trackers, and management evidence kept under control."
    )

    cta_buttons("Ask About Monthly Support", f"mailto:{EMAIL}")

    st.markdown("""
    <div class="card">
        <h2>Why monthly support matters</h2>
        <div class="gold-line"></div>
        <p>
        Compliance is not a one-time cleanup. Evidence must be maintained, reviewed,
        updated, and explained over time. Monthly support helps prevent documents
        from becoming outdated, scattered, or forgotten.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="grid-2">
        <div class="card">
            <h2>Monthly support can include</h2>
            <ul>
                <li>Monthly evidence tracker update</li>
                <li>Action tracker review</li>
                <li>Policy and SOP update support</li>
                <li>Incident, complaints, training, audit, and risk record checks</li>
                <li>Monthly management summary notes</li>
                <li>Compliance improvement follow-up</li>
                <li>Support preparing internal review packs</li>
            </ul>
        </div>
        <div class="card">
            <h2>Pricing</h2>
            <div class="price">Scoped</div>
            <p>
            Monthly retainer pricing is agreed after scope review based on provider size,
            document volume, urgency, and support level.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    email_request_form(default_service="Monthly Compliance Retainer", key="retainer")
    footer()

# =========================================================
# SMALL BUSINESS
# =========================================================
elif page == "Small Business Compliance Readiness":
    hero(
        "Small Business Compliance",
        "Small Business Compliance Readiness.",
        "Compliance and operations support for small businesses that need clearer documents, stronger internal controls, better records, and more professional procedures."
    )

    cta_buttons("Request Small Business Support", f"mailto:{EMAIL}")

    st.markdown("""
    <div class="card">
        <h2>What can be included</h2>
        <ul>
            <li>Business readiness checklist</li>
            <li>Policy and procedure structure</li>
            <li>Risk and control register template</li>
            <li>Customer and supplier record guidance</li>
            <li>Basic privacy and data protection document support</li>
            <li>Internal operations checklist</li>
            <li>Management action tracker</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    email_request_form(default_service="Small Business Compliance Readiness", key="smallbiz")
    footer()

# =========================================================
# FAQ
# =========================================================
elif page == "FAQs":
    hero(
        "Questions & Answers",
        "CQC compliance support FAQs.",
        "Clear answers for care managers and small providers considering Nexus Conformité support."
    )

    with st.expander("Is the £149 CQC Evidence File Review a full compliance audit?"):
        st.write("No. It is a focused evidence structure review. It helps identify obvious gaps, weak organisation, and practical next steps. A deeper cleanup or audit-style review may require a larger package.")

    with st.expander("Does Nexus replace the provider’s responsibility to comply with CQC requirements?"):
        st.write("No. Nexus supports evidence organisation, documentation structure, trackers, and management review preparation. The provider remains responsible for meeting regulatory requirements.")

    with st.expander("Can Nexus support domiciliary care providers?"):
        st.write("Yes. The services are suitable for small care providers, domiciliary care providers, home care providers, supported living providers, and managers who need clearer evidence structures.")

    with st.expander("What should I send before the £149 review?"):
        st.write("Send your role, provider type, current document condition, main concern, urgency, and whether you have existing evidence folders, policies, SOPs, trackers, training records, incident logs, complaints records, audits, or risk documents.")

    with st.expander("Is the 30-Day Cleanup Sprint suitable before inspection pressure?"):
        st.write("It can help organise records and identify gaps before inspection pressure increases. The earlier the provider starts, the better the outcome. Urgent work may affect pricing.")

    with st.expander("How are digital packages delivered?"):
        st.write("Digital products and packages are delivered securely through Payhip where applicable. Custom support is scoped first before the final delivery method is confirmed.")

    with st.expander("Can I move from the £149 review to the 30-Day Sprint?"):
        st.write("Yes. The £149 review is designed as the first step. If the evidence file needs deeper cleanup, the provider can move into the 30-Day Sprint or monthly compliance support.")

    with st.expander("Do you provide legal advice?"):
        st.write("No. Nexus Conformité provides compliance organisation, governance documentation, evidence readiness, and operational support. It does not replace legal advice.")

    what_to_email_card()
    cta_buttons()
    footer()

# =========================================================
# ABOUT
# =========================================================
elif page == "About Nexus":
    hero(
        "About the Firm",
        "Practical compliance support with a governance-first approach.",
        "Nexus Conformité connects law, risk, compliance, data protection, governance, and operational documentation into practical support for regulated and growing businesses."
    )

    st.markdown("""
    <div class="card">
        <h2>Our focus</h2>
        <div class="gold-line"></div>
        <p>
        Nexus Conformité focuses on practical compliance systems, not generic paperwork.
        The aim is to help businesses organise their evidence, strengthen governance records,
        improve accountability, and prepare clearer documentation for review.
        </p>
        <p>
        The firm supports care compliance, small business readiness, policy and SOP structure,
        evidence tracking, risk documentation, and internal control organisation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="grid-2">
        <div class="card">
            <h2>Our approach</h2>
            <ul>
                <li>Evidence-first compliance support</li>
                <li>Governance and internal control focus</li>
                <li>Clear action trackers and management summaries</li>
                <li>Practical organisation for real business operations</li>
            </ul>
        </div>
        <div class="card">
            <h2>Core areas</h2>
            <ul>
                <li>CQC evidence organisation</li>
                <li>Policy and SOP structure</li>
                <li>Risk and action tracking</li>
                <li>Compliance documentation cleanup</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    cta_buttons()
    footer()

# =========================================================
# CONTACT
# =========================================================
elif page == "Contact":
    hero(
        "Contact Nexus",
        "Start with the right support level.",
        "Message Nexus Conformité to request the £149 review, discuss the 30-Day Cleanup Sprint, or ask about monthly compliance support."
    )

    cta_buttons()

    st.markdown(f"""
    <div class="grid-2">
        <div class="card">
            <h2>Contact details</h2>
            <p><strong>Email:</strong> {EMAIL}</p>
            <p><strong>Facebook:</strong> @nexusconformite</p>
            <p><strong>Payhip:</strong> payhip.com/NexusConformite</p>
            <p><strong>LinkedIn:</strong> {LINKEDIN_NAME}</p>
        </div>
        <div class="card">
            <h2>Best first step</h2>
            <p>
            Start with the £149 CQC Evidence File Review if you are unsure what support you need.
            If your records are already known to be scattered or urgent, request a 30-Day Cleanup Sprint scope review.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    what_to_email_card()
    email_request_form(default_service="Not sure yet", key="contact")
    footer()