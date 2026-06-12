import streamlit as st

st.set_page_config(
    page_title="Clearsulting × Snowflake — Future State Architecture",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.html("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
  }

  /* hide default Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  .stApp { background: #F0F4F8; }

  /* ── section label ── */
  .section-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #64748B;
    margin: 0 0 12px 4px;
  }

  /* ── card ── */
  .card {
    background: #FFFFFF;
    border-radius: 12px;
    padding: 20px 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,.08), 0 1px 6px rgba(0,0,0,.04);
  }

  /* ── badge ── */
  .badge-structured {
    display: inline-block;
    background: #EFF6FF;
    color: #1D4ED8;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 4px;
    margin-top: 6px;
  }
  .badge-unstructured {
    display: inline-block;
    background: #FFF7ED;
    color: #C2410C;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 4px;
    margin-top: 6px;
  }

  /* ── divider arrow ── */
  .arrow-down {
    text-align: center;
    font-size: 28px;
    color: #29B5E8;
    margin: 16px 0;
    line-height: 1;
  }

  /* ── pipeline box ── */
  .pipeline-box {
    border-radius: 10px;
    padding: 16px 20px;
  }
  .pipeline-structured {
    background: #F0FDF4;
    border-left: 4px solid #22C55E;
  }
  .pipeline-unstructured {
    background: #FFFBEB;
    border-left: 4px solid #F59E0B;
  }
  .pipeline-title {
    font-weight: 700;
    font-size: 14px;
    color: #1A202C;
    margin-bottom: 8px;
  }
  .pipeline-item {
    font-size: 12px;
    color: #4B5563;
    padding: 2px 0;
  }
  .pipeline-item::before { content: "• "; color: #29B5E8; }

  /* ── openflow badge ── */
  .openflow-badge {
    display: inline-block;
    background: #29B5E8;
    color: white;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    padding: 3px 10px;
    border-radius: 4px;
    margin-right: 10px;
    vertical-align: middle;
  }
  .openflow-title {
    font-size: 15px;
    font-weight: 700;
    color: #1A202C;
    letter-spacing: 0.5px;
    vertical-align: middle;
  }

  /* ── raw zone table ── */
  .raw-table {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
    margin-top: 12px;
  }
  .raw-cell {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 12px;
    text-align: center;
  }
  .raw-cell-name {
    font-size: 12px;
    font-weight: 700;
    color: #1A202C;
    font-family: 'Courier New', monospace;
  }
  .raw-cell-type {
    font-size: 11px;
    color: #94A3B8;
    margin-top: 2px;
  }

  /* ── dynamic table cards ── */
  .dt-card {
    border-radius: 8px;
    padding: 12px 16px;
    background: white;
    border: 1px solid #E2E8F0;
  }
  .dt-staging { border-top: 3px solid #22C55E; }
  .dt-intermediate { border-top: 3px solid #F59E0B; }
  .dt-mart { background: #FAF5FF; border: 1px solid #DDD6FE; text-align: center; }
  .dt-name {
    font-size: 12px;
    font-weight: 700;
    color: #1A202C;
    font-family: 'Courier New', monospace;
  }
  .dt-desc {
    font-size: 11px;
    color: #6B7280;
    margin-top: 3px;
  }

  /* ── cortex cards ── */
  .cortex-card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 18px 20px;
    height: 100%;
  }
  .cortex-title {
    font-size: 14px;
    font-weight: 700;
    color: #1A202C;
    margin-bottom: 10px;
  }
  .cortex-item {
    font-size: 12px;
    color: #4B5563;
    padding: 3px 0;
  }
  .cortex-item::before { content: "› "; color: #29B5E8; font-weight: 700; }

  /* ── governance bar ── */
  .governance-bar {
    background: #0E1A2E;
    border-radius: 10px;
    padding: 16px 24px;
    display: flex;
    gap: 32px;
    flex-wrap: wrap;
    margin-top: 16px;
  }
  .gov-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    color: #CBD5E1;
  }
  .gov-check { color: #29B5E8; font-weight: 700; }

  /* ── consumption card ── */
  .consumption-card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    border: 1px solid #E2E8F0;
    height: 100%;
  }
  .consumption-title {
    font-size: 15px;
    font-weight: 700;
    color: #1A202C;
    margin-bottom: 12px;
  }
  .consumption-item {
    font-size: 12px;
    color: #4B5563;
    padding: 3px 0;
  }
  .consumption-item::before { content: "• "; color: #29B5E8; }
  .consumption-note {
    background: #F8FAFC;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 11px;
    color: #64748B;
    font-style: italic;
    margin-top: 10px;
  }
  .consumption-border-yellow { border-top: 3px solid #F59E0B; }
  .consumption-border-pink   { border-top: 3px solid #EC4899; }
  .consumption-border-purple { border-top: 3px solid #A855F7; }

  /* ── flow diagram ── */
  .flow-container {
    background: white;
    border-radius: 12px;
    padding: 28px 32px;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,.06);
  }
  .flow-title {
    font-size: 16px;
    font-weight: 700;
    color: #1A202C;
    margin-bottom: 20px;
  }
  .flow-steps {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    flex-wrap: wrap;
  }
  .flow-step {
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    white-space: nowrap;
  }
  .flow-step-outline {
    border: 2px solid #CBD5E1;
    color: #374151;
  }
  .flow-step-blue {
    background: #29B5E8;
    color: white;
  }
  .flow-step-light {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    color: #1D4ED8;
  }
  .flow-step-dark {
    background: #0E1A2E;
    color: white;
  }
  .flow-arrow {
    color: #94A3B8;
    font-size: 20px;
    padding: 0 6px;
  }

  /* ── decisions table ── */
  .decisions-table { width: 100%; border-collapse: collapse; }
  .decisions-table th {
    background: #0E1A2E;
    color: white;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 12px 16px;
    text-align: left;
  }
  .decisions-table th:first-child { border-radius: 8px 0 0 0; }
  .decisions-table th:last-child { border-radius: 0 8px 0 0; }
  .decisions-table td {
    padding: 12px 16px;
    font-size: 12px;
    color: #374151;
    border-bottom: 1px solid #F1F5F9;
    vertical-align: top;
  }
  .decisions-table tr:hover td { background: #F8FAFC; }
  .decisions-table td:first-child { font-weight: 600; color: #1A202C; }
  .decisions-table td:nth-child(2) { font-family: 'Courier New', monospace; font-size: 11px; color: #4B5563; }
  .decisions-table tr:last-child td { border-bottom: none; }

  /* ── segments table ── */
  .seg-table { width: 100%; border-collapse: collapse; }
  .seg-table th {
    background: #0E1A2E;
    color: white;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 12px 16px;
    text-align: left;
  }
  .seg-table td {
    padding: 12px 16px;
    font-size: 12px;
    color: #374151;
    border-bottom: 1px solid #F1F5F9;
    vertical-align: top;
  }
  .seg-table tr:hover td { background: #F8FAFC; }
  .seg-table td:first-child { font-weight: 700; color: #1A202C; }
  .seg-table td:nth-child(3) { font-family: 'Courier New', monospace; font-size: 11px; color: #29B5E8; }
  .seg-table tr:last-child td { border-bottom: none; }

  /* ── source system card ── */
  .source-card {
    background: #EBF3FF;
    border: 1px solid #BFDBFE;
    border-radius: 10px;
    padding: 20px 16px;
    text-align: center;
  }
  .source-icon { font-size: 32px; margin-bottom: 8px; }
  .source-name { font-size: 14px; font-weight: 700; color: #1A202C; }
  .source-type { font-size: 12px; color: #64748B; margin-top: 2px; }

  /* ── snowflake platform wrapper ── */
  .snowflake-platform {
    border: 2px solid #29B5E8;
    border-radius: 16px;
    padding: 24px;
    position: relative;
    margin-top: 8px;
  }
  .snowflake-platform-label {
    position: absolute;
    top: -14px;
    left: 20px;
    background: #29B5E8;
    color: white;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    padding: 3px 12px;
    border-radius: 4px;
  }
  .platform-section-dot-green  { color: #22C55E; }
  .platform-section-dot-orange { color: #F59E0B; }
  .platform-section-dot-red    { color: #EF4444; }
  .platform-section-title {
    font-size: 14px;
    font-weight: 700;
    color: #1A202C;
    display: inline;
  }
</style>
""")

# ── PAGE HEADER ────────────────────────────────────────────────────────────────
st.html("""
<div style="
  background: linear-gradient(135deg, #0E1A2E 0%, #1A3050 100%);
  padding: 52px 64px 44px;
  margin-bottom: 0;
">
  <div style="font-size:13px; font-weight:600; letter-spacing:2px; text-transform:uppercase; color:#29B5E8; margin-bottom:14px;">
    SNOWFLAKE DATA &amp; AI PLATFORM
  </div>
  <h1 style="margin:0; font-size:40px; font-weight:800; color:#FFFFFF; line-height:1.15;">
    Clearsulting — Future State Architecture
  </h1>
  <div style="margin-top:18px; display:flex; gap:32px; align-items:center; flex-wrap:wrap;">
    <span style="font-size:14px; color:#94A3B8;">Prepared by Snowflake</span>
    <span style="color:#475569;">|</span>
    <span style="font-size:14px; color:#94A3B8;">June 2026</span>
    <span style="color:#475569;">|</span>
    <span style="font-size:14px; color:#94A3B8;">Confidential</span>
  </div>
</div>
""")

# ── MAIN CONTENT ───────────────────────────────────────────────────────────────
with st.container():
    st.html('<div style="padding: 32px 64px 48px;">')

    # ── 1. SOURCE SYSTEMS ──────────────────────────────────────────────────────
    st.html('<div class="section-label">Source Systems</div>')
    st.html("""
    <div class="card">
      <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:14px;">
        <div class="source-card">
          <div class="source-icon">☁️</div>
          <div class="source-name">Salesforce</div>
          <div class="source-type">CRM</div>
          <div class="badge-structured">Structured</div>
        </div>
        <div class="source-card">
          <div class="source-icon">💰</div>
          <div class="source-name">Certinia</div>
          <div class="source-type">ERP / Accounting</div>
          <div class="badge-structured">Structured</div>
        </div>
        <div class="source-card">
          <div class="source-icon">👥</div>
          <div class="source-name">Rippling</div>
          <div class="source-type">HR</div>
          <div class="badge-structured">Structured</div>
        </div>
        <div class="source-card" style="background:#FFF7ED; border-color:#FED7AA;">
          <div class="source-icon">📁</div>
          <div class="source-name">SharePoint</div>
          <div class="source-type">Document Management</div>
          <div class="badge-unstructured">Unstructured</div>
        </div>
        <div class="source-card">
          <div class="source-icon">🔍</div>
          <div class="source-name">ZoomInfo</div>
          <div class="source-type">Enrichment</div>
          <div class="badge-structured">Structured</div>
        </div>
      </div>
    </div>
    """)

    # ── Arrow ─────────────────────────────────────────────────────────────────
    st.html('<div class="arrow-down">↓</div>')

    # ── 2. INGESTION LAYER ─────────────────────────────────────────────────────
    st.html('<div class="section-label">Ingestion Layer</div>')
    st.html("""
    <div class="card">
      <div style="margin-bottom:18px;">
        <span class="openflow-badge">OPENFLOW</span>
        <span class="openflow-title">NATIVE SNOWFLAKE DATA INTEGRATION</span>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
        <div class="pipeline-box pipeline-structured">
          <div class="pipeline-title">Structured Data Pipeline</div>
          <div class="pipeline-item">CDC from Salesforce, Certinia, Rippling, ZoomInfo</div>
          <div class="pipeline-item">Real-time / near-real-time streaming</div>
          <div class="pipeline-item">Schema evolution support</div>
          <div class="pipeline-item">Automated connector management</div>
        </div>
        <div class="pipeline-box pipeline-unstructured">
          <div class="pipeline-title">Unstructured Data Pipeline</div>
          <div class="pipeline-item">SharePoint document ingestion</div>
          <div class="pipeline-item">PDFs, Word docs, PowerPoints</div>
          <div class="pipeline-item">Proposals, SOWs, thought leadership</div>
          <div class="pipeline-item">Automated file detection &amp; loading</div>
          <div class="pipeline-item">Landing to internal Snowflake stage</div>
        </div>
      </div>
    </div>
    """)

    # ── Arrow ─────────────────────────────────────────────────────────────────
    st.html('<div class="arrow-down">↓</div>')

    # ── 3. CORE PLATFORM ──────────────────────────────────────────────────────
    st.html('<div class="section-label">Core Platform</div>')
    st.html("""
    <div class="snowflake-platform">
      <div class="snowflake-platform-label">SNOWFLAKE DATA PLATFORM</div>

      <!-- Raw Zone -->
      <div style="margin-bottom:24px;">
        <span class="platform-section-dot-green">●</span>&nbsp;
        <span class="platform-section-title">Raw / Landing Zone</span>
        <div class="raw-table" style="margin-top:12px;">
          <div class="raw-cell"><div class="raw-cell-name">RAW_SALESFORCE</div><div class="raw-cell-type">tables</div></div>
          <div class="raw-cell"><div class="raw-cell-name">RAW_CERTINIA</div><div class="raw-cell-type">tables</div></div>
          <div class="raw-cell"><div class="raw-cell-name">RAW_RIPPLING</div><div class="raw-cell-type">tables</div></div>
          <div class="raw-cell"><div class="raw-cell-name">RAW_DOCUMENTS</div><div class="raw-cell-type">internal stage</div></div>
          <div class="raw-cell"><div class="raw-cell-name">RAW_ZOOMINFO</div><div class="raw-cell-type">tables</div></div>
        </div>
      </div>

      <!-- Transformation Layer -->
      <div style="margin-bottom:24px;">
        <span class="platform-section-dot-orange">●</span>&nbsp;
        <span class="platform-section-title">Transformation Layer — Dynamic Tables</span>
        <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-top:12px;">
          <div class="dt-card dt-staging">
            <div class="dt-name">DT: STG_ACCOUNTS</div>
            <div class="dt-desc">Cleansed CRM data</div>
          </div>
          <div class="dt-card dt-staging">
            <div class="dt-name">DT: STG_CONTACTS</div>
            <div class="dt-desc">Unified people data</div>
          </div>
          <div class="dt-card dt-staging">
            <div class="dt-name">DT: STG_FINANCIAL_CLOSE</div>
            <div class="dt-desc">AR / GL / Journal Entries</div>
          </div>
          <div class="dt-card dt-intermediate">
            <div class="dt-name">DT: INT_PIPELINE</div>
            <div class="dt-desc">Sales pipeline metrics</div>
          </div>
          <div class="dt-card dt-intermediate">
            <div class="dt-name">DT: INT_ENGAGEMENT</div>
            <div class="dt-desc">Account activity &amp; personas</div>
          </div>
          <div class="dt-card dt-intermediate">
            <div class="dt-name">DT: INT_BAD_DEBT_ANALYSIS</div>
            <div class="dt-desc">Aging buckets, risk score, policy compliance</div>
          </div>
        </div>
        <!-- MART layer -->
        <div style="border:1px solid #DDD6FE; border-radius:10px; padding:16px; margin-top:10px; background:#FAF5FF;">
          <div style="font-size:13px; font-weight:700; color:#6D28D9; margin-bottom:10px;">
            DT: MART_* — Consumption-Ready Models
          </div>
          <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:8px;">
            <div class="dt-card dt-mart"><div class="dt-name">MART_FUNNEL_ANALYTICS</div></div>
            <div class="dt-card dt-mart"><div class="dt-name">MART_CFO_INSIGHTS</div></div>
            <div class="dt-card dt-mart"><div class="dt-name">MART_RESOURCE_UTILIZATION</div></div>
            <div class="dt-card dt-mart"><div class="dt-name">MART_CLIENT_360</div></div>
            <div class="dt-card dt-mart"><div class="dt-name">MART_PRACTICE_PERF</div></div>
            <div class="dt-card dt-mart"><div class="dt-name">MART_REVENUE_RECOGNITION</div></div>
          </div>
        </div>
        <div style="text-align:center; font-size:11px; color:#94A3B8; font-style:italic; margin-top:8px;">
          Target Lag: minutes (staging) → hours (intermediate) → scheduled (marts)
        </div>
      </div>

      <!-- AI/ML Layer -->
      <div style="margin-bottom:20px;">
        <span class="platform-section-dot-red">●</span>&nbsp;
        <span class="platform-section-title">AI / ML Layer — Snowflake Cortex</span>
        <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:12px;">
          <div class="cortex-card">
            <div class="cortex-title">Cortex Search Service</div>
            <div class="cortex-item">Document RAG</div>
            <div class="cortex-item">SharePoint docs vectorized</div>
            <div class="cortex-item">Knowledge base search</div>
            <div class="cortex-item">Thought leadership retrieval</div>
          </div>
          <div class="cortex-card">
            <div class="cortex-title">Cortex Analyst</div>
            <div class="cortex-item">Natural language queries over financial data</div>
            <div class="cortex-item">Self-service analytics</div>
            <div class="cortex-item">Ad-hoc business insights</div>
          </div>
          <div class="cortex-card">
            <div class="cortex-title">Cortex Agents</div>
            <div class="cortex-item">Funnel Filler Agent</div>
            <div class="cortex-item">Bad Debt Provision Agent</div>
            <div class="cortex-item">Autonomous outreach</div>
            <div class="cortex-item">Journal entry review</div>
            <div class="cortex-item">MCP server integration</div>
          </div>
        </div>
      </div>

      <!-- Governance -->
      <div class="governance-bar">
        <div style="font-size:11px; font-weight:800; letter-spacing:1.5px; color:#CBD5E1; width:100%; margin-bottom:4px; text-transform:uppercase;">Governance &amp; Security</div>
        <div class="gov-item"><span class="gov-check">✓</span> Role-Based Access Control (RBAC) — unified across all services</div>
        <div class="gov-item"><span class="gov-check">✓</span> Data Sharing — governed, zero-copy with partners (SAP, BlackLine, Coupa)</div>
        <div class="gov-item"><span class="gov-check">✓</span> Dynamic Data Masking — PII protection for HR/Finance</div>
        <div class="gov-item"><span class="gov-check">✓</span> Audit &amp; Compliance — SOX-ready controls for financial close</div>
      </div>
    </div>
    """)

    # ── Arrow ─────────────────────────────────────────────────────────────────
    st.html('<div class="arrow-down">↓</div>')

    # ── 4. CONSUMPTION LAYER ──────────────────────────────────────────────────
    st.html('<div class="section-label">Consumption Layer</div>')
    st.html("""
    <div class="card">
      <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px;">
        <div class="consumption-card consumption-border-yellow">
          <div class="consumption-title">Power BI</div>
          <div class="consumption-item">Executive dashboards</div>
          <div class="consumption-item">Practice performance</div>
          <div class="consumption-item">Revenue &amp; pipeline</div>
          <div class="consumption-item">Financial close KPIs</div>
          <div class="consumption-item">Self-service reporting</div>
          <div class="consumption-note">Direct Snowflake connector — live queries against MART tables</div>
        </div>
        <div class="consumption-card consumption-border-pink">
          <div class="consumption-title">Streamlit Apps (in Snowflake)</div>
          <div class="consumption-item">Funnel Filler UI</div>
          <div class="consumption-item">Bad Debt Analysis</div>
          <div class="consumption-item">CFO Insights App</div>
          <div class="consumption-item">Document Search</div>
          <div class="consumption-item">Resource Planning</div>
          <div class="consumption-item">Client 360 View</div>
          <div class="consumption-note">Governed by same RBAC — no data leaves security perimeter</div>
        </div>
        <div class="consumption-card consumption-border-purple">
          <div class="consumption-title">Additional Channels</div>
          <div class="consumption-item">Cortex Agents (autonomous)</div>
          <div class="consumption-item">Snowflake Intelligence</div>
          <div class="consumption-item">Data Sharing to Partners (BlackLine, SAP, Coupa)</div>
          <div class="consumption-item">Email / Gmail integration</div>
          <div class="consumption-item">Salesforce write-back</div>
        </div>
      </div>
    </div>
    """)

    # ── 5. END-TO-END FLOW ────────────────────────────────────────────────────
    st.html('<div style="height:24px;"></div>')
    st.html("""
    <div class="flow-container">
      <div class="flow-title">End-to-End Data Flow</div>
      <div class="flow-steps">
        <div class="flow-step flow-step-outline">Source Systems</div>
        <div class="flow-arrow">→</div>
        <div class="flow-step flow-step-blue">Openflow (CDC + Unstructured)</div>
        <div class="flow-arrow">→</div>
        <div class="flow-step flow-step-light">Raw Zone</div>
        <div class="flow-arrow">→</div>
        <div class="flow-step flow-step-dark">Dynamic Tables (STG → INT → MART)</div>
        <div class="flow-arrow">→</div>
        <div class="flow-step flow-step-light">Power BI / Streamlit / Cortex Agents</div>
      </div>
    </div>
    """)

    # ── 6. ARCHITECTURE DECISIONS ─────────────────────────────────────────────
    st.html('<div style="height:36px;"></div>')
    st.html("""
    <div style="font-size:20px; font-weight:800; color:#0E1A2E; margin-bottom:16px;">
      Architecture Decisions
    </div>
    <div class="card" style="padding:0; overflow:hidden;">
      <table class="decisions-table">
        <thead>
          <tr>
            <th style="width:140px;">Component</th>
            <th style="width:200px;">Choice</th>
            <th>Rationale</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Ingestion</td>
            <td>Openflow</td>
            <td>Native Snowflake connector; handles both structured CDC and unstructured document pipelines from SharePoint. Eliminates need for separate Fivetran license.</td>
          </tr>
          <tr>
            <td>Transformation</td>
            <td>Dynamic Tables</td>
            <td>Declarative SQL-based transformations with automatic dependency management. No dbt licensing cost. Target lag provides near-real-time freshness for operational use cases.</td>
          </tr>
          <tr>
            <td>Unstructured Data</td>
            <td>Openflow → Stage → Cortex Search</td>
            <td>Automated ingestion of SharePoint docs; Cortex handles vectorization and RAG without external vector DB.</td>
          </tr>
          <tr>
            <td>AI / ML</td>
            <td>Cortex (Search, Analyst, Agents)</td>
            <td>Native LLM access (Claude, etc.) within Snowflake security perimeter. Supports Funnel Filler and bad debt provision use cases.</td>
          </tr>
          <tr>
            <td>BI Reporting</td>
            <td>Power BI</td>
            <td>Familiar to finance teams; direct Snowflake connector for live queries against MART tables.</td>
          </tr>
          <tr>
            <td>Operational Apps</td>
            <td>Streamlit in Snowflake</td>
            <td>Secure, governed apps for interactive workflows (agent UIs, write-back, approvals). Same RBAC as underlying data.</td>
          </tr>
          <tr>
            <td>Governance</td>
            <td>Snowflake RBAC + Data Sharing</td>
            <td>Unified permissions across all consumption channels. Zero-copy sharing with alliance partners.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """)

    # ── 7. BUSINESS SEGMENTS MAPPED ───────────────────────────────────────────
    st.html('<div style="height:36px;"></div>')
    st.html("""
    <div style="font-size:20px; font-weight:800; color:#0E1A2E; margin-bottom:16px;">
      Business Segments Mapped
    </div>
    <div class="card" style="padding:0; overflow:hidden;">
      <table class="seg-table">
        <thead>
          <tr>
            <th style="width:160px;">Segment</th>
            <th style="width:220px;">Source</th>
            <th>Key Dynamic Tables</th>
            <th>Consumption</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Commercial</td>
            <td>Salesforce, ZoomInfo</td>
            <td>MART_FUNNEL_ANALYTICS, MART_CLIENT_360</td>
            <td>Streamlit (Funnel Filler Agent), Power BI</td>
          </tr>
          <tr>
            <td>GTM</td>
            <td>Salesforce, SharePoint</td>
            <td>MART_PIPELINE, INT_ENGAGEMENT</td>
            <td>Streamlit, Cortex Agents</td>
          </tr>
          <tr>
            <td>Delivery</td>
            <td>Certinia, SharePoint</td>
            <td>MART_RESOURCE_UTILIZATION</td>
            <td>Power BI, Streamlit</td>
          </tr>
          <tr>
            <td>Practice Mgmt</td>
            <td>SharePoint (documents)</td>
            <td>Cortex Search Service</td>
            <td>Streamlit (Doc Search), Agents</td>
          </tr>
          <tr>
            <td>Operations / Finance</td>
            <td>Certinia, Rippling</td>
            <td>MART_CFO_INSIGHTS, MART_REVENUE_RECOGNITION</td>
            <td>Power BI, Streamlit (Bad Debt Agent)</td>
          </tr>
        </tbody>
      </table>
    </div>
    """)

    # ── FOOTER ─────────────────────────────────────────────────────────────────
    st.html("""
    <div style="
      text-align:center;
      margin-top:52px;
      padding-top:24px;
      border-top:1px solid #E2E8F0;
      font-size:12px;
      color:#94A3B8;
      padding-bottom: 24px;
    ">
      Clearsulting × Snowflake — Future State Architecture — Confidential
    </div>
    """)

    st.html('</div>')  # close main padding div
