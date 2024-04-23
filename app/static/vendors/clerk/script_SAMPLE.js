const publishableKey = ""; // <- Add Publishable Key here and then rename file to script.js

const startClerk = async () => {
    const Clerk = window.Clerk;

    try {
        // Load Clerk environment and session if available
        await Clerk.load();

        const userButton = document.getElementById("user-button");
        const authLinks = document.getElementById("auth-links");

        Clerk.addListener(({user}) => {
            // Display links conditionally based on user state
            authLinks.style.display = user ? "none" : "block";
        });

        if (Clerk.user) {
            // Mount user button component
            Clerk.mountUserButton(userButton);
            userButton.style.margin = "auto";
            console.log(Clerk.user);
            var welcome = document.getElementById("welcome-name");
            welcome.innerHTML = "Welcome, " + Clerk.user.firstName + "!";
            addUser();
            checkQuestionsRemaining(Clerk.user);
        }
    } catch (err) {
        console.error("Error starting Clerk: ", err);
    }
};

async function addUser() {
    var url = "/mongo?userid=" + Clerk.user.id +
        "&firstname=" + Clerk.user.firstName +
        "&lastname=" + Clerk.user.lastName +
        "&email=" + Clerk.user.primaryEmailAddress.emailAddress;

    console.log(url);

    try {
        let response = await fetch(url);
        let data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}

(() => {
    const script = document.createElement("script");
    script.setAttribute("data-clerk-publishable-key", publishableKey);
    script.async = true;
    script.src = `https://cdn.jsdelivr.net/npm/@clerk/clerk-js@latest/dist/clerk.browser.js`;
    script.crossOrigin = "anonymous";
    script.addEventListener("load", startClerk);
    script.addEventListener("error", () => {
        document.getElementById("no-frontend-api-warning").hidden = false;
    });
    document.body.appendChild(script);
})();