
            // main picture
            var picture = document.querySelector('#pic');

            // side pictures
            var picture1 = document.querySelector('#pic1');
            var picture2 = document.querySelector('#pic2');
            var picture3 = document.querySelector('#pic3');
            

            // Main picture container
            var mainContainer = document.querySelector('#picture');

            // selector
            var rect = document.querySelector("#rect");

            // Zoom window
            var zoom = document.querySelector('#zoom');

            // list of pictures 
            picList = [picture1, picture2, picture3]

            // Active side picture
            let picActive = 1;

            // Add a boxshodow to the first piture (Current active picture)
            picture1.classList.add('img-active');

            // change image 
            function changeImage(imgSrc, n) {
                // This will change the main image
                picture.src = imgSrc;
                // This will change the background image of the zoom window
                zoom.style.backgroundImage = "url(" + imgSrc + ")";
                // removing box shodow from the previous active side picture
                picList[picActive-1].classList.remove('img-active');
                // Add box shodow to active side picture
                picList[n-1].classList.add('img-active');
                // update the active side picture 
                picActive = n;
            }


            // Width and height of main picture in px
            let w1 = mainContainer.offsetWidth;
            let h1 = mainContainer.offsetHeight;

            // Zoom ratio
            let ratio = 3;

            // Zoom window background-image size
            zoom.style.backgroundSize = w1 * ratio + 'px ' + h1 * ratio + 'px';

            // Coordinates of mouse cursor
            let x, y, xx, yy;

            // Width and height of selector
            let w2 = rect.offsetWidth;
            let h2 = rect.offsetHeight;

            // zoom window width and height
            zoom.style.width = w2 * ratio + 'px';
            zoom.style.height = h2 * ratio + 'px';

            // half of selector shows outside the main picture
            // We need half of width and height
            w2 = w2/2;
            h2 = h2/2;
            // moving the selector box 
            function move(event) {
                // How far is the mouse cursor from an element
                // x how far the cursor from left of element
                x = event.offsetX;
                // y how far the cursor from the top of an element
                y = event.offsetY;

                xx = x - w2;
                yy = y - h2;
                // Keeping the selector inside the main picture
                // left of picture
                if (x < w2) {
                    x = w2;
                    // matching the zoom window with the selector
                    xx = 0;
                }
                // right of main picture
                if (x > w1 - w2) {
                    x = w1 - w2; 
                    xx = x - w2;
                }
                // top of main picture 
                if (y < h2) {
                    y = h2;
                    yy = 0;
                } 
                // bottom of main picture
                if (y > h1 - h2) {
                    y = h1 - h2;
                }

                xx = xx * ratio;
                yy = yy * ratio;
                // changing the position of the selector
                rect.style.left = x + 'px';
                rect.style.top = y + 'px';
                // changing background image of zoom window
                zoom.style.backgroundPosition = '-' + xx + 'px ' + '-' + yy + 'px';  
            }

            mainContainer.addEventListener('mousemove', function(){
                move(event);
                addOpacity();
            })

            // show selector
            // show zoom window
            function addOpacity() {
                rect.classList.add('rect-active'); 
                zoom.classList.add('rect-active');
            }

            // Hide the zoom window 
            function removeOpacity() {
                zoom.classList.remove('rect-active');
            }

            mainContainer.addEventListener('mouseout', function() {
                removeOpacity(); 
            })


            const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

    document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);
        