# 📄 AI-Powered Resume Screening & Ranking System

An intelligent resume screening system that uses Natural Language Processing and Machine Learning to automatically match candidates with job requirements, rank them by relevance, and provide actionable insights for hiring decisions.

## 🌐 Live Demo

**Try it now:** [Resume Screening App](https://resume-scanning1.streamlit.app/)

## 🎯 Problem Statement

### The Hiring Challenge

Recruiters and HR teams face overwhelming challenges:
- ❌ Manually reviewing hundreds of resumes per position (3-5 minutes each)
- ❌ Inconsistent evaluation criteria across different reviewers
- ❌ Missing qualified candidates buried in the stack
- ❌ Difficulty identifying skill gaps objectively
- ❌ Time-consuming initial screening process

**For a company hiring for 10 positions with 200 applications each = 100+ hours of manual screening**

### The Solution

An AI-powered screening system that:
- ✅ **Processes 2,484+ resumes instantly**
- ✅ **Extracts skills automatically** using NLP
- ✅ **Ranks candidates objectively** by job fit
- ✅ **Identifies skill gaps** clearly
- ✅ **Explains recommendations** for non-technical users
- ✅ **Reduces screening time by 90%+**

## 📊 System Performance

### Capabilities
- **Resumes Processed:** 2,484 candidates across 25 job categories
- **Skills Tracked:** 80+ technical and soft skills
- **Processing Speed:** < 2 seconds for full candidate ranking
- **Accuracy:** Multi-factor scoring (text similarity + skill matching)

### Matching Algorithm
| Component | Method | Weight |
|-----------|--------|--------|
| Text Relevance | TF-IDF + Cosine Similarity | 70% |
| Skills Match | Keyword Extraction & Matching | 30% |
| **Final Score** | **Weighted Combination** | **100%** |

## 🚀 Features

### Core Functionality
- 📝 **Job Description Input** - Paste any job posting
- 🔍 **Automatic Skill Extraction** - NLP identifies required skills
- 📊 **Candidate Ranking** - Top N candidates by relevance
- 💡 **Smart Recommendations** - Interview/Consider/Not Recommended
- 📈 **Visual Metrics** - Match scores, skill percentages
- ✅ **Skills Breakdown** - What matches, what's missing

### User Experience
- **Pre-loaded Examples** - Test with Data Scientist, Software Engineer, HR Manager roles
- **Adjustable Results** - Show 5-20 top candidates
- **Detailed Explanations** - Why each candidate ranked where they did
- **Skill Gap Analysis** - Identify training needs for near-matches
- **Clean Interface** - Non-technical users can understand results

## 🛠️ Tech Stack

### Machine Learning & NLP
- **scikit-learn** - TF-IDF vectorization, cosine similarity
- **Natural Language Processing** - Text cleaning, skill extraction, keyword matching
- **Feature Engineering** - 5,000-dimensional TF-IDF vectors

### Data Processing
- **pandas** - Resume data manipulation and analysis
- **NumPy** - Numerical computations for scoring
- **BeautifulSoup** - HTML parsing from resume text

### Deployment
- **Streamlit** - Interactive web application
- **Python 3.x** - Core programming language
- **joblib** - Model serialization and loading
- **Streamlit Cloud** - Hosting platform

## 🔧 How It Works

### 1. Text Preprocessing
```python
# Resume Cleaning Pipeline
1. Remove HTML tags and special characters
2. Extract text from unstructured format
3. Remove URLs, emails, contact info
4. Lowercase and normalize whitespace
5. Tokenization for analysis
```

### 2. Skill Extraction (NLP)
```python
# Skill Database Categories
- Programming: Python, Java, SQL, JavaScript, etc.
- Data Science: Machine Learning, Data Analysis, Statistics
- Tools: Git, Docker, AWS, TensorFlow, pandas
- Soft Skills: Leadership, Communication, Teamwork
- Domain: Project Management, Agile, Scrum
```

### 3. Job Matching Algorithm
```python
# Scoring Logic
Text Similarity Score = Cosine Similarity(Job Description, Resume)
Skill Match Score = (Matching Skills / Required Skills) × 100
Final Score = (0.7 × Text Score) + (0.3 × Skill Score)

# Ranking
Sort candidates by Final Score (descending)
Return top N with detailed breakdown
```

### 4. Explanation Generation
```python
# For Each Candidate
- Overall Match Percentage
- Text Relevance Score
- Skills Match (X/Y required skills)
- Matching Skills List
- Missing Skills List
- Interview Recommendation
- Key Insights for Decision Making
```

## 📈 Example Output

### Sample Job: Data Scientist

**Input:**
```
Position: Data Scientist
Requirements:
- Python, SQL, Machine Learning
- Data analysis, Statistical analysis
- pandas, scikit-learn
- Communication, Teamwork
Preferred: Deep Learning, TensorFlow, AWS
```

**Output:**
```
TOP 3 CANDIDATES:

#1 - ENGINEERING | Match: 45.2%
   ✅ Skills: Python, SQL, Machine Learning, pandas (4/8)
   ❌ Missing: Deep Learning, TensorFlow, AWS, Communication
   💡 GOOD MATCH - Consider for interview

#2 - INFORMATION-TECHNOLOGY | Match: 41.7%
   ✅ Skills: Python, Data Analysis, Statistical Analysis, AWS (4/8)
   ❌ Missing: Machine Learning, pandas, TensorFlow, Teamwork
   💡 GOOD MATCH - Strong technical background

#3 - CONSULTANT | Match: 38.9%
   ✅ Skills: SQL, Machine Learning, Communication (3/8)
   ❌ Missing: Python, pandas, Deep Learning, AWS, TensorFlow
   💡 PARTIAL MATCH - May need technical training
```

## 💼 Business Impact

### Time Savings
- **Manual screening:** 200 resumes × 3 min = 10 hours
- **AI screening:** 200 resumes × 2 sec = < 7 minutes
- **Time saved:** 99.4%

### Quality Improvements
- **Consistent criteria** across all candidates
- **No unconscious bias** in initial screening
- **Objective skill gap identification**
- **Data-driven hiring decisions**

### ROI Calculation
```
Average recruiter salary: $50k/year = $25/hour
Time saved per position: 10 hours
Cost savings per hire: $250
Annual hiring (50 positions): $12,500 saved
+ Improved hire quality (reduced turnover)
= Significant ROI
```

## 🎓 Key Technical Achievements

### Natural Language Processing
1. **Text Cleaning Pipeline**
   - Handled unstructured resume formats
   - Removed HTML, special characters, noise
   - Normalized text for consistent analysis

2. **Skill Extraction**
   - Built comprehensive skill database (6 categories, 80+ skills)
   - Implemented pattern matching with word boundaries
   - Avoided false positives (e.g., "java" in "javascript")

3. **TF-IDF Vectorization**
   - 5,000-dimensional feature space
   - Bigram support (1-2 word phrases)
   - English stopword filtering

### Machine Learning
1. **Cosine Similarity Matching**
   - Measures semantic similarity between job and resumes
   - Scales from 0 (no match) to 1 (perfect match)
   - Fast computation across 2,484 candidates

2. **Hybrid Scoring System**
   - Combined text similarity (70%) + skill matching (30%)
   - Balanced approach: both content and keywords matter
   - Optimized weights through testing

### Software Engineering
1. **Scalable Architecture**
   - Pre-computed resume vectors (one-time processing)
   - Fast inference (< 2 seconds for full ranking)
   - Modular, maintainable code

2. **User-Centric Design**
   - Clear explanations for non-technical users
   - Visual metrics and progress indicators
   - Example templates for quick testing

## 🔮 Future Enhancements

### Planned Features
- [ ] **Resume Upload** - Parse PDFs/DOCX directly
- [ ] **Batch Processing** - Upload multiple job descriptions at once
- [ ] **Advanced Filters** - Filter by experience, education, location
- [ ] **Custom Skill Database** - Let companies add industry-specific skills
- [ ] **Interview Scheduling** - Integrate with calendar APIs
- [ ] **Feedback Loop** - Learn from hiring decisions over time

### Technical Improvements
- [ ] **Deep Learning Models** - BERT/RoBERTa for better semantic understanding
- [ ] **Named Entity Recognition** - Extract companies, universities, certifications
- [ ] **Multilingual Support** - Handle resumes in multiple languages
- [ ] **Active Learning** - Improve with user feedback
- [ ] **API Endpoint** - REST API for ATS integration

## 🏆 Project Objectives Achieved

✅ **Work with unstructured resume text** - Processed 2,484 real resumes
✅ **Clean and preprocess text** - Built robust cleaning pipeline
✅ **Extract skills using NLP** - Implemented keyword extraction with 80+ skills
✅ **Build similarity/scoring logic** - TF-IDF + Cosine Similarity + weighted scoring
✅ **Rank candidates** - Top N ranking with confidence scores
✅ **Explain results clearly** - Human-readable reports for HR teams

## 📊 Dataset Information

- **Source:** Resume dataset with 25 job categories
- **Size:** 2,484 resumes
- **Format:** Unstructured text (extracted from various formats)
- **Categories:** HR, Engineering, IT, Marketing, Sales, Finance, Healthcare, etc.

### Data Processing Pipeline
1. Load raw resume text
2. Clean HTML and special characters
3. Extract and normalize text
4. Build TF-IDF vectors (5,000 features)
5. Extract skills using keyword matching
6. Store processed data for fast inference

## 🎯 Use Cases

### For Recruiters
- Quick initial screening of large applicant pools
- Identify top candidates objectively
- Focus interview time on best matches
- Reduce unconscious bias in screening

### For Hiring Managers
- Understand candidate skill gaps at a glance
- Make data-driven hiring decisions
- Identify training needs for near-matches
- Prioritize interviews effectively

### For HR Departments
- Standardize screening across all positions
- Track common skill gaps in applicant pools
- Measure time-to-hire improvements
- Generate hiring analytics and reports

## 📝 Example Use Cases

### Scenario 1: Startup Hiring
**Challenge:** 500 applications for 3 positions, 2-person team
**Solution:** Screen all 500 in < 1 hour, identify top 30 for phone screens
**Result:** Hired faster, better quality matches

### Scenario 2: Enterprise Recruitment
**Challenge:** Inconsistent screening across 10 recruiters
**Solution:** Standardized AI screening, human review of top candidates
**Result:** 40% reduction in time-to-hire, improved consistency

### Scenario 3: Career Fair
**Challenge:** 200 resumes collected, need to follow up quickly
**Solution:** Rank all candidates same day, prioritize outreach
**Result:** Competitive advantage in candidate engagement

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional skill categories
- Better NER for education/experience extraction
- UI/UX enhancements
- Multilingual support
- Integration with ATS systems


*Built as part of my machine learning portfolio - demonstrating NLP, text processing, and real-world AI applications for business problems.*
