import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Nexus Conformité | CQC Compliance Support for UK Care Providers",
    page_icon="NC",
    layout="wide"
)

# ---------------- BUSINESS DETAILS ----------------
BUSINESS_NAME = "Nexus Conformité"
EMAIL = "nexusconformite@proton.me"
FACEBOOK_URL = "https://www.facebook.com/nexusconformite"
PAYHIP_URL = "https://payhip.com/NexusConformite"
LINKEDIN_NAME = "Nexus Conformité"
LOGO_PATH = "Nexus_Conformite_logo_transparent.png"


# ---------------- CSS STYLE ----------------
st.markdown("""
<style>
.stApp {
    background-color: #F5F6F8;
    color: #1F2937;
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    max-width: 1180px;
}

h1, h2, h3 {
    color: #0B1F3A;
}

p, li {
    font-size: 18px;
    line-height: 1.65;
}

.hero {
    background: linear-gradient(135deg, #0B1F3A 0%, #12375B 60%, #0F766E 100%);
    padding: 58px 42px;
    border-radius: 28px;
    color: white;
    margin-bottom: 28px;
}

.hero h1 {
    color: white;
    font-size: 54px;
    line-height: 1.05;
    margin-bottom: 18px;
}

.hero p {
    color: #EEF2F7;
    font-size: 23px;
    max-width: 980px;
}

.hero .tag {
    color: #D6C18A;
    font-size: 18px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 14px;
}

.card {
    background: #FFFFFF;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid #E3E7ED;
    box-shadow: 0 8px 22px rgba(11, 31, 58, 0.06);
    margin-bottom: 22px;
}

.card h2 {
    font-size: 32px;
    margin-bottom: 12px;
}

.card h3 {
    font-size: 24px;
    color: #12375B;
}

.price-card {
    background: #FFFFFF;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid #E3E7ED;
    box-shadow: 0 8px 22px rgba(11, 31, 58, 0.06);
    height: 100%;
}

.price-card h3 {
    color: #0B1F3A;
    font-size: 25px;
}

.price {
    color: #0F766E;
    font-size: 30px;
    font-weight: 700;
    margin: 12px 0;
}

.gold-line {
    height: 4px;
    width: 86px;
    background: #C8A96A;
    border-radius: 20px;
    margin: 10px 0 18px 0;
}

.notice {
    background: #FFF8E8;
    border-left: 6px solid #C8A96A;
    padding: 20px;
    border-radius: 16px;
    margin: 16px 0;
}

.green-notice {
    background: #EAF7F4;
    border-left: 6px solid #0F766E;
    padding: 20px;
    border-radius: 16px;
    margin: 16px 0;
}

.footer {
    text-align: center;
    color: #6B7280;
    padding: 34px 12px;
    font-size: 16px;
}

.nav-box {
    background: #FFFFFF;
    padding: 18px;
    border-radius: 18px;
    border: 1px solid #E3E7ED;
    margin-bottom: 18px;
}

.small {
    font-size: 15px;
    color: #6B7280;
}
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER / LOGO ----------------
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=210)
else:
    st.markdown("## Nexus Conformité")

st.markdown(
    "<p class='small'>CQC compliance support, evidence organisation, governance documentation, and operational readiness support.</p>",
    unsafe_allow_html=True
)


# ---------------- NAVIGATION ----------------
page = st.radio(
    "Navigation",
    [
        "Home",
        "£149 CQC Evidence File Review",
        "30-Day Cleanup Sprint",
        "Monthly Retainer",
        "Small Business Readiness",
        "About",
        "FAQs",
        "Contact"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()


# ---------------- REUSABLE CTA ----------------
def contact_buttons():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("Message on Facebook", FACEBOOK_URL, use_container_width=True)
    with col2:
        st.link_button("Payhip Shop", PAYHIP_URL, use_container_width=True)
    with col3:
        st.link_button("Email Nexus", f"mailto:{EMAIL}", use_container_width=True)


def footer():
    st.markdown(f"""
    <div class="footer">
        <strong>Nexus Conformité</strong><br>
        Connecting Law, Risk, and Compliance<br>
        Email: {EMAIL} | Facebook: @nexusconformite | Payhip: payhip.com/NexusConformite
    </div>
    """, unsafe_allow_html=True)


# ---------------- HOME PAGE ----------------
if page == "Home":
    st.markdown("""
    <div class="hero">
        <div class="tag">UK Care Compliance Support</div>
        <h1>CQC evidence support for UK care managers and small care providers.</h1>
        <p>
        Nexus Conformité helps care managers organise evidence files, policies, SOPs,
        trackers, and governance records so compliance is clearer, easier to review,
        and better prepared for inspection pressure.
        </p>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()

    st.markdown("""
    <div class="card">
        <h2>Built for care managers who need proof, not just paperwork.</h2>
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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="price-card">
            <h3>£149 CQC Evidence File Review</h3>
            <div class="gold-line"></div>
            <div class="price">£149</div>
            <p>
            A focused review of your current evidence structure with gap notes,
            action points, and a practical improvement direction.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="price-card">
            <h3>30-Day CQC Evidence Cleanup Sprint</h3>
            <div class="gold-line"></div>
            <div class="price">£750–£1,500</div>
            <p>
            A structured cleanup service for care providers that need stronger
            evidence files, trackers, policies, SOPs, and management review records.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="price-card">
            <h3>Monthly Compliance Retainer</h3>
            <div class="gold-line"></div>
            <div class="price">Scoped</div>
            <p>
            Ongoing compliance organisation, document updates, evidence tracking,
            action tracker support, and management summary preparation.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>Who Nexus supports</h2>
        <ul>
            <li>UK care managers preparing for stronger compliance records</li>
            <li>CQC-regulated providers with scattered evidence folders</li>
            <li>Domiciliary care and home care providers needing clearer governance files</li>
            <li>Small providers that need support before inspection pressure increases</li>
            <li>Small businesses that need better compliance and operations documentation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="green-notice">
        <strong>Recommended client journey:</strong><br>
        Start with the £149 CQC Evidence File Review. If deeper support is needed,
        move into the 30-Day Cleanup Sprint, then monthly compliance support.
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()
    footer()


# ---------------- £149 REVIEW PAGE ----------------
elif page == "£149 CQC Evidence File Review":
    st.markdown("""
    <div class="hero">
        <div class="tag">Entry Review Offer</div>
        <h1>£149 CQC Evidence File Review</h1>
        <p>
        A focused review for UK care managers who need to understand what is missing,
        weak, scattered, or unclear in their compliance evidence structure.
        </p>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()

    st.markdown("""
    <div class="card">
        <h2>What this review is for</h2>
        <p>
        This review is designed for care managers and small providers who need a practical
        starting point before investing in a larger compliance cleanup package.
        </p>
        <p>
        It helps identify whether your records are easy to explain, easy to locate,
        and strong enough to support management review, internal monitoring, and
        inspection preparation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>What is included</h2>
        <ul>
            <li>Review of your current evidence folder structure</li>
            <li>Gap notes identifying missing, weak, or unclear records</li>
            <li>CQC evidence checklist direction</li>
            <li>Basic action tracker</li>
            <li>Notes on policy and SOP organisation</li>
            <li>Short written summary of recommended next steps</li>
            <li>Recommendation on whether a full cleanup sprint is needed</li>
        </ul>
        <div class="price">Price: £149</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>Best for</h2>
        <ul>
            <li>Care managers who feel their evidence is scattered</li>
            <li>Providers unsure whether their records are inspection-ready</li>
            <li>New or small providers needing structure</li>
            <li>Managers who want a low-risk first step before deeper support</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="notice">
        This service supports evidence organisation and compliance readiness.
        It does not replace legal advice or the provider’s own regulatory responsibility.
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()
    footer()


# ---------------- 30 DAY SPRINT PAGE ----------------
elif page == "30-Day Cleanup Sprint":
    st.markdown("""
    <div class="hero">
        <div class="tag">Higher Support Package</div>
        <h1>30-Day CQC Evidence Cleanup Sprint</h1>
        <p>
        A structured cleanup service for care providers that need stronger evidence files,
        clearer trackers, better documentation, and a more organised compliance system.
        </p>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()

    st.markdown("""
    <div class="card">
        <h2>What the sprint solves</h2>
        <p>
        Care providers often have policies, training records, incidents, audits,
        complaints, risk documents, and management notes spread across different
        folders or formats. This creates stress when managers need to explain what
        is happening in the service.
        </p>
        <p>
        The 30-Day CQC Evidence Cleanup Sprint helps bring those records into a clearer
        structure so management can see what exists, what is missing, and what needs action.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
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
            <li>Priority recommendations for improvement</li>
        </ul>
        <div class="price">Price range: £750 – £1,500</div>
        <p>
        Final pricing depends on document volume, urgency, business size, and the current
        condition of the records.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>Expected outcome</h2>
        <p>
        At the end of the sprint, the provider should have a clearer evidence structure,
        a stronger action tracker, better organised policies and SOPs, and a management
        summary showing what has been reviewed and what still needs attention.
        </p>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()
    footer()


# ---------------- MONTHLY RETAINER PAGE ----------------
elif page == "Monthly Retainer":
    st.markdown("""
    <div class="hero">
        <div class="tag">Ongoing Support</div>
        <h1>Monthly Compliance Retainer</h1>
        <p>
        Ongoing compliance organisation for care providers and small businesses that want
        their records, policies, trackers, and management evidence kept under control.
        </p>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()

    st.markdown("""
    <div class="card">
        <h2>Why monthly support matters</h2>
        <p>
        Compliance is not a one-time cleanup. Evidence must be maintained, reviewed,
        updated, and explained over time. A monthly retainer helps prevent documents
        from becoming outdated, scattered, or forgotten.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
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
        <div class="price">Pricing: agreed after scope review</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="green-notice">
        Best for providers that want continuity after the £149 review or 30-Day Cleanup Sprint.
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()
    footer()


# ---------------- SMALL BUSINESS PAGE ----------------
elif page == "Small Business Readiness":
    st.markdown("""
    <div class="hero">
        <div class="tag">Small Business Compliance</div>
        <h1>Small Business Readiness Package</h1>
        <p>
        Compliance and operations support for small businesses that need clearer documents,
        stronger internal controls, better records, and more professional procedures.
        </p>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()

    st.markdown("""
    <div class="card">
        <h2>Who this is for</h2>
        <p>
        This package is for small businesses that are growing but do not yet have strong
        documentation, recordkeeping, policy, or internal control systems.
        </p>
    </div>
    """, unsafe_allow_html=True)

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

    contact_buttons()
    footer()


# ---------------- ABOUT PAGE ----------------
elif page == "About":
    st.markdown("""
    <div class="hero">
        <div class="tag">About the Firm</div>
        <h1>About Nexus Conformité</h1>
        <p>
        Nexus Conformité connects law, risk, compliance, data protection, governance,
        and operational documentation into practical support for regulated and growing businesses.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>Our focus</h2>
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
    <div class="card">
        <h2>What makes the approach different</h2>
        <ul>
            <li>Evidence-first compliance support</li>
            <li>Governance and internal control focus</li>
            <li>Clear action trackers and management summaries</li>
            <li>Practical organisation for real business operations</li>
            <li>Support designed for small and growing providers</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()
    footer()


# ---------------- FAQ PAGE ----------------
elif page == "FAQs":
    st.markdown("""
    <div class="hero">
        <div class="tag">Questions & Answers</div>
        <h1>CQC Compliance Support FAQs</h1>
        <p>
        Clear answers for care managers and small providers considering Nexus Conformité support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Is the £149 CQC Evidence File Review a full compliance audit?"):
        st.write("""
        No. It is a focused evidence structure review. It helps identify obvious gaps,
        weak organisation, and practical next steps. A deeper cleanup or audit-style review
        may require a larger package.
        """)

    with st.expander("Do you replace the provider’s responsibility to comply with CQC requirements?"):
        st.write("""
        No. Nexus Conformité supports organisation, evidence readiness, documentation,
        trackers, and management review preparation. The provider remains responsible
        for meeting regulatory requirements.
        """)

    with st.expander("Is the 30-Day Cleanup Sprint suitable before an inspection?"):
        st.write("""
        It may help organise records and identify gaps before inspection pressure increases.
        The earlier the provider starts, the better the outcome. Urgent work may affect pricing.
        """)

    with st.expander("Can Nexus support domiciliary care providers?"):
        st.write("""
        Yes. The services are suitable for small care providers, domiciliary care providers,
        home care providers, and managers who need clearer evidence structures.
        """)

    with st.expander("How are digital packages delivered?"):
        st.write("""
        Digital products and packages are delivered securely through Payhip where applicable.
        Custom support is scoped first before the final delivery method is confirmed.
        """)

    with st.expander("Can I move from the £149 review to the 30-Day Sprint?"):
        st.write("""
        Yes. The £149 review is designed as the first step. If the evidence file needs deeper
        cleanup, the provider can move into the 30-Day Sprint or monthly retainer support.
        """)

    contact_buttons()
    footer()


# ---------------- CONTACT PAGE ----------------
elif page == "Contact":
    st.markdown("""
    <div class="hero">
        <div class="tag">Contact Nexus</div>
        <h1>Start with the right support level.</h1>
        <p>
        Message Nexus Conformité to request the £149 review, discuss the 30-Day Cleanup Sprint,
        or ask about monthly compliance support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <h2>Contact details</h2>
        <p><strong>Email:</strong> {EMAIL}</p>
        <p><strong>Facebook:</strong> @nexusconformite</p>
        <p><strong>Payhip:</strong> payhip.com/NexusConformite</p>
        <p><strong>LinkedIn:</strong> {LINKEDIN_NAME}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>What to include in your message</h2>
        <ul>
            <li>Your name and business name</li>
            <li>Whether you are a care provider, care manager, or small business owner</li>
            <li>The support you are interested in</li>
            <li>Your main compliance concern</li>
            <li>Whether your documents are already organised or scattered</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    contact_buttons()
    footer()