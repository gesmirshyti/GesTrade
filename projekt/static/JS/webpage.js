var nav = document.querySelector('nav');

      window.addEventListener('scroll', function () {
        if (window.pageYOffset > 100) {
          nav.classList.add('bg-dark', 'shadow');
        } else {
          nav.classList.remove('bg-dark', 'shadow');
        }
      });


function message(){
  var inputbox = document.getElementById('inputbox')
  // var email = document.getElementById('email')
  // var msg = document.getElementById('msg')
  const success = document.getElementById('success')
  const failed = document.getElementById('failed')

  if(inputbox.value === '' ){
    failed.style.display = 'block';
  }
else{
  setTimeout(() => {
    inputbox.value = '';
    // email.value = '';
    // msg.value = '';
    
},2000);
success.style.display = 'block';
}
}
