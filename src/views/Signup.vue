<template>
  <div class="signup">
    <div class="container">
      <h2>CREATE NEW ACCOUNT</h2>
      <input v-model="fullname" type="text" placeholder="Full Name">
      <input v-model="email" type="text" placeholder="Email">
      <input v-model="password" type="password" placeholder="Password">
      <input  v-model="confirmPw" type="password" placeholder="Confirm Password">
      <button @click="signUpUser">Sign up</button>
      <p><b>Already have an account?</b> <router-link to="/">Sign in here</router-link></p>
    </div>
  </div>
</template>
<style>
  
  /* Avatar image */
  img.avatar {
    width: 40%;
  }

</style>
<script>
  import * as AmazonCognitoIdentity from 'amazon-cognito-identity-js';
  var cognitoUserPoolId = process.env.VUE_APP_USER_POOL_ID;
  var cognitoUserPoolClientId = process.env.VUE_APP_USER_POOL_CLIENT_ID;

  export default {
    name: 'signup',
    data(){
      return {
        fullname: '',
        email: '',
        password: '',
        confirmPw: ''    
      }
    },
    methods: {
      signUpUser: function(){

        var email_address = this.email;
        var password = this.password;

        var navigate = this.$router;

        function signUp(userPool, attributeList){

          return new Promise(function(resolve, reject){
            
            userPool.signUp(email_address, password, attributeList, null, function(err, result){
              

              if (err) {
                  // console.log(err.message);
                  alert(err);
                  console.log(err);
                  reject();
                  return;
              } 

              localStorage.setItem('email', email_address);
              alert("Successfully signed up!!")
              
              resolve(result);

              });

          });

        }

        var poolData = {
          UserPoolId : cognitoUserPoolId,
          ClientId : cognitoUserPoolClientId
        };

        var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

        var attributeList = [];
        
        var dataEmail = {
            Name : 'email',
            Value : this.email
        };

        var dataFullname = {
            Name : 'custom:fullname',
            Value : this.fullname
        };


        var custom_fields = [
            'custom:fullname',
            'custom:age',
            'custom:height',
            'custom:weight',
            'custom:allergies',
            'custom:history_diseases'
        ]

          var attributeEmail = new AmazonCognitoIdentity.CognitoUserAttribute(dataEmail);
          attributeList.push(attributeEmail);


          var attributeFullname = new AmazonCognitoIdentity.CognitoUserAttribute(dataFullname);
          attributeList.push(attributeFullname);


          custom_fields.forEach(function(element){
            attributeList.push(new AmazonCognitoIdentity.CognitoUserAttribute(
              {
                Name: element,
                Value: ''
              }
            ));
          });

          if (this.password === this.confirmPw) {
            navigate.push({name: 'login'})
            // signUp(userPool, attributeList).then(res =>{
            //   console.log(res);

            // });

          } else {
            alert('Passwords do not match.')
          }
      }
    }
  }
</script>