//const goToNewPage=()=>{
//        var url = document.getElementById('list').value;
  //      const clicked = document.querySelector('#clicked');
    //    clicked.addEventListener('click', (event) =>{
      //  window.location.assign(url);
        //});
//}
function goToNewPage()
   {
       var url = document.getElementById('list').value;
       if(url != 'none') {
           window.location = url;
       }
   }
