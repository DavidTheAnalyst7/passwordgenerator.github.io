function generatePassword() {
    var min_length = document.getElementById('passwordLength').value;
    var numbers = document.getElementById('includeNumbers').checked;
    var special_character = document.getElementById('includeSpecialCharacters').checked;
    
    var generatedPassword = password_generator(min_length, numbers, special_character);
    
    document.getElementById('password').value = generatedPassword;
  }
  