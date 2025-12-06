import React from 'react'

const Register = () => {

    const handleForm=(event)=>{
        event.preventDefault()
        console.log(event)
    }



  return (
    <form onSubmit={handleForm}>
        <label>Username:</label>
        <input type="text" placeholder='enter your name...' />
        <label htmlFor="">Email:</label>
        <input type="email" placeholder='enter your email'/>
        <label htmlFor="">Password:</label>
        <input type="password" placeholder='enter your password...'/>
        <button type='submit'>Register</button>
    </form>
  )
}

export default Register
