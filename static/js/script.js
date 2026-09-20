document.addEventListener("DOMContentLoaded", () => {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = Number(counter.getAttribute("data-target"));

        let count = 0;

        const speed = target / 50;

        const updateCounter = () => {

            count += speed;

            if(count < target){

                counter.innerText = Math.floor(count);

                requestAnimationFrame(updateCounter);

            }
            else{

                counter.innerText = target;

            }

        };

        updateCounter();

    });

});