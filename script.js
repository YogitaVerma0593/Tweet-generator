
document.getElementById("generate-tweet").addEventListener("click", function() {
    fetch('/generate_tweet')
        .then(response => response.json())
        .then(data => {
            let tweetContainer = document.getElementById("generated-tweet");
            tweetContainer.innerHTML = data.tweet;  // Display the new tweet
        })
        .catch(error => console.error('Error generating tweet:', error));
});
