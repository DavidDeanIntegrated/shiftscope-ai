"""Seed data for ShiftScope AI. Every fact below was taken from the linked sources on 2026-10-18.
Anything not found in a source is recorded as 'Unknown' / 'Not publicly stated'. Physician review fields are intentionally empty."""
import json
V = "2026-10-18"
U = "Unknown"
NP = "Not publicly stated"
NA = "Not applicable (not a regulated medical device function as described by vendor)"
tools = []
def T(slug, name, company, url, category, tagline, features, ehr, pricing, hipaa, fda, sources, studies=None, ed_vendor=None, notes=None):
    tools.append({
        "slug": slug, "name": name, "company": company, "url": url, "category": category,
        "tagline": tagline, "features": features, "ehr_integrations": ehr,
        "pricing": pricing, "hipaa_baa": hipaa, "fda_status": fda,
        "ed_specific_vendor_claims": ed_vendor or [],
        "studies": studies or [], "sources": sources, "notes": notes or "",
        "last_verified": V,
        "ed_criteria": {k: "Not yet evaluated" for k in ["interruptions","multi_patient","noisy_environment","trauma_resus","ehr_fit","privacy_baa","pricing_value","evidence"]},
        "physician_review": None, "ratings": None, "sponsored": False, "affiliate_link": None,
    })

# ---------------- AI scribes & documentation ----------------
T("abridge","Abridge Inside for Emergency Medicine","Abridge","https://www.abridge.com","ambient-documentation",
  "Enterprise ambient AI documentation with an ED-specific Epic workflow launched from the Track Board.",
  ["Ambient recording started from Epic Haiku; note text flows into Hyperspace","Populates ED Provider Note sections such as HPI, Physical Exam and MDM (per a hospital tip sheet)","Speech models detect specialty, language and multiple speakers (per vendor)","Linked clinical evidence including UpToDate inside the Abridge activity (per hospital tip sheet)"],
  ["Epic (ASAP module in Haiku and Hyperspace; SmartLinks)"],
  "Enterprise / health-system contracts; "+NP, U, "None found (documentation tool)",
  ["https://www.abridge.com/blog/inside-for-emergency-medicine-announcement","https://www.fiercehealthcare.com/ai-and-machine-learning/abridge-offers-generative-ai-tool-emergency-medicine-emory-healthcare-johns","https://nwhed.org/wp-content/uploads/ASAP_QSG_Abridge-Inside-for-Emergency-Department.pdf","https://support.abridge.com/hc/en-us/articles/30235172323731-Send-an-Abridge-Note-Into-Epic"],
  ed_vendor=["Built with Epic's Workshop program for the ED (Jan 2025)","Clinicians select patients from the department Track Board and start recording in Haiku","Named early ED users: Deaconess, Emory, Johns Hopkins, Mayo Clinic, UChicago Medicine (vendor announcement)"])

T("dragon-copilot","Microsoft Dragon Copilot (formerly DAX Copilot)","Microsoft (Nuance)","https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/","ambient-documentation",
  "Microsoft's ambient + dictation clinical assistant with an Emergency Department specialty output.",
  ["Selecting 'Emergency Medicine' as primary specialty maps to an Emergency Department note output","ED guidance: speak MDM aloud as a narrative; timestamps and critical care minutes must be spoken to be captured","ED model updates for reduced repetition, billing-relevant elements and timestamp capture (release notes)"],
  ["Epic (DAX Copilot for Epic / Dragon Copilot embedded)","Other EHRs: "+U],
  NP, U, "None found (documentation tool)",
  ["https://support.microsoft.com/en-us/dragon-copilot/physicians/ai-specialty-mapping","https://support.microsoft.com/en-us/dragon-copilot/physicians/current/emergency-department-recording-best-practices","https://learn.microsoft.com/en-us/industry/healthcare/dragon-copilot/whats-new/3-5-1"],
  ed_vendor=["Dedicated Emergency Department specialty output","Published ED recording best practices from Microsoft"])

T("freed","Freed","Freed","https://www.getfreed.ai","ambient-documentation",
  "Self-serve AI scribe for individual clinicians with a Chrome extension that pushes notes into browser-based EHRs.",
  ["Specialty-specific templates; unlimited notes on Core and above","Premier adds visit summaries, patient instructions/letters, EHR push and ICD-10/CPT coding","EHR Push via Chrome extension (Starter/Core limited to 5 lifetime transfers)"],
  ["Browser-based EHR push (verified list includes athenahealth, eClinicalWorks, Practice Fusion, Elation, NextGen Office, AdvancedMD browser instances)","Epic / Cerner / Meditech: not on Freed's verified push list"],
  "Starter $39/mo (40 notes/mo); Core $79/mo; Premier $119/mo monthly or $104/mo billed annually; Groups custom. Pricing page advertises a resident/student/trainee offer.",
  "BAA included in Platform Terms (Schedule A) for all users; org-wide BAA for Groups (per third-party BAA tracker citing Freed's terms)",
  "None found (documentation tool)",
  ["https://www.getfreed.ai/pricing","https://help.getfreed.ai/en/articles/11328264-ehr-push","https://aivendorbaacheck.com/tools/freed"],
  notes="Freed's EHR push targets browser-based (mostly ambulatory) EHRs; most US EDs run Epic, Oracle Health (Cerner) or Meditech, so ED fit needs physician testing.")

T("heidi","Heidi","Heidi Health","https://www.heidihealth.com","ambient-documentation",
  "AI scribe with a free-forever tier, cited Evidence answers, and Epic/Oracle Health integrations on team plans.",
  ["Free: unlimited transcription and standard-template notes, Evidence queries with citations, 10 advanced actions/month","Clinician: unlimited advanced templates, documents and Ask Heidi","Practice/Enterprise: full EHR integration access and team features"],
  ["Epic, Oracle Health (Cerner, incl. FirstNet MPage components per third-party listing), athenahealth, eClinicalWorks and others; full integration requires Practice/Enterprise"],
  "Free $0; Clinician about $150/mo monthly or about $110/mo billed annually (US, per third-party price check, Sept 2026); Practice/Enterprise custom",
  "Vendor states HIPAA compliance (per third-party summary of vendor security claims); BAA terms: "+U,
  "None found (documentation tool)",
  ["https://support.heidihealth.com/en/articles/8885030-heidi-s-pricing-plans-cost-and-features","https://www.heidihealth.com/en-us/pricing","https://clinicframe.com/blog/heidi-health-pricing","https://agenticindex.io/vendors/heidi","https://www.heidihealth.com/legal/referral-program-terms-and-conditions"],
  notes="Heidi runs a public referral program (USD $25 to $50 per paid referral, capped at 10 per month). Any ShiftScope referral link must be disclosed.")

T("suki","Suki Assistant","Suki","https://www.suki.ai","ambient-documentation",
  "Ambient documentation and voice assistant with bidirectional integrations into Epic, Oracle Health and MEDITECH Expanse.",
  ["Ambient note generation and dictation","Reads chart data and writes generated note content back to the EHR","Suki Inside listed for Epic Haiku emergency notes (per third-party integration review)"],
  ["Epic","Oracle Health (Cerner)","MEDITECH Expanse","athenahealth"],
  NP, U, "None found (documentation tool)",
  ["https://www.suki.ai/ehr-integrations/","https://ehr.meditech.com/vendors/suki","https://www.healthcareitnews.com/news/vendor-notebook-epic-and-microsoft-showcase-copiloted-ai-capabilities-cerner-adds-suki-ai","https://clunic.com/integrations/suki-epic"])

T("nabla","Nabla","Nabla","https://www.nabla.com","ambient-documentation",
  "Ambient clinical AI for notes, dictation and coding suggestions, with an EHR connector and API.",
  ["Ambient documentation and dictation","Coding suggestions","Nabla Connect plug-and-play integration; Core API for deeper integration"],
  ["Epic","Oracle Health","athenahealth","NextGen","Greenway Health","Others via API"],
  "30-day free trial for individuals; paid pricing "+NP, U, "None found (documentation tool)",
  ["https://www.nabla.com/ehr","https://help.nabla.com/en/categories/137474","https://docs.nabla.com/guides/ehr-integration"])

T("ambience","Ambience","Ambience Healthcare","https://www.ambiencehealthcare.com","ambient-documentation",
  "Ambient documentation with CDI and point-of-care coding across emergency, inpatient and outpatient settings.",
  ["Ambient documentation","Coding-aware notes with ICD-10/CPT suggestions for clinician review","Clinical documentation integrity (CDI) support"],
  ["Epic (including Haiku via Epic Toolbox)"],
  NP, U, "None found (documentation tool)",
  ["https://www.ambiencehealthcare.com/","https://www.ambiencehealthcare.com/blog/ambience-healthcare-joins-epic-toolbox-unlocking-advanced-ai-functionality-within-haiku-for-epic-customers","https://www.ambiencehealthcare.com/blog/ambience-healthcare-s-ai-platform-surpasses-clinician-performance-by-27-in-medical-coding-powered-by-new-openai-breakthrough"],
  ed_vendor=["Vendor lists emergency settings among supported care settings"],
  notes="Cleveland Clinic's announced 2025 rollout was for ambulatory providers, not the ED.")

T("commure-ambient","Commure Ambient","Commure (incl. former Augmedix)","https://www.commure.com","ambient-documentation",
  "Ambient AI with deep MEDITECH Expanse integration and an HCA Healthcare partnership covering ED care.",
  ["Embedded in MEDITECH Expanse Now (mobile)","Structured note writeback via Expanse Observation API (Expanse 2.1.70+ or 2.2.58+)","Later Expanse versions add patient instructions, orders and coding support"],
  ["MEDITECH Expanse","Other EHRs: "+U],
  NP, U, "None found (documentation tool)",
  ["https://www.commure.com/ambient-ai/meditech","https://docs.ambient.commure.com/ehr-integrations/meditech-expanse-integration","https://www.commure.com/press-releases/hca-and-commure-announce-largest-ai-deployment-in-healthcare"],
  ed_vendor=["HCA partnership targets ED, hospitalist and ambulatory care"])

T("deepscribe","DeepScribe","DeepScribe","https://www.deepscribe.ai","ambient-documentation",
  "Ambient documentation with bidirectional Epic integration and coding suggestions.",
  ["Ambient note generation with customizable templates","Chart-context pull-forward and structured note write-back in Epic","Coding suggestions"],
  ["Epic (incl. Haiku and Canto)"],
  "Quote-only; "+NP+" (third-party estimates not used here)", U, "None found (documentation tool)",
  ["https://www.deepscribe.ai/ehr-integrations/epic","https://clunic.com/integrations/deepscribe-epic","https://litmustools.com/review/deepscribe/"])

T("doximity-scribe","Doximity Scribe","Doximity","https://www.doximity.com/clinicians/scribe","ambient-documentation",
  "Free AI scribe inside the Doximity app for verified US physicians, NPs, PAs and medical students.",
  ["Note templates (SOAP, H&P, consults, procedure summaries, dictation) plus custom templates","Works with Doximity Dialer visits and Doximity Ask","Copy/send note to the chart (no named EHR integration)"],
  ["No named EHR integration; copy into chart"],
  "Free for verified US physicians, NPs, PAs and medical students",
  "Vendor states HIPAA compliant",
  "None found (documentation tool)",
  ["https://www.doximity.com/clinicians/scribe","https://support.doximity.com/hc/en-us/articles/55409797170451-How-To-Use-Doximity-Scribe"])

T("eluve","Eluve","Eluve","https://www.eluve.com","ambient-documentation",
  "AI documentation marketed specifically for the ED: notes, MDM, critical care time, procedure notes and discharge instructions.",
  ["Ambient ED note generation (CC, HPI, ROS, exam, MDM, disposition)","Suggested ED E/M (99281-99285) and critical care (99291-99292) codes","Procedure note templates (laceration, I&D, LP, central line, etc.)","Discharge instructions with return precautions; consult request drafts"],
  ["Vendor says it integrates with 'major hospital and urgent care EHR platforms'; specific EHRs not named on the ED page"],
  NP, "Vendor states HIPAA compliant, SOC 2 Type II, and a BAA for every practice", "None found (documentation tool)",
  ["https://www.eluve.com/specialities/emergency-medicine"],
  ed_vendor=["ED-specific page claims support for trauma, STEMI, stroke and sepsis workflows and 20+ simultaneous patients","Vendor-reported metrics (75% less charting, 99% accuracy) are unverified marketing claims"])

T("sayvant","Sayvant","Sayvant","https://www.sayvant.com","ambient-documentation",
  "Acute-care documentation quality platform for ED and hospital medicine: ambient notes plus guideline and coding checks.",
  ["Builds notes from ambient listening, dictation and EMR data","Surfaces differentials and workups for high-risk chief complaints","Flags documentation gaps against guidelines (CMS, ACEP, BMJ) and suggests E/M and critical care capture","Sayvant Quality System note scoring"],
  [U+" (an integrations list is shown on the site but not readable in our fetch)"],
  NP+" (offers a free chart analysis)", U, "None found (documentation tool)",
  ["https://www.sayvant.com/"],
  ed_vendor=["Built for emergency and hospital medicine; co-founded by an emergency physician (per site)","Vendor-reported outcomes from a 50-ED analysis (1+ hour saved per shift) are not independently verified"])

# ---------------- Clinical Q&A ----------------
T("openevidence","OpenEvidence","OpenEvidence","https://www.openevidence.com","clinical-qa",
  "Free, citation-backed medical AI search for verified US clinicians, with content deals with NEJM, JAMA and others.",
  ["Models: Osler (fast), Sackett (more thorough), Snow (multi-minute structured report; replaced DeepConsult)","Content agreements with NEJM, JAMA Network, NCCN, Cochrane and more","Society partnerships listed include ACEP"],
  ["No EHR integration stated"],
  "Free for verified US healthcare professionals",
  "HIPAA compliant since April 2025; PHI handled under OpenEvidence's BAA for US covered entities; SOC 2 Type 2 listed on Trust Center",
  "None found",
  ["https://www.openevidence.com/","https://www.openevidence.com/user-guide/models","https://www.openevidence.com/announcements/openevidence-is-now-hipaa-compliant","https://trust.openevidence.com/"],
  studies=[{"title":"2026 review in npj Digital Medicine noting the limited published evidence on OpenEvidence","url":"https://doi.org/10.1038/s41746-026-03077-4"}])

T("glass-health","Glass Health","Glass Health","https://glass.health","clinical-qa",
  "Clinical decision support (differentials, assessment & plan drafts, cited Q&A) combined with an ambient scribe.",
  ["Differential diagnosis and A&P drafting","Cited clinical Q&A","Ambient scribing"],
  ["EHR-connected workflows on Max plan: Epic, eClinicalWorks, athenahealth, Elation"],
  "Lite $0 (limited, ad-sponsored); Starter $20/mo; Pro $90/mo; Max $200/mo (about 10% less billed annually)",
  U, "None found",
  ["https://glass.health/pricing","https://glass.health/integrations","https://prescriber.io/glass-health-pricing"],
  notes="Free tier is ad-sponsored. Paid tier prices are confirmed by a third-party summary; only the Lite tier was readable directly on our fetch of glass.health/pricing.")

T("doximity-ask","Doximity Ask (formerly DoxGPT)","Doximity","https://www.doximity.com/gpt/","clinical-qa",
  "Free clinical AI assistant for verified US clinicians, built into the Doximity app.",
  ["Clinical questions answered in the Doximity app (vendor calls it a 'workflow assistant')","Connected with Doximity Scribe and Dialer"],
  ["No EHR integration stated"],
  "Free for verified US physicians, NPs, PAs and medical students",
  "Vendor states HIPAA compliant",
  "None found",
  ["https://www.doximity.com/gpt/","https://support.doximity.com/hc/en-us/articles/55381817186195-Doximity-Ask-FAQs","https://blog.doximity.com/articles/Doximity-GPT-Faster-and-Peer-Reviewed"])

T("uptodate-expert-ai","UpToDate Expert AI","Wolters Kluwer","https://www.wolterskluwer.com/en/solutions/uptodate/uptodate-expert-ai","clinical-qa",
  "Generative AI answers grounded only in UpToDate's expert-authored content, with transparent reasoning.",
  ["Conversational, cited answers grounded in UpToDate content","AI drug-dosing guidance added in 2026 (per news coverage)"],
  ["Institutional deployments; specific EHR integration for Expert AI: "+U],
  "Via institutional and individual UpToDate subscriptions; "+NP, U, "None found",
  ["https://www.wolterskluwer.com/en/news/uptodate-expert-ai-genai-clinical-decision-support","https://www.wolterskluwer.com/en/solutions/uptodate/uptodate-expert-ai","https://www.fiercehealthcare.com/ai-and-machine-learning/wolters-kluwer-rolls-out-gen-ai-version-uptodate-clinical-decision-support"],
  notes="Launched September 2025; reported at about 2,500 US hospitals and health systems by August 2026.")

T("clinicalkey-ai","ClinicalKey AI","Elsevier","https://subscriptions.elsevier.com/clinicalkey-ai.html","clinical-qa",
  "Elsevier's generative AI clinical answers grounded in its curated content, with linked citations.",
  ["Natural-language clinical Q&A","Answers grounded in Elsevier evidence-based content with citations","Patient-context inputs"],
  ["Institutional integration: "+U],
  "Individual about $39/mo or $349/yr; residents about $19/mo or $199/yr (per third-party summary); free trial advertised (14 to 90 days depending on store page); institutional "+NP,
  U, "None found",
  ["https://subscriptions.elsevier.com/clinicalkey-ai.html","https://www.elsevier.support/clinicalkeyai/answer/how-can-i-start-a-clinicalkey-ai-trial","https://prescriber.io/blog/clinicalkey-subscription-cost"])

# ---------------- ECG & cardiac ----------------
T("pmcardio-queen-of-hearts","PMcardio Queen of Hearts","Powerful Medical","https://www.powerfulmedical.com/pmcardio-stemi/","ecg-cardiac",
  "AI ECG model for acute coronary syndrome, including STEMI equivalents/OMI, from a photo or digital 12-lead.",
  ["Interprets any 12-lead ECG from a photo or digital file in seconds","Detects ECG findings suggestive of urgent ACS incl. STEMI equivalents, and notifies clinicians","PMcardio platform: pre-hospital, ED and cardiology handoff"],
  ["Enterprise integration via PMcardio platform; specific EHRs: "+U],
  NP+" (US health systems contact sales)", U,
  "FDA De Novo authorization (DEN250044), announced September 15, 2026; FDA Breakthrough Device Designation March 2025",
  ["https://www.powerfulmedical.com/blog/powerful-medical-receives-fda-de-novo-authorization-for-pmcardio-queen-of-hearts-its-ai-ecg-model-for-detecting-acute-heart-attacks/","https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm?id=DEN250044","https://www.tctmd.com/news/fda-clears-first-ai-ecg-model-acute-mi-detection"],
  notes="Vendor cites 20+ peer-reviewed studies incl. RCTs; individual citations to be added after physician review.")

T("anumana-lef","Anumana ECG-AI LEF","Anumana","https://anumana.ai","ecg-cardiac",
  "12-lead ECG algorithm that flags likely low ejection fraction (LVEF 40% or less).",
  ["Screens adults at risk of heart failure for LVEF of 40% or less from a standard 12-lead ECG","Notification software; not a standalone diagnostic"],
  [U],
  NP, U, "FDA 510(k) K250652 (July 28, 2025), Class II, product code QYE; earlier clearance K232699",
  ["https://anumana.ai/anumana-receives-u-s-fda-510k-clearance-for-ecg-ai-algorithm-to-detect-low-ejection-fraction/","https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K250652"])

T("kardia-12l","Kardia 12L","AliveCor","https://alivecor.com/products/kardia12l","ecg-cardiac",
  "Handheld 12-lead ECG system (single cable, five electrodes) with KAI 12L AI determinations.",
  ["12-lead ECG from five electrodes on one cable","KAI 12L AI: 39 cardiac determinations as of January 2026"],
  [U],
  NP, U, "FDA-cleared; January 2026 clearance expanded KAI 12L to 39 determinations",
  ["https://alivecor.com/products/kardia12l","https://alivecor.com/press/press_release/alivecor-announces-fda-clearance-new-cardiac-determinations-kardia-12l-ecg-system"])

T("eko-core-500","Eko CORE 500","Eko Health","https://www.ekohealth.com","ecg-cardiac",
  "Digital stethoscope with 3-lead ECG, noise cancellation and FDA-cleared murmur and AFib AI.",
  ["Audio amplification and noise cancellation (relevant to loud EDs; untested by us)","3-lead ECG and color display","AI murmur and AFib detection via Eko+; low-EF detection via enterprise SENSORA platform"],
  ["Enterprise SENSORA platform; EHR specifics "+U],
  "CORE 500 listed at $389 (regularly $449); Eko+ $119.99/yr after 14-day trial (store pages, Oct 2026)",
  U, "FDA-cleared device and AI (structural murmur, AFib); low EF detection available through SENSORA",
  ["https://www.ekohealth.com/collections/stethoscopes","https://support.ekohealth.com/hc/en-us/articles/16698084427547-CORE-500-FAQ","https://www.ekohealth.com/products/prepaid-eko-annual-membership","https://www.ekohealth.com/pages/sensora"])

# ---------------- Imaging triage ----------------
T("aidoc","Aidoc (aiOS / CARE)","Aidoc","https://www.aidoc.com","imaging-triage",
  "Enterprise radiology AI platform; its CARE foundation model is cleared for multi-condition CT triage.",
  ["Comprehensive body-CT triage of acute findings in one workflow (CARE)","Earlier BriefCase clearances incl. ICH and PE","Delivered via Aidoc aiOS with performance monitoring"],
  ["PACS/worklist integration; EHR specifics "+U],
  NP+" (enterprise)", U,
  "FDA 510(k) K253578 (Feb 26, 2026): CARE Multi-Triage CT for pneumothorax, pericardial effusion, large aortic aneurysm, shoulder fracture/dislocation; earlier BriefCase clearances incl. K190072 (ICH, PE), K201020 (incidental PE)",
  ["https://www.aidoc.com/about/news/aidoc-secures-fda-clearance-for-healthcares-first-comprehensive-foundation-model-ai/","https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K253578","https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201020.pdf","https://fda.innolitics.com/device/K190072"],
  ed_vendor=["Positioned as a 'safety net' for ED crowding and imaging backlogs"],
  notes="The vendor reports mean sensitivity of 97% and specificity of 98% for the 11 indications in its pivotal study. These are vendor-reported figures.")

T("viz-ai","Viz.ai","Viz.ai","https://www.viz.ai","imaging-triage",
  "Care-coordination platform that started with the first FDA De Novo AI triage clearance (LVO stroke, 2018).",
  ["Viz LVO detects suspected large vessel occlusion on CTA and notifies specialists","Further cleared modules incl. ICH, SDH, AAA, RV/LV, aneurysm","Mobile viewing and team communication (mobile images non-diagnostic)"],
  ["PACS and mobile app; EHR specifics "+U],
  NP+" (enterprise)", U,
  "FDA De Novo DEN170073 (2018, ContaCT/Viz LVO); 510(k)s incl. K223042 (LVO), K210209 (ICH), K220439 (SDH), K223443 (AAA), K221100 (RV/LV)",
  ["https://www.fda.gov/news-events/press-announcements/fda-permits-marketing-clinical-decision-support-software-alerting-providers-potential-stroke","https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN170073.pdf","https://www.viz.ai/indications-for-use","https://www.fiercebiotech.com/medtech/viz-ai-upgrades-triage-platform-avicenna-ai-s-pulmonary-embolism-aortic-dissection"],
  notes="PE and aortic dissection detection on the Viz platform comes from Avicenna.AI's CINA CHEST.")

T("rapidai","RapidAI","RapidAI","https://www.rapidai.com","imaging-triage",
  "Stroke and neurovascular imaging AI: LVO, ICH and non-contrast CT stroke triage.",
  ["Rapid LVO: suspected ICA/MCA-M1 occlusion on CTA","Rapid ICH: suspected hemorrhage on non-contrast CT","Rapid NCCT Stroke: combined ICH and LVO triage on NCCT","Lumina 3D head and neck CTA reconstruction"],
  ["PACS; EHR specifics "+U],
  NP+" (enterprise)", U,
  "FDA 510(k) clearances incl. K221248 (2022) and K222884 (2023); Lumina 3D cleared Feb 2025",
  ["https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221248.pdf","https://www.accessdata.fda.gov/cdrh_docs/pdf22/K222884.pdf","https://www.rapidai.com/press-release/ncct-stroke","https://www.rapidai.com/press-release/rapidai-secures-fda-clearance-for-groundbreaking-ai-3d-head-and-neck-cta-imaging-lumina-3d"])

T("annalise-cxr","Annalise Enterprise CXR","Annalise.ai (Harrison.ai)","https://harrison.ai","imaging-triage",
  "Chest X-ray triage AI that pushes case-level alerts for pneumothorax and other acute findings to the worklist.",
  ["Triage of pneumothorax and tension pneumothorax","2025 expansion: pleural effusion, pneumoperitoneum, vertebral compression fracture","Alerts to PACS/RIS worklist; not a rule-out tool"],
  ["PACS/RIS worklist"],
  NP, U, "FDA 510(k) K213941 (Feb 24, 2022); K250831 (Apr 23, 2025), patients 22 and older",
  ["https://www.accessdata.fda.gov/cdrh_docs/pdf21/K213941.pdf","https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K250831","https://harrison.ai/news/annalise-enterprise-cxr-receives-first-u-s-fda-510k-clearance/"])

T("gleamer-boneview","BoneView","Gleamer","https://www.gleamer.ai","imaging-triage",
  "Fracture-detection aid for X-rays that highlights suspected fractures for the reading clinician.",
  ["Concurrent reading aid that flags suspected fractures on radiographs","Not a replacement for physician interpretation"],
  ["PACS; EHR specifics "+U],
  NP, U, "FDA 510(k) K222176 (March 2, 2023), Class II; earlier K212365",
  ["https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K222176","https://interventionalnews.com/boneview-ai-detect-fractures/"],
  studies=[{"title":"Guermazi et al., Improving Radiographic Fracture Recognition Performance and Efficiency Using AI (Radiology; reader study, 480 exams, 24 readers)","url":"https://seelearn-emea.fujifilm.com/wp-content/uploads/2022/11/Radiology_BoneView-US_Guermazi.pdf"}])

T("qure-qer","qER (and qXR)","Qure.ai","https://www.qure.ai/us","imaging-triage",
  "Head CT triage for ICH, mass effect, midline shift and cranial fracture; separate chest X-ray triage product.",
  ["qER: triage of non-contrast adult head CT","qXR-PTX-PE: pneumothorax and pleural effusion triage on CXR"],
  ["PACS; EHR specifics "+U],
  NP, U, "qER FDA 510(k) K200921 (June 17, 2020); qXR-PTX-PE K230899 (Aug 22, 2023)",
  ["https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm?ID=K200921","https://www.accessdata.fda.gov/cdrh_docs/pdf23/K230899.pdf","https://www.qure.ai/us/regulatory-and-privacy"])

T("avicenna-cina","CINA","Avicenna.AI","https://avicenna.ai/solutions/emergency/","imaging-triage",
  "Emergency CT triage for PE, aortic dissection, ICH and LVO; also embedded in other platforms such as Viz.ai.",
  ["CINA CHEST: suspected PE on CTPA and aortic dissection on chest/thoraco-abdominal CTA","CINA-iPE: incidental PE on non-dedicated contrast CT","Neurovascular triage for ICH and LVO"],
  ["PACS/worklist; available via partner platforms"],
  NP, U, "FDA 510(k) clearances incl. K210237 (May 2021) and K233968 (March 2024, CINA-iPE)",
  ["https://www.accessdata.fda.gov/cdrh_docs/pdf21/K210237.pdf","https://www.accessdata.fda.gov/cdrh_docs/pdf23/K233968.pdf","https://avicenna.ai/solutions/emergency/"])

T("brainomix-360","Brainomix 360 Stroke","Brainomix","https://www.brainomix.com","imaging-triage",
  "Stroke imaging AI: e-ASPECTS scoring plus NCCT triage for LVO and ICH.",
  ["e-ASPECTS: editable ASPECTS score on NCCT within 24h of last known well","Triage Stroke: NCCT triage for suspected ICA/M1 LVO and ICH"],
  ["PACS; EHR specifics "+U],
  NP, U, "FDA 510(k) K221564 / K243294 (e-ASPECTS); K232496 (Triage Stroke, Nov 2023)",
  ["https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243294.pdf","https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm?ID=K232496","https://evtoday.com/news/brainomix-stroke-ai-platform-launched-in-united-states"])

# ---------------- POCUS AI ----------------
T("ge-venue-caption","Venue Family with Caption Guidance","GE HealthCare (Caption Health)","https://gehealthcare-ultrasound.com/en/venue-family/venue-caption-guidance/","pocus-ai",
  "Point-of-care ultrasound with real-time AI probe guidance for acquiring standard cardiac views.",
  ["Step-by-step probe-positioning guidance","Image-quality feedback and auto-capture of diagnostic-quality cardiac views","Interpretation still requires a qualified clinician"],
  [U],
  NP, NA, "FDA De Novo DEN190040 (Aug 27, 2019, Caption Guidance); product code QJU, Class II; later 510(k) K243065",
  ["https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN190040.pdf","https://www.gehealthcare.com/en-us/about/newsroom/press-releases/ge-healthcare-launches-enhanced-venue-family-point-of-care-ultrasound-systems-featuring-ai-driven-caption-guidance","https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K243065"])

T("echonous-kosmos","Kosmos","EchoNous","https://echonous.com/specialty/emergency-medicine/","pocus-ai",
  "Handheld POCUS platform with AI-assisted EF and Trio auto-labeling, grading and guidance.",
  ["AI-assisted EF workflow","Trio: auto-labeling, auto-grading, auto-guidance","Us2.ai partnership for automated echo analysis","Kosmos EDU training app"],
  [U],
  NP, NA, "Kosmos FDA 510(k) K233826 (Aug 29, 2024). Older user guide said some AI features relied on FDA's COVID-era enforcement policy; check current status per feature",
  ["https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm?ID=K233826","https://echonous.com/specialty/emergency-medicine/","https://www.businesswire.com/news/home/20210805005796/en/EchoNous-Partners-with-Us2.ai-for-Machine-Learning-enabled-Analysis-of-Heart-Scans"],
  notes="EchoNous has sponsored EM ultrasound education podcasts (Ultrasound GEL, 2024).")

T("butterfly-iq3","Butterfly iQ3","Butterfly Network","https://www.butterflynetwork.com/iq3","pocus-ai",
  "Single-probe whole-body handheld ultrasound with FDA-cleared AI tools such as auto B-line counting and bladder volume.",
  ["Auto B-Line Counter (cleared April 2023)","Auto Bladder Volume (cleared June 2020)","AI tools require an Advanced Technology membership"],
  [U],
  "iQ3 $3,899 (3-yr warranty) or $2,699 (1-yr warranty); AI features need membership: $420/yr or $1,500 one-time 5-year plan (per pricing page summary)",
  NA, "FDA 510(k) for device and AI tools incl. K200980 (bladder volume, 2020) and auto B-lines (2023)",
  ["https://www.butterflynetwork.com/pricing","https://www.butterflynetwork.com/press-releases/fda-clearance-butterfly-auto-b-lines-ai-tool","https://www.accessdata.fda.gov/cdrh_docs/pdf20/K200980.pdf"])

T("exo-iris","Exo Iris","Exo","https://www.exo.inc/iris","pocus-ai",
  "Handheld ultrasound with FDA-cleared AI for cardiac, lung, IVC and bladder, plus Exo Works workflow software.",
  ["Cardiac, lung, IVC and bladder AI","Quality AI expanded to abdominal upper-quadrant and pelvic views (2026)","Exo Works for documentation, storage and credentialing workflows"],
  ["Exo Works workflow software; EHR specifics "+U],
  NP, NA, "FDA 510(k) K260217 (Feb 24, 2026) for AI Platform 2.2",
  ["https://www.exo.inc/ai","https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K260217","https://www.exo.inc/article/exo-launches-fda-cleared-ai-on-exo-iris-to-address-heart-failure"])

# ---------------- Sepsis, triage & early warning ----------------
T("prenosis-immunoscore","Sepsis ImmunoScore","Prenosis","https://prenosis.com","sepsis-triage-early-warning",
  "First FDA-authorized AI/ML sepsis risk tool; uses up to 22 EMR inputs for patients with suspected infection in the ED or hospital.",
  ["Risk of sepsis within 24 hours for patients with suspected infection","Uses up to 22 EMR inputs","Adjunctive tool; not a continuous alert system"],
  ["EMR-integrated; specific EHRs "+U],
  NP, U, "FDA De Novo DEN230036 (April 2, 2024), Class II",
  ["https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm?id=DEN230036","https://prenosis.com/news/prenosis-announces-fda-de-novo-marketing-authorization-of-immunoscore/"],
  studies=[{"title":"FDA-Authorized AI/ML Tool for Sepsis Prediction: Development and Validation (NEJM AI)","url":"https://ai.nejm.org/doi/full/10.1056/AIoa2400867"}])

T("bayesian-trews","Bayesian Health (TREWS)","Bayesian Health","https://www.bayesianhealth.com","sepsis-triage-early-warning",
  "Real-time clinical intelligence platform whose TREWS sepsis model was studied prospectively at 5 sites.",
  ["Continuous monitoring for sepsis, deterioration and other conditions","EHR-integrated alerts and guidance"],
  ["Works alongside Epic (vendor compares against the Epic sepsis algorithm); specifics "+U],
  NP, U, U,
  ["https://www.bayesianhealth.com/","https://www.nature.com/articles/s41591-022-01894-0"],
  studies=[{"title":"Adams et al., Prospective, multi-site study of patient outcomes after implementation of TREWS (Nature Medicine, 2022)","url":"https://doi.org/10.1038/s41591-022-01894-0"},{"title":"Critique preprint: Randomized Clinical Trials or Convenient Controls: TREWS or FALSE? (2022)","url":"https://doi.org/10.1101/2022.08.08.22278526"}],
  notes="The Nature Medicine study was observational, not randomized.")

T("epic-sepsis-model","Epic Sepsis Model","Epic Systems","https://www.epic.com","sepsis-triage-early-warning",
  "Proprietary sepsis prediction model built into Epic and widely deployed; independent validations have been mixed.",
  ["Sepsis risk score inside Epic"],
  ["Epic (native)"],
  "Included with Epic; "+NP, NA, "Not FDA-authorized as a device (none found)",
  ["https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307"],
  studies=[{"title":"Wong et al., External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients (JAMA Intern Med, 2021): hospitalization-level AUC 0.63","url":"https://doi.org/10.1001/jamainternmed.2021.2626"}],
  notes="Included as a benchmark because most EM physicians already see its alerts.")

T("kate-mednition","KATE","Mednition","https://mednition.com/emergency-department-triage-ai/","sepsis-triage-early-warning",
  "EHR-integrated ED triage decision support: recommends acuity and flags high-risk patients incl. early sepsis.",
  ["Analyzes triage intake data and nursing notes","Acuity recommendation; nurse keeps final decision","Early sepsis flag at triage"],
  ["EHR-integrated; specific EHRs "+U],
  NP, U, "KATE Sepsis: FDA Breakthrough Device Designation (Nov 2023). Not authorized/cleared per sources found",
  ["https://mednition.com/emergency-department-triage-ai/","https://mednition.com/fda-grants-kate-ai-breakthrough-device-designation-for-early-sepsis-detection/"],
  studies=[{"title":"Retrospective sepsis study of KATE Triage v4 (arXiv 2204.07657)","url":"https://arxiv.org/pdf/2204.07657"}],
  ed_vendor=["Built for ED triage nurses"])

T("corti","Corti","Corti","https://www.corti.ai","sepsis-triage-early-warning",
  "Real-time AI for emergency calls that flags suspected out-of-hospital cardiac arrest for dispatchers.",
  ["Listens to emergency call audio and alerts dispatchers to suspected OHCA"],
  ["Dispatch / EMS systems"],
  NP, U, U,
  ["https://doi.org/10.1001/jamanetworkopen.2020.32320","https://pubmed.ncbi.nlm.nih.gov/30664917/"],
  studies=[{"title":"Blomberg et al., Effect of Machine Learning on Dispatcher Recognition of OHCA: RCT (JAMA Netw Open, 2021): no significant improvement in dispatcher recognition","url":"https://doi.org/10.1001/jamanetworkopen.2020.32320"},{"title":"Machine learning as a supportive tool to recognize cardiac arrest in emergency calls (Resuscitation, 2019)","url":"https://pubmed.ncbi.nlm.nih.gov/30664917/"}],
  notes="Relevant to EMS-facing EM physicians. Corti also sells other clinical AI products not reviewed here.")

# ---------------- Discharge & patient follow-up ----------------
T("palmer-discharger","DischargER","palmER","https://www.palm-er.com/palmer/assistants/discharger","discharge-patient-comms",
  "Writes ED discharge instructions, work notes and school notes from the chart, adjusted for whoever will read them.",
  ["Discharge instructions with home care, follow-up and return precautions","Work, school, daycare and return-to-play notes with minimum necessary information","Adjustable reading level and translation"],
  ["Vendor says it 'works with any EMR' (paste-in or chart view)"],
  NP, U, "None found",
  ["https://www.palm-er.com/palmer/assistants/discharger"],
  ed_vendor=["Built for the ED (name and positioning)"])

T("hippocratic-ai","Hippocratic AI","Hippocratic AI","https://hippocraticai.com","discharge-patient-comms",
  "Generative AI voice agents that call patients after ED visits or discharge and escalate to a nurse when needed.",
  ["Post-ER and post-discharge phone follow-up","Symptom checks, medication and discharge-instruction review, appointment confirmation","Escalation to a human nurse"],
  [U],
  NP, U, "None found",
  ["https://hippocraticai.com/ai-agents-that-call-your-patients/","https://uhs.com/news/universal-health-services-launches-hippocratic-ais-generative-ai-healthcare-agents-to-assist-with-post-discharge-patient-engagement/"])

FREE = {"heidi","doximity-scribe","openevidence","glass-health","doximity-ask"}
FDA_AUTH = {"pmcardio-queen-of-hearts","anumana-lef","kardia-12l","eko-core-500","aidoc","viz-ai","rapidai","annalise-cxr","gleamer-boneview","qure-qer","avicenna-cina","brainomix-360","ge-venue-caption","echonous-kosmos","butterfly-iq3","exo-iris","prenosis-immunoscore"}
for t in tools:
    t["free_tier"] = t["slug"] in FREE
    t["fda_authorized"] = t["slug"] in FDA_AUTH
json.dump(tools, open("data/tools.json","w"), indent=2)
print(len(tools))
from collections import Counter; print(Counter(t["category"] for t in tools))
