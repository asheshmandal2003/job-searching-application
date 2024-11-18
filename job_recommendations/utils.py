import numpy as np
from sklearn.neighbors import NearestNeighbors
from jobs.models import Job

def encode_features(student_profile, jobs):
    all_skills = set(skill.id for job in jobs for skill in job.required_skills.all())
    all_skills.update(skill.id for skill in student_profile.skills.all())
    skill_encoder = {skill_id: idx for idx, skill_id in enumerate(all_skills)}

    def encode_skills(skills):
        skill_vector = np.zeros(len(skill_encoder))
        for skill in skills:
            skill_vector[skill_encoder[skill.id]] = 1
        return skill_vector

    student_vector = np.concatenate([
        encode_skills(student_profile.skills.all()),  
        [float(student_profile.cgpa)],       
    ])

    job_vectors = []
    job_objects = []
    for job in jobs:
        job_vector = np.concatenate([
            encode_skills(job.required_skills.all()),  
            [0],
        ])
        job_vectors.append(job_vector)
        job_objects.append(job)

    return student_vector, np.array(job_vectors), job_objects



def recommend_jobs_knn(student_profile, n_neighbors=10):
    jobs = Job.objects.order_by('created_at')[:50]

    student_vector, job_vectors, job_objects = encode_features(student_profile, jobs)

    knn = NearestNeighbors(n_neighbors=n_neighbors, metric='cosine')
    knn.fit(job_vectors)

    distances, indices = knn.kneighbors([student_vector])

    recommendations = [(job_objects[idx], 1 - distances[0][i]) for i, idx in enumerate(indices[0])]
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations
