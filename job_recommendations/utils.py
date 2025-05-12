from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from jobs.models import Job


def get_skill_text(skills):
    """Convert skill objects to a space-separated string of skill names."""
    return ' '.join([skill.name.lower() for skill in skills])


def get_profile_text(student_profile):
    """Create a text representation of a student profile."""
    skills_text = get_skill_text(student_profile.skills.all())
    
    cgpa = float(student_profile.cgpa)
    cgpa_text = ""
    if cgpa >= 9.0:
        cgpa_text = "excellent cgpa"
    elif cgpa >= 8.0:
        cgpa_text = "very good cgpa"
    elif cgpa >= 7.0:
        cgpa_text = "good cgpa"
    elif cgpa >= 6.0:
        cgpa_text = "average cgpa"
    else:
        cgpa_text = "below average cgpa"
    
    profile_text = f"{skills_text} {cgpa_text}"
    
    return profile_text


def get_job_text(job):
    """Create a text representation of a job."""
    skills_text = get_skill_text(job.required_skills.all())
    
    job_text = f"{job.title.lower()} {skills_text}"
    
    return job_text


def recommend_jobs_tfidf(student_profile, top_n=10):
    """Recommend jobs using TF-IDF and linear kernel."""
    jobs = Job.objects.order_by('-created_at')[:100]
    
    if not jobs:
        return []
    
    job_texts = [get_job_text(job) for job in jobs]
    
    profile_text = get_profile_text(student_profile)
    all_texts = [profile_text] + job_texts
    
    tfidf_vectorizer = TfidfVectorizer(
        analyzer='word',
        token_pattern=r'\b\w+\b',  # Consider complete words only
        min_df=0.0,  # Include all terms, even if they appear in only one document
        stop_words='english',  # Remove English stop words
        sublinear_tf=True,  # Apply sublinear tf scaling (logarithmic)
        ngram_range=(1, 2)  # Include both unigrams and bigrams for better feature representation
    )
    
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)
    
    cosine_similarities = linear_kernel(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    job_score_pairs = list(zip(jobs, cosine_similarities))
    
    recommendations = sorted(job_score_pairs, key=lambda x: x[1], reverse=True)
    
    return recommendations[:top_n]