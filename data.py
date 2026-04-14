ISSUES = [
    {"title": "School Lunch Waste in Massachusetts", "category": "Environment", "region": "Northeast", "emoji": "🥦", "desc": "Thousands of pounds of food wasted daily in school cafeterias."},
    {"title": "Teen Mental Health Support", "category": "Health", "region": "National", "emoji": "🧠", "desc": "Lack of accessible, affordable mental health resources for teens."},
    {"title": "Digital Divide in Rural Texas", "category": "Equity", "region": "South", "emoji": "📡", "desc": "Many students lack reliable internet for online learning."},
    {"title": "Plastic Pollution in Local Parks", "category": "Environment", "region": "West", "emoji": "♻️", "desc": "Single‑use plastics littering community green spaces."},
    {"title": "Youth Voter Registration", "category": "Civic", "region": "National", "emoji": "🗳️", "desc": "Low registration and turnout among 16‑18 year olds."},
    {"title": "Affordable Tutoring Gaps", "category": "Education", "region": "Urban", "emoji": "📚", "desc": "High cost of private tutoring widens achievement gap."},
    {"title": "Bike Lane Safety", "category": "Infrastructure", "region": "Northeast", "emoji": "🚲", "desc": "Dangerous intersections and lack of protected bike lanes."},
    {"title": "Fast Fashion Impact", "category": "Sustainability", "region": "Global", "emoji": "👕", "desc": "Encouraging clothing swaps and upcycling in schools."},
]

COMMUNITY_PROJECTS = [
    {"id": 1, "name": "Compost Crew", "issue": "School Lunch Waste", "impact": "Diverted 500 lbs of waste", "likes": 12, "author": "EcoWarriors"},
    {"id": 2, "name": "Mindful Mornings", "issue": "Teen Mental Health", "impact": "100+ students attended workshops", "likes": 27, "author": "WellnessClub"},
    {"id": 3, "name": "Hotspot Helpers", "issue": "Digital Divide", "impact": "Provided 30 mobile hotspots", "likes": 19, "author": "Tech4All"},
]

def get_issues():
    return ISSUES

def get_community_projects():
    return COMMUNITY_PROJECTS
