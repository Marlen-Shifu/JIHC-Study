let loadFile = function(event) {
  let reader = new FileReader();
  reader.onload = function(){
    let output = document.getElementById('output');
    output.src = reader.result;
  };
  reader.readAsDataURL(event.target.files[0]);
};