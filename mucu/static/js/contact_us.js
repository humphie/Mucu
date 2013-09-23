function contactUs(){
   
   var name    = document.contact_us.name.value;
   var e_mail  = document.contact_us.e_mail.value;
   var subject = document.contact_us.subject.value;
   var message = document.contact_us.message.value;   
   //check network connection
   if(window.navigator.onLine )
   {
    if (name !="" || e_mail != "" || subject != "" || message != "")
    {
     document.getElementById('response').innerHTML = "<img src='/static/images/Loader.gif'/>";
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
                document.getElementById('contact_us').reset();
                //return the connect method
                document.getElementById('response').innerHTML=xmlhttp.responseText;
            }
          
      }
        //data here
        data = "?name="+name +"&e_mail="+e_mail +"&subject="+subject +"&message="+message
        xmlhttp.open("GET",'/sendMail/'+data,true);
        xmlhttp.send();

    
    }
    else
    {
    //return the connect method
    document.getElementById('response').innerHTML= "All fields must be filled!!";   
    return false;
    
    }
   }
   else
   {
     document.getElementById('response').innerHTML = "<img src='/static/images/Loader.gif'/>";
    //return the connect method
     setTimeout(function(){
                     document.getElementById('response').innerHTML= "No internet connection available.";   
                       }, 3000);
    return false;
   }


}

