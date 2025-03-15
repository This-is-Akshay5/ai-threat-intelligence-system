document.getElementById('analyzeBtn').addEventListener('click', () => {
    let url = document.getElementById('urlInput').value.trim();

    if (!url) {
        alert("Please enter a URL!");
        return;
    }

    fetch('https://ai-threat-intelligence-system.onrender.com/analyze', {  // Ensure this matches your backend URL
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to analyze URL.");
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('resultContainer').classList.remove('hidden');
        document.getElementById('urlOutput').innerText = url;
        document.getElementById('threatScore').innerText = data.threat_score;

        let threatLevel;
        if (data.threat_score <= 20) {
            threatLevel = "Low";
        } else if (data.threat_score <= 50) {
            threatLevel = "Moderate";
        } else {
            threatLevel = "High";
        }

        document.getElementById('threatLevel').innerText = threatLevel;
    })
    .catch(error => {
        alert("Error analyzing URL! Please check your backend.");
        console.error(error);
    });
});
