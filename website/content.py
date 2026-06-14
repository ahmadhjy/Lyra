"""Static page content from Lyra Website Content - Draft."""


def media(label, size, ratio="4x3", icon="image", variant=""):
    item = {"label": label, "size": size, "ratio": ratio, "icon": icon}
    if variant:
        item["variant"] = variant
    return item


NAV = [
    {"label": "Home", "url_name": "home"},
    {"label": "About Lyra", "url_name": "about"},
    {"label": "Our Ecosystem", "url_name": "ecosystem"},
    {"label": "Who We Serve", "url_name": "who_we_serve"},
    {"label": "Our Approach", "url_name": "approach"},
    {"label": "Why Lyra", "url_name": "why_lyra"},
    {"label": "Contact", "url_name": "contact"},
]

HOME = {
    "hero_title": "Preparing people and institutions for the AI era",
    "hero_subtitle": (
        "LYRA is an AI capability and transformation company. We work across "
        "strategy, learning, and implementation to enable structured AI readiness "
        "at the level where it matters most."
    ),
    "hero_media": media(
        "Hero banner — AI capability & transformation",
        "1400 × 720 px",
        ratio="16x9",
        icon="network",
        variant="hero",
    ),
    "approach_media": media(
        "Capability model — literacy to transformation",
        "900 × 600 px",
        ratio="4x3",
        icon="strategy",
    ),
    "pillars": [
        {
            "title": "AI Agora",
            "summary": "Professional AI capability platform for applied, role-specific competence.",
            "anchor": "ecosystem",
            "media": media("AI Agora platform visual", "600 × 400 px", ratio="3x2", icon="network"),
        },
        {
            "title": "LYRA Education",
            "summary": "Structured AI literacy pathways across K–12 environments.",
            "anchor": "ecosystem",
            "media": media("Education & classroom visual", "600 × 400 px", ratio="3x2", icon="education"),
        },
        {
            "title": "Advisory & Transformation",
            "summary": "AI strategy and capability building for institutions.",
            "anchor": "ecosystem",
            "media": media("Institutional advisory visual", "600 × 400 px", ratio="3x2", icon="building"),
        },
    ],
}

ABOUT = {
    "title": "About Lyra",
    "intro": (
        "LYRA is an AI capability and transformation company preparing people "
        "and institutions for the realities of the AI era."
    ),
    "hero_media": media("About Lyra — brand story visual", "1400 × 560 px", ratio="21x9", icon="people", variant="banner"),
    "sections": [
        {
            "heading": "Who We Are",
            "media": media("Team / leadership in context", "800 × 600 px", ratio="4x3", icon="people"),
            "paragraphs": [
                (
                    "We work across strategy, learning, and implementation to enable "
                    "structured AI readiness at the level where it matters most: "
                    "leadership, workforce, and education systems."
                ),
                (
                    "Our focus is not on tools alone, but on the capability required "
                    "to use them with clarity, judgment, and purpose."
                ),
                (
                    "LYRA supports organizations and societies in moving from fragmented "
                    "AI awareness to deliberate, applied capability."
                ),
            ],
        },
        {
            "heading": "Our Vision",
            "media": media("Vision — future of AI & society", "800 × 600 px", ratio="4x3", icon="vision"),
            "paragraphs": [
                (
                    "A world where artificial intelligence strengthens human potential, "
                    "advances institutional intelligence, and contributes to meaningful "
                    "societal progress."
                ),
            ],
        },
        {
            "heading": "Our Mission",
            "media": media("Mission — capability across sectors", "800 × 600 px", ratio="4x3", icon="strategy"),
            "paragraphs": [
                (
                    "To make AI capability accessible, structured, and responsibly "
                    "embedded across generations, professions, and sectors."
                ),
            ],
        },
        {
            "heading": "Founders",
            "paragraphs": [],
            "media": media("Dr. Sally Hammoud — portrait", "600 × 750 px", ratio="portrait", icon="people", variant="portrait"),
            "cards": [
                {
                    "name": "Dr. Sally Hammoud",
                    "role": "Co-Founder",
                    "bio": (
                        "Dr. Sally Hammoud is an artificial intelligence and communication "
                        "specialist focused on AI capability, digital ecosystems, and institutional "
                        "transformation. Her work explores how AI reshapes professions, organizations, "
                        "and decision-making systems, translating it from concept into applied, "
                        "real-world capability. As the voice behind LYRA, she leads the thinking and "
                        "direction of its approach to AI capability."
                    ),
                },
            ],
        },
    ],
}

ECOSYSTEM = {
    "title": "Our Ecosystem",
    "intro": (
        "AI capability cannot be built through isolated initiatives. LYRA operates "
        "through three interconnected pillars designed to build AI capability at scale."
    ),
    "hero_media": media("Ecosystem overview visual", "1400 × 560 px", ratio="21x9", icon="network", variant="banner"),
    "sections": [
        {
            "heading": "AI Agora",
            "tagline": "AI capability platform for professionals and organizations",
            "media": media("AI Agora — platform & workflows", "800 × 600 px", ratio="4x3", icon="network"),
            "paragraphs": [
                (
                    "AI AGORA is a professional AI capability platform built to move individuals "
                    "and teams beyond basic AI exposure into applied, role-specific competence."
                ),
                "AI AGORA is designed for application, not observation.",
            ],
            "bullets": [
                "AI tools and workflows for professional use",
                "AI strategy and governance modules",
                "Sector-specific AI applications",
                "Practical implementation guides",
                "AI transformation frameworks",
            ],
        },
        {
            "heading": "LYRA Education",
            "tagline": "Structured AI literacy across K–12",
            "media": media("LYRA Education — schools & learning", "800 × 600 px", ratio="4x3", icon="education"),
            "paragraphs": [
                (
                    "LYRA Education establishes structured AI literacy and capability pathways "
                    "across K–12 environments, enabling students, educators, and schools to engage "
                    "with AI in a responsible and informed way."
                ),
                "LYRA Education prepares students to think critically about AI, not depend on it passively.",
            ],
            "bullets": [
                "K–12 AI literacy curriculum",
                "Safe AI tools for classroom environments",
                "Teacher capability pathways",
                "School-level AI integration guidance",
                "AI ethics and digital citizenship",
            ],
        },
        {
            "heading": "Advisory & Transformation",
            "tagline": "AI strategy and capability building for institutions",
            "media": media("Advisory — institutions & transformation", "800 × 600 px", ratio="4x3", icon="building"),
            "paragraphs": [
                (
                    "LYRA works with organizations and public institutions to design and implement "
                    "AI capability strategies grounded in structure, governance, and long-term integration."
                ),
                "We help institutions move from fragmented experimentation to structured AI capability.",
            ],
            "bullets": [
                "AI readiness and capability assessment",
                "AI strategy and roadmap design",
                "Leadership AI literacy",
                "Workforce capability development programs",
                "AI governance and responsible use frameworks",
                "AI implementation guidance",
            ],
        },
    ],
}

WHO_WE_SERVE = {
    "title": "Who We Serve",
    "intro": (
        "LYRA works across the full spectrum of stakeholders shaping and responding to the AI era."
    ),
    "hero_media": media("Audience overview — sectors & stakeholders", "1400 × 560 px", ratio="21x9", icon="audience", variant="banner"),
    "sections": [
        {
            "heading": "Organizations and Enterprises",
            "media": media("Enterprises & teams", "480 × 360 px", ratio="4x3", icon="building", variant="tile"),
            "paragraphs": [
                "Building AI capability across leadership, teams, and operational workflows."
            ],
        },
        {
            "heading": "Government and Public Sector",
            "media": media("Government & public sector", "480 × 360 px", ratio="4x3", icon="building", variant="tile"),
            "paragraphs": [
                "Supporting structured, responsible AI adoption within public institutions and systems."
            ],
        },
        {
            "heading": "Universities and Education Systems",
            "media": media("Universities & higher education", "480 × 360 px", ratio="4x3", icon="education", variant="tile"),
            "paragraphs": [
                "Integrating AI into academic environments, research, and institutional strategy."
            ],
        },
        {
            "heading": "Schools (K–12)",
            "media": media("K–12 schools", "480 × 360 px", ratio="4x3", icon="education", variant="tile"),
            "paragraphs": [
                "Developing foundational AI literacy and responsible use from an early stage."
            ],
        },
        {
            "heading": "Professionals and Leaders",
            "media": media("Professionals & leaders", "480 × 360 px", ratio="4x3", icon="people", variant="tile"),
            "paragraphs": [
                "Equipping individuals with the judgment and capability to apply AI in real contexts."
            ],
        },
        {
            "heading": "Youth and Emerging Workforce",
            "media": media("Youth & emerging workforce", "480 × 360 px", ratio="4x3", icon="audience", variant="tile"),
            "paragraphs": [
                "Preparing the next generation to engage with AI with awareness, adaptability, and responsibility."
            ],
        },
    ],
}

APPROACH = {
    "title": "Our Approach",
    "intro": (
        "LYRA's methodology is defined through the LYRA AI Capability Model, a three-layer "
        "framework that guides individuals and institutions from initial awareness to embedded AI transformation."
    ),
    "hero_media": media("LYRA AI Capability Model diagram", "1400 × 560 px", ratio="21x9", icon="strategy", variant="banner"),
    "sections": [
        {
            "heading": "AI Literacy",
            "tagline": "Understanding before application",
            "media": media("AI Literacy — understanding layer", "800 × 600 px", ratio="4x3", icon="education"),
            "paragraphs": [
                (
                    "AI Literacy establishes a grounded understanding of how artificial intelligence works, "
                    "where it applies, and what its implications are across roles and systems."
                ),
                "Without this layer, AI is used blindly.",
            ],
        },
        {
            "heading": "AI Capability",
            "tagline": "From knowledge to execution",
            "media": media("AI Capability — application layer", "800 × 600 px", ratio="4x3", icon="strategy"),
            "paragraphs": [
                (
                    "AI Capability focuses on applying AI within real professional and institutional contexts. "
                    "At this stage, AI shifts from being a tool to becoming part of how work is performed."
                ),
            ],
        },
        {
            "heading": "AI Transformation",
            "tagline": "Embedding AI into how systems operate",
            "media": media("AI Transformation — systems layer", "800 × 600 px", ratio="4x3", icon="network"),
            "paragraphs": [
                (
                    "AI Transformation is where capability is integrated at the level of strategy, operations, "
                    "and organizational culture. At this level, AI is no longer an addition—it becomes part of "
                    "how the institution thinks and operates."
                ),
            ],
        },
    ],
}

WHY_LYRA = {
    "title": "Why Lyra",
    "intro": (
        "AI adoption is not failing because of technology. It is failing because capability "
        "is missing where it matters most."
    ),
    "hero_media": media("Why Lyra — differentiation visual", "1400 × 560 px", ratio="21x9", icon="vision", variant="banner"),
    "sections": [
        {
            "heading": "The gap we address",
            "media": media("The capability gap in AI adoption", "800 × 600 px", ratio="4x3", icon="strategy"),
            "paragraphs": [
                (
                    "Organizations invest in tools, but overlook the people, structures, and decisions "
                    "required to use them effectively. LYRA addresses the human and institutional capability "
                    "required for AI to function in real environments."
                ),
            ],
        },
        {
            "heading": "What LYRA translates AI into",
            "media": media("AI impact — practice, workflows, education, society", "800 × 600 px", ratio="4x3", icon="network"),
            "bullets": [
                "Professional practice — how individuals think, decide, and perform their work",
                "Organizational workflows — how teams operate and integrate AI into processes",
                "Education systems — how institutions prepare current and future generations",
                "Societal readiness — how AI is understood, adopted, and governed at a broader level",
            ],
        },
    ],
}

CONTACT = {
    "title": "Partnership",
    "intro": (
        "AI capability is not built through tools alone. It is built through clarity and structure. "
        "Build real capability across your organization, workforce, or education system."
    ),
    "cta": "Start the conversation.",
    "hero_media": media("Partnership & collaboration visual", "1400 × 560 px", ratio="21x9", icon="contact", variant="banner"),
    "side_media": media("Contact / office / collaboration scene", "800 × 900 px", ratio="portrait", icon="contact", variant="portrait"),
}
