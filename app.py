import streamlit as st
import pandas as pd
import joblib
import re
from bs4 import BeautifulSoup
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide"
)

# Load models and data
@st.cache_resource
def load_models():
    vectorizer = joblib.load('resume_vectorizer.pkl')
    resume_vectors = joblib.load('resume_vectors.pkl')
    resumes_df = pd.read_csv('processed_resumes.csv')
    skills_database = joblib.load('skills_database.pkl')
    all_skills = joblib.load('all_skills.pkl')
    return vectorizer, resume_vectors, resumes_df, skills_database, all_skills

vectorizer, resume_vectors, resumes_df, skills_database, all_skills = load_models()

# Clean text function
def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = text.lower()
    text = ' '.join(text.split())
    return text

# Extract skills function
def extract_skills(text):
    text_lower = text.lower()
    found_skills = []
    for skill in all_skills:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
    return found_skills

# Matching function
def match_resumes(job_description, top_n=10):
    job_clean = clean_text(job_description)
    job_skills = extract_skills(job_clean)
    job_vector = vectorizer.transform([job_clean])
    similarities = cosine_similarity(job_vector, resume_vectors)[0]
    
    results = resumes_df.copy()
    results['match_score'] = similarities * 100
    
    def calc_skill_match(candidate_skills_str):
        candidate_skills = eval(candidate_skills_str) if isinstance(candidate_skills_str, str) else []
        if len(job_skills) == 0:
            return 0, [], job_skills
        matching = [s for s in job_skills if s in candidate_skills]
        missing = [s for s in job_skills if s not in candidate_skills]
        match_pct = (len(matching) / len(job_skills)) * 100
        return match_pct, matching, missing
    
    results[['skill_match_pct', 'matching_skills', 'missing_skills']] = \
        results['extracted_skills'].apply(lambda x: pd.Series(calc_skill_match(x)))
    
    results['final_score'] = 0.7 * results['match_score'] + 0.3 * results['skill_match_pct']
    results = results.sort_values('final_score', ascending=False)
    
    return results.head(top_n), job_skills

# App Title
st.title('📄 AI-Powered Resume Screener')
st.markdown('Automatically rank candidates based on job requirements using NLP and Machine Learning')

st.markdown('---')

# Sidebar
st.sidebar.title('About')
st.sidebar.info(
    'This system uses Natural Language Processing to:\n\n'
    '• Extract skills from resumes\n'
    '• Match candidates to job descriptions\n'
    '• Rank by relevance\n'
    '• Identify skill gaps'
)

st.sidebar.markdown('---')
st.sidebar.subheader('System Stats')
st.sidebar.metric('Resumes in Database', f'{len(resumes_df):,}')
st.sidebar.metric('Skills Tracked', len(all_skills))
st.sidebar.metric('Categories', resumes_df['Category'].nunique())

st.sidebar.markdown('---')
st.sidebar.caption('Built by Eric')
st.sidebar.caption('[GitHub](https://github.com/e-ric79)')

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader('📝 Enter Job Description')
    
    # Example or custom
    input_type = st.radio('', ['Use Example', 'Enter Custom Job Description'])
    
    if input_type == 'Use Example':
        examples = {
            'Data Scientist': '''Data Scientist Position

Requirements:
- Python programming and data analysis
- Machine learning and statistical analysis
- SQL and database management
- Experience with pandas, scikit-learn
- Strong communication skills
- Teamwork and collaboration

Preferred:
- Deep learning, TensorFlow, PyTorch
- AWS or cloud experience''',
            
            'Software Engineer': '''Software Engineer Position

Requirements:
- Java or Python programming
- Web development experience
- SQL databases
- Git version control
- Problem solving skills
- Agile development

Preferred:
- React or Angular
- AWS experience
- Docker/Kubernetes''',
            
            'HR Manager': '''HR Manager Position

Requirements:
- Human resources management
- Leadership and communication
- Payroll and benefits administration
- Recruitment and talent acquisition
- Employee relations
- Analytical skills

Preferred:
- HRIS systems (Oracle, SAP)
- Project management'''
        }
        
        selected = st.selectbox('Select example:', list(examples.keys()))
        job_desc = st.text_area('Job Description:', value=examples[selected], height=300)
    else:
        job_desc = st.text_area(
            'Job Description:', 
            height=300,
            placeholder='Paste the job description here...\n\nExample:\nData Scientist needed with Python, ML, and SQL skills...'
        )

with col2:
    st.subheader('⚙️ Settings')
    top_n = st.slider('Number of candidates to show:', 5, 20, 10)
    
    st.markdown('---')
    
    st.info('**How it works:**\n\n'
            '1. Enter job requirements\n'
            '2. System analyzes 2,484 resumes\n'
            '3. Extracts & matches skills\n'
            '4. Ranks by relevance\n'
            '5. Shows top candidates with explanations')

# Match button
st.markdown('---')

if st.button('🔍 Find Best Candidates', type='primary', use_container_width=True):
    if job_desc and len(job_desc.strip()) > 50:
        with st.spinner('Analyzing resumes...'):
            top_candidates, required_skills = match_resumes(job_desc, top_n)
        
        st.success(f'✓ Found {len(top_candidates)} matching candidates!')
        
        # Show required skills
        st.subheader('📋 Required Skills Detected')
        if required_skills:
            cols = st.columns(4)
            for i, skill in enumerate(required_skills):
                cols[i % 4].markdown(f'`{skill}`')
        else:
            st.warning('No specific skills detected in job description')
        
        st.markdown('---')
        
        # Show top candidates
        st.subheader(f'🏆 Top {len(top_candidates)} Candidates')
        
        for idx, (_, row) in enumerate(top_candidates.iterrows(), 1):
            with st.expander(
                f"**#{idx} - {row['Category']}** | Match: {row['final_score']:.1f}% | "
                f"Skills: {row['skill_match_pct']:.0f}%"
            ):
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric('Overall Match', f"{row['final_score']:.1f}%")
                with col_b:
                    st.metric('Text Relevance', f"{row['match_score']:.1f}%")
                with col_c:
                    matching = eval(row['matching_skills']) if isinstance(row['matching_skills'], str) else []
                    missing = eval(row['missing_skills']) if isinstance(row['missing_skills'], str) else []
                    st.metric('Skills Match', f"{len(matching)}/{len(required_skills)}")
                
                # Recommendation
                score = row['final_score']
                if score >= 50:
                    st.success('✅ **STRONG MATCH** - Highly recommended for interview')
                elif score >= 35:
                    st.info('💡 **GOOD MATCH** - Consider for interview')
                elif score >= 20:
                    st.warning('⚠️ **PARTIAL MATCH** - May need training')
                else:
                    st.error('❌ **WEAK MATCH** - Not recommended')
                
                # Skills breakdown
                col_x, col_y = st.columns(2)
                
                with col_x:
                    st.markdown('**✅ Matching Skills:**')
                    if matching:
                        for skill in matching:
                            st.markdown(f'• {skill}')
                    else:
                        st.markdown('*None detected*')
                
                with col_y:
                    st.markdown('**❌ Missing Skills:**')
                    if missing:
                        for skill in missing[:5]:  # Show first 5
                            st.markdown(f'• {skill}')
                        if len(missing) > 5:
                            st.markdown(f'*...and {len(missing) - 5} more*')
                    else:
                        st.markdown('*None*')
                
                # Key insight
                st.markdown('---')
                st.markdown('**💡 Key Insight:**')
                insight = f"Candidate has {len(matching)}/{len(required_skills)} required skills. "
                if matching:
                    insight += f"Strong in: {', '.join(matching[:3])}. "
                if missing:
                    insight += f"Needs development in: {', '.join(missing[:3])}."
                st.markdown(insight)
        
    else:
        st.warning('⚠️ Please enter a job description (at least 50 characters)')

# Footer
st.markdown('---')
st.caption('AI Resume Screener | Powered by NLP & Machine Learning | 2,484 Resumes Analyzed')