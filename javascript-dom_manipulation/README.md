# JavaScript DOM Manipulation

** Learning Objectives **

 I've accomplished the following:

- I've learned how to select HTML elements using JavaScript and understand the differences between ID, class, and tag name selectors.
- I now know how to alter an HTML element's style, update its content, and modify the DOM itself.
- I've mastered making requests using both XmlHTTPRequest and the Fetch API.
- I've become proficient in listening to and binding both DOM and user events.

---

## Tasks

---

### 0. Update Text Color
**Filename**: `0-script.js`

**Description**:
  - JavaScript script that updates the text color of the header element to red (#FF0000) that uses `document.querySelector` to select the HTML tag.

---

---

### 1. Click and turn red
**Filename**: `1-script.js`

**Description**:
  - JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id `red_header`.

---

---

### 2. Add `.red` class
**Filename**: `2-script.js`

**Description**:
  - JavaScript script that adds the class `red` to the header element when the user clicks on the tag with id `red_header`.

---

---

### 3. Toggle classes
**Filename**: `3-script.js`

**Description**:
  - JavaScript script that toggles the class of the header element when the user clicks on the tag with id `toggle_header`.
  - The header element must always have one class: either `red` or `green`, but never both simultaneously and never be without a class. If the current class is `red`, when the user clicks on the `toggle_header` element, the class must change to `green`, and

---

---

### 4. List of elements
**Filename**: `4-script.js`

**Description**:
  - JavaScript script that adds a `li` element to a list when the user clicks on the tag with id `add_item`.
  - The new element should be: `<li>Item</li>`. This new element should be added to the `ul` element with class `my_list`.

---

---

### 5. Change the text
**Filename**: `5-script.js`

**Description**:
  - JavaScript script that updates the text of the header element to "New Header!!!" when the user clicks on the tag with id `update_header`.

---

---

### 6. Star Wars character
**Filename**: `6-script.js`

**Description**:
  - JavaScript script that fetches the character name from the URL: [https://swapi-api.hbtn.io/api/people/5/?format=json](https://swapi-api.hbtn.io/api/people/5/?format=json).
  - The name must be displayed in the HTML tag with id `character`.
  - The script should use the Fetch API.
  - Note: It's advisable to read more about using Promises.

---

---

### 7. Star Wars movies
**Filename**: `7-script.js`

**Description**:
  - JavaScript script that fetches and lists the titles of all movies from the URL: [https://swapi-api.hbtn.io/api/films/?format=json](https://swapi-api.hbtn.io/api/films/?format=json).
  - All movie titles should be listed in the HTML `ul` element with id `list_movies`.
  - The script should utilize the Fetch API.

---

---

### 8. Say Hello!
**Filename**: `8-script.js`

**Description**:
  - JavaScript script that fetches from [https://hellosalut.stefanbohacek.dev/?lang=fr](https://hellosalut.stefanbohacek.dev/?lang=fr) and displays the value of "hello" from that fetch in the HTML element with id `hello`.
  - The translation of "hello" should be displayed in the HTML tag with id `hello`.
  - The script should function correctly when it's imported from the `<head>` tag.

---
