function enlargeImage(img) {
   const currentSrc = img.src;
   const modal = document.createElement('div');
   const modalImg = document.createElement('img');
   modalImg.src = currentSrc;
   modalImg.style.maxWidth = '90%';
   modalImg.style.maxHeight = '90%';
   modal.style.position = 'fixed';
   modal.style.top = '50%';
   modal.style.left = '50%';
   modal.style.transform = 'translate(-50%, -50%)';
   modal.style.justifyContent = 'center';
   modal.style.cursor = 'pointer';

   modal.appendChild(modalImg);
   document.body.appendChild(modal);

   modal.addEventListener('click', () => {
     modal.remove();
   });
}