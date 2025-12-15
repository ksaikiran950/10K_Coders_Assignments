import {useState} from 'react'


function Register(){

    const[username,setUsername]=useState("")
    const[email,setEmail]=useState("")
    const[password,setPassword]=useState("")

    const handleForm=(event)=>{
        event.preventDefault()
        const new_user ={username,email,password}
        const addNewUser = async()=>{
          try{
            let check_user=await fetch(`http://localhost:3000/users?email=${new_user.email}`);
            let jsonRes = await check_user.json()
            if(jsonRes.length==0){
              let response = await fetch(`http://localhost:3000/users`,{
                method:"POST",
                headers:{
                  "Content-Type":"application/json"
                },
                body:JSON.stringify(new_user)
              })
              if(response.status==201){
                alert("registration successful")
              }}
              else{
                alert("user already exist....")
              }
            }catch(error){
                console.log(error);
              }
          }
        addNewUser()

}
  return (
    <form onSubmit={handleForm}>
        <label>Username:</label>
        <input 
          type="text" 
          placeholder='enter your name...'
          onChange={(event)=>setUsername(event.target.value)}/>
        <label htmlFor="">Email:</label>
        <input 
          type="email" 
          placeholder='enter your email'
          onChange={(event)=>setEmail(event.target.value)}/>
        <label htmlFor="">Password:</label>
        <input 
          type="password" 
          placeholder='enter your password...'
          onChange={(event)=>setPassword(event.target.value)}/>
        <button type='submit'>Register</button>
    </form>
  )
}

export default Register
