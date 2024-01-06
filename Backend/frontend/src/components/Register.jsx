

const  Register= () =>{
   
    return(
    <div className="container">
<div className="login-box">
  <h2>Register</h2>
  <form action="#">
  
    <div className="input-box">
      <input type="email" required="" />
      <label>Email</label>
    </div>

    <div className="input-box">
      <input type="text" required="" />
      <label>Phone Number</label>
    </div>

    <div className="input-box">
      <input type="password" required="" />
      <label>Password</label>
    </div>

    <div className="input-box">
      <input type="password" required="" />
      <label>Confirm Password</label>
    </div>

    <button type="submit" className="btn">
      Submit
    </button>
    <div className="signup-link">
      <a href="/login">Login</a>
    </div>
  </form>

</div>
</div>
);}

export default Register;

