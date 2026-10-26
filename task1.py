
def allocate_scholarships(applicants, quota):
    eligible = []
    rejected = []

    for student in applicants:
        reasons = []

        if student["aggregate"] < 75:
            reasons.append("Aggregate below 75%")

        if any(mark < 60 for mark in student["subjects"]):
            reasons.append("Subject mark below 60%")

        if student["attendance"] < 85:
            reasons.append("Attendance below 85%")

        if student["income"] > 250000:
            reasons.append("Family income exceeds limit")

        if reasons:
            rejected.append({
                "student_id": student["student_id"],
                "reasons": reasons
            })
        else:
            eligible.append(student)

    # Higher academic performance and attendance first;
    # lower income preferred when previous criteria tie.
    eligible.sort(
        key=lambda s: (
            -s["aggregate"],
            -s["core_subject_score"],
            -s["attendance"],
            s["income"],
            s["student_id"]
        )
    )

    # Student ID provides a deterministic final ordering.
    # Use an approved random draw instead if policy requires it.
    selected = eligible[:max(0, quota)]

    return {
        "selected": selected,
        "waiting_list": eligible[max(0, quota):],
        "rejected": rejected
    }
