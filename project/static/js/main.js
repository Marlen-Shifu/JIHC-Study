//NAVBAR JS START
//cours js start
const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");
const optionsList = document.querySelectorAll(".option");

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
//cours js end

//username js start
const nabvarUserName = document.querySelector(".nabvar_user-name");
const navbarUserContainer = document.querySelector(".navbar_user-container");
const userOption = document.querySelectorAll(".user_option");

nabvarUserName.addEventListener("click", () => {
    navbarUserContainer.classList.toggle("active");
    nabvarUserName.classList.toggle("active");
});

userOption.forEach(o => {
    o.addEventListener("click", ( ) => {
        nabvarUserName.innerHTML = o.querySelector("label").innerHTML;
        navbarUserContainer.classList.remove("active");   
    });
});

//username js end

//burger start осы жакта туру керек обязательно!!!!!!!!!!!!!
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

navbarSignUp.addEventListener("click", () => {
    registerEffect.classList.toggle("blur_effect-active");
    registerEffect.classList.toggle("active");
    navbarExitBtn.classList.toggle("active");
    navbarTitle.classList.toggle("active")
    navbarTitleSpan.classList.toggle("active")
});

navbarRegister.addEventListener("click", () => {
    registerEffect.classList.toggle("blur_effect-active");
    registerEffect.classList.toggle("active");
    navbarExitBtn.classList.toggle("active");
    navbarTitle.classList.toggle("active")
    navbarTitleSpan.classList.toggle("active")
});

navbarExitBtn.addEventListener("click", () => {
    registerEffect.classList.remove("blur_effect-active");
    registerEffect.classList.remove("active");
    navbarExitBtn.classList.remove("active");
    navbarTitle.classList.toggle("active")
    navbarTitleSpan.classList.toggle("active")
})



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
//NAVBAR JS END