function toggleDropdown() {
    var dropdownContent = document.getElementById("myDropdown");
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
}  

window.addEventListener('scroll', function() {
  // Calculate the scroll position
  let scrollPosition = window.scrollY;
  
  // Get the image container
  let container = document.querySelector('.image-container');
  
  // Get all the images within the container
  let images = container.querySelectorAll('img');
  
  // Loop through each image
  images.forEach(function(image, index) {
    // Calculate the animation speed based on the screen width
    let animationSpeed = (window.innerWidth < 768) ? 100 : 200;

    // Calculate the opacity based on the scroll position and image index
    let opacity = Math.max(0, Math.min(1, (scrollPosition - (index * animationSpeed)) / animationSpeed));
    
    // Apply the opacity to the image
    image.style.opacity = opacity;
  });
});