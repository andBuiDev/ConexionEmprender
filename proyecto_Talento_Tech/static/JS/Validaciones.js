const validators = {
    nombres: (value) => /^([a-zA-ZÀ-ÿ]+|[a-zA-ZÀ-ÿ]+\s[a-zA-ZÀ-ÿ]+)$/.test(value),
    cedula: (value) => /^\d{7,11}$/.test(value),
    celular: (value) => /^3\d{2}\s?\d{3}(\s?\d{2}){2}$/.test(value),
    fecha_nacimiento: (value) => {
        const hoy = new Date();
        const fechaNacimiento = new Date(value);
        const edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
        return edad >= 18; // Verifica si es mayor de edad
    },
    contrasena: (value) => /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&\.])[A-Za-z\d@$!%*?&\.]{8,}$/.test(value),
    apellidos: (value) => /^([a-zA-ZÀ-ÿ]+\s[a-zA-ZÀ-ÿ]+)$/.test(value),
    nombre_usuario: (value) => /^[a-z0-9-_.]{5,15}$/.test(value),
    email: (value) => /^([a-zA-Z0-9]+[_\-.+%]?)+@([a-zA-Z0-9]+[_\-.]?)+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$/.test(value),
    direccion: (value) => /^(Calle|Cll|Carrera|Cra|Avenida|Av|Transversal|Tv|Diagonal|Dg)\s\d+[A-Z]{0,2}\s?(Bis)?\s?(Norte|Sur|Este|Oeste)?\s?#\s?\d+-\d+$/i.test(value),
    confirmar_contrasena: (value) => {
        const contrasena = document.getElementById("contrasena").value;
        return value === contrasena;
    }
};

function validateField(input, validator) {
    const value = input.value;
    const isValid = validator(value);
    const errorElement = input.nextElementSibling; // Accede al <p> de error

    if (value === "") {
        errorElement.style.display = "none"; // Oculta el mensaje si el campo está vacío
        input.style.borderBottom = "2px solid #00bfb2"; // Borde normal
    } else if (!isValid) {
        errorElement.style.display = "block"; // Muestra el mensaje de error
        input.style.borderBottom = "2px solid #ff0000"; // Borde de error
    } else {
        errorElement.style.display = "none"; // Oculta el mensaje si es válido
        input.style.borderBottom = "2px solid #00bfb2"; // Borde normal
    }
    return isValid && value !== "";
}


function validateAllFields() {
    const ids = [
        "nombres", "cedula", "celular", "fecha_nacimiento", "contrasena",
        "apellidos", "nombre_usuario", "email", "direccion", "confirmar_contrasena"
    ];

    let allValid = true; // Suponemos que todos los campos son válidos

    ids.forEach(id => {
        const input = document.getElementById(id);
        const validator = validators[id];
        const isValid = validateField(input, validator); // Valida el campo

        if (!isValid) {
            allValid = false; // Si algún campo no es válido, cambia a false
        }
    });

    return allValid; // Devuelve si todos los campos son válidos
}

function showSuccessMessage() {
    const successMessage = document.querySelector(".mensaje-exito");
    successMessage.style.display = "block"; // Muestra el mensaje de éxito

    // Oculta el mensaje después de 3 segundos
    setTimeout(() => {
        successMessage.style.display = "none";
    }, 3000); // 3000 milisegundos = 3 segundos
}

window.onload = function () {
    const ids = [
        "nombres", "cedula", "celular", "fecha_nacimiento", "contrasena",
        "apellidos", "nombre_usuario", "email", "direccion", "confirmar_contrasena"
    ];

    ids.forEach(id => {
        const input = document.getElementById(id);
        const validator = validators[id];

        input.addEventListener("input", () => {
            validateField(input, validator);
        });

        // Validación adicional para confirmar contraseña
        if (id === "confirmar_contrasena") {
            input.addEventListener("input", () => {
                const isValid = input.value === document.getElementById("contrasena").value;
                validateField(input, () => isValid);
            });
        }
    });

    // Validar todos los campos al presionar el botón "Registrarse"
    const registerButton = document.querySelector("#button-container button");
    registerButton.addEventListener("click", (e) => {
        e.preventDefault(); // Evita el envío del formulario

        const allFieldsValid = validateAllFields(); // Valida todos los campos

        if (allFieldsValid) {
            //showSuccessMessage(); // Muestra el mensaje de éxito
        window.location.href = "../html/log_in.html";
        }
    });

};
