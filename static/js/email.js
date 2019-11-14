function sendMail(contactForm) {
    emailjs.send("gmail", "template_MQ3tbSC5", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "description": contactForm.projectsummary.value,
        })
.then(
        function(response) {
            console.log("SUCCESS", response);
           
        },
        function(error) {
            console.log("FAILED", error);
            alert('Your message has not been sent');
            
        }
   );
           
}