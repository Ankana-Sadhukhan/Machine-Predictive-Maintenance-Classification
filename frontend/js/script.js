async function predict() {

    const f1 = document.getElementById("f1").value;
    const f2 = document.getElementById("f2").value;

    const response = await fetch("http://127.0.0.1:5000/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            features: [f1, f2]
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        "Prediction: " + data.prediction;
}