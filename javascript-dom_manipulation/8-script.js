async function sayHello() {
  const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
  const data = await response.json();
  document.getElementById("hello").textContent = data.hello;
}
sayHello();