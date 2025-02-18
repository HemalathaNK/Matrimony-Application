document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const passwordInput = document.querySelector('input[name="pswd"]');

    form.addEventListener("submit", function (event) {
        const password = passwordInput.value;

        // Password Validation Rules
        const minLength = 8;
        const maxLength = 16;
        const hasUppercase = /[A-Z]/.test(password);
        const hasLowercase = /[a-z]/.test(password);
        const hasNumber = /[0-9]/.test(password);
        const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

        if (
            password.length < minLength ||
            password.length > maxLength ||
            !hasUppercase ||
            !hasLowercase ||
            !hasNumber ||
            !hasSpecialChar
        ) {
            alert(
                `Password must meet the following requirements:\n` +
                    `- Between ${minLength}-${maxLength} characters\n` +
                    `- At least one uppercase letter\n` +
                    `- At least one lowercase letter\n` +
                    `- At least one number\n` +
                    `- At least one special character`
            );
            event.preventDefault();
        }
    });
});
