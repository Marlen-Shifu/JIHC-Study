//NAVBAR JS START
const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");
const optionsList = document.querySelectorAll(".option");
const navbarSignUp = document.querySelector(".navbar_register-sign-up")
const navbarRegister = document.querySelector(".navbar_register-registration")
const registerEffect = document.querySelector(".register_effect");
const registerTabsLinks = document.querySelectorAll(".register_tabs a");
const registerPanels = document.querySelectorAll(".register_panel");
const navbarExitBtn = document.querySelector(".navbar_exit-btn");
const navbarTitle = document.querySelector(".navbar_title-link")
const navbarTitleSpan = document.querySelector(".navbar_span-title")
const headerRegister = document.querySelector(".header_register_registration")

//курсы start
selected.addEventListener("click", () => {
    optionsContainer.classList.toggle("active");
    selected.classList.toggle("active");
});


optionsList.forEach(o => {
    o.addEventListener("click", ( ) => {
        selected.innerHTML = o.querySelector("label").innerHTML;
        optionsContainer.classList.remove("active");   
    });
});

//курсы end

//войти start


navbarSignUp.addEventListener("click", () => {
    registerEffect.classList.toggle("blur_effect-active");
    registerEffect.classList.toggle("active");
    navbarExitBtn.classList.toggle("active");
    navbarTitle.classList.toggle("active");
    navbarTitleSpan.classList.toggle("active");
    document.body.style.overflow = "hidden";
});

//войти end

//регистрация start
navbarRegister.addEventListener("click", () => {
    registerEffect.classList.toggle("blur_effect-active");
    registerEffect.classList.toggle("active");
    navbarExitBtn.classList.toggle("active");
    navbarTitle.classList.toggle("active");
    navbarTitleSpan.classList.toggle("active");
    document.body.style.overflow = "hidden";
});
//регистрация end

//exit btn start
navbarExitBtn.addEventListener("click", () => {
    registerEffect.classList.remove("blur_effect-active");
    registerEffect.classList.remove("active");
    navbarExitBtn.classList.remove("active");
    navbarTitle.classList.toggle("active");
    navbarTitleSpan.classList.toggle("active");
    document.body.style.overflow = "visible";
})

//exit btn end

//Войти Регистрация modal window start

for (let el of registerTabsLinks) {
    el.addEventListener("click", e => {
      e.preventDefault();
  
      document.querySelector(".register_tabs li.register_active").classList.remove("register_active");
      document.querySelector(".register_panel.active").classList.remove("active");
  
      const parentListItem = el.parentElement;
      parentListItem.classList.add("register_active");
      const index = [...parentListItem.parentElement.children].indexOf(parentListItem);
  
      const panel = [...registerPanels].filter(el => el.getAttribute("data-index") == index);
      panel[0].classList.add("active");
      });
    }
//Войти Регистрация modal window end

//header "Присоединиться" btn start
headerRegister.addEventListener("click", () => {
        registerEffect.classList.toggle("blur_effect-active");
        registerEffect.classList.toggle("active");
        navbarExitBtn.classList.toggle("active");
        navbarTitle.classList.toggle("active");
        navbarTitleSpan.classList.toggle("active");
        document.body.style.overflow = "hidden";
})    
//header "Присоединиться" btn end

//burger осы жакта туру керек обязательно!!!!!!!!!!!!!!!!!!!!!!!!!!
(function() {
    const burgerItem = document.querySelector('.burger');
    const menu = document.querySelector('.navbar_content');
    const menuCloseItem = document.querySelector('.header__nav-close');
    burgerItem.addEventListener('click', () => {
        menu.classList.add('header__nav_active');
        document.body.style.overflow = 'hidden'
    });
    menuCloseItem.addEventListener('click', () => {
        menu.classList.remove('header__nav_active');
        document.body.style.overflow = 'visible'
    });
}());

//burger end 

//NAVBAR JS END