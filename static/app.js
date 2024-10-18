
const apiUrl = "http://127.0.0.1:8000";  // Replace with your backend URL

function balance() {
    fetch(`${apiUrl}/balance`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('balance').innerText = data.balance.toFixed(2);
        });
}

function deposit() {
    document.getElementById('input-area').style.display = 'block';
    document.getElementById('input-area').setAttribute('data-action', 'deposit');
}

function withdraw() {
    document.getElementById('input-area').style.display = 'block';
    document.getElementById('input-area').setAttribute('data-action', 'withdraw');
}

function submitAmount() {
    const amount = parseFloat(document.getElementById('amount').value);
    const action = document.getElementById('input-area').getAttribute('data-action');

    if (action === 'deposit') {
        deposit(amount);
    } else if (action === 'withdraw') {
        withdraw(amount);
    }
}

function deposit(amount) {
    fetch(`${apiUrl}/deposit`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ amount })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('balance').innerText = data.balance.toFixed(2);
        document.getElementById('input-area').style.display = 'none';
    });
}

function withdraw(amount) {
    fetch(`${apiUrl}/withdraw`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ amount })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('balance').innerText = data.balance.toFixed(2);
        document.getElementById('input-area').style.display = 'none';
    });
}
