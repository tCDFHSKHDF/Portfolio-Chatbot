// Toggle popup
const toggleBtn = document.getElementById("chatbot-btn");
const chatWindow = document.getElementById("chatbot-window");
const messages = document.getElementById("chatbot-messages");
const input = document.getElementById("chat-input");
const sendBtn = document.getElementById("chat-send");

toggleBtn.addEventListener("click", () => {
  chatWindow.style.display = (chatWindow.style.display === "flex") ? "none" : "flex";
  if (chatWindow.style.display === "flex") {
    input.focus();
  }
});

// Send on button click
sendBtn.addEventListener("click", sendMessage);
// Send on Enter
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});

function addMessage(sender, text) {
  const div = document.createElement("div");
  div.className = `msg ${sender === "You" ? "you" : "bot"}`;
  div.innerHTML = `<strong>${sender}:</strong> ${escapeHtml(text)}`;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage() {
  const text = (input.value || "").trim();
  if (!text) return;

  addMessage("You", text);
  input.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });
    const data = await res.json();
    addMessage("Bot", data.reply ?? "Sorry, something went wrong.");
  } catch (err) {
    addMessage("Bot", "Network error. Please try again.");
  }
}

function escapeHtml(str) {
  return str.replace(/[&<>"']/g, s => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;"
  }[s]));
}
