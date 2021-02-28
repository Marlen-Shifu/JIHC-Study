
function send_get_request_to_back() {
    let git_link = document.querySelector('#git_link_input').value
    let lesson_name = document.querySelector('.inside__course-name').textContent

    //let xhttp = new XMLHttpRequest()
    let isDataCorrect = confirm('Уверены в подлинности данных?')

    if (isDataCorrect) {
        window.location.replace('/check/?git=' + git_link + '&ln=' + lesson_name)
    }
}


//NAVBAR JS START
//cours js start
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

try {
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
} catch{};

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


try {
    navbarSignUp.addEventListener("click", () => {
    registerEffect.classList.toggle("blur_effect-active");
    registerEffect.classList.toggle("active");
    navbarExitBtn.classList.toggle("active");
    navbarTitle.classList.toggle("active")
    navbarTitleSpan.classList.toggle("active")
    console.log('asdfgds')
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
} catch{};



try{
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
} catch {}



