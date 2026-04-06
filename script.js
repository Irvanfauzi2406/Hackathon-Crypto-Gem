const BASE_URL = "http://localhost:8000";

async function getPrice() {
  const res = await fetch("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT");
  const data = await res.json();
  document.getElementById("price").innerText = "$" + parseFloat(data.price).toFixed(2);
}

async function getSignal() {
  const res = await fetch(`${BASE_URL}/signal`);
  const data = await res.json();

  document.getElementById("signal").innerText = data.signal;
  document.getElementById("confidence").innerText = data.confidence;
}

async function getWhale() {
  const res = await fetch(`${BASE_URL}/whale`);
  const data = await res.json();

  document.getElementById("whale").innerText =
    `${data.type} | $${data.amount}`;
}

async function toggleAuto() {
  const res = await fetch(`${BASE_URL}/toggle`);
  const data = await res.json();

  document.getElementById("autoStatus").innerText =
    data.auto_trade ? "ON" : "OFF";
}

async function getLeaderboard() {
  const res = await fetch(`${BASE_URL}/leaderboard`);
  const data = await res.json();

  let html = "";
  data.forEach((u, i) => {
    html += `${i+1}. ${u.name} - ${u.score}%<br>`;
  });

  document.getElementById("leaderboard").innerHTML = html;
}

async function executeTrade() {
  await fetch(`${BASE_URL}/execute`);
  alert("Trade executed!");
}

setInterval(() => {
  getPrice();
  getSignal();
  getWhale();
  getLeaderboard();
}, 5000);
