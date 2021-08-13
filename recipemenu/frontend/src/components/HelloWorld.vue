<template>
  <div class="hello">
    <div class="mb-5">
    <h1>Weekly Menu</h1>
     <table style="width:100%" class="menu_table">
      <tr>
        <th>ID</th>
        <th>NAME</th>
        <th>ACTION</th>
      </tr>     
        <tr class="mr-5" v-for="(menu, index) in WeeklyMenu"
                    v-bind:value="menu"
                    :key="index" > 
          <td>{{menu.id}}</td>
          <td>{{menu.menu_name}}</td>
          <td>          <button 
            class="border border-danger ml-2" 
            @click="deleteMenu(menu.id)"> - delete menu</button>

          <button class="ml-2" @click="showupdateMenu(menu)">update menu</button>
          <button @click="getRecipes(menu)">See Recipes</button>
            </td>
        </tr>
    </table> 
    </div>
    <div class="row mt-5">
      <div class="col-6"> 
        <input type="text" v-model="addedmenu"/>
        <button @click="addMenu()">  + add menu</button>
      </div>      
      <div class="col-6" 
        v-if="showMenuUpdateModel">
        <input type="text" class="updatemenu" v-model="updatedmenu">
        <button class="update" @click="updateMenu()">update</button>
      </div>      
    </div>
    <div class="row mt-5" v-if="showRecipeModel">
    <div><h1>Recipes</h1></div> 
         <div class="mt-5">
             Name:
            <input type="text" v-model="recipe_name"/>
              Instructions:
            <input type="text" v-model="recipe_instruction"/>
                  Classification:
            <input type="text" v-model="recipe_classification"/>
                  Metadata:
            <input type="text" v-model="recipe_metadata"/>
            <button @click="addRecipe()"> + Add Recipe</button>
         </div> 

     <table style="width:100%" class="mt-5">
      <tr>
        <th>Name</th>
        <th>Instructions</th>
        <th>Classification</th>
        <th>Metadata</th>   
        <th>Action</th>     
      </tr>     
         <tr class="mr-5" v-for="(recipe, index) in Recipes"
                        v-bind:value="recipe"
                        :key="index" > 
          <td>{{recipe.recipe_name}}</td>
          <td>{{recipe.instructions}}</td>
          <td> {{recipe.classification}}</td>
          <td>{{recipe.metadata}}</td>
          <td>                        <button class="ml-5" @click="deleteRecipe(recipe.id)">Delete</button>
                        <button class="ml-5" @click="showupdateRecipe(recipe)">Update</button>
            </td>
        </tr>
    </table>
    </div>
    <div class="mt-5" v-if="updateRecipeModel">
      <h2>Update Recipe</h2>
                        recipe name : <input type="text" v-model="recipe.name"/>
                        instructions : <input type="text" v-model="recipe.instruction"/>
                        classification : <input type="text" v-model="recipe.classification"/>
                        metadata : <input type="text" v-model="recipe.metadata"/>
                        <button @click="updateRecipe()"> Update This Recipe </button>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data:function(){
    return {
      WeeklyMenu : '',
      Recipes : '',
      Ingredients : '',
      Reviews :'',
      addedmenu:'',
      updatedmenu:'',
      showMenuUpdateModel:false,
      updateRecipeModel:false,
      menu_id : null,
      showRecipeModel : false,
      recipe_menu_id : '',
      recipe_name:'',
      recipe_instruction:'',
      recipe_classification:'',
      recipe_metadata:'',
      recipe:{
        id:'',
        name:'',
        instruction:'',
        classification:'',
        metadata:''
      }
    }
  },
  created(){
    this.getMenus();
  },
  methods:{
    // axios call for fetching menus via api
    getMenus(){
      Axios.defaults.xsrfHeaderName = "X-CSRFToken";
      Axios.defaults.xsrfCookieName = "csrftoken";
      Axios.get('http://127.0.0.1:8000/api/get_menu/', {
        headers: {
          'Authorization': 
          'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'
        }
      })
      .then((res) => {
        console.log(res.data);
        this.WeeklyMenu = res.data.menus;
      })  
    },
    // axios call for adding menu via api
    addMenu(){
      if((this.addedmenu).length !== 0){
        Axios.defaults.xsrfHeaderName = "X-CSRFToken";
        Axios.defaults.xsrfCookieName = "csrftoken";
        var data = new FormData();
        data.append('menu_name', this.addedmenu);        
        Axios.post('http://127.0.0.1:8000/api/add_menu/',data, {
          headers: {
            'Authorization': 
            'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'
          }
        })
        .then((res) => {
          console.log(res.data);
          this.getMenus();
        })        
      }
      else{
        alert('please enter the menu to add')
      }
    
    },
    
    // axios call for deleting menu via api    
    deleteMenu(id){
        Axios.defaults.xsrfHeaderName = "X-CSRFToken";
        Axios.defaults.xsrfCookieName = "csrftoken";    
        Axios.delete('http://127.0.0.1:8000/api/delete_menu/' + id + '/',{
          headers: {
            'Authorization': 
            'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'          }
        })
        .then((res) => {
          console.log(res.data);
          this.getMenus();
        }) 

    },
    // show update menu options   
    showupdateMenu(menu){
      this.showMenuUpdateModel = true;
      this.updatedmenu = menu.menu_name;
      this.menu_id = menu.id
    },

    // axios call for updating menu
    updateMenu(){
      if((this.updatedmenu).length !== 0){
        Axios.defaults.xsrfHeaderName = "X-CSRFToken";
        Axios.defaults.xsrfCookieName = "csrftoken";
        var data = new FormData();
        data.append('menu_name', this.updatedmenu);        
        Axios.put('http://127.0.0.1:8000/api/update_menu/' + this.menu_id +'/',data, {
          headers: {
            'Authorization': 
            'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'
          }
        })
        .then((res) => {
          console.log(res.data);     
          this.updatedmenu = '';
          this.showMenuUpdateModel = false;
          this.getMenus();
        })        
      }
      else{
        alert('please enter the menu to add')
      }
    },
    //axios call for getting recipe via api
    getRecipes(menu){
      this.showRecipeModel = false;
      Axios.defaults.xsrfHeaderName = "X-CSRFToken";
      Axios.defaults.xsrfCookieName = "csrftoken";
      var data = new FormData();
      data.append('menu_id', menu.id);      
      Axios.post('http://127.0.0.1:8000/api/get_recipe/',data,{
        headers: {
          'Authorization': 
          'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'
        },
      },
      )
      .then((res) => {
        console.log(res.data);
        this.showRecipeModel = true;
        this.Recipes = res.data.recipes;
        this.recipe_menu_id = res.data.recipe_menu_id;
      })  
    },

    // axios call for deleting recipe via api
    deleteRecipe(id){
        Axios.defaults.xsrfHeaderName = "X-CSRFToken";
        Axios.defaults.xsrfCookieName = "csrftoken";   
        Axios.delete('http://127.0.0.1:8000/api/delete_recipe/' + id + '/',{
          headers: {
            'Authorization': 
            'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'          }
        })
        .then((res) => {
          console.log(res.data);          
          this.getRecipes(id=this.recipe_menu_id);
        })       
    },

    // axios call with adding api
    addRecipe(){
      if((this.recipe_name).length !== 0){
        Axios.defaults.xsrfHeaderName = "X-CSRFToken";
        Axios.defaults.xsrfCookieName = "csrftoken";
        var data = new FormData();
        data.append('menu_id', this.recipe_menu_id);
        data.append('recipe_name', this.recipe_name);
        data.append('instructions', this.recipe_instruction);
        data.append('classification', this.recipe_classification); 
        data.append('metadata', this.recipe_metadata);                                  
        Axios.post('http://127.0.0.1:8000/api/add_recipe/',data, {
          headers: {
            'Authorization': 
            'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'
          }
        })
        .then((res) => {
          this.showRecipeModel = false;
          this.recipe_menu ='';
          this.recipe_instruction ='';
          this.recipe_classification ='';
          this.recipe_metadata ='';
          console.log(res.data);
          // this.getMenus();
        })        
      }      
    },

    // show update recipe option
    showupdateRecipe(recipe){
      this.updateRecipeModel = true;
      this.recipe.id = recipe.id;
      this.recipe.name = recipe.recipe_name;
      this.recipe.instruction = recipe.instructions;
      this.recipe.classification = recipe.classification;
      this.recipe.metadata = recipe.metadata;                  
    },

    // axios call for updating recipe via api
    updateRecipe(){
      if((this.recipe.name).length !== 0){
        Axios.defaults.xsrfHeaderName = "X-CSRFToken";
        Axios.defaults.xsrfCookieName = "csrftoken";
        var data = new FormData();
        data.append('recipe_id', this.recipe.id);
        data.append('recipe_name', this.recipe.name);
        data.append('instructions', this.recipe.instruction);
        data.append('classification', this.recipe.classification); 
        data.append('metadata', this.recipe.metadata);           
        Axios.put('http://127.0.0.1:8000/api/update_recipe/' + this.recipe.id +'/',data, {
          headers: {
            'Authorization': 
            'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5OTg3MzAzLCJqdGkiOiI0NDU3ZDg3ZWE5Y2Y0OGE5YTMzNjYxMzg4ZDQwNGI1ZCIsInVzZXJfaWQiOjF9.s9VlGokA5nyUU3OFKQm4z1Cwq5Tnq55dlAqRPqwyFnA'
          }
        })
        .then((res) => {
          console.log(res.data);
          this.updateRecipeModel = false;
          this.showRecipeModel = false;
        })        
      }
      else{
        alert('please enter the menu to add')
      }
    },
    getIngredients(){
    },
    getReviews(){
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.updatemenu{
    width: 200px;
    height: 30px;
    padding-right: 50px;
}

.update{
    margin-left: -64px;
    height: 25px;
    width: 60px;
    background: yellowgreen;
    color: white;
    border: 0;
    -webkit-appearance: none;
}
.menu_table{
  margin-left: 180px;
}
</style>
