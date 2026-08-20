const imageInput = document.getElementById("imageInput");
const previewContainer = document.getElementById("previewContainer");
const previewImage = document.getElementById("previewImage");
const removeButton = document.getElementById("removeButton");
const diagnoseButton = document.getElementById("diagnoseButton");
const loading = document.getElementById("loading");
const resultCard = document.getElementById("resultCard");
const resultTitle = document.getElementById("resultTitle");
const resultText = document.getElementById("resultText");
const uploadArea = document.getElementById("uploadArea");


/* IMAGE SELECTION */

imageInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) {
        return;
    }

    if (!file.type.startsWith("image/")) {
        alert("Please select a valid image.");
        return;
    }

    const reader = new FileReader();

    reader.onload = function (event) {

        previewImage.src = event.target.result;

        previewContainer.style.display = "block";

        resultCard.style.display = "none";
    };

    reader.readAsDataURL(file);

});


/* REMOVE IMAGE */

removeButton.addEventListener("click", function () {

    imageInput.value = "";

    previewImage.src = "";

    previewContainer.style.display = "none";

    resultCard.style.display = "none";

});


/* DRAG AND DROP */

uploadArea.addEventListener("dragover", function (event) {

    event.preventDefault();

    uploadArea.style.borderColor = "#08a657";

});


uploadArea.addEventListener("dragleave", function () {

    uploadArea.style.borderColor = "#77d9a1";

});


uploadArea.addEventListener("drop", function (event) {

    event.preventDefault();

    const file = event.dataTransfer.files[0];

    if (!file || !file.type.startsWith("image/")) {

        alert("Please drop a valid image.");

        return;
    }

    imageInput.files = event.dataTransfer.files;

    const reader = new FileReader();

    reader.onload = function (e) {

        previewImage.src = e.target.result;

        previewContainer.style.display = "block";

        resultCard.style.display = "none";

    };

    reader.readAsDataURL(file);

});


/* DIAGNOSE */

/* DIAGNOSE */

diagnoseButton.addEventListener("click", async function () {

    const file = imageInput.files[0];

    if (!file) {
        alert("🌱 Please choose a plant image first.");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    diagnoseButton.disabled = true;
    loading.style.display = "block";
    resultCard.style.display = "none";

    try {

        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        loading.style.display = "none";
        resultCard.style.display = "block";

        if (!response.ok) {
            throw new Error(data.error || "Prediction failed");
        }

        resultTitle.innerHTML =
            "🌿 " + data.prediction;

        resultText.innerHTML = `
            <strong>🌱 Plant:</strong> ${data.plant}<br><br>

            <strong>🦠 Disease:</strong> ${data.prediction}<br><br>

            <strong>📊 Confidence:</strong> ${data.confidence}%<br><br>

            <strong>💡 Recommendation:</strong><br>
            ${data.recommendation}
        `;

    } catch (error) {

        loading.style.display = "none";
        resultCard.style.display = "block";

        resultTitle.innerHTML =
            "⚠️ Unable to Analyze";

        resultText.innerHTML =
            "Something went wrong while analyzing the image.";

        console.error("Prediction error:", error);

    }

    diagnoseButton.disabled = false;

});