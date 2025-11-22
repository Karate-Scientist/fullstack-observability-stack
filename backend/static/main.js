const baseURL = "http://localhost:5000";

// Load users on page load
window.onload = () => {
    loadUsers();
};

function loadUsers() {
    fetch(`${baseURL}/users`)
        .then(res => res.json())
        .then(data => {
            const table = document.querySelector("#userTable tbody");
            table.innerHTML = "";

            data.forEach(user => {
                let row = `
                    <tr>
                        <td>${user.id}</td>
                        <td><input id="name_${user.id}" value="${user.name}"></td>
                        <td><input id="email_${user.id}" value="${user.email}"></td>
                        <td>
                            <button onclick="updateUser(${user.id})">Update</button>
                            <button onclick="deleteUser(${user.id})">Delete</button>
                        </td>
                    </tr>
                `;
                table.innerHTML += row;
            });
        });
}

// ADD
function addUser() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    fetch(`${baseURL}/users`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, email})
    })
    .then(() => loadUsers());
}

// UPDATE
function updateUser(id) {
    const name = document.getElementById(`name_${id}`).value;
    const email = document.getElementById(`email_${id}`).value;

    fetch(`${baseURL}/users/${id}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, email})
    })
    .then(() => loadUsers());
}

// DELETE
function deleteUser(id) {
    fetch(`${baseURL}/users/${id}`, {
        method: "DELETE"
    })
    .then(() => loadUsers());
}
