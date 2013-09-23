function Subscriber(){
   
   var e_mail  = document.news_letter_form.e_mail.value;
   //check network connection
   if(window.navigator.onLine )
   {
    if ( e_mail != "" )
    {
     document.getElementById('news_letter_res').innerHTML = "<img src='/static/images/Loader.gif'/>";
    var xmlhttp;
    if (window.XMLHttpRequest)
      {
         xmlhttp=new XMLHttpRequest();
               }
    else
      {
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
         
      }
    xmlhttp.onreadystatechange=function()
      {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {

                //reset the form
                document.getElementById('news_letter_form').reset();
                //return the connect method
                document.getElementById('news_letter_res').innerHTML=xmlhttp.responseText;
            }
          
      }
        xmlhttp.open("GET",'/news_letter/?e_mail='+e_mail,true);
        xmlhttp.send();

    
    }
    else
    {
    //return the connect method
    document.getElementById('news_letter_res').innerHTML= "The email must be filled!!";   
    return false;
    
    }
   }
   else
   {
     document.getElementById('news_letter_res').innerHTML = "<img src='/static/images/Loader.gif'/>";
    //return the connect method
     setTimeout(function(){
            document.getElementById('news_letter_res').innerHTML= "No internet connection available.";   
                       }, 3000);
    return false;
   }


}

