def calculate_threat_score(virustotal_score):
    if virustotal_score is None:
        return 50  # Neutral if API fails
    return min(100, virustotal_score * 10)  # Scale to 0-100
