"""Initial website content, taken from the UniLeap Overseas prototype designs.

Everything here is editable afterwards from the Website Admin panel.
"""

from datetime import datetime


def img(photo_id, width=1600):
    return f"https://images.unsplash.com/photo-{photo_id}?w={width}&q=75&auto=format&fit=crop"


LONDON = "1513635269975-59663e0ac1ad"
NYC = "1485871981521-5b1fd3805eee"
TORONTO = "1486325212027-8081e485255e"
SYDNEY = "1506973035872-a4ec16b8e8d9"
DUBLIN = "1549918864-48ac978761a4"
BERLIN = "1560969184-10fe8719e047"
GRAD = "1541339907198-e08756dedf3f"
STUDENTS = "1517486808906-6ca8b3f04846"
FRIENDS = "1529156069898-49953e39b3ac"
LECTURE = "1519452575417-564c1401ecc0"
LIBRARY = "1564981797816-1043664bf78d"
CLASSROOM = "1580582932707-520aed937b7b"
CAMPUS = "1607237138185-eedd9c632b0b"
PLANE = "1436491865332-7a61a109cc05"
DESK = "1488190211105-8b0e65b80b4e"
BOOKS = "1503676260728-1c00da094a0b"

SITE = {
    "facebook_url": "https://www.facebook.com/share/1WXZc5QbUY/",
    "instagram_url": "https://www.instagram.com/unileapoverseas/",
    "whatsapp": "918688088983",
    "office_image_url": img(CAMPUS, 800),
    "cta_image_url": img(PLANE),
    "map_embed_url": "https://maps.google.com/maps?q=Gachibowli%2C%20Hyderabad&z=13&output=embed",
}

HOME_HERO_FEATURES = [
    ("fa-solid fa-graduation-cap", "Course Guidance"),
    ("fa-solid fa-building-columns", "University Shortlisting"),
    ("fa-solid fa-file-lines", "Application Assistance"),
    ("fa-solid fa-plane", "Visa Guidance"),
    ("fa-solid fa-users", "Loan Assistance"),
]

HEROES = {
    "home": {
        "eyebrow": "Study Abroad. Build a Brighter Tomorrow",
        "title": "Your Global Education Journey [[Starts Here]]",
        "subtitle": "Personalised guidance to help you choose the right country, university and course for a brighter future.",
        "script_text": "Your|Global Dreams|Our Guidance",
        "image_url": img(LONDON),
        "show_counselling_form": True,
        "features": HOME_HERO_FEATURES,
    },
    "about": {
        "eyebrow": "About UniLeap Overseas",
        "title": "Guiding Students Towards a Brighter [[Global Future]]",
        "subtitle": "At UniLeap Overseas, we help ambitious students turn their dreams of international education into reality with the right guidance, support and opportunities.",
        "script_text": "Your|Global Dreams|Our Guidance",
        "image_url": img(GRAD),
        "features": [
            ("fa-solid fa-users", "Student-Centric Approach"),
            ("fa-solid fa-briefcase", "Transparent Process"),
            ("fa-solid fa-user-group", "Expert Guidance"),
            ("fa-solid fa-camera", "End-to-End Support"),
        ],
    },
    "destinations": {
        "eyebrow": "Study Destinations",
        "title": "Explore Global [[Opportunities]]",
        "subtitle": "Discover top study destinations, world-class universities and career opportunities. Find the right country to build a brighter future.",
        "script_text": "A Brighter|Future|Across|Borders",
        "image_url": img(LONDON),
        "features": [
            ("fa-solid fa-earth-americas", "World-Class Education"),
            ("fa-solid fa-briefcase", "Global Career Opportunities"),
            ("fa-solid fa-users", "Diverse & Inclusive Culture"),
            ("fa-solid fa-plane", "Life-Changing Experiences"),
        ],
    },
    "universities": {
        "eyebrow": "",
        "title": "Universities & [[Courses]]",
        "subtitle": "Explore top universities and industry-relevant courses across leading study destinations.",
        "image_url": img(CAMPUS),
        "features": [
            ("fa-solid fa-building-columns", "Wide Range of Options"),
            ("fa-solid fa-graduation-cap", "Courses for Your Career Goals"),
            ("fa-solid fa-file-lines", "Updated Information and Guidance"),
        ],
    },
    "loan": {
        "eyebrow": "Education Loan Assistance",
        "title": "Fund Your Global Education [[With Confidence]]",
        "subtitle": "Explore education loan options, understand eligibility and get expert guidance to make your study abroad dreams more accessible.",
        "image_url": img(LIBRARY),
        "show_counselling_form": True,
        "features": [
            ("fa-solid fa-scale-balanced", "Compare Loan Options"),
            ("fa-solid fa-clipboard-check", "Understand Eligibility"),
            ("fa-solid fa-route", "Step-by-Step Support"),
            ("fa-solid fa-hand-holding-dollar", "Guidance on Repayment"),
        ],
    },
    "blog": {
        "eyebrow": "Our Blog",
        "title": "Latest Insights on [[Study Abroad]]",
        "subtitle": "Stay updated with the latest news, expert insights and guides on international education, university admissions, visas, education loans and more.",
        "script_text": "Insights|Updates|Guidance|for Your|Global Journey",
        "image_url": img(DESK),
        "features": [
            ("fa-solid fa-book-open", "Expert Insights"),
            ("fa-solid fa-file-lines", "Latest News"),
            ("fa-solid fa-graduation-cap", "Study Guides"),
            ("fa-solid fa-globe", "Country Updates"),
        ],
    },
    "contact": {
        "eyebrow": "Contact Us",
        "title": "We're Here to Help You [[Go Further]]",
        "subtitle": "Have questions about studying abroad? Our experts are ready to guide you with the right information, options and personalised support.",
        "script_text": "Let's|Plan Your|Global Future|together",
        "image_url": img(STUDENTS),
        "features": [
            ("fa-solid fa-bolt", "Quick Response"),
            ("fa-solid fa-headset", "Expert Support"),
            ("fa-solid fa-user-group", "Personalised Guidance"),
            ("fa-solid fa-comments", "Free Counselling"),
        ],
    },
    "counselling": {
        "eyebrow": "Free Counselling",
        "title": "Talk to an Expert – [[It's Free]]",
        "subtitle": "Book a free one-to-one session with our study abroad counsellors. We'll understand your goals and help you plan the right country, university, course and budget.",
        "image_url": img(FRIENDS),
        "show_counselling_form": True,
        "features": [
            ("fa-solid fa-video", "Online or In-Person"),
            ("fa-regular fa-clock", "Flexible Time Slots"),
            ("fa-solid fa-hand-holding-heart", "No Obligation"),
        ],
    },
}

# Home page sections added with the second home page design.
HOME_WHY = {
    "eyebrow": "Why UniLeap Overseas",
    "title": "More Than Admissions, A Partner in [[Your Journey]]",
    "subtitle": "We go beyond just admissions. We provide personalised guidance, transparent advice and continuous support to help you achieve your global education goals.",
    "button_text": "Know More About Us",
    "button_link": "/about-us/",
}
HOME_CTA = {
    "title": "Let's Plan Your [[Global Education]] Journey",
    "subtitle": "Get a free counselling session with our experts and take the first step towards a brighter future.",
    "button_text": "Get Free Counselling",
    "button_link": "/free-counselling/",
    "script_text": "Different|Destinations|One Greater|Tomorrow",
    "image_url": img(FRIENDS, 1000),
}
HOME_BLOG = {"eyebrow": "Insights & Guides", "title": "Latest from [[Our Blog]]"}
HOME_TRENDING = ["MSc Digital Marketing", "MBA", "Data Science", "Business Analytics", "Computer Science", "Finance"]

THANKS_SECTIONS = {
    "thanks.hero": {
        "title": "Thank [[You!]]",
        "subtitle": "Your enquiry has been submitted successfully.",
        "body": "<p>Our education experts will review your details and get back to you within 24 hours. Meanwhile, feel free to explore more about studying abroad with UniLeap Overseas.</p>",
        "script_text": "A Brighter|Global Future|Awaits You!",
        "image_url": img(GRAD, 1100),
    },
    "thanks.next": {"title": "What Happens [[Next?]]"},
    "thanks.explore": {"title": "In the Meantime, Explore", "subtitle": "Discover useful resources to plan your study abroad journey."},
}
THANKS_NEXT = [
    ("fa-solid fa-envelope", "We Review Your Enquiry", "Our team will check your details and requirements."),
    ("fa-solid fa-phone", "We'll Contact You", "Our education counsellor will reach out to you within 24 hours."),
    ("fa-solid fa-comment-dots", "Personalised Guidance", "Get expert advice based on your goals, profile and preferences."),
    ("fa-solid fa-file-lines", "Start Your Journey", "Receive university shortlisting, application guidance and support."),
]

SECTIONS = {
    **THANKS_SECTIONS,
    "home.destinations": {"title": "Explore [[Top Study Destinations]]", "subtitle": "Discover global opportunities and world-class education in top countries."},
    "home.courses": {"title": "Popular [[Course Categories]]", "subtitle": "Explore industry-relevant courses to build your global career."},
    "home.services": {"eyebrow": "Comprehensive Support", "title": "Our [[Services]]", "subtitle": "End-to-end support for your overseas education journey.", "button_text": "View All Services", "button_link": "/free-counselling/"},
    "home.journey": {"title": "Your Study Abroad Journey in [[5 Simple Steps]]", "subtitle": "A clear and guided process from your first enquiry to your dream university."},
    "home.why": HOME_WHY,
    "home.cta": HOME_CTA,
    "home.blog": HOME_BLOG,
    "home.faq": {"title": "Frequently Asked [[Questions]]", "subtitle": "Get answers to common questions about studying abroad.", "script_text": "Global|Opportunities|Brighter Futures", "image_url": img(STUDENTS, 900)},
    "about.story": {
        "eyebrow": "Our Story",
        "title": "Who [[We Are]]",
        "body": "<p>UniLeap Overseas is an international education consultancy committed to helping students from India and beyond access world-class education opportunities across the UK, USA, Canada, Australia, Ireland, Germany and other destinations.</p><p>We provide personalised guidance at every step – from choosing the right course and university to application support, education loan guidance and pre-departure assistance. Our goal is to make your study abroad journey simple, transparent and stress-free.</p>",
        "button_text": "Get to Know Us",
        "button_link": "#mission",
        "script_text": "Different|Destinations|One Greater|Tomorrow",
        "image_url": img(LONDON, 1000),
    },
    "about.foundation": {"eyebrow": "Our Foundation", "title": "Our Mission, Vision [[& Values]]", "subtitle": "We are driven by a strong purpose and values that keep students at the centre of everything we do."},
    "about.why": {"title": "Why Choose [[UniLeap Overseas?]]", "subtitle": "We go beyond just admissions. We focus on your goals, preferences and future opportunities, providing expert guidance and personalised support.", "script_text": "More|Than Admissions|A Partner in|Your Journey", "image_url": img(GRAD, 900)},
    "about.cta": {"title": "Let's Build Your [[Global Future]] Together", "subtitle": "Get expert guidance, personalised support and the right opportunities to make your study abroad dreams a reality.", "image_url": img(GRAD)},
    "destinations.list": {"title": "Our [[Study Destinations]]", "subtitle": "Explore popular study destinations for Indian students, each offering unique opportunities, world-class education and global career pathways."},
    "destinations.compare": {"title": "Compare [[Study Destinations]]", "subtitle": "Find the best country based on tuition fees, work opportunities, living costs and more.", "button_text": "Compare Now"},
    "destinations.why": {"title": "Why [[Study Abroad?]]", "subtitle": "A global education can open doors to endless opportunities."},
    "destinations.cta": {"eyebrow": "Ready to explore your study destination?", "title": "Get Personalised Guidance from Our Experts", "subtitle": "We'll help you choose the right country, university and course based on your goals and profile.", "script_text": "Your|Global Journey|Starts Here", "image_url": img(GRAD)},
    "universities.help": {"title": "Not sure which university or course is right for you?", "subtitle": "Get personalised guidance from our expert counsellors.", "button_text": "Get Free Counselling", "button_link": "/free-counselling/"},
    "loan.partners": {
        "title": "Our [[Lending Partners]]",
        "subtitle": "We help you explore education loan options from leading banks and financial institutions.",
        "body": "<p><strong>Note:</strong> The lenders listed above are for informational purposes only. UniLeap Overseas does not guarantee loan approval. All applications are subject to the lender's eligibility criteria, documentation and independent assessment.</p>",
    },
    "loan.process": {"title": "Our [[Education Loan Process]]", "subtitle": "A simple and transparent process with expert support at every step.", "script_text": "From Application|to Your Dream"},
    "loan.types": {"title": "Types of [[Education Loans]]", "subtitle": "Explore the options available based on your profile and requirements.", "script_text": "A Step|Closer to|Your Global|Dreams", "image_url": img(STUDENTS, 900)},
    "loan.eligibility": {"title": "General Eligibility [[Criteria]]", "subtitle": "Eligibility may vary by lender. Here are some common criteria."},
    "loan.details": {"title": "Loan Details [[(Indicative)]]", "subtitle": "Loan terms and features may vary by lender and applicant profile."},
    "loan.documents": {"title": "Required [[Documents]]", "subtitle": "Keep these ready to speed up your education loan application."},
    "loan.faq": {"title": "Frequently Asked [[Questions]]", "subtitle": "Get answers to common questions about education loans."},
    "loan.cta": {
        "title": "Need Personalised Guidance?",
        "subtitle": "Talk to our experts and get clear guidance on education loan options for your preferred country and course.",
        "body": "<p>UniLeap Overseas does not guarantee education loan approval or scholarship awards. All funding is subject to the relevant lender's or scholarship provider's eligibility criteria, documentation, terms, and independent assessment.</p>",
        "image_url": img(GRAD, 900),
    },
    "blog.categories": {"title": "Explore by Category"},
    "blog.latest": {"title": "Latest Articles"},
    "blog.newsletter": {"title": "Stay Updated", "subtitle": "Subscribe to our blog and get the latest study abroad news, tips and updates directly in your inbox.", "button_text": "Subscribe"},
    "contact.form": {"title": "Get in [[Touch]]", "subtitle": "Fill out the form and our experts will get back to you shortly."},
    "contact.info": {"title": "Contact [[Information]]", "subtitle": "You can also reach us directly through the following channels."},
    "contact.follow": {"title": "Follow Us", "subtitle": "Stay connected for the latest updates, university news and study abroad tips."},
    "contact.location": {"title": "Our Location", "subtitle": "Visit our office or connect with us online."},
    "contact.online": {"title": "[[Can't Visit Us]] in Person?", "subtitle": "No problem! You can book an online counselling session with our experts at a time that works for you.", "button_text": "Book Online Counselling", "button_link": "/free-counselling/"},
    "contact.faq": {"title": "Frequently Asked [[Questions]]", "subtitle": "Get quick answers to common questions."},
    "contact.cta": {"title": "Still Have Questions?", "subtitle": "Talk to our experts and get personal guidance on your study abroad journey.", "button_text": "Talk to Our Experts", "button_link": "#form", "image_url": img(LONDON, 900)},
    "team.intro": {"eyebrow": "Our Team", "title": "Meet Our [[Experts]]", "subtitle": "Experienced counsellors who have guided hundreds of students to top universities worldwide."},
    "partners.intro": {"eyebrow": "Our Partners", "title": "Trusted [[Partners]]", "subtitle": "We work with universities, lenders and service providers to give you a smooth, end-to-end experience."},
    "testimonials.intro": {"eyebrow": "Testimonials", "title": "What Our [[Students]] Say", "subtitle": "Real stories from students who started their global journey with UniLeap Overseas."},
}

FEATURES = {
    "thanks_next": THANKS_NEXT,
    "home_trending": [("", term, "") for term in HOME_TRENDING],
    "home_why": [
        ("fa-regular fa-user", "Student-Centric Approach", "Personalised guidance based on your goals."),
        ("fa-regular fa-file-lines", "Clear & Transparent Process", "Honest advice and step-by-step support."),
        ("fa-solid fa-globe", "Wide Range of Options", "Explore multiple countries, universities and courses."),
        ("fa-solid fa-headset", "Ongoing Support", "Assistance even after you reach your destination."),
    ],
    "about_why": [
        ("fa-solid fa-users", "Personalised Guidance", "Solutions tailored to your profile and career goals."),
        ("fa-solid fa-file-lines", "End-to-End Support", "From university selection to pre-departure."),
        ("fa-solid fa-globe", "Wide Range of Options", "Top universities and courses across countries."),
        ("fa-solid fa-handshake", "Trusted Advice", "Transparent and unbiased guidance for your future."),
    ],
    "about_foundation": [
        ("fa-solid fa-bullseye", "Our Mission", "To empower students with the right guidance, resources and opportunities to achieve their global education goals and build successful careers."),
        ("fa-regular fa-eye", "Our Vision", "To be a trusted global education consultancy recognised for transparency, quality guidance and positive student outcomes."),
    ],
    "about_values": [
        ("", "Student-first approach", ""),
        ("", "Honest and transparent advice", ""),
        ("", "Commitment to quality and integrity", ""),
        ("", "Continuous support and long-term relationships", ""),
    ],
    "destinations_why": [
        ("fa-solid fa-person-walking-luggage", "Global Exposure", "Experience new cultures, ideas and perspectives."),
        ("fa-solid fa-chart-column", "Better Career Opportunities", "Gain international experience and build a global career."),
        ("fa-solid fa-graduation-cap", "Personal Growth", "Develop independence, confidence and life skills."),
        ("fa-solid fa-people-group", "Build a Global Network", "Connect with students and professionals from around the world."),
    ],
    "compare_factors": [
        ("fa-solid fa-graduation-cap", "Tuition Fees", ""),
        ("fa-solid fa-briefcase", "Post-Study Work", ""),
        ("fa-solid fa-house", "Cost of Living", ""),
        ("fa-solid fa-users", "PR Options", ""),
        ("fa-solid fa-building-columns", "Top Universities", ""),
    ],
    "universities_help": [
        ("fa-regular fa-id-badge", "Understand your profile", ""),
        ("fa-solid fa-list-check", "Shortlist the right universities", ""),
        ("fa-regular fa-calendar-check", "Get course and intake guidance", ""),
        ("fa-solid fa-magnifying-glass", "Clarify admission and visa process", ""),
    ],
    "loan_highlights": [
        ("fa-solid fa-percent", "Competitive Loan Options", "Explore education loan options with interest rates starting from 8.45%, subject to lender eligibility and applicable terms."),
        ("fa-solid fa-coins", "Flexible Funding Solutions", "Explore secured and unsecured education loan options for eligible students, with funding of up to ₹3 crore depending on the lender and applicant profile."),
        ("fa-solid fa-graduation-cap", "Scholarship & Financial Aid Guidance", "Get guidance on identifying scholarships and financial assistance opportunities that may help reduce your overall study costs."),
        ("fa-solid fa-shield-halved", "Lender & Government Scheme Guidance", "Understand relevant lender offerings and eligible government-backed education loan schemes, subject to their respective criteria."),
    ],
    "loan_eligibility": [
        ("fa-regular fa-user", "Indian citizen", ""),
        ("fa-solid fa-school", "Admission offer from a recognised foreign university", ""),
        ("fa-solid fa-graduation-cap", "Minimum academic qualification (varies by lender)", ""),
        ("fa-solid fa-house-lock", "Meet the lender's income and credit criteria", ""),
    ],
    "loan_details": [
        ("fa-solid fa-indian-rupee-sign", "Loan Amount", "Up to ₹3 Crore", "(Varies by lender)"),
        ("fa-solid fa-percent", "Interest Rate (p.a.)", "Starting from 8.45%", "(Varies by lender)"),
        ("fa-regular fa-calendar", "Repayment Period", "Up to 15 years", "(Varies by lender)"),
        ("fa-regular fa-clock", "Moratorium Period", "During study period", "(Varies by lender)"),
    ],
    "loan_documents": [
        ("fa-regular fa-id-card", "KYC documents", "PAN, Aadhaar and passport of the student and co-applicant."),
        ("fa-solid fa-envelope-open-text", "Admission letter", "Offer / admission letter from the university with fee details."),
        ("fa-solid fa-award", "Academic records", "Mark sheets and certificates (10th, 12th, graduation) and test scores."),
        ("fa-solid fa-file-invoice-dollar", "Income proof", "Co-applicant salary slips / ITRs and bank statements."),
        ("fa-solid fa-house", "Collateral documents", "Property papers for secured loans, as required by the lender."),
        ("fa-solid fa-calculator", "Cost of study", "Estimated expenses for tuition, living and travel."),
    ],
    "contact_online": [
        ("fa-solid fa-video", "Video Call Counselling", ""),
        ("fa-regular fa-clock", "Flexible Time Slots", ""),
        ("fa-solid fa-user-tie", "Expert Guidance", ""),
    ],
    "contact_cta": [
        ("fa-solid fa-user-group", "Personalised Guidance", ""),
        ("fa-solid fa-envelope", "No Obligation Counselling", ""),
        ("fa-solid fa-users", "Trusted Support", ""),
    ],
}

# (title, icon, description, "Learn More" link)
SERVICES = [
    ("Personalised Counselling", "fa-solid fa-users", "Understand your goals and get expert guidance.", "/free-counselling/"),
    ("University Shortlisting", "fa-solid fa-building-columns", "Find the right universities based on your profile.", "/university-shortlisting/"),
    ("Application Assistance", "fa-solid fa-file-lines", "Support with documents and application process.", "/free-counselling/"),
    ("Visa Guidance", "fa-solid fa-plane", "Step-by-step guidance for a smooth visa process.", "/blog/category/visa-immigration/"),
    ("Education Loan Assistance", "fa-solid fa-indian-rupee-sign", "Get guidance on education loan options from leading lenders.", "/education-loan/"),
]

STEPS = {
    "home_journey": [
        ("fa-solid fa-comments", "Free Counselling", "Discuss your goals and explore options."),
        ("fa-solid fa-list-check", "Shortlist Universities", "Based on your profile and preferences."),
        ("fa-solid fa-file-pen", "Apply to Universities", "Get complete support with documentation."),
        ("fa-solid fa-passport", "Receive Offer & Visa", "Guidance through offer acceptance and visa process."),
        ("fa-solid fa-plane-departure", "Fly to Your Dream", "Begin your global education journey."),
    ],
    "loan_process": [
        ("fa-solid fa-comments", "Initial Counselling", "Understand your goals and loan requirements."),
        ("fa-solid fa-file-circle-check", "Check Eligibility", "Review basic eligibility and required documents."),
        ("fa-solid fa-magnifying-glass", "Compare Options", "Explore suitable lenders and loan products."),
        ("fa-solid fa-file-lines", "Application Support", "Guidance with application and documentation."),
        ("fa-solid fa-shield-halved", "Loan Disbursal", "Track your application till disbursal."),
    ],
}

FAQS = {
    "home": [
        ("When should I start planning for overseas education?", "It is recommended to start 8-12 months before your intended intake to have enough time for research, applications and visa processing."),
        ("Do I need to give IELTS or TOEFL?", "Most universities require an English proficiency test such as IELTS, TOEFL, PTE or Duolingo. Some universities may waive it based on your academic background – our counsellors will check this for you."),
        ("Can I apply to multiple universities?", "Yes. We usually recommend applying to 4-6 universities across ambitious, moderate and safe options to maximise your chances."),
        ("How long does the visa process take?", "It depends on the country and season – typically 3 to 8 weeks. We help you prepare documents early so there are no last-minute surprises."),
        ("Do you help with education loans?", "Yes. We guide you through secured and unsecured loan options from leading banks and NBFCs and help you prepare your application."),
        ("Can you help me choose the right country and course?", "Absolutely. Based on your profile, budget and career goals we recommend the best-fit countries, universities and courses."),
    ],
    "loan": [
        ("Do you guarantee education loan approval?", "No. Loan approval is entirely at the lender's discretion and depends on their eligibility criteria and assessment. We help you prepare a strong application."),
        ("What documents are required for an education loan?", "Typically KYC documents, admission letter, academic records, cost of study, co-applicant income proof and – for secured loans – collateral documents."),
        ("Can I get a loan without collateral?", "Yes, many lenders offer unsecured education loans based on your academic profile, university, course and co-applicant's financial profile."),
        ("What is the typical interest rate for an education loan?", "Interest rates generally start from around 8.45% p.a. and vary by lender, loan type and applicant profile."),
        ("When do I need to start repaying the loan?", "Most lenders offer a moratorium during the course period plus 6-12 months, after which EMIs begin. Some require simple interest during the course."),
        ("Can NRIs co-apply for an education loan?", "Some lenders accept NRI co-applicants subject to additional conditions. We'll help you find lenders that support this."),
        ("Which expenses are covered under an education loan?", "Tuition fees, living expenses, travel, insurance, laptop and other course-related costs are usually covered, depending on the lender."),
    ],
    "contact": [
        ("How can I book a free counselling session?", "Fill in the enquiry form on this page or call us – our team will call you back to fix a convenient slot, online or in person."),
        ("Do you provide admission support for all countries?", "We support admissions to the UK, USA, Canada, Australia, Ireland, Germany and several other destinations."),
        ("Is there any fee for counselling?", "No. Our initial counselling session is completely free and there is no obligation."),
        ("Can I get education loan assistance?", "Yes – we guide you on lenders, eligibility and documentation for secured and unsecured education loans."),
        ("How long does it take to get a university shortlist?", "Usually within 2-3 working days after we receive your academic documents and preferences."),
    ],
    "general": [
        ("What services does UniLeap Overseas offer?", "Personalised counselling, university and course shortlisting, application and SOP assistance, visa guidance, education loan assistance and pre-departure support."),
        ("Which intakes are available for studying abroad?", "Major intakes are September/Fall and January/Spring. Some countries also offer May (UK), February and July (Australia) and April (Germany) intakes."),
        ("Can I work while studying abroad?", "Most destinations allow international students to work part-time during term and full-time during holidays, subject to visa conditions."),
    ],
}

STATS = [
    ("fa-solid fa-graduation-cap", "500+", "Students Guided"),
    ("fa-solid fa-building-columns", "100+", "Global Universities"),
    ("fa-solid fa-users", "6+", "Study Destinations"),
    ("fa-solid fa-file-circle-check", "95%", "Student Satisfaction"),
]

COURSE_CATEGORIES = [
    ("Business & Management", "business", "fa-solid fa-chart-column"),
    ("Engineering & Technology", "engineering", "fa-solid fa-gear"),
    ("Computer Science & IT", "computer-science", "fa-solid fa-laptop"),
    ("Data Science & Analytics", "data-science", "fa-solid fa-database"),
    ("Healthcare & Life Sciences", "healthcare", "fa-solid fa-heart-pulse"),
    ("Arts, Design & Media", "arts-design", "fa-solid fa-palette"),
    ("Law & Social Sciences", "law", "fa-solid fa-scale-balanced"),
    ("Hospitality & Tourism", "hospitality", "fa-solid fa-plane"),
]

DESTINATIONS = [
    {
        "name": "UK", "full_name": "United Kingdom", "slug": "uk", "country_code": "gb", "currency": "£",
        "image_url": img(LONDON, 900),
        "short_description": "World-class education and global recognition",
        "tagline": "World-class education",
        "summary": "Globally recognised degrees, diverse courses and strong career opportunities.",
        "tuition_fees": "£12,000 – £30,000", "post_study_work": "Graduate Route visa (18 months – 2 years)",
        "cost_of_living": "£12,000 – £16,000", "pr_options": "Skilled Worker visa → settlement (ILR)", "popular_intakes": "January, May, September",
        "highlights": [("fa-solid fa-graduation-cap", "Top-ranked Universities"), ("fa-solid fa-briefcase", "Post-study Work Opportunities"), ("fa-solid fa-users", "Rich Culture & Diversity"), ("fa-solid fa-book", "Wide Range of Courses")],
        "description": "<h2>Why study in the UK?</h2><p>The UK is home to some of the world's oldest and most respected universities. Master's programmes are typically just one year long, which saves both tuition and living costs compared with many other destinations.</p><ul><li>Globally recognised qualifications</li><li>One-year master's degrees</li><li>Graduate Route visa to gain work experience after study</li><li>Large Indian student community and direct flights</li></ul><h2>Popular courses</h2><p>Business &amp; Management, Data Science, Computer Science, Engineering, Law and Public Health.</p>",
    },
    {
        "name": "USA", "full_name": "United States of America", "slug": "usa", "country_code": "us", "currency": "$",
        "image_url": img(NYC, 900),
        "short_description": "Diverse courses and strong career opportunities",
        "tagline": "Innovation & opportunities",
        "summary": "World-leading education, innovation and unmatched career opportunities.",
        "tuition_fees": "$20,000 – $55,000", "post_study_work": "OPT 12 months (+24 months for STEM)",
        "cost_of_living": "$12,000 – $20,000", "pr_options": "H-1B work visa → Green Card (employer sponsored)", "popular_intakes": "September (Fall), January (Spring)",
        "highlights": [("fa-solid fa-graduation-cap", "Global Universities"), ("fa-solid fa-flask", "STEM & Research Opportunities"), ("fa-solid fa-users", "Diverse Career Pathways"), ("fa-solid fa-landmark", "Cultural Exposure")],
        "description": "<h2>Why study in the USA?</h2><p>The USA hosts the largest number of top-ranked universities in the world and offers flexible programmes, cutting-edge research and access to leading global employers.</p><ul><li>Flexible curriculum and wide choice of specialisations</li><li>STEM OPT extension of up to 3 years of work in total</li><li>Generous assistantships and scholarships</li></ul>",
    },
    {
        "name": "Canada", "full_name": "Canada", "slug": "canada", "country_code": "ca", "currency": "CA$",
        "image_url": img(TORONTO, 900),
        "short_description": "Quality education and a welcoming environment",
        "tagline": "Quality education & PR options",
        "summary": "Quality education, affordable options and a welcoming environment.",
        "tuition_fees": "CA$18,000 – CA$45,000", "post_study_work": "Post-Graduation Work Permit (up to 3 years)",
        "cost_of_living": "CA$15,000 – CA$22,000", "pr_options": "Express Entry & Provincial Nominee Programs", "popular_intakes": "September, January, May",
        "highlights": [("fa-solid fa-graduation-cap", "High-Quality Education"), ("fa-solid fa-briefcase", "Post-Study Work Visa"), ("fa-solid fa-users", "Pathway to Permanent Residency"), ("fa-solid fa-shield-heart", "Safe & Inclusive Society")],
        "description": "<h2>Why study in Canada?</h2><p>Canada combines high-quality education with a safe, multicultural society and clear pathways from study to work and permanent residency.</p><ul><li>Affordable tuition compared with the USA and UK</li><li>Post-Graduation Work Permit</li><li>Co-op programmes with paid work terms</li></ul>",
    },
    {
        "name": "Australia", "full_name": "Australia", "slug": "australia", "country_code": "au", "currency": "A$",
        "image_url": img(SYDNEY, 900),
        "short_description": "Globally recognised degrees and great lifestyle",
        "tagline": "Globally recognised degrees",
        "summary": "Globally recognised degrees, work opportunities and an enriching lifestyle.",
        "tuition_fees": "A$22,000 – A$50,000", "post_study_work": "Temporary Graduate visa (2 – 3 years)",
        "cost_of_living": "A$25,000 – A$30,000", "pr_options": "Points-based skilled migration", "popular_intakes": "February, July",
        "highlights": [("fa-solid fa-graduation-cap", "Top Universities"), ("fa-solid fa-briefcase", "Work While You Study"), ("fa-solid fa-users", "Post-Study Work Opportunities"), ("fa-solid fa-sun", "High Quality of Life")],
        "description": "<h2>Why study in Australia?</h2><p>Australia offers globally ranked universities, excellent student support and a relaxed, outdoor lifestyle in some of the world's most liveable cities.</p><ul><li>Part-time work rights during study</li><li>Temporary Graduate visa after graduation</li><li>February and July intakes</li></ul>",
    },
    {
        "name": "Ireland", "full_name": "Ireland", "slug": "ireland", "country_code": "ie", "currency": "€",
        "image_url": img(DUBLIN, 900),
        "short_description": "Affordable education and growth opportunities",
        "tagline": "Affordable education",
        "summary": "Affordable education, growing job market and a strong tech industry.",
        "tuition_fees": "€10,000 – €28,000", "post_study_work": "Stamp 1G – up to 2 years for Master's graduates",
        "cost_of_living": "€10,000 – €14,000", "pr_options": "Critical Skills Employment Permit → Stamp 4", "popular_intakes": "September, January",
        "highlights": [("fa-solid fa-graduation-cap", "Globally Recognised Degrees"), ("fa-solid fa-briefcase", "Strong Job Market"), ("fa-solid fa-earth-europe", "Gateway to Europe"), ("fa-solid fa-users", "Vibrant Student Life")],
        "description": "<h2>Why study in Ireland?</h2><p>Ireland is the European home of many of the world's biggest tech and pharma companies, and the only English-speaking country in the Eurozone.</p><ul><li>One-year master's programmes</li><li>Up to 2 years post-study work for master's graduates</li><li>Friendly, safe and English-speaking</li></ul>",
    },
    {
        "name": "Germany", "full_name": "Germany", "slug": "germany", "country_code": "de", "currency": "€",
        "image_url": img(BERLIN, 900),
        "short_description": "High-quality education with low or no tuition fees",
        "tagline": "High-quality education",
        "summary": "High-quality education, low or no tuition fees and strong career prospects.",
        "tuition_fees": "Low or no tuition at most public universities", "post_study_work": "18-month job-seeker residence permit",
        "cost_of_living": "~€12,000 (blocked account)", "pr_options": "EU Blue Card → settlement permit", "popular_intakes": "October (Winter), April (Summer)",
        "highlights": [("fa-solid fa-graduation-cap", "Tuition-Free / Low Tuition Fees"), ("fa-solid fa-industry", "Strong Industrial Base"), ("fa-solid fa-flask", "Research & Innovation"), ("fa-solid fa-users", "Excellent Career Opportunities")],
        "description": "<h2>Why study in Germany?</h2><p>Germany is Europe's largest economy and offers world-class engineering and technology education, often with little or no tuition at public universities.</p><ul><li>Low or no tuition fees at most public universities</li><li>Strong links with industry</li><li>18-month post-study job-seeker permit</li></ul>",
    },
]

# (name, slug-of-destination, city, type, established, image, is_top, [(course, category, level, duration, intakes, fee, popular)])
UNIVERSITIES = [
    ("University of Birmingham", "uk", "Birmingham", "public", 1900, CAMPUS, True, [
        ("MSc Management", "business", "pg", "1 year", "September", 27000, True),
        ("MSc Digital Marketing", "business", "pg", "1 year", "September", 27500, True),
        ("MSc International Business", "business", "pg", "1 year", "September", 27000, True),
        ("MSc Computer Science", "computer-science", "pg", "1 year", "September", 31000, False),
        ("MSc Data Science", "data-science", "pg", "1 year", "September", 31000, False),
    ]),
    ("Coventry University", "uk", "Coventry", "public", 1843, LECTURE, False, [
        ("MSc Digital Marketing", "business", "pg", "1 year", "January, May, September", 19650, True),
        ("MSc Business Management", "business", "pg", "1 year", "January, May, September", 19650, True),
        ("MSc Project Management", "business", "pg", "1 year", "January, September", 19650, True),
        ("MSc Cyber Security", "computer-science", "pg", "1 year", "January, September", 20500, False),
        ("BSc (Hons) Computer Science", "computer-science", "ug", "3 years", "September", 17000, False),
    ]),
    ("University of Leicester", "uk", "Leicester", "public", 1921, LIBRARY, True, [
        ("MSc Management", "business", "pg", "1 year", "January, September", 23000, True),
        ("MSc International Marketing", "business", "pg", "1 year", "January, September", 23000, True),
        ("MSc Data Analytics", "data-science", "pg", "1 year", "January, September", 24500, True),
        ("MSc Advanced Computer Science", "computer-science", "pg", "1 year", "September", 24500, False),
        ("LLM International Law", "law", "pg", "1 year", "September", 22000, False),
    ]),
    ("Aston University", "uk", "Birmingham", "public", 1895, CLASSROOM, False, [
        ("MSc Business Analytics", "data-science", "pg", "1 year", "January, September", 22500, True),
        ("MSc Marketing", "business", "pg", "1 year", "January, September", 22000, True),
        ("MSc International Business", "business", "pg", "1 year", "January, September", 22000, True),
        ("MSc Mechanical Engineering", "engineering", "pg", "1 year", "September", 23000, False),
    ]),
    ("De Montfort University", "uk", "Leicester", "public", 1870, LONDON, False, [
        ("MSc Digital Marketing", "business", "pg", "1 year", "January, September", 17250, True),
        ("MSc Management", "business", "pg", "1 year", "January, September", 17250, True),
        ("MSc Data Science", "data-science", "pg", "1 year", "January, September", 17750, True),
        ("MA Graphic Design", "arts-design", "pg", "1 year", "September", 17250, False),
        ("MSc Public Health", "healthcare", "pg", "1 year", "January, September", 17250, False),
    ]),
    ("University of Nottingham", "uk", "Nottingham", "public", 1881, GRAD, True, [
        ("MSc Marketing", "business", "pg", "1 year", "September", 30000, True),
        ("MSc Management", "business", "pg", "1 year", "September", 30000, True),
        ("MSc International Business", "business", "pg", "1 year", "September", 30000, True),
        ("MSc Civil Engineering", "engineering", "pg", "1 year", "September", 31500, False),
        ("MSc Public Health", "healthcare", "pg", "1 year", "September", 29000, False),
    ]),
    ("Arizona State University", "usa", "Tempe, Arizona", "public", 1885, CAMPUS, False, [
        ("MS Computer Science", "computer-science", "pg", "2 years", "January, September", 34000, True),
        ("MS Business Analytics", "data-science", "pg", "1 year", "September", 38000, True),
        ("MS Industrial Engineering", "engineering", "pg", "2 years", "January, September", 34000, False),
        ("BS Hospitality Management", "hospitality", "ug", "4 years", "September", 33000, False),
    ]),
    ("Northeastern University", "usa", "Boston, Massachusetts", "private", 1898, NYC, True, [
        ("MS Data Science", "data-science", "pg", "2 years", "January, September", 50000, True),
        ("MS Information Systems", "computer-science", "pg", "2 years", "January, September", 50000, True),
        ("MS Project Management", "business", "pg", "2 years", "January, September", 48000, False),
    ]),
    ("University at Buffalo (SUNY)", "usa", "Buffalo, New York", "public", 1846, LIBRARY, False, [
        ("MS Computer Science & Engineering", "computer-science", "pg", "2 years", "January, September", 30000, True),
        ("MS Electrical Engineering", "engineering", "pg", "2 years", "January, September", 30000, False),
        ("MPH Public Health", "healthcare", "pg", "2 years", "September", 29000, False),
    ]),
    ("University of Toronto", "canada", "Toronto, Ontario", "public", 1827, TORONTO, True, [
        ("MEng Electrical & Computer Engineering", "engineering", "pg", "1.5 years", "September", 52000, True),
        ("Master of Information", "computer-science", "pg", "2 years", "September", 45000, False),
        ("Master of Management Analytics", "data-science", "pg", "1 year", "September", 70000, True),
    ]),
    ("University of Waterloo", "canada", "Waterloo, Ontario", "public", 1957, CAMPUS, True, [
        ("MEng Civil Engineering", "engineering", "pg", "1 year", "January, May, September", 32000, True),
        ("Master of Data Science & AI", "data-science", "pg", "1.5 years", "September", 40000, True),
        ("BCS Computer Science (Co-op)", "computer-science", "ug", "4-5 years", "September", 66000, False),
    ]),
    ("Conestoga College", "canada", "Kitchener, Ontario", "college", 1967, CLASSROOM, False, [
        ("Graduate Certificate – Project Management", "business", "diploma", "1 year", "January, May, September", 17000, True),
        ("Graduate Certificate – Big Data Solutions Architecture", "data-science", "diploma", "1 year", "January, September", 17500, True),
        ("Diploma – Hospitality Management", "hospitality", "diploma", "2 years", "January, May, September", 16500, False),
    ]),
    ("Monash University", "australia", "Melbourne, Victoria", "public", 1958, SYDNEY, True, [
        ("Master of Business Analytics", "data-science", "pg", "2 years", "February, July", 52000, True),
        ("Master of Information Technology", "computer-science", "pg", "2 years", "February, July", 50000, True),
        ("Master of Professional Engineering", "engineering", "pg", "2 years", "February, July", 52000, False),
    ]),
    ("Deakin University", "australia", "Melbourne / Geelong, Victoria", "public", 1974, LECTURE, False, [
        ("Master of Business Administration", "business", "pg", "2 years", "February, July", 42000, True),
        ("Master of Data Science", "data-science", "pg", "2 years", "February, July", 42000, True),
        ("Master of Public Health", "healthcare", "pg", "2 years", "February, July", 38000, False),
    ]),
    ("The University of Sydney", "australia", "Sydney, New South Wales", "public", 1850, GRAD, True, [
        ("Master of Commerce", "business", "pg", "2 years", "February, July", 56000, True),
        ("Master of Computer Science", "computer-science", "pg", "2 years", "February, July", 54000, False),
        ("Master of Laws (LLM)", "law", "pg", "1 year", "February, July", 50000, False),
    ]),
    ("University College Dublin", "ireland", "Dublin", "public", 1854, DUBLIN, True, [
        ("MSc Business Analytics", "data-science", "pg", "1 year", "September", 27000, True),
        ("MSc Digital Marketing", "business", "pg", "1 year", "September", 25000, True),
        ("MSc Computer Science (Conversion)", "computer-science", "pg", "1 year", "September", 24000, False),
    ]),
    ("Trinity College Dublin", "ireland", "Dublin", "public", 1592, LIBRARY, True, [
        ("MSc Computer Science – Data Science", "data-science", "pg", "1 year", "September", 28000, True),
        ("MSc Management", "business", "pg", "1 year", "September", 26000, True),
        ("MSc Global Health", "healthcare", "pg", "1 year", "September", 24000, False),
    ]),
    ("University of Galway", "ireland", "Galway", "public", 1845, CAMPUS, False, [
        ("MSc Data Analytics", "data-science", "pg", "1 year", "September", 19500, True),
        ("MSc Biomedical Engineering", "engineering", "pg", "1 year", "September", 20000, False),
        ("MSc Marketing Practice", "business", "pg", "1 year", "September", 18500, False),
    ]),
    ("Technical University of Munich", "germany", "Munich", "public", 1868, BERLIN, True, [
        ("MSc Informatics", "computer-science", "pg", "2 years", "April, October", 12000, True),
        ("MSc Mechanical Engineering", "engineering", "pg", "2 years", "April, October", 12000, True),
        ("MSc Management", "business", "pg", "2 years", "October", 12000, False),
    ]),
    ("RWTH Aachen University", "germany", "Aachen", "public", 1870, LECTURE, True, [
        ("MSc Automotive Engineering", "engineering", "pg", "2 years", "April, October", 0, True),
        ("MSc Data Science", "data-science", "pg", "2 years", "October", 0, True),
        ("MSc Computer Science", "computer-science", "pg", "2 years", "April, October", 0, False),
    ]),
    ("Constructor University", "germany", "Bremen", "private", 2001, CAMPUS, False, [
        ("MSc Data Science for Society and Business", "data-science", "pg", "2 years", "September", 20000, True),
        ("MSc Supply Chain Engineering & Management", "business", "pg", "2 years", "September", 20000, False),
        ("BSc Computer Science", "computer-science", "ug", "3 years", "September", 20000, False),
    ]),
]

LENDERS = [
    ("SBI", "#22409a"),
    ("HDFC Bank", "#004c8f"),
    ("Axis Bank", "#97144d"),
    ("ICICI Bank", "#f37e20"),
    ("Avanse", "#0d3a6e"),
    ("InCred", "#f15a22"),
]

LOAN_TYPES = [
    ("Secured Education Loans", "fa-solid fa-shield-halved", "Higher loan amounts with lower interest rates. Requires collateral as per lender policy.",
     "Suitable for higher loan amounts\nLower interest rates (varies by lender)\nCollateral required (e.g., property)", "blue"),
    ("Unsecured Education Loans", "fa-regular fa-file-lines", "No collateral required. Based on profile and lender eligibility criteria.",
     "Based on academic and financial profile\nNo collateral required\nSuitable for select courses and universities", "amber"),
]

BLOG_CATEGORIES = [
    ("Study Abroad Guides", "study-abroad", "fa-solid fa-graduation-cap"),
    ("Country Guides", "country-guides", "fa-solid fa-globe"),
    ("University Updates", "university-updates", "fa-solid fa-building-columns"),
    ("Education Loan", "education-loan", "fa-solid fa-wallet"),
    ("Visa & Immigration", "visa-immigration", "fa-solid fa-passport"),
    ("Scholarships", "scholarships", "fa-solid fa-trophy"),
    ("Career & Jobs", "career-jobs", "fa-solid fa-briefcase"),
    ("Student Life", "student-life", "fa-solid fa-users"),
]


def _article(intro, sections, outro="Need help planning your next step? Book a free counselling session with UniLeap Overseas and our experts will guide you."):
    html = f"<p>{intro}</p>"
    for heading, points in sections:
        html += f"<h2>{heading}</h2>"
        if isinstance(points, str):
            html += f"<p>{points}</p>"
        else:
            html += "<ul>" + "".join(f"<li>{p}</li>" for p in points) + "</ul>"
    return html + f"<blockquote>{outro}</blockquote>"


# (title, slug, category, tag, tag_color, image, date, featured, excerpt, content)
POSTS = [
    ("Top 10 UK Universities for MSc Digital Marketing in 2027", "top-uk-universities-msc-digital-marketing-2027", "university-updates", "UK", "blue", LONDON, datetime(2026, 10, 25), False,
     "Explore the best UK universities for MSc Digital Marketing, including tuition fees, entry requirements and career opportunities.",
     _article("Digital marketing is one of the fastest-growing career fields, and UK universities offer focused one-year master's programmes that combine strategy, analytics and hands-on projects.",
              [("What to look for in a programme", ["Accreditation and industry partnerships (e.g. CIM, Google, HubSpot)", "Modules in analytics, SEO, social media and content strategy", "Live client projects and placement options", "Graduate outcomes and alumni network"]),
               ("Universities worth considering", ["University of Birmingham", "University of Leicester", "Coventry University", "De Montfort University", "University of Nottingham", "Aston University"]),
               ("Typical entry requirements", "Most universities ask for a 55-60% undergraduate degree, IELTS 6.5 overall (no band below 6.0) and a strong statement of purpose. Work experience is useful but not always mandatory.")])),
    ("Study in Canada in 2027: A Complete Guide for Indian Students", "study-in-canada-2027-guide", "country-guides", "Canada", "red", TORONTO, datetime(2026, 10, 22), False,
     "Everything you need to know about courses, costs, visas, and post-study work opportunities in Canada.",
     _article("Canada remains a top choice for Indian students thanks to its quality education, multicultural cities and clear pathways from study to work.",
              [("Popular programmes", ["Graduate certificates in project management, data and supply chain", "Master's degrees in engineering and computer science", "Co-op programmes with paid work terms"]),
               ("Costs to plan for", "Tuition typically ranges from CA$18,000 to CA$45,000 per year depending on the institution and programme. You will also need to show funds for living expenses as part of your study permit application."),
               ("Work and stay options", ["Part-time work during studies, subject to permit conditions", "Post-Graduation Work Permit after eligible programmes", "Express Entry and Provincial Nominee pathways to PR"])])),
    ("Education Loan for Study Abroad: Eligibility, Documents & Best Lenders", "education-loan-study-abroad-guide", "education-loan", "Education Loan", "green", BOOKS, datetime(2026, 10, 20), False,
     "A complete guide to education loans for international studies, including interest rates, eligibility and required documents.",
     _article("An education loan can make studying abroad possible without draining your family's savings. Here's how to approach it the right way.",
              [("Secured vs unsecured loans", "Secured loans need collateral such as property but offer higher amounts and lower interest rates. Unsecured loans need no collateral and depend on your academic profile, university and co-applicant's income."),
               ("Documents you'll need", ["KYC documents for student and co-applicant", "University admission letter", "Academic records and test scores", "Co-applicant income proof", "Collateral documents (for secured loans)"]),
               ("Tips for a smooth approval", ["Apply early – ideally as soon as you receive your offer", "Compare interest rates, processing fees and moratorium terms", "Keep your documents complete and consistent"])])),
    ("Study in Australia: Courses, Fees, and PR Opportunities", "study-in-australia-courses-fees-pr", "country-guides", "Australia", "orange", SYDNEY, datetime(2026, 10, 18), False,
     "Learn about top courses, tuition fees, work opportunities and pathways to permanent residency in Australia.",
     _article("Australia offers globally ranked universities, a great lifestyle and strong post-study work opportunities.",
              [("Top courses", ["Business Analytics and Data Science", "Information Technology", "Engineering", "Nursing and Public Health"]),
               ("Fees and living costs", "Tuition usually ranges from A$22,000 to A$50,000 per year. Plan for living costs of roughly A$25,000–A$30,000 per year depending on the city."),
               ("After graduation", "Eligible graduates can apply for a Temporary Graduate visa. Skilled migration programmes offer points-based routes to permanent residency for in-demand occupations.")])),
    ("Study in Germany for International Students: A Complete Guide", "study-in-germany-complete-guide", "country-guides", "Germany", "yellow", BERLIN, datetime(2026, 10, 15), False,
     "Discover tuition-free options, application process, eligibility and top universities in Germany.",
     _article("Germany is famous for engineering excellence, research and low or no tuition fees at most public universities.",
              [("Why Germany?", ["Low or no tuition at most public universities", "Strong industry links and internships", "18-month post-study job-seeker permit"]),
               ("Application essentials", ["Recognised bachelor's degree with good grades", "English (IELTS/TOEFL) or German language proof", "Blocked account for living expenses", "APS certificate for Indian applicants"]),
               ("Intakes", "Most programmes start in the winter semester (October) with some in the summer semester (April). Deadlines are often 6-9 months earlier, so start early.")])),
    ("Student Visa Process: Step-by-Step Guide for 2027", "student-visa-process-guide-2027", "visa-immigration", "Visa", "purple", PLANE, datetime(2026, 10, 12), False,
     "Understand the complete student visa process, required documents, interview tips and common mistakes to avoid.",
     _article("A well-prepared visa application is the final step between you and your dream university.",
              [("The typical process", ["Receive and accept your unconditional offer", "Pay the deposit and receive your CAS / I-20 / CoE / LOA", "Arrange financial documents", "Complete the online application and biometrics", "Attend the interview (if required)"]),
               ("Common mistakes to avoid", ["Insufficient or inconsistent financial documents", "Gaps in your study plan that you can't explain", "Applying too close to the course start date"]),
               ("Interview tips", "Be clear and honest about why you chose your course, university and country, how you will fund your studies and what your career plans are.")])),
    ("Why Ireland is a Great Choice for Indian Students in 2027", "why-ireland-indian-students-2027", "study-abroad", "Ireland", "green", DUBLIN, datetime(2026, 10, 10), False,
     "Explore top courses, affordable education, work opportunities and growing job market in Ireland.",
     _article("Ireland is home to the European headquarters of many global tech and pharma companies, making it an attractive destination for ambitious students.",
              [("Key advantages", ["One-year master's programmes", "Up to 2 years post-study work for master's graduates", "English-speaking and part of the EU", "Strong demand in tech, data and life sciences"]),
               ("Popular universities", ["University College Dublin", "Trinity College Dublin", "University of Galway"])])),
    ("Top Scholarships for Indian Students in 2027", "top-scholarships-indian-students-2027", "scholarships", "Scholarships", "pink", GRAD, datetime(2026, 10, 8), False,
     "A list of popular scholarships offered by universities and governments across the UK, USA, Canada and more.",
     _article("Scholarships can significantly reduce the cost of studying abroad. Most are competitive, so planning ahead is key.",
              [("Types of scholarships", ["Government scholarships (e.g. Chevening, Fulbright-Nehru, DAAD)", "University merit scholarships and fee waivers", "Country-specific scholarships for Indian students"]),
               ("How to improve your chances", ["Apply early – many deadlines are 8-12 months before the intake", "Write a strong, specific personal statement", "Highlight leadership, projects and community work"])])),
    ("Top In-Demand Jobs After Studying Abroad in 2027", "in-demand-jobs-after-studying-abroad-2027", "career-jobs", "Career", "blue", STUDENTS, datetime(2026, 10, 5), False,
     "Explore high-demand job roles, average salaries and career opportunities across global markets.",
     _article("Choosing a course with strong employment demand helps you get the best return on your study abroad investment.",
              [("High-demand fields", ["Data science and AI", "Cyber security", "Healthcare and nursing", "Engineering and construction management", "Supply chain and logistics"]),
               ("How to stand out", "Combine your degree with internships, certifications and a strong LinkedIn profile. Networking and part-time work in your field can make a big difference.")])),
    ("How to Choose the Right Country for Your Higher Studies?", "how-to-choose-the-right-country", "study-abroad", "Guide", "teal", FRIENDS, datetime(2026, 10, 10, 9), True,
     "A detailed comparison of the UK, USA, Canada, Australia, Ireland and Germany to help you make the right decision.",
     _article("The right country depends on your course, budget, career goals and long-term plans. Here's a simple framework to decide.",
              [("Questions to ask yourself", ["What is my total budget for tuition and living costs?", "How long is the course and what work rights will I have afterwards?", "Do I want to settle abroad long term?", "Which countries are strongest for my field?"]),
               ("Quick comparison", ["UK – one-year master's, Graduate Route visa", "USA – top research universities, STEM OPT", "Canada – PGWP and PR pathways", "Australia – lifestyle and post-study work", "Ireland – tech hub with 2-year stay-back", "Germany – low or no tuition"])])),
    ("Your First Month Abroad: A Student Survival Guide", "first-month-abroad-survival-guide", "student-life", "Student Life", "teal", FRIENDS, datetime(2026, 10, 2), False,
     "Practical tips on accommodation, banking, SIM cards, part-time jobs and making friends in your first weeks abroad.",
     _article("The first few weeks abroad are exciting – and a little overwhelming. A bit of planning makes settling in much easier.",
              [("Before you fly", ["Book temporary accommodation for your first week", "Carry copies of all key documents", "Get an international debit / forex card"]),
               ("First week checklist", ["Collect your residence permit / BRP if required", "Open a local bank account and get a SIM card", "Register with a doctor and your university", "Join student societies to meet people"])])),
]

TEAM = [
    ("Ananya Reddy", "Founder & Lead Counsellor", "Over a decade of experience helping students secure admissions in the UK, Ireland and Europe."),
    ("Rahul Varma", "Senior Counsellor – USA & Canada", "Specialises in STEM admissions, assistantships and scholarships in North America."),
    ("Sneha Iyer", "Visa & Compliance Specialist", "Guides students through visa documentation, interviews and pre-departure."),
    ("Karthik Rao", "Education Loan Advisor", "Helps families compare lenders and prepare strong education loan applications."),
]

TESTIMONIALS = [
    ("Priya S.", "MSc Data Analytics, University of Leicester", "UniLeap made the whole process so simple. From shortlisting to my visa, they were with me at every step and answered every question patiently."),
    ("Arjun K.", "MS Computer Science, Arizona State University", "Their guidance on my SOP and university shortlist was spot on. I got admits from 4 out of 5 universities I applied to!"),
    ("Meghana R.", "Master of Business Analytics, Monash University", "I was confused between Canada and Australia. The counsellors compared everything clearly and helped me pick what suited my goals."),
    ("Vikram T.", "MSc Management, University College Dublin", "The education loan support was a huge relief for my family. They helped us compare lenders and get our documents right the first time."),
    ("Divya P.", "MSc Digital Marketing, Coventry University", "Friendly, honest and super responsive. I'd recommend UniLeap to anyone planning to study abroad."),
    ("Rohit M.", "MSc Informatics, Technical University of Munich", "Germany's process felt complicated, but the team explained the APS, blocked account and visa steps clearly."),
]

PARTNERS = [
    ("University Partners", "Direct relationships with universities across the UK, USA, Canada, Australia, Ireland and Germany."),
    ("Education Loan Partners", "Leading banks and NBFCs that offer secured and unsecured education loans."),
    ("Accommodation Partners", "Trusted student housing providers to help you find a safe home near campus."),
    ("Forex & Travel Partners", "Competitive forex, international money transfers and student travel deals."),
    ("Test Preparation Partners", "IELTS, PTE, TOEFL, GRE and GMAT coaching to help you hit your target scores."),
    ("Insurance Partners", "Student health and travel insurance that meets university and visa requirements."),
]

LEGAL_PAGES = [
    ("Privacy Policy", "privacy-policy",
     "<p>UniLeap Overseas (\"we\", \"us\") respects your privacy. This policy explains how we collect, use and protect your personal information when you use our website and services.</p>"
     "<h2>Information we collect</h2><ul><li>Contact details you share with us, such as your name, phone number and email address</li><li>Study preferences such as destination, course level and intake</li><li>Technical information such as IP address and browser type</li></ul>"
     "<h2>How we use your information</h2><ul><li>To respond to your enquiries and provide counselling</li><li>To help with university, visa and education loan applications at your request</li><li>To send updates you have subscribed to</li></ul>"
     "<h2>Sharing your information</h2><p>We share your information only with universities, lenders or service providers when required to deliver services you have requested, or when required by law. We never sell your personal data.</p>"
     "<h2>Your rights</h2><p>You may request access to, correction of or deletion of your personal data at any time by emailing us.</p>"
     "<h2>Contact</h2><p>For privacy questions, contact info@unileapoverseas.com.</p>"),
    ("Terms & Conditions", "terms-conditions",
     "<p>By using the UniLeap Overseas website and services you agree to these terms.</p>"
     "<h2>Our services</h2><p>We provide guidance and support for overseas education. Admission, visa, scholarship and loan decisions are made solely by the respective universities, authorities and lenders.</p>"
     "<h2>Your responsibilities</h2><ul><li>Provide accurate and complete information and documents</li><li>Meet deadlines communicated by us, universities and authorities</li></ul>"
     "<h2>Website content</h2><p>Information on this website is for general guidance and may change without notice. Please verify details such as fees and visa rules with official sources.</p>"
     "<h2>Limitation of liability</h2><p>UniLeap Overseas is not liable for decisions made by third parties or for losses arising from the use of information on this website.</p>"),
    ("Disclaimer", "disclaimer",
     "<p>The information on this website is provided for general informational purposes only.</p>"
     "<p>UniLeap Overseas does not guarantee university admission, visa approval, scholarship awards or education loan approval. All outcomes are subject to the eligibility criteria, documentation and independent assessment of the relevant university, authority, lender or scholarship provider.</p>"
     "<p>Tuition fees, living costs, interest rates and immigration rules mentioned on this website are indicative and may change. Always confirm the latest details with the official source or with our counsellors.</p>"),
]
