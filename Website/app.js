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
  images.forEach(function(image,index) {
      // Calculate the opacity based on the scroll position and image index
      let opacity = Math.max(0, Math.min(1, (scrollPosition - (index * 300)) / 300));
      
      // Apply the opacity to the image
      image.style.opacity = opacity;


  });

  let elements = container.querySelectorAll('.animate');
  
  // Loop through each element
  elements.forEach(function(element, index) {
      // Calculate the opacity based on the scroll position and element index
      let opacity = Math.max(0, Math.min(1, (scrollPosition - (index * 150)) / 150));
      
      // Apply the opacity to the element
      element.style.opacity = opacity;
  });
});