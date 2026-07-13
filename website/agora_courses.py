"""Matrix TRC course catalog for the AI Agora referral archive."""

MATRIX_BASE = "https://www.matrixtrc.ai/course"

AGORA = {
    "title": "AI Agora",
    "intro": (
        "Professional AI capability courses delivered through our partner Matrix TRC. "
        "Browse the archive below and enroll on their platform."
    ),
    "partner_name": "Matrix TRC",
    "partner_url": "https://www.matrixtrc.ai/courses",
    "hero_media": {
        "label": "AI Agora — professional courses",
        "file": "media/home/pillar-agora.png",
        "ratio": "3x2",
    },
}

COURSES = [
    {
        "slug": "designing-data",
        "title": "Visualizing and Describing Data",
        "description": (
            "Compare visualization tools, design effective data collection, validate "
            "data quality, and interpret results with descriptive statistics using SAS-Viya and Python."
        ),
        "image": "media/agora/courses/designing-data.webp",
    },
    {
        "slug": "course-2-statistical-data-analysis",
        "title": "Statistical Data Analysis",
        "description": (
            "Design smart data collection processes, choose sampling methods, validate "
            "data quality, and apply descriptive statistics to interpret results effectively."
        ),
        "image": "media/agora/courses/course-2-statistical-data-analysis.webp",
    },
    {
        "slug": "course-3",
        "title": "Supervised Machine Learning",
        "description": (
            "Build predictive models from labeled data using SAS, Alteryx, STATISTICA, "
            "and Python to support accurate, data-driven decisions."
        ),
        "image": "media/agora/courses/course-3.webp",
    },
    {
        "slug": "course-4-unsupervised-machine-learning",
        "title": "Unsupervised Machine Learning",
        "description": (
            "Uncover hidden patterns with PCA and clustering, define market niches, "
            "and apply unsupervised techniques across practical business contexts."
        ),
        "image": "media/agora/courses/course-4-unsupervised-machine-learning.webp",
    },
    {
        "slug": "course-5-deep-and-generative-deep-learning",
        "title": "Deep & Generative Deep Learning",
        "description": (
            "Hands-on exploration of GANs, VAEs, diffusion models, and sequential "
            "networks for generative AI applications in media, healthcare, and analytics."
        ),
        "image": "media/agora/courses/course-5-deep-and-generative-deep-learning.webp",
    },
    {
        "slug": "course-6-natural-language-processing",
        "title": "Natural Language Processing",
        "description": (
            "Learn how machines understand and generate language through embeddings, "
            "transformers, and LLMs — applied in a practical no-code AI workflow."
        ),
        "image": "media/agora/courses/course-6-natural-language-processing.webp",
    },
    {
        "slug": "forecasting-models-from-a-to-z",
        "title": "Forecasting Models from A to Z",
        "description": (
            "Master forecasting methods from basic models through advanced techniques, "
            "quality indicators, and model selection for reliable near-future predictions."
        ),
        "image": "media/agora/courses/forecasting-models-from-a-to-z.webp",
    },
    {
        "slug": "statistical-quality-control-measurements",
        "title": "Statistical Quality Control",
        "description": (
            "Comprehensive SQC training covering SPC, process capability analysis, and "
            "design of experiments for consistent product and process quality."
        ),
        "image": "media/agora/courses/statistical-quality-control-measurements.webp",
    },
    {
        "slug": "data-management-and-sql",
        "title": "Data Management and SQL",
        "description": (
            "Govern, unify, and access data across sources with practical data management, "
            "SQL, warehousing, and governance strategies for business decisions."
        ),
        "image": "media/agora/courses/data-management-and-sql.webp",
    },
    {
        "slug": "course-10-designing-an-ai-agent",
        "title": "Agentic AI",
        "description": (
            "Design, build, test, and improve AI agents under the structured DMAIC "
            "framework — covering the full agent development lifecycle from definition to control."
        ),
        "image": "media/agora/courses/course-10-designing-an-ai-agent.webp",
    },
]


def course_by_slug(slug):
    for course in COURSES:
        if course["slug"] == slug:
            return course
    return None


def matrix_course_url(slug):
    return f"{MATRIX_BASE}/{slug}"
