// alert
function alertPopup(id, title, text) {
    Swal.fire({
        title: title,
        text: text,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            if (id === '') {
                fetchMethod(`/logout/`, 'GET', '', '')
            } else {
                fetchMethod(`/delete/${id}/`, 'DELETE', '', '')
            }
        }
    });
}

// Toast
function toast(icon, msg) {
    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: icon,
        title: msg,
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true
    });

}

function fetchMethod(url, method, csrftoken, jsonData) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    };

    if (method !== 'GET' && method !== 'HEAD') {
        options.body = JSON.stringify(jsonData);
    }

    fetch(url, options)
        .then((res) => res.json())
        .then((data) => {
            if (data.redirect) {
                toast('success', data.message);
                setTimeout(() => {
                    window.location.href = data.redirect;
                }, 3000)

            } else {
                toast('error', data.message);
            }
        })
        .catch((error) => toast('error', error));

}


document.addEventListener('DOMContentLoaded', function () {
    // LOGIN FORM HANDLING
    const loginFrm = document.getElementById('login-frm');
    if (loginFrm) {
        const togglePassword = document.getElementById("togglePassword");
        const passwordInput = document.getElementById("password");

        togglePassword.addEventListener("click", () => {
            const type =
                passwordInput.getAttribute("type") === "password"
                    ? "text"
                    : "password";
            passwordInput.setAttribute("type", type);
            togglePassword.classList.toggle("fa-eye");
            togglePassword.classList.toggle("fa-eye-slash");
        });

        document.addEventListener('submit', function (e) {
            e.preventDefault()

            const jsonData = {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value
            }

            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetchMethod('/login/', 'POST', csrftoken, jsonData)
        })
    }

    // UPDATE FORM HANDLING
    const updateFrm = document.getElementById('updateForm');
    if (updateFrm) {
        updateFrm.addEventListener('submit', function (e) {
            e.preventDefault();

            const id = document.getElementById("editId").value;

            const jsonData = {
                student_name: document.getElementById('editName').value,
                subject: document.getElementById('editSubject').value,
                marks: document.getElementById('editMark').value
            }

            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            fetchMethod(`/update/${id}/`, 'UPDATE', csrftoken, jsonData)
        });
    }

    // CREATE FORM HANDLING
    const createFrm = document.getElementById('createForm');
    if (createFrm) {

        createFrm.addEventListener('submit', function (e) {
            e.preventDefault();

            const jsonData = {
                student_name: document.getElementById('name').value,
                subject: document.getElementById('subject').value,
                marks: document.getElementById('mark').value
            }

            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            fetchMethod(`/add-student/`, 'POST', csrftoken, jsonData)
        });

    }

    // CREATE MODAL HANDLING
    const modal = document.getElementById("modal");
    const openModal = document.getElementById("openModal");
    const closeModal = document.getElementById("closeModal");

    openModal.addEventListener("click", () => {
        modal.style.display = "flex";
    });

    closeModal.addEventListener("click", () => {
        modal.style.display = "none";
    });

    window.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });

    // EDIT MODAL HANDLING
    const editModal = document.getElementById("editModal");
    const editOpenModal = document.getElementById("editOpenModal");
    const editCloseModal = document.getElementById("editCloseModal");

    document.querySelectorAll(".edit-button").forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault();

            const id = button.getAttribute("data-id");
            const name = button.getAttribute("data-name");
            const subject = button.getAttribute("data-subject");
            const mark = button.getAttribute("data-mark");

            document.getElementById("editId").value = id;
            document.getElementById("editName").value = name;
            document.getElementById("editSubject").value = subject;
            document.getElementById("editMark").value = mark;

            editModal.style.display = "flex";
        });
    });


    editCloseModal.addEventListener("click", () => {
        editModal.style.display = "none";
    });

    window.addEventListener("click", (e) => {
        if (e.target === editModal) {
            editModal.style.display = "none";
        }
    });
})