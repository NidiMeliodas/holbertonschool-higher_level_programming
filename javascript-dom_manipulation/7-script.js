async function getMovies(){
  const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
  const data = await response.json();

  let myMovieList = document.getElementById("list_movies");

  for (const movie of data.results) {
    let newListItem = document.createElement("li");
    newListItem.textContent = movie.title;
    myMovieList.appendChild(newListItem);
  }
}
getMovies();