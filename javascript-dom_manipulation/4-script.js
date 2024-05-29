document.getElementById("add_item").addEventListener("click", addLi)

function addLi() {
  let newListItem = document.createElement("li");
  newListItem.textContent = "Item";
  let myList = document.querySelector(".my_list");
  myList.appendChild(newListItem);
}