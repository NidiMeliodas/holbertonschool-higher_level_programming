async function getName() {
  const reposnse = await fetch("https://swapi-api.hbtn.io/api/people/4/?format=json")
  const data = await reposnse.json()
  document.getElementById("character").textContent = data.name;
}
getName()