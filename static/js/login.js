
let tabPanes = document.getElementsByClassName("headerlogin")[0].getElementsByTagName("div");

for(let i=0;i<tabPanes.length;i++){
  tabPanes[i].addEventListener("click",function(){
    document.getElementsByClassName("headerlogin")[0].getElementsByClassName("active")[0].classList.remove("active");
    tabPanes[i].classList.add("active");
    
    document.getElementsByClassName("loginblock")[0].getElementsByClassName("active")[0].classList.remove("active");
    document.getElementsByClassName("loginblock")[0].getElementsByClassName("loginbody")[i].classList.add("active");
  });
}

let sendbtn = document.getElementsByClassName("loginelement")[0].getElementsByTagName("div");

for(let i=0;i<tabPanes.length;i++){
  tabPanes[i].addEventListener("click",function(){
    document.getElementsByClassName("headerlogin")[0].getElementsByClassName("active")[0].classList.remove("active");
    tabPanes[i].classList.add("active");
    
    document.getElementsByClassName("loginblock")[0].getElementsByClassName("active")[0].classList.remove("active");
    document.getElementsByClassName("loginblock")[0].getElementsByClassName("loginbody")[i].classList.add("active");
  });
}